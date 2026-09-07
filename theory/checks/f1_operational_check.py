#!/usr/bin/env python3
"""Exact Hecke/quantum-net falsifiers. No floats and no theorem by sampling.

Rational permutation-basis arithmetic is compared with independent finite-field
flag adjacency matrices and explicit observable/probability formulas.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import prod
import numpy as np

CHECKED,FAILED={},{}

def need(condition, gate, message):
    # Each H-gate is one conjunction of independently computed probes.
    # Evaluate every probe, also on red runs: early exit used to hide later
    # diagnostics. We claim mutation coverage of these gates, not every line.
    CHECKED[gate]=CHECKED.get(gate,0)+1
    if not condition:
        FAILED.setdefault(gate,[])
        if message not in FAILED[gate]:FAILED[gate].append(message)


def length(w):
    return sum(w[i] > w[j] for i in range(len(w)) for j in range(i+1,len(w)))


def inverse(w):
    return tuple(w.index(i) for i in range(len(w)))


def word(w):
    a, moves = list(w), []
    while any(a[i]>a[i+1] for i in range(len(a)-1)):
        i = next(i for i in range(len(a)-1) if a[i]>a[i+1])
        a[i],a[i+1] = a[i+1],a[i]
        moves.append(i)
    return tuple(reversed(moves))


def rank(rows):
    a=[list(map(F,r)) for r in rows]
    r=0
    for col in range(len(a[0])):
        pivot=next((j for j in range(r,len(a)) if a[j][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        lead=a[r][col];a[r]=[x/lead for x in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][col]:
                lead=a[j][col];a[j]=[x-lead*y for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r


class Hecke:
    def __init__(self,n,q,red_product=False):
        self.n,self.q,self.red_product=n,F(q),red_product
        self.perms=tuple(permutations(range(n)))
        self.e=tuple(range(n));self.one={self.e:F(1)}

    def basis(self,w):return {tuple(w):F(1)}

    def simple(self,i):
        w=list(self.e);w[i],w[i+1]=w[i+1],w[i]
        return self.basis(w)

    def add(self,*xs):
        out={}
        for x in xs:
            for w,c in x.items():out[w]=out.get(w,F(0))+c
        return {w:c for w,c in out.items() if c}

    def scale(self,c,x):return {w:F(c)*d for w,d in x.items() if c*d}

    @lru_cache(None)
    def basis_mul(self,u,v):
        out=self.basis(u)
        for i in word(v):
            nxt={}
            for w,c in out.items():
                s=list(w);s[i],s[i+1]=s[i+1],s[i];s=tuple(s)
                if w[i]<w[i+1]:nxt[s]=nxt.get(s,F(0))+c
                else:
                    nxt[w]=nxt.get(w,F(0))+(self.q-1)*c
                    factor=self.q+(1 if self.red_product else 0)
                    nxt[s]=nxt.get(s,F(0))+factor*c
            out={w:c for w,c in nxt.items() if c}
        return out

    def mul(self,x,y):
        return self.add(*(self.scale(a*b,self.basis_mul(u,v))
                          for u,a in x.items() for v,b in y.items()))

    def star(self,x):return {inverse(w):c for w,c in x.items()}

    def tau(self,x,wrong=False):
        out=x.get(self.e,F(0))
        if wrong and self.n>1:
            out+=x.get(next(iter(self.simple(0))),F(0))
        return out

    def minus(self,x,y):return self.add(x,self.scale(-1,y))


def embed(h,x,dest,offset=0):
    out={}
    for w,c in x.items():
        z=list(dest.e)
        for i in range(h.n):z[offset+i]=offset+w[i]
        out[tuple(z)]=c
    return out


def expectation(h,x,cut,wrong=False):
    out={w:c for w,c in x.items() if set(w[:cut])==set(range(cut))}
    if wrong:out={w:c*(1 if w==h.e else 2) for w,c in out.items()}
    return out


def algebra_tests(args):
    for q in [F(1),F(2),F(3),F(5),F(1,2)]+([F(-1)] if args.red_positive_domain else []):
        for n in [2,3,4]:
            h=Hecke(n,q,args.red_product)
            ts=[h.simple(i) for i in range(n-1)]
            for t in ts:
                need(h.mul(t,t)==h.add(h.scale(q-1,t),h.scale(q,h.one)),"H1","quadratic relation")
            for i in range(n-2):
                s,t=ts[i:i+2]
                need(h.mul(h.mul(s,t),s)==h.mul(h.mul(t,s),t),"H1","braid relation")
            if n==4:need(h.mul(ts[0],ts[2])==h.mul(ts[2],ts[0]),"H1","far commutation")
            for u,v in product(h.perms,repeat=2):
                x,y=h.basis(u),h.basis(v)
                need(h.star(h.mul(x,y))==h.mul(h.star(y),h.star(x)),"H1","star antimultiplicativity")
                gram=h.tau(h.mul(h.star(x),y),args.red_trace)
                need(gram==(q**length(u) if u==v else 0),"H2",f"Gram q={q}, n={n}")
            if n==3:
                for u,v,w in product(h.perms,repeat=3):
                    x,y,z=map(h.basis,(u,v,w))
                    need(h.mul(h.mul(x,y),z)==h.mul(x,h.mul(y,z)),"H1","associativity")
            need(all(q**length(w)>0 for w in h.perms),"H2","strictly positive Gram diagonal")
    print("H1 evaluated: exact Hecke/star/associativity identities, q=1,2,3,5,1/2; n≤4")
    print("H2 evaluated: positive canonical Gram form, all basis pairs")


def block_tests(args):
    for q in [F(1),F(2),F(3),F(1,2)]:
        a,b,h=Hecke(2,q),Hecke(2,q),Hecke(4,q)
        blocks=[w for w in h.perms if set(w[:2])=={0,1}]
        ex=lambda x:expectation(h,x,2,args.red_expectation)
        for u,v in product(a.perms,repeat=2):
            x,y=a.basis(u),a.basis(v)
            need(embed(a,a.mul(x,y),h)==h.mul(embed(a,x,h),embed(a,y,h)),"H3","left inclusion")
            need(h.mul(embed(a,x,h),embed(b,y,h,2))==h.mul(embed(b,y,h,2),embed(a,x,h)),"H3","commuting blocks")
        for w in h.perms:
            x=h.basis(w)
            need(h.tau(ex(x))==h.tau(x),"H3","trace-preserving expectation")
            if w in blocks:need(ex(x)==x,"H3","expectation fixes subalgebra")
            for u in blocks:
                y=h.basis(u)
                need(ex(h.mul(x,y))==h.mul(ex(x),y),"H3","right bimodule")
                need(ex(h.mul(y,x))==h.mul(y,ex(x)),"H3","left bimodule")
        def ev(x,r,s):
            return sum(c*r**int(w[0]>w[1])*s**int(w[2]>w[3]) for w,c in x.items())
        # Matrix-level positivity: evaluate E entrywise on X*X in M2(H4)
        # in every character of the commutative target H2 tensor H2.
        for j,w in enumerate(h.perms):
            x=[[h.basis(w),h.basis(h.perms[(j+3)%24])],[h.simple(1),h.one]]
            if j==0:x[0][0]=h.mul(h.add(h.one,h.simple(0)),h.add(h.one,h.simple(2)))
            def pos_ex(a):
                value=ex(a)
                return h.minus(h.scale(2*h.tau(a),h.one),value) if args.red_amplified else value
            y=[[pos_ex(h.add(*(h.mul(h.star(x[k][i]),x[k][l]) for k in range(2))))
                for l in range(2)] for i in range(2)]
            for r,s in product([q,F(-1)],repeat=2):
                mat=[[ev(y[i][j],r,s) for j in range(2)] for i in range(2)]
                need(mat[0][0]>=0 and mat[1][1]>=0 and mat[0][1]==mat[1][0]
                     and mat[0][0]*mat[1][1]>=mat[0][1]**2,"H3","amplified positivity")
    print("H3 evaluated: block inclusions, trace/bimodule expectation and 2x2 positivity probes")


def central_data(h):
    d=sum(h.q**length(w) for w in h.perms)
    plus={w:F(1,d) for w in h.perms}
    dm=sum(h.q**(-length(w)) for w in h.perms)
    minus={w:(-h.q)**(-length(w))/dm for w in h.perms}
    z=h.minus(h.minus(h.one,plus),minus)
    return plus,minus,z


def overlap_tests(args):
    for q in [F(1),F(2),F(3),F(5),F(1,2)]:
        h=Hecke(3,q);plus,minus,z=central_data(h)
        for c,r in [(plus,1),(minus,1),(z,4)]:
            need(h.mul(c,c)==c and h.star(c)==c,"H4","central projection")
            cols=[]
            for w in h.perms:
                col=h.mul(c,h.basis(w));cols.append([col.get(v,F(0)) for v in h.perms])
            need(rank(cols)==r,"H4","central summand algebra dimension")
        e=[h.scale(1/(q+1),h.add(h.simple(i),h.one)) for i in range(2)]
        p=[h.mul(z,x) for x in e]
        a=q/(q+1)**2
        ratio=h.tau(h.mul(p[0],p[1]))/h.tau(p[0])
        want=F(1,4) if args.red_overlap else a
        need(ratio==want,"H4",f"intrinsic overlap q={q}: {ratio}")
        need(h.tau(e[0])==1/(q+1),"H4","trivial projector flag probability")
        rho=p[1] if args.red_density_norm else h.scale(1/h.tau(p[1]),p[1])
        u=h.minus(h.scale(2,e[0]),h.one)
        need(h.mul(u,u)==h.one,"H5","local unitary")
        need(h.mul(u,e[0])==h.mul(e[0],u),"H5","local CP identity")
        actual_u=h.one if args.red_local_collapse else u
        moved=h.mul(h.mul(actual_u,rho),actual_u)
        probability=h.tau(h.mul(moved,p[1]))
        need(h.tau(rho)==1 and h.tau(h.mul(rho,p[1]))==1,"H5","density/effect normalization")
        need(probability==(1-2*a)**2,"H5",f"context probability q={q}: {probability}")
        us=[h.minus(h.scale(2,t),h.one) for t in e]
        defect=h.minus(h.mul(h.mul(us[0],us[1]),us[0]),h.mul(h.mul(us[1],us[0]),us[1]))
        norm=h.tau(h.mul(h.star(defect),defect))
        need((norm==0)==(True if args.red_unitary_braid else q==1),"H6","unitarized braid")
        # Negative-eigenvalue idempotents: the sign block is the TL obstruction.
        r=[h.minus(h.one,t) for t in e]
        lhs=h.minus(h.mul(h.mul(r[0],r[1]),r[0]),h.scale(a,r[0]))
        rhs={} if args.red_tl_trace else h.scale(1-a,minus)
        need(lhs==rhs,"H10","TL relation needs the sign-block quotient")
        need(h.tau(minus)>0,"H10","faithful flag trace does not descend through TL quotient")
        print(f"q={q}: overlap={a}, after locally invisible unitary={probability}")
    print("H4 evaluated: central dimensions 1,1,4 and intrinsic parameter overlaps")
    print("H5 evaluated: isolated CP identity becomes a measurable collective operation")
    print("H6 evaluated: unitarized generators braid only at q=1 in this positive sample")
    print("H10 evaluated: TL quotient distinguished from canonical flag-trace theory")


def injection(w,f,n,wrong=False):
    use=tuple(range(len(f))) if wrong else f
    z=list(range(n))
    for i in range(len(f)):z[use[i]]=use[w[i]]
    return tuple(z)


def net_tests(args):
    for f in permutations(range(3),2):
        for g in permutations(range(4),3):
            fg=tuple(g[f[i]] for i in range(2))
            for w in permutations(range(2)):
                im=injection(w,f,3,args.red_injection)
                need(all(im[f[i]]==f[w[i]] for i in range(2)),"H7","permutation extension along injection")
                need(injection(im,g,4)==injection(w,fg,4),"H7","injection composition")
    h=Hecke(3,1);sub={injection(w,(0,2),3) for w in permutations(range(2))}
    for w in h.perms:
        ex=h.basis(w) if w in sub else {}
        need(h.tau(ex)==h.tau(h.basis(w)),"H7","noncontiguous subgroup expectation")
    print("H7 evaluated: q=1 arbitrary injections compose, including noncontiguous subsystems")
    a=Hecke(2,1)
    e=a.scale(F(1,2),a.add(a.one,a.simple(0)))
    ks=[e,a.minus(a.one,e)]
    if args.red_kraus:ks[0]=a.scale(2,ks[0])
    need(a.add(*(a.mul(a.star(k),k) for k in ks))==a.one,"H8","Kraus normalization")
    ls=[a.add(a.scale(F(3,5),ks[0]),a.scale(F(3 if args.red_kraus_mix else 4,5),ks[1])),
        a.add(a.scale(F(-4,5),ks[0]),a.scale(F(3,5),ks[1]))]
    def channel(h,ops,x):return h.add(*(h.mul(h.mul(k,x),h.star(k)) for k in ops))
    ekh,elh=[[embed(a,k,h) for k in ops] for ops in [ks,ls]]
    for w in h.perms:
        x=h.basis(w)
        need(channel(h,ekh,x)==channel(h,elh,x),"H8","scalar-isometry equivalence in ambient context")
        need(h.tau(channel(h,ekh,x))==h.tau(x),"H8","ambient channel trace preservation")
    big=Hecke(4,1)
    parallel=[big.mul(embed(a,k,big),embed(a,l,big,2)) for k,l in product(ks,repeat=2)]
    need(big.add(*(big.mul(big.star(k),k) for k in parallel))==big.one,"H8","parallel Kraus normalization")
    print("H8 evaluated: Kraus normalization, scalar-isometry equivalence and parallel contextual extension")


def flag_tests(args):
    for p in [2,3]:
        points=[]
        for x in product(range(p),repeat=3):
            if any(x) and next(t for t in x if t)!=1:continue
            if any(x):points.append(x)
        flags=[(i,j) for i,x in enumerate(points) for j,y in enumerate(points)
               if sum(a*b for a,b in zip(x,y))%p==0]
        n=len(flags);identity=np.eye(n,dtype=np.int64)
        ts=[]
        for which in [1,0]:
            t=np.array([[int(x!=y and x[which]==y[which]) for y in flags] for x in flags],dtype=np.int64)
            if args.red_flag and which==0:t[0,0]=1
            ts.append(t)
            need(np.array_equal(t@t,(p-1)*t+p*identity),"H9",f"flag adjacency F{p}")
        need(np.array_equal(ts[0]@ts[1]@ts[0],ts[1]@ts[0]@ts[1]),"H9","flag braid")
        h=Hecke(3,p);mats={}
        for w in h.perms:
            m=identity
            for i in word(w):m=m@ts[i]
            mats[w]=m
        for u,v in product(h.perms,repeat=2):
            gram=F(int(np.trace(mats[u].T@mats[v])),n)
            need(gram==(p**length(u) if u==v else 0),"H9","independent flag normalized Gram")
        need(n==(p+1)*(p*p+p+1),"H9","complete flag count")
        coordinate=1 if args.red_incidence else 0
        same_line=np.array([[int(x[coordinate]==y[coordinate]) for y in flags] for x in flags],dtype=np.int64)
        need(np.array_equal(identity+ts[1],same_line),"H9","partial-flag incidence projection")
        axes=[points.index(tuple(int(i==j) for i in range(3))) for j in range(3)]
        apartment=[flags.index((axes[w[0]],axes[w[2]])) for w in h.perms]
        if args.red_apartment:apartment[-1]=apartment[0]
        need(len(set(apartment))==6,"H9","apartment inclusion is an isometry")
        for w in h.perms:
            wi=inverse(w)
            regular=np.array([[int(u==tuple(v[wi[i]] for i in range(3))) for v in h.perms]
                              for u in h.perms],dtype=np.int64)
            need(np.array_equal(mats[w][np.ix_(apartment,apartment)],regular),
                 "H9","apartment CP comparison sends T_w to the regular permutation")
        print(f"H9 evaluated: independent F{p}^3 flags ({n} flags), adjacency and normalized trace")


def context_depth_tests(args):
    for q,n in product([F(1),F(2)],[2,3]):
        local=Hecke(n,q);pt,ps,pr=central_data(local)
        kp=[local.add(pt,ps),pr];km=[local.minus(pt,ps),pr]
        for ks in [kp,km]:
            need(local.add(*(local.mul(local.star(k),k) for k in ks))==local.one,
                 "H11","sharpness Kraus normalization")
        size=n if args.red_context_size else 2*n-1
        big=Hecke(size,q)
        d=tuple(range(size)) if args.red_context_size else (0,)+tuple(range(n,2*n-1))+tuple(range(1,n))
        images=set()
        td=big.basis(d)
        for u,v in product(local.perms,repeat=2):
            left=embed(local,local.star(local.basis(u)),big)
            right=embed(local,local.basis(v),big)
            out=big.mul(big.mul(left,td),right)
            need(len(out)==1 and next(iter(out.values()))==1,
                 "H11","double coset has no lower Hecke terms")
            images.add(next(iter(out)))
        need(len(images)==len(local.perms)**2,"H11","ambient context separates every Kraus Gram coefficient")
        def phi(ks,x):
            ops=[embed(local,k,big) for k in ks]
            return big.add(*(big.mul(big.mul(big.star(k),x),k) for k in ops))
        bound=max(q,F(1))**length(d)
        effect=big.scale(F(1,2),big.add(big.one,big.scale(1/bound,td)))
        plus,minus=phi(kp,effect),phi(km,effect)
        delta=big.minus(plus,minus);rho=big.add(big.one,delta)
        need(delta and big.star(delta)==delta and big.tau(delta)==0,
             "H11","nonzero Hermitian zero-trace channel difference")
        gap=big.tau(big.mul(delta,delta))
        pplus=big.tau(big.mul(rho,plus));pminus=big.tau(big.mul(rho,minus))
        need(big.tau(rho)==1 and gap>0 and pplus-pminus==gap
             and 0<=pplus<=1 and 0<=pminus<=1,"H11","explicit positive-state Born witness")
        for smaller in range(n,2*n-1+int(args.red_context_lower)):
            h=Hecke(smaller,q);p=embed(local,pt,h);s=embed(local,ps,h)
            for w in h.perms:
                need(not h.mul(h.mul(s,h.basis(w)),p),"H11","no smaller context couples sign and trivial sectors")
        print(f"H11 evaluated: n={n}, q={q}: sharp ambient size {size}, Born gap {gap}")


def partial_map_tests(args):
    @lru_cache(None)
    def maps(n,m):
        return tuple(f for f in product(range(-1,m),repeat=n)
                     if len([x for x in f if x>=0])==len({x for x in f if x>=0}))
    def act(f,m,w):
        if w is None:return None
        if args.red_partial_zero and all(x<0 for x in f):return None
        if any(f[i]<0 and w[i]!=i for i in range(len(f))):return None
        out=list(range(m))
        for i,y in enumerate(f):
            if y>=0:out[y]=f[w[i]]
        return tuple(out)
    for n,m in product(range(4),repeat=2):
        for f in maps(n,m):
            need(act(f,m,tuple(range(n)))==tuple(range(m)),"H12","even empty partial maps must be unital")
            adj=tuple(next((i for i,y in enumerate(f) if y==j),-1) for j in range(m))
            if args.red_partial_dagger and n==m==3:adj=f
            for w,v in product(permutations(range(n)),permutations(range(m))):
                need((act(f,m,w)==v)==(act(adj,n,v)==w),"H12","trace-adjoint partial-map dagger")
    for n,m,l in product(range(4),repeat=3):
        for f,g in product(maps(n,m),maps(m,l)):
            gf=tuple(-1 if j<0 else g[j] for j in f)
            if args.red_partial_comp and n==m==l==3:gf=f
            for w in permutations(range(n)):
                need(act(g,l,act(f,m,w))==act(gf,l,w),"H12","partial-map composition")
    small=[(n,m,f) for n,m in product(range(3),repeat=2) for f in maps(n,m)]
    for (n,m,f),(r,s,g) in product(small,repeat=2):
        fg=f+tuple(-1 if j<0 else m+j for j in g)
        if args.red_partial_lax and n==m==r==s==2:fg=fg[:-1]+(-1,)
        for u,v in product(permutations(range(n)),permutations(range(r))):
            uv=u+tuple(n+j for j in v)
            left,right=act(f,m,u),act(g,s,v)
            expected=None if left is None or right is None else left+tuple(m+j for j in right)
            need(act(fg,m+s,uv)==expected,"H12","lax monoidal naturality on block algebra")
    print("H12 evaluated: normal F1 maps realize as CP reset/restriction/extension; composition, dagger and block naturality")


def corner_tests(args):
    def compositions(n):
        if n==0:return [()]
        return [(i,)+r for i in range(1,n+1) for r in compositions(n-i)]
    def parabolic(h,alpha):
        borders=[0]
        for a in alpha:borders.append(borders[-1]+a)
        ws=[w for w in h.perms if all(set(w[a:b])==set(range(a,b)) for a,b in zip(borders,borders[1:]))]
        denominator=sum(h.q**length(w) for w in ws)
        return set(ws),{w:1/denominator for w in ws},denominator
    for q,n in product([F(1),F(2)],[3,4]):
        h=Hecke(n,q);data=[parabolic(h,alpha) for alpha in compositions(n)]
        for ws,e,p in data:
            need(h.star(e)==e and h.mul(e,e)==e,"H13","parabolic projection")
            physical=(1 if args.red_corner_trace else p)*h.tau(e)
            need(physical==1,"H13","normalized corner trace of identity")
            for vs,f,_ in data:
                if ws<=vs or (args.red_refinement and vs<ws):
                    need(h.mul(e,f)==f and h.mul(f,e)==f,"H13","typed refinement isometry")
        a,b=Hecke(2,q),Hecke(n-2,q)
        for alpha,beta in product(compositions(2),compositions(n-2)):
            _,ea,_=parabolic(a,alpha);_,eb,_=parabolic(b,beta)
            _,target,_=parabolic(h,alpha+beta)
            need(h.mul(embed(a,ea,h),embed(b,eb,h,2))==target,"H13","corner tensor concatenation")
    print("H13 evaluated: positive parabolic corners, normalized identities, refinement and tensor concatenation")


def bell_tests(args):
    small,big=Hecke(3,1),Hecke(6,1)
    _,_,z=central_data(small);s,t=small.simple(0),small.simple(1)
    zz=small.mul(z,s)
    xx=small.mul(z,small.add(small.scale(2,t),s))
    yy=small.mul(z,small.minus(small.mul(s,t),small.mul(t,s)))
    def tensor(a,b):return big.mul(embed(small,a,big),embed(small,b,big,3))
    bell=big.scale(F(1,4),big.add(tensor(z,z),tensor(zz,zz),
                    big.scale(F(1,3),tensor(xx,xx)),
                    big.scale(F(-1 if args.red_bell_sign else 1,3),tensor(yy,yy))))
    need(big.star(bell)==bell and big.mul(bell,bell)==bell,"H14","Bell effect is an orthogonal projection")
    rho=big.scale(9,bell)
    need(big.tau(rho)==1,"H14","full group-trace Bell density normalization")
    left={w[:3]:c for w,c in rho.items() if w[3:]==(3,4,5)}
    need(left==small.scale(F(3,2),z),"H14","maximally mixed standard-sector marginal")
    for obs,expected in [(tensor(zz,zz),F(1)),
                         (big.scale(F(1,3),tensor(xx,xx)),F(1)),
                         (tensor(zz,xx),F(0)),(tensor(xx,zz),F(0))]:
        need(big.tau(big.mul(rho,obs))==expected,"H14","Bell correlations giving CHSH 2sqrt(2)")
    print("H14 evaluated: six-constituent Bell state, exact normalization/marginal and Pauli correlations")


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name,help_text in [
        ('product','H1: wrong descent coefficient'),('trace','H2: wrong trace support'),
        ('expectation','H3: expectation fails to fix parabolic algebra'),
        ('overlap','H4: erase parameter from overlap'),
        ('local-collapse','H5: identify isolated CP actions before extension'),
        ('unitary-braid','H6: assume unitarization preserves braid'),
        ('injection','H7: ignore injection image'),('kraus','H8: unnormalized local Kraus list'),
        ('flag','H9: add forbidden self-adjacency'),('tl-trace','H10: omit nonzero quotient ideal'),
        ('context-size','H11: try to recover all Kraus data without sufficient context'),
        ('partial-zero','H12: send empty partial maps to zero instead of the reference reset'),
        ('corner-trace','H13: omit physical corner-trace normalization'),
        ('positive-domain','H2: include an indefinite negative parameter'),
        ('amplified','H3: replace expectation by a nonpositive unital traced map'),
        ('density-norm','H5: omit standard-sector density normalization'),
        ('kraus-mix','H8: use a nonisometric Kraus mixing matrix'),
        ('incidence','H9: forget the wrong flag subspace'),
        ('context-lower','H11: extend the lower-bound assertion to the separating context'),
        ('partial-dagger','H12: use a partial map instead of its inverse'),
        ('partial-comp','H12: omit the second partial-map factor'),
        ('partial-lax','H12: lose a wire in disjoint partial-map assembly'),
        ('refinement','H13: reverse the refinement containment'),
        ('bell-sign','H14: reverse the antisymmetric Bell correlation'),
        ('apartment','H9: duplicate a thin-apartment flag')]:
        ap.add_argument('--red-'+name,action='store_true',help=help_text)
    args=ap.parse_args()
    print('MODE:',','.join(k for k,v in vars(args).items() if v) or 'green')
    algebra_tests(args);block_tests(args);overlap_tests(args);net_tests(args);flag_tests(args)
    context_depth_tests(args)
    partial_map_tests(args)
    corner_tests(args)
    bell_tests(args)
    for gate in sorted(CHECKED,key=lambda x:int(x[1:])):
        if gate in FAILED:
            print(f"FAIL {gate}: "+'; '.join(FAILED[gate][:5]))
        else:print(f"{gate} PASS: {CHECKED[gate]} exact probes in the acceptance conjunction")
    if FAILED:raise SystemExit(1)
    print('ALL OPERATIONAL EXAMPLE GATES PASSED (exact; no general theorem inferred)')


if __name__=='__main__':
    try:main()
    except AssertionError as e:
        print('FAIL',e)
        raise SystemExit(1)
