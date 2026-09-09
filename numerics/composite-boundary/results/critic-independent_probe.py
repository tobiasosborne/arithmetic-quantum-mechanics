#!/usr/bin/env python3
"""Critic recomputation. Independent polynomial arithmetic and integer matrices.
No imports from the prover or verifier. All assertions are exact. --red changes
an expected experimental probability, giving a reachable data falsifier.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd
import json
import numpy as np


def mu(n):
    sign, d = 1, 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            sign *= -1
            if n % d == 0:
                return 0
        d += 1
    return -sign if n > 1 else sign


def c(d, t):
    return sum(mu(d//a)*t**a for a in range(1,d+1) if d % a == 0)


def phi(d):
    return sum(gcd(a,d)==1 for a in range(1,d+1))


class Field:
    def __init__(self, p, f):
        self.p,self.f,self.r = p,tuple(f),len(f)-1
        self.labels=list(product(range(p),repeat=self.r))
        self.q=len(self.labels)
        self.lookup={a:i for i,a in enumerate(self.labels)}
        self.zero=self.lookup[(0,)*self.r]
        self.one=self.lookup[(1,)+(0,)*(self.r-1)]
        self.plus=np.empty((self.q,self.q),dtype=int)
        self.times=np.empty_like(self.plus)
        for a,A in enumerate(self.labels):
            for b,B in enumerate(self.labels):
                self.plus[a,b]=self.lookup[tuple((x+y)%p for x,y in zip(A,B))]
                coeff=[0]*(2*self.r-1)
                for i,x in enumerate(A):
                    for j,y in enumerate(B):
                        coeff[i+j]=(coeff[i+j]+x*y)%p
                while len(coeff)>self.r:
                    x=coeff.pop()
                    offset=len(coeff)-self.r
                    for j,y in enumerate(f[:-1]):
                        coeff[offset+j]=(coeff[offset+j]-x*y)%p
                self.times[a,b]=self.lookup[tuple(coeff)]
        self.minus=[self.lookup[tuple(-x%p for x in A)] for A in self.labels]
        assert all(self.pow(a,self.q-1)==self.one for a in range(1,self.q))
        self.abs=[self.pow(a,p) for a in range(self.q)]
        self.period=[self.orbit(a,self.abs) for a in range(self.q)]
        self.trace=[]
        for a in range(self.q):
            b,acc=a,self.zero
            for _ in range(self.r):
                acc=self.plus[acc,b]
                b=self.abs[b]
            assert all(x==0 for x in self.labels[acc][1:])
            self.trace.append(self.labels[acc][0])

    def pow(self,a,k):
        value=self.one
        while k:
            if k&1: value=self.times[value,a]
            a=self.times[a,a]
            k//=2
        return int(value)

    def orbit(self,a,perm):
        result=[a]
        b=perm[a]
        while b!=a:
            result.append(b)
            b=perm[b]
        return tuple(result)

    def diagonal(self,t):
        result=[]
        for a,O in enumerate(self.period):
            d=len(O)
            top=t-1 if d==1 else c(d,t)
            bot=self.p-1 if d==1 else c(d,self.p)
            result.append(F(1) if a==self.zero else F(top,bot))
        return result


def case(p,polynomial,s,red=False):
    e=Field(p,polynomial)
    q,n=e.q,e.r//s
    sigma=[e.pow(a,p**s) for a in range(q)]
    periods=[e.orbit(a,sigma) for a in range(q)]
    orbits=sorted(set(tuple(sorted(O)) for O in periods))
    triples=list(product(range(q),repeat=3))
    idx={a:i for i,a in enumerate(triples)}
    # Reversible multiplication and middle Frobenius are composed as actual
    # permutations independently of the predicted relative graph shift.
    m=np.array([idx[x,y,int(e.plus[z,e.times[x,y]])] for x,y,z in triples])
    inv=np.argsort(m)
    mid=np.array([idx[x,sigma[y],z] for x,y,z in triples])
    relative=m[mid[inv]]
    delta=np.array([idx[sigma[x],sigma[y],sigma[z]] for x,y,z in triples])
    labels=[]
    columns=[]
    for O in orbits:
        for k in range(len(O)):
            column=np.zeros(q**3,dtype=np.int64)
            for x in O:
                y=x
                for _ in range(k): y=sigma[y]
                column[idx[x,y,int(e.times[x,y])]]=1
            labels.append((O,k))
            columns.append(column)
    W=np.stack(columns,axis=1)
    norms=np.array([len(O) for O,k in labels])
    assert np.array_equal(W.T@W,np.diag(norms)), 'exact graph Gram'
    assert np.array_equal(W[delta],W), 'diagonal fixed code'
    actual=W.T@W[np.argsort(relative)]
    predicted=np.zeros((q,q),dtype=np.int64)
    for j,(O,k) in enumerate(labels):
        predicted[labels.index((O,(k+1)%len(O))),j]=len(O)
    assert np.array_equal(actual,predicted), 'actual relative matrix'
    primitive=[a for a,O in enumerate(periods) if len(O)==n]
    C=np.zeros((q**3,q),dtype=np.int64)
    for a in primitive: C[idx[a,a,int(e.times[a,a])],a]=1
    A=np.zeros_like(C)
    powers=np.arange(q**3)
    for _ in range(n):
        A+=C[np.argsort(powers)]
        powers=delta[powers]
    assert np.array_equal(A.T@A+(n*C-A).T@(n*C-A),n*n*(C.T@C)), 'complete retained averaging instrument on coherent inputs'
    q1=[j for j,(O,k) in enumerate(labels) if len(O)==n and k==1]
    W1=W[:,q1]
    out=A[np.argsort(relative)]
    success_diag=[F(int(x),n*n) for x in np.sum(A*A,axis=0)]
    effect=W1.T@out
    final_diag=[F(int(x),n**3) for x in np.sum(effect*effect,axis=0)]
    identity_diag=[F(int(x),n**3) for x in np.sum((W1.T@A)**2,axis=0)]
    # Projector diagonal on each tuple is 1/n; a dephased density has no
    # cross terms. Compute its support incidence independently of amplitudes.
    pdiag=np.sum(W1*W1,axis=1)
    dephased_diag=[F(int(x),n**3) for x in pdiag@(out*out)]
    expected_full=F(0) if red else F(1)
    event_records=[]
    for t in (F(1),F(6,5),F(3,2),F(p)):
        D=e.diagonal(t)
        assert sum(D)==t**e.r
        w=sum(D[a]*success_diag[a] for a in range(q))/t**e.r
        assert w==c(n,t**s)/(n*t**e.r), 'weighted primitive success'
        branches=[sum(D[a]*probe[a] for a in range(q))/t**e.r for probe in (final_diag,identity_diag,dephased_diag)]
        if t>1:
            assert [x/w for x in branches]==[expected_full,F(0),F(1,n)], 'full/identity/dephased probability data'
        primitive_mass=sum(D[a] for a in primitive)/t**e.r
        histories=[1-primitive_mass,primitive_mass-w,branches[0],w-branches[0]]
        assert sum(histories)==1
        event_records.append({'t':str(t),'w':str(w),'finals':list(map(str,branches)),'histories':list(map(str,histories))})
    B=[F(0) if a==e.zero else F(phi(len(O)),p-1 if len(O)==1 else c(len(O),p)) for a,O in enumerate(e.period)]
    coefficient=sum(B[a]*success_diag[a] for a in range(q))
    assert coefficient==F(s*phi(n),n)
    # Fourier compression using exact root-of-unity coefficient counts. A
    # length-p coefficient vector is zero modulo Phi_p iff entries coincide.
    primitive_columns=[j for j,(O,k) in enumerate(labels) if len(O)==n]
    phase_exponents=set()
    for i in primitive_columns:
        for j in primitive_columns:
            coeff=[0]*p
            for a in np.flatnonzero(W[:,i]):
                x,y,z=triples[a]
                for b in np.flatnonzero(W[:,j]):
                    u,v,w=triples[b]
                    if (y,z)==(v,w): coeff[-e.trace[e.times[x,u]]%p]+=1
            x=labels[j][0][0]
            exponent=-e.trace[e.times[x,x]]%p
            phase_exponents.add(exponent)
            if i==j: coeff[exponent]-=n
            assert len(set(coeff))==1, 'actual cyclotomic Fourier matrix'
    permutation=np.argmax(predicted,axis=0)
    rpow=np.arange(q)
    traces=[]
    channel_traces=[]
    for j in range(n+1):
        trace=int(np.count_nonzero(rpow==np.arange(q)))
        actual_channel=sum(rpow[a]==a and rpow[b]==b for a,b in product(range(q),repeat=2))
        assert trace==(p**s)**gcd(n,j)
        assert actual_channel==trace*trace
        traces.append(trace)
        channel_traces.append(int(actual_channel))
        rpow=permutation[rpow]
    multiplicities=Counter(len(O) for O in orbits)
    moving={d:F(s*phi(d),d) for d in multiplicities if d>1}
    weights={d:str(w/sum(moving.values())) for d,w in moving.items()}
    return {'p':p,'absolute_degree':e.r,'base_degree':s,'relative_degree':n,'orbit_multiplicities':dict(multiplicities),'integer_graph_dimension':q,'grade_one':str(coefficient),'full_identity_dephased':[str(expected_full),'0',str(F(1,n))],'events':event_records,'fourier_phase_exponents':sorted(phase_exponents),'fourier_probability':str(F(1,q)),'implementer_traces':traces,'full_channel_traces':channel_traces,'moving_boundary_weights':weights}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--red',action='store_true')
    args=parser.parse_args()
    fibres=[(2,[1,1,1],1),(3,[1,0,1],1),(2,[1,1,0,0,1],1),(2,[1,1,0,0,1],2),(2,[1,1,0,1],1),(3,[1,2,0,1],1)]
    results=[case(*entry,red=args.red) for entry in fibres]
    print(json.dumps({'status':'PASS','arithmetic':'integer and rational; exact cyclotomic coefficient counts','tolerance':None,'fibres':results},indent=2))


if __name__=='__main__': main()
