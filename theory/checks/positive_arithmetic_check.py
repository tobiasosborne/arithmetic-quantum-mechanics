#!/usr/bin/env python3
"""Exact bounded P1--P7 falsifiers; passing never proves the universal claims."""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, gcd, prod
import json
import numpy as np

MUTATIONS={'mass':'P1','jordan':'P1','moment':'P1','embedding':'P2',
 'fourier-invariance':'P2','tracial-complement':'P3','compression':'P4',
 'coherence':'P4','fourier-phase':'P4','profile':'P5','total-first-order':'P5',
 'discard-later-rare':'P5','multiplication-entry':'P6','arity':'P6',
 'erase-characteristic':'P7','normalizer':'P5'}

class Failure(Exception):
    def __init__(self,gate,detail): self.gate,self.detail=gate,detail

class Checks:
    def __init__(self,red=None): self.red,self.counts,self.records=red,{},{}
    def check(self,g,condition,detail):
        self.counts[g]=self.counts.get(g,0)+1
        if not condition: raise Failure(g,detail)

def eye(n): return np.eye(n,dtype=object)
def same(a,b): return np.array_equal(a,b)
def diag(xs): return np.diag(np.array(xs,dtype=object))
def unit(n,i,j):
    a=np.zeros((n,n),dtype=object); a[i,j]=1; return a
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def primes(n): return [p for p in range(2,n+1) if n%p==0 and all(p%a for a in range(2,p))]
def polynomial(d):
    out={d:1}
    for e in divisors(d)[:-1]:
        for k,v in polynomial(e).items(): out[k]=out.get(k,0)-v
    return {k:v for k,v in out.items() if v}
def bpoly(d):
    out=polynomial(d)
    if d==1: out[0]=-1
    return out
def bvalue(d,t): return sum(v*t**e for e,v in bpoly(d).items())
def jordan(d,k): return F(d**k)*prod(1-F(1,p**k) for p in primes(d))

class Field:
    """Polynomial quotient with independently computed operations and periods."""
    def __init__(self,p,mod):
        self.p,self.mod,self.r=p,mod,len(mod)-1; self.q=p**self.r
        self.coords=[[(x//p**j)%p for j in range(self.r)] for x in range(self.q)]
        # A finite quotient in which a^(Q-1)=1 for every nonzero a is a field.
        assert all(self.power(a,self.q-1)==1 for a in range(1,self.q)),(p,mod)
        self.frob=[self.power(x,p) for x in range(self.q)]
        self.period=[]
        for x in range(self.q):
            y=self.frob[x]; d=1
            while y!=x: y=self.frob[y]; d+=1; assert d<=self.r
            self.period.append(d)
    def encode(self,xs): return sum((x%self.p)*self.p**j for j,x in enumerate(xs))
    def add(self,a,b): return self.encode([x+y for x,y in zip(self.coords[a],self.coords[b])])
    def mul(self,a,b):
        out=[0]*(2*self.r-1)
        for i,j in product(range(self.r),repeat=2): out[i+j]+=self.coords[a][i]*self.coords[b][j]
        for i in range(2*self.r-2,self.r-1,-1):
            for j in range(self.r): out[i-self.r+j]-=out[i]*self.mod[j]
        return self.encode(out[:self.r])
    def power(self,a,k):
        out=1
        while k:
            if k%2: out=self.mul(out,a)
            a,k=self.mul(a,a),k//2
        return out
    def absolute_trace(self,a):
        out=0
        for j in range(self.r): out=self.add(out,self.power(a,self.p**j))
        assert out<self.p
        return out

MODULI={2:[[0,1],[1,1,1],[1,1,0,1],[1,1,0,0,1]],
 3:[[0,1],[1,0,1],[1,2,0,1],[2,1,0,0,1]],
 5:[[0,1],[2,0,1],[1,1,0,1],[2,0,0,0,1]]}
FIELDS={}
def field(p,r):
    if (p,r) not in FIELDS: FIELDS[p,r]=Field(p,MODULI[p][r-1])
    return FIELDS[p,r]
def density(e,t): return np.array([F(1) if x==0 else bvalue(e.period[x],t)/bvalue(e.period[x],F(e.p)) for x in range(e.q)],dtype=object)
def coefficients(e,limit=6):
    out=[np.array([F(x==0) for x in range(e.q)],dtype=object)]
    for k in range(1,limit+1):
        out.append(np.array([F(0) if x==0 else sum(F(v*j**k,factorial(k)) for j,v in bpoly(e.period[x]).items())/bvalue(e.period[x],F(e.p)) for x in range(e.q)],dtype=object))
    return out

class Cyclo:
    """Exact Q(zeta_p), with canonical coefficients on 1,...,zeta^(p-2)."""
    def __init__(self,p,coeff=0):
        self.p=p
        self.a=tuple(map(F,coeff)) if isinstance(coeff,(tuple,list)) else (F(coeff),)+(F(0),)*(p-2)
    def coerce(self,x):
        if isinstance(x,Cyclo): assert self.p==x.p; return x
        return Cyclo(self.p,x)
    @staticmethod
    def root(p,k):
        k%=p
        return Cyclo(p,[-1]*(p-1) if k==p-1 else [int(j==k) for j in range(p-1)])
    def __add__(self,x):
        x=self.coerce(x); return Cyclo(self.p,[a+b for a,b in zip(self.a,x.a)])
    __radd__=__add__
    def __neg__(self): return Cyclo(self.p,[-a for a in self.a])
    def __sub__(self,x): return self+-self.coerce(x)
    def __rsub__(self,x): return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x); out=[F(0)]*self.p
        for i,j in product(range(self.p-1),repeat=2): out[(i+j)%self.p]+=self.a[i]*x.a[j]
        return Cyclo(self.p,[out[i]-out[-1] for i in range(self.p-1)])
    __rmul__=__mul__
    def __truediv__(self,x): return Cyclo(self.p,[a/F(x) for a in self.a])
    def conjugate(self): return sum((Cyclo.root(self.p,-i)*a for i,a in enumerate(self.a)),Cyclo(self.p,0))
    def __eq__(self,x):
        try: return self.a==self.coerce(x).a
        except (TypeError,ValueError): return False
    def __repr__(self): return str(self.a)
    def real(self): assert all(x==0 for x in self.a[1:]),self; return self.a[0]

def star(a): return np.array([[x.conjugate() if hasattr(x,'conjugate') else x for x in row] for row in a.T],dtype=object)
def character(e,a,sign=-1): return Cyclo.root(e.p,sign*e.absolute_trace(a))
def fourier(e,sign=-1): return np.array([[character(e,e.mul(x,y),sign) for x in range(e.q)] for y in range(e.q)],dtype=object)

def P1(c):
    records=[]
    for p,r in product((2,3,5),range(1,5)):
        e=field(p,r); counts=Counter(e.period[x] for x in range(1,e.q))
        c.check('P1',all(counts[d]==bvalue(d,F(p)) for d in divisors(r)),'actual nonzero exact-period census')
        for t in {F(1),F(6,5),F(3,2),F(2),F(3),F(p)}:
            D=density(e,t)
            if c.red=='mass': D[0]=0
            c.check('P1',sum(D)==t**r and all(x>=0 for x in D),'state normalization and positivity')
            c.check('P1',t==1 or all(x>0 for x in D),'positive interior faithfulness')
            for k in range(r):
                action=[x if c.red=='moment' else e.power(x,p**k) for x in range(e.q)]
                moment=sum(D[x] for x in range(e.q) if action[x]==x)/t**r
                c.check('P1',moment==t**(gcd(r,k)-r),'all Frobenius power moments')
            c.check('P1',sum(D[1:])/t**r==1-t**(-r),'nonzero reference mass')
            if t>1 and r>1:
                moving=sum(D[x] for x in range(e.q) if e.period[x]>1)
                c.check('P1',moving==t**r-t,'moving reference mass')
                for d in divisors(r)[1:]:
                    c.check('P1',sum(D[x] for x in range(e.q) if e.period[x]==d)/moving==bvalue(d,t)/(t**r-t),'conditional FRL period weights')
        c.check('P1',same(density(e,F(p)),np.ones(e.q,dtype=object)),'uniform arithmetic comparison D(p)=I')
        c.check('P1',same(density(e,F(1)),coefficients(e,0)[0]),'zero-ket endpoint')
        A=coefficients(e)
        for k in range(1,7):
            candidate=np.array([F(0) if x==0 else jordan(e.period[x],k)/F(factorial(k))/bvalue(e.period[x],F(p)) for x in range(e.q)],dtype=object)
            if c.red=='jordan': candidate*=k
            c.check('P1',same(A[k],candidate),'independent exponential derivative versus Jordan coefficient')
            c.check('P1',sum(A[k])==F(r**k,factorial(k)) and all(x>0 for x in A[k][1:]),'coefficient trace and nonzero faithfulness')
            normalized=A[k]*F(factorial(k),r**k)
            c.check('P1',sum(normalized)==1,'Poisson component state normalization')
        for k in range(7):
            trace=sum(sum(A[j])*F((-r)**(k-j),factorial(k-j)) for j in range(k+1))
            c.check('P1',trace==int(k==0),'normalized exponential series trace coefficients')
        records.append({'p':p,'r':r,'Q':e.q,'period_counts':dict(counts),'B_nonzero_trace':str(sum(A[1]))})
    c.records['P1']=records

def embedding(k,e,twist=False):
    assert k.p==e.p and e.r%k.r==0
    def evaluate(x):
        out=0
        for v in reversed(k.mod): out=e.add(e.mul(out,x),v)
        return out
    root=next(x for x in range(e.q) if evaluate(x)==0)
    out=[]
    for a in range(k.q):
        value=0
        for v in reversed(k.coords[k.frob[a] if twist else a]): value=e.add(e.mul(value,root),v)
        out.append(value)
    assert len(set(out))==k.q
    assert all(out[k.mul(a,b)]==e.mul(out[a],out[b]) and out[k.add(a,b)]==e.add(out[a],out[b]) for a,b in product(range(k.q),repeat=2))
    return out

def transfer(k,e,emb=None):
    emb=embedding(k,e) if emb is None else emb
    inv={x:a for a,x in enumerate(emb)}; trace=[]
    for x in range(e.q):
        value=0
        for j in range(e.r//k.r): value=e.add(value,e.power(x,k.q**j))
        trace.append(inv[value])
    J=np.zeros((e.q,k.q),dtype=object); B=np.zeros_like(J)
    for a,x in enumerate(emb): J[x,a]=1
    for x,a in enumerate(trace): B[x,a]=1
    assert same(B.T@B,(e.q//k.q)*eye(k.q))
    return emb,trace,J,B

def P2(c):
    records=[]
    samples=[(2,1,2,False),(2,1,3,False),(2,2,4,False),(2,2,4,True),(3,1,2,False),(3,1,3,False)]
    for p,s,r,twist in samples:
        k,e=field(p,s),field(p,r)
        emb,trace,J,B=transfer(k,e,embedding(k,e,twist)); kap=e.q//k.q
        if c.red=='embedding': J[:,1]=J[:,0]
        for t in (F(1),F(6,5),F(p)):
            D,Dk=diag(density(e,t)),diag(density(k,t))
            c.check('P2',same(J.T@D@J,Dk),'named inclusion density restriction')
            c.check('P2',np.trace(J.T@D@J)/t**r==t**(s-r),'code success and conditional state')
        Ae,Ak=coefficients(e),coefficients(k)
        for j in range(7): c.check('P2',same(J.T@diag(Ae[j])@J,diag(Ak[j])),'coefficient inclusion restrictions including finite L-profile')
        CE,CK=fourier(e),fourier(k)
        c.check('P2',same(CE@star(CE),e.q*eye(e.q)),'exact Fourier unitarity')
        c.check('P2',same(CE@J,B@CK) and same(CE@B,kap*J@CK),'actual J/V Fourier amplitude squares')
        D,Dk=diag(density(e,F(6,5))),diag(density(k,F(6,5)))
        dual=CE@D@star(CE)*F(1,e.q)
        if c.red=='fourier-invariance': dual=D
        expected=CK@Dk@star(CK)*F(1,k.q)
        c.check('P2',same(B.T@dual@B*F(1,kap),expected),'Fourier transported code reference')
        QJ,QV=eye(e.q)-J@J.T,eye(e.q)-B@B.T*F(1,kap)
        c.check('P2',same(CE@QJ@D@QJ@star(CE)*F(1,e.q),QV@dual@QV),'Fourier retained failure reference')
        zero=unit(e.q,0,0); dualzero=CE@zero@star(CE)*F(1,e.q)
        c.check('P2',not same(dualzero,zero) and all(x==F(1,e.q) for x in dualzero.flat),'reference Fourier transport is not invariance')
        records.append({'p':p,'s':s,'r':r,'twisted':twist,'degree':r//s,'kappa':kap})
    a,b,e=field(2,1),field(2,2),field(2,4)
    ia=embedding(a,b); ib=embedding(b,e,True); ic=[ib[x] for x in ia]
    _,_,Jab,_=transfer(a,b,ia); _,_,Jbe,_=transfer(b,e,ib); _,_,Jae,_=transfer(a,e,ic)
    c.check('P2',same(Jbe@Jab,Jae),'twisted singular-degree tower matrices')
    for t in (F(1),F(6,5),F(2)):
        D=diag(density(e,t))
        c.check('P2',same(Jab.T@(Jbe.T@D@Jbe)@Jab,Jae.T@D@Jae),'tower reference restriction')
    c.records['P2']=records

def inverse(a):
    n=len(a); rows=[[F(a[i,j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot=next(k for k in range(i,n) if rows[k][i]); rows[i],rows[pivot]=rows[pivot],rows[i]
        scale=rows[i][i]; rows[i]=[x/scale for x in rows[i]]
        for k in range(n):
            if k!=i:
                scale=rows[k][i]; rows[k]=[x-scale*y for x,y in zip(rows[k],rows[i])]
    return np.array([row[n:] for row in rows],dtype=object)

def P3(c):
    k,e=field(2,1),field(2,3); _,_,J,B=transfer(k,e)
    frame=np.column_stack((J,B)); support=frame@inverse(frame.T@frame)@frame.T
    complement=eye(e.q)-support
    c.check('P3',same(complement@complement,complement) and np.trace(support)==4,'actual generic joint-support projection')
    rows=[]
    for t in (F(1),F(6,5),F(3,2),F(2)):
        D=density(e,t); actual=sum(D[i]*complement[i,i] for i in range(e.q))/t**e.r
        old=1-2/t**(e.r-k.r)
        observed=old if c.red=='tracial-complement' else actual
        c.check('P3',observed>=0,'new reference is positive on the actual complement')
        c.check('P3',actual==sum(D[i]*sum(complement[j,i]**2 for j in range(e.q)) for i in range(e.q))/t**e.r,'positive expectation as squared column sum')
        if t==F(6,5): c.check('P3',old<0 and actual>0,'state continuation differs from old tracial continuation')
        rows.append({'t':str(t),'state_complement':str(actual),'old_tracial_complement':str(old)})
    D=density(e,F(6,5)); a=2
    c.check('P3',D[0]!=D[a],'nontracial matrix-unit commutator expectation')
    c.records['P3']=rows

def tensor_series(a,b,limit):
    out=[]
    for k in range(limit+1):
        terms=[np.kron(a[j],b[k-j]) for j in range(k+1) if j<len(a) and k-j<len(b)]
        out.append(sum(terms,np.zeros(len(a[0])*len(b[0]),dtype=object)))
    return out

def word_series(fields,limit=6,profile=False,red=None):
    out=[np.array([F(1)],dtype=object)]+[np.array([F(0)],dtype=object) for _ in range(limit)]
    for i,e in enumerate(fields):
        local=coefficients(e,1 if profile else limit)
        if profile and red=='profile' and i==0: local[1]=2*local[1]
        out=tensor_series(out,local,limit)
    if profile and red=='total-first-order':
        out=[row if k<2 else np.zeros_like(row) for k,row in enumerate(out)]
    return out

def cp_series(K,series): return [K@diag(row)@star(K) for row in series]
def leading(series): return next(((k,a) for k,a in enumerate(series) if np.any(a!=0)),(None,None))

def direct_word_coefficients(fields,limit=6):
    """Expand the PRODUCT as a polynomial in t before t=exp(h), no Cauchy helper."""
    rows=[[] for _ in range(limit+1)]
    for labels in product(*(range(e.q) for e in fields)):
        poly={0:F(1)}
        for e,x in zip(fields,labels):
            local={0:F(1)} if x==0 else {j:F(v)/bvalue(e.period[x],F(e.p)) for j,v in bpoly(e.period[x]).items()}
            merged={}
            for i,a in poly.items():
                for j,b in local.items(): merged[i+j]=merged.get(i+j,0)+a*b
            poly=merged
        for k in range(limit+1): rows[k].append(sum(v*F(j**k,factorial(k)) for j,v in poly.items()))
    return [np.array(row,dtype=object) for row in rows]

def P5(c):
    e=field(2,2); rows=[]
    for m in (1,2,3):
        actual=word_series([e]*m)
        expanded=direct_word_coefficients([e]*m)
        c.check('P5',all(same(a,b) for a,b in zip(actual,expanded)),'positive Cauchy coefficients versus independent product expansion')
        profile=word_series([e]*m,profile=True,red=c.red)
        for grade in range(m+1):
            source=sum((2 if j<grade else 0)*e.q**(m-1-j) for j in range(m))
            K=np.zeros((2,e.q**m),dtype=object); K[0,source]=F(1,3); K[1,source]=F(2,3)
            full=cp_series(K,actual); short=cp_series(K,profile)
            d,A=leading(full); k,B=leading(short)
            c.check('P5',d==grade==k and same(A,B),'finite profile first nonzero matrix coefficient')
            c.check('P5',d<=m and all(np.trace(x)>=0 for x in full),'positive CP coefficient traces and bounded order')
            state=A/np.trace(A)
            c.check('P5',np.trace(state)==1 and same(state@state,state),'conditional leading state is normalized and pure')
            rows.append({'registers':m,'event_order':d,'leading_probability':str(np.trace(A))})
    actual=word_series([e,e]); profile=word_series([e,e],profile=True)
    index=2*e.q+2
    entangler=np.zeros((4,e.q**2),dtype=object)
    entangler[0,index]=entangler[3,index]=F(1,2)
    d,A=leading(cp_series(entangler,actual)); k,B=leading(cp_series(entangler,profile))
    c.check('P5',d==k==2 and same(A,B),'independent references followed by entangling CP map')
    state=A/np.trace(A)
    partial=np.array([[sum(state[2*i+j,2*k+j] for j in range(2)) for k in range(2)] for i in range(2)],dtype=object)
    c.check('P5',same(state@state,state) and same(partial,F(1,2)*eye(2)),'entangled leading Bell density')
    second=np.zeros_like(entangler); second[1,index+1]=F(1,2)
    multi=[a+b for a,b in zip(cp_series(entangler,actual),cp_series(second,actual))]
    multi_short=[a+b for a,b in zip(cp_series(entangler,profile),cp_series(second,profile))]
    d,A=leading(multi); k,B=leading(multi_short)
    c.check('P5',d==k==2 and same(A,B) and np.trace(A)>0,'multiple Kraus branch retains the leading matrix')
    first=unit(16,0,0)+unit(16,index,index); later=unit(16,index,index)
    intermediate=cp_series(first,profile)
    if c.red=='discard-later-rare': intermediate=[intermediate[0]]+[np.zeros_like(x) for x in intermediate[1:]]
    composed=[later@x@later for x in intermediate]
    direct=cp_series(later@first,actual)
    sequential=[later@x@later for x in cp_series(first,actual)]
    c.check('P5',all(same(a,b) for a,b in zip(direct,sequential)),'sequential CP action on every retained coefficient')
    order,A=leading(composed); expected,B=leading(direct)
    c.check('P5',order==expected==2 and same(A,B),'later rare branch survives full finite profile')
    c.check('P5',not np.any(later@intermediate[0]@later) and np.trace(A)==F(1,4),'leading state alone loses the later event')
    # Same nonzero diagonal event, different preparation contexts.
    nzdiag=[j*e.q+j for j in range(1,e.q)]
    independent=[sum(row[j] for j in nzdiag) for row in actual]
    copy=np.zeros((16,4),dtype=object)
    for j in range(4): copy[j*4+j,j]=1
    copied=cp_series(copy,coefficients(e))
    copied_event=[sum(row[j,j] for j in nzdiag) for row in copied]
    c.check('P5',next(k for k,x in enumerate(independent) if x)==2 and next(k for k,x in enumerate(copied_event) if x)==1,'independent diagonal event differs from copied reference')
    c.check('P5',independent[2]==F(3,2) and copied_event[1]==2,'diagonal-event leading coefficients from actual preparations')
    t=F(6,5); D=density(e,t)
    observed=sum(D[j]**2 for j in range(1,4))/t**4
    naive=(t**2-1)/t**4
    c.check('P5',observed!=naive,'mixed reference probabilities are not naive polynomial counts')
    # Coefficient-state tensor weights computed from the independent
    # binomial distribution, including grade zero.
    f=field(2,1); Ae,Af=coefficients(e),coefficients(f)
    tensor=word_series([e,f]); R=e.r+f.r
    for degree in range(7):
        expected=np.zeros(e.q*f.q,dtype=object); total=F(0)
        for j in range(degree+1):
            weight=F(comb(degree,j)*e.r**j*f.r**(degree-j),R**degree)
            total+=weight
            expected+=weight*np.kron(Ae[j]/sum(Ae[j]),Af[degree-j]/sum(Af[degree-j]))
        c.check('P5',total==1 and same(tensor[degree]/sum(tensor[degree]),expected),'Poisson coefficient-state binomial tensor law')
    # Positive process-series representatives, represented on matrix units.
    X=np.array([[0,1],[1,0]],dtype=object); H=np.array([[1,1],[1,-1]],dtype=object)
    phi=[eye(4),np.kron(X,X)]; psi=[eye(4),np.kron(H,H)]
    z,w=[F(1),F(1)],[F(1),F(2)]
    if c.red=='normalizer': w[1]=1
    comp=[eye(4),phi[1]+psi[1],psi[1]@phi[1]]
    denom=[z[0]*w[0],z[0]*w[1]+z[1]*w[0],z[1]*w[1]]
    trace_row=np.array([1,0,0,1],dtype=object)
    c.check('P5',all(same(trace_row@a,b*trace_row) for a,b in zip(comp,denom)),'positive process normalizers multiply coefficientwise')
    h=F(1,3)
    direct=sum((h**j*a for j,a in enumerate(comp)),np.zeros((4,4),dtype=object))/sum(b*h**j for j,b in enumerate(denom))
    evaluated=(psi[0]+h*psi[1])/(1+2*h)@((phi[0]+h*phi[1])/(1+h))
    c.check('P5',same(direct,evaluated),'normalized series evaluation respects CP composition')
    # Multiplying numerator and denominator by 1+3h gives the same map.
    lifted=[phi[0],phi[1]+3*phi[0],3*phi[1]]; zl=[F(1),F(4),F(3)]
    for degree in range(4):
        lhs=sum((zl[j]*phi[degree-j] for j in range(3) if 0<=degree-j<2),np.zeros((4,4),dtype=object))
        rhs=sum((z[j]*lifted[degree-j] for j in range(2) if 0<=degree-j<3),np.zeros((4,4),dtype=object))
        c.check('P5',same(lhs,rhs),'cross-multiplied equality of positive-series representatives')
    c.records['P5']={'branches':rows,'entangled_event_order':2,'later_event_coefficient':'1/4',
      'independent_nonzero_diagonal_order':2,'copied_nonzero_diagonal_order':1,
      'independent_nonzero_diagonal_leading':'3/2','copied_nonzero_diagonal_leading':'2',
      't_6_5_diagonal_probability':str(observed),'naive_point_count_probability':str(naive)}

def P7(c):
    records=[]
    for p in (2,3):
        e=field(p,2); B=coefficients(e,1)[1]; rare=B/F(2)
        column=fourier(e)[:,0]
        denominator=4 if c.red=='erase-characteristic' and p==3 else e.q
        value=born({(i,):a for i,a in enumerate(column)},denominator,{(0,):Cyclo(p,1)},1)
        c.check('P7',value==F(1,p**2),'Fourier-zero Born observable retains characteristic')
        fixed=sum(rare[x] for x in range(1,e.q) if e.period[x]==1)
        moving=sum(rare[x] for x in range(1,e.q) if e.period[x]==2)
        c.check('P7',fixed==moving==F(1,2),'same-degree period masses agree across characteristic')
        records.append({'p':p,'degree':2,'dimension':e.q,'rho_0':'zero ket',
          'nonzero_conditional_fixed_label_weight':str(rare[1]),
          'nonzero_conditional_moving_label_weight':str(rare[p]),
          'conditional_purity':str(sum(x*x for x in rare)),
          'period_mass_fixed':'1/2','period_mass_moving':'1/2','Fourier_zero_return':str(value)})
    c.check('P7',records[0]['conditional_purity']=='3/8' and records[1]['conditional_purity']=='1/6','residual conditional-state purity dependence')
    c.records['P7']={'comparison':records,'scope':'Common degree moments do not identify full endpoints or erase p-dependent arithmetic tables.'}

def vector_map(v,fn):
    out={}
    for x,a in v.items():
        for y,b in fn(x): out[y]=out.get(y,0)+a*b
    return {x:a for x,a in out.items() if a!=0}
def vector_norm(v,den):
    value=sum((a.conjugate()*a for a in v.values()),0)
    return (value.real() if isinstance(value,Cyclo) else F(value))/den
def born(v,den,w,wden):
    value=sum((a.conjugate()*v.get(x,0) for x,a in w.items()),0)
    square=value.conjugate()*value if hasattr(value,'conjugate') else value*value
    return (square.real() if isinstance(square,Cyclo) else F(square))/(den*wden)
def vector_fourier(v,den,e,sign):
    out=vector_map(v,lambda x:[(x[:-1]+(y,),character(e,e.mul(x[-1],y),sign)) for y in range(e.q)])
    return out,den*e.q
def vector_multiply(v,e,table=None):
    return vector_map(v,lambda x:[(x[:-1]+(e.add(x[-1],e.mul(x[0],x[1]) if table is None else table[x[0],x[1]]),),1)])

def find_controls(k,e,trace):
    return next((a,b) for a,b in product(range(1,e.q),repeat=2)
        if trace[e.mul(a,b)]==0 and trace[e.mul(e.power(a,k.q),b)]==1)

def protocol(k,e,emb,trace,a,b,omit=None,prepared=None,phase_bad=False,mul_table=None):
    kap=e.q//k.q
    if prepared is None:
        v={(a,b,y):Cyclo(e.p,1) for y in range(e.q) if trace[y]==0}; den=kap
    else: v,den=prepared
    if omit!='frobenius': v=vector_map(v,lambda x:[((e.power(x[0],k.q),)+x[1:],1)])
    if omit!='multiplication': v=vector_multiply(v,e,mul_table)
    if omit!='fourier': v,den=vector_fourier(v,den,e,1 if phase_bad else -1)
    back={y:x for x,y in enumerate(emb)}
    success={x[:-1]+(back[x[-1]],):a for x,a in v.items() if x[-1] in back}
    failure={x:a for x,a in v.items() if x[-1] not in back}
    success,sden=vector_fourier(success,den,k,1)
    return success,sden,failure,den

def P4(c):
    records=[]
    samples=[(2,1,2),(2,1,3),(2,2,4),(3,1,2),(3,1,3),(5,1,2)]
    for p,s,r in samples:
        k,e=field(p,s),field(p,r); emb,trace,_,_=transfer(k,e); kap=e.q//k.q
        a,b=find_controls(k,e,trace)
        output,den,failure,fden=protocol(k,e,emb,trace,a,b,phase_bad=c.red=='fourier-phase')
        success=vector_norm(output,den)
        c.check('P4',all(x[-1]==1 for x in output) and success==1,'full mixed protocol detects relative Frobenius multiplication and Fourier')
        c.check('P4',vector_norm(failure,fden)==0,'full mixed retained failure branch')
        dephased=F(0); dephased_failure=F(0)
        for y in range(e.q):
            if trace[y]!=0: continue
            out,d,fail,fd=protocol(k,e,emb,trace,a,b,prepared=({(a,b,y):Cyclo(p,1)},1))
            c.check('P4',all(x[-1]==1 for x in out),'dephased successful target label')
            dephased+=vector_norm(out,d)/kap; dephased_failure+=vector_norm(fail,fd)/kap
        observed=dephased if c.red=='coherence' else success
        c.check('P4',observed==1 and dephased==F(1,kap),'coherent trace-fibre target increases decoder success')
        c.check('P4',dephased+dephased_failure==1,'dephased retained outcomes remain normalized')
        variants={}
        for omit in ('frobenius','multiplication','fourier'):
            out,d,fail,fd=protocol(k,e,emb,trace,a,b,omit=omit)
            prob=vector_norm(out,d); failprob=vector_norm(fail,fd)
            c.check('P4',prob+failprob==1,'omitted-gate protocol retains both decoder outcomes')
            if omit=='fourier':
                expected=F(1,kap) if (r//s)%p else F(0)
                c.check('P4',prob==expected,'omitted Fourier distinguishes singular degrees')
                if prob:
                    base_label=next(x for x in range(k.q) if k.mul((r//s)%p,x)==1)
                    ideal={(e.power(a,k.q),b,y):character(k,k.mul(y,base_label),1) for y in range(k.q)}
                    c.check('P4',born(out,d,ideal,k.q)==prob,'omitted Fourier conditional state retains Fourier phase')
                    c.check('P4',all(vector_norm({x:z for x,z in out.items() if x[-1]==y},d)==prob/k.q for y in range(k.q)),'omitted Fourier target is uniform in the computational basis')
            else: c.check('P4',prob==1 and all(x[-1]==0 for x in out),'omitting arithmetic gate changes target one to zero')
            variants[omit]={'success':str(prob),'failure':str(failprob)}
        A=coefficients(e,2); point=[sum(A[i][a]*A[j][b]*coefficients(k,2)[2-i-j][0] for i in range(3) for j in range(3-i))]
        rare=A[1][a]*A[1][b]
        c.check('P4',point[0]==rare>0,'rare mixed preparation order-two coefficient independent of output')
        records.append({'p':p,'q':k.q,'Q':e.q,'a':a,'b':b,'trace_ab':trace[e.mul(a,b)],
          'trace_frobenius_ab':trace[e.mul(e.power(a,k.q),b)],'rare_order':2,'rare_leading':str(rare),
          'full_success':'1','dephased_success':str(dephased),'omitted':variants})
    # Coherent controls are retained through the ENTIRE mixed circuit.
    k,e=field(2,1),field(2,2); emb,trace,_,_=transfer(k,e); a,b=find_controls(k,e,trace); ap=e.power(a,k.q)
    v={(x,b,y):Cyclo(2,1) for x in (a,ap) for y in range(e.q) if trace[y]==0}
    out,den,fail,fd=protocol(k,e,emb,trace,a,b,prepared=(v,2*(e.q//k.q)))
    expected={(ap,b,1):Cyclo(2,1),(a,b,0):Cyclo(2,1)}
    c.check('P4',born(out,den,expected,2)==1 and vector_norm(fail,fd)==0,'coherent control superposition survives full mixed circuit')
    dephased_return=sum(born({x:z},den,expected,2) for x,z in out.items())
    c.check('P4',dephased_return==F(1,2),'full mixed output coherence is measurable')
    # Actual leave-and-return path, with coherent input, not a compressed gate.
    a=2; ap=e.power(a,2)
    initial={(a,a,ap):Cyclo(2,1),(ap,ap,a):Cyclo(2,1)}
    mid=vector_multiply(initial,e)
    retained={x:z for x,z in mid.items() if all(e.period[y]>1 for y in x)}
    rejected={x:z for x,z in mid.items() if not all(e.period[y]>1 for y in x)}
    full=vector_multiply(retained if c.red=='compression' else mid,e)
    c.check('P4',born(full,2,initial,2)==1,'full multiplication return retains intermediate sector leakage')
    c.check('P4',vector_norm(retained,2)==0 and born(vector_multiply(rejected,e),2,initial,2)==1,'retained failure history returns coherently')
    phased={x:z*character(e,e.mul(2,x[0]),1) for x,z in initial.items()}
    c.check('P4',born(phased,2,initial,2)==0,'noncommutative arithmetic phase and rank-one Born witness')
    c.records['P4']={'protocols':records,'coherent_control_return':'1','dephased_output_return':'1/2',
      'full_leakage_return':'1','compressed_return':'0','retained_failure_return':'1','phase_shifted_Born_return':'0'}

def P6(c):
    records=[]
    for p,r in ((2,1),(3,1),(2,2),(3,2)):
        e=field(p,r)
        for d in (1,2,3):
            for t in (F(6,5),F(p)):
                weights=density(e,t)/t**r; active=F(0); gate_trace=F(0); norm=F(0)
                for xs in product(range(e.q),repeat=d):
                    amount=1
                    for x in xs: amount=e.mul(amount,x)
                    required=xs[:-1] if c.red=='arity' and d>1 else xs
                    for z in range(e.q):
                        weight=prod(weights[x] for x in xs)*weights[z]
                        moved=e.add(z,amount)!=z
                        active+=weight*int(all(required)); gate_trace+=weight*int(not moved); norm+=weight*2*int(moved)
                expected=(1-t**(-r))**d
                c.check('P6',active==expected,'actual active control mass and arity')
                c.check('P6',gate_trace==1-expected and norm==2*expected,'weighted multiplication trace and squared difference')
            series=word_series([e]*d,limit=3)
            indices=[sum(x*e.q**(d-1-j) for j,x in enumerate(xs)) for xs in product(range(1,e.q),repeat=d)]
            mass=[sum(row[i] for i in indices) for row in series]
            c.check('P6',next(k for k,x in enumerate(mass) if x)==d and mass[d]==r**d,'interaction arity gives leading order and coefficient')
            records.append({'p':p,'r':r,'arity':d,'order':d,'leading':str(mass[d]),'conditional_squared_difference':'2'})
    k,e=field(2,1),field(2,2); emb,trace,J,B=transfer(k,e); a,b=find_controls(k,e,trace)
    key=(e.power(a,k.q),b)
    table={(x,y):e.mul(x,y) for x,y in product(range(e.q),repeat=2)}
    if c.red=='multiplication-entry': table[key]=0
    out,den,_,_=protocol(k,e,emb,trace,a,b,mul_table=table)
    c.check('P6',all(x[-1]==1 for x in out) and vector_norm(out,den)==1,'actual multiplication-table entry is observable')
    support=J@J.T+np.outer(B[:,1],B[:,1])*F(1,2); complement=eye(4)-support
    w=np.array([0,0,1,-1],dtype=object); v=np.array([1,0,1,-1],dtype=object)
    U=np.zeros((4,4),dtype=object)
    for x in range(4): U[e.frob[x],x]=1
    c.check('P6',same(complement@w,w) and same(U@w,-w),'relative Frobenius survives outside old joint support')
    c.check('P6',F(int(v@U@v)**2,int(v@v)**2)==F(1,9),'relative Frobenius phase against joint sector is measurable')
    leading_mass=F(w@diag(coefficients(e,1)[1])@w,w@w)
    c.check('P6',leading_mass==F(1,2),'outside-joint rare reference mass')
    c.records['P6']={'arity_samples':records,'outside_joint_Born_return':'1/9','outside_joint_order':1,'outside_joint_leading':'1/2',
      'hierarchy_scope':'Order d is an arity diagnostic; exact hierarchy level d+1 is an admitted input, not re-proved by this count.'}

def run(red=None,only=None):
    c=Checks(red)
    targets=[MUTATIONS[red]] if red else ([only] if only else ['P1','P2','P3','P4','P5','P6','P7'])
    try:
        for name in targets: globals()[name](c)
    except Failure as err:
        return {'status':'FAIL','mutation':red,'failed_gate':err.gate,'detail':err.detail,'counts':c.counts}
    return {'status':'PASS','mutation':red,'counts':c.counts,'records':c.records,'scope':'Exact bounded samples only; no universal theorem inferred.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    for name,gate in MUTATIONS.items(): group.add_argument('--red-'+name,dest='red',action='store_const',const=name,help='mutate mathematical data at '+gate)
    parser.add_argument('--only',choices=['P1','P2','P3','P4','P5','P6','P7'],help='run one positive gate group')
    args=parser.parse_args(); result=run(args.red,args.only)
    print(json.dumps(result,indent=2)); return 0 if result['status']=='PASS' else 1

if __name__=='__main__': raise SystemExit(main())
