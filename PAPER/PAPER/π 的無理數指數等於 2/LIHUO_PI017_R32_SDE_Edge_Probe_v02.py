#!/usr/bin/env python3
"""Reproducible, local, finite identity checks, not a proof of global interpolation or Lean kernel receipt."""
import sympy as sp

# Coefficient-level test of the exact translation in determinant.tex lines 196-218.
t,u,r,omega=sp.symbols('t u r omega')
log3=t-t**2/sp.Integer(2)+t**3/sp.Integer(3)
G=t-t**2/sp.Integer(2)
tau=G-log3
checks=0
for h in (0,1,2):
    for alpha in (0,1,2,3):
        for beta in range(alpha+1):
            for j in (0,1,2):
                # Identity of u^beta coefficients BEFORE extracting t^s,
                # with distinct near-period r and exact period omega.
                left=sp.binomial(alpha,beta)*(1+t)**h*(j*r+G)**(alpha-beta)
                right=sum(sp.binomial(a,beta)*sp.binomial(alpha,a)*(1+t)**h*(j*omega+log3)**(alpha-a)
                          *(j*(r-omega)+tau)**(a-beta)
                          for a in range(beta,alpha+1))
                difference=sp.Poly(sp.expand(left-right),t)
                assert difference.is_zero,(h,alpha,beta,j)
                checks+=4 # coefficients t^0... t^3 tested via exact polynomial identity
print('Exact-row-translation symbolic zero-differences (h, alpha, beta, j × t^0..t^3):',checks)
print('Near-period and exact-period independent symbols:',r,omega)
print('Taylor tail tau =',tau)

# Check determinant comparison key inequality as an arithmetic implication.
# For t=mean bbar in [0,theta], g>0,
# ν*(A*(1-eta)-bbar)-(1-bbar) >= g.
nu,A,eta,theta,bbar=sp.symbols('nu A eta theta bbar', real=True)
lhs=nu*(A*(1-eta)-bbar)-(1-bbar)
gap=nu*(A*(1-eta)-theta)-(1-theta)
print('Determinant gap difference exact factorization =',sp.factor(lhs-gap))
assert sp.simplify(lhs-gap-(nu-1)*(theta-bbar))==0

# Exhibit rational parameter witnesses from conclusion.tex for nu=3.
from fractions import Fraction as F
nu=F(3); b=F(3,5); delta=F(1,20); theta=1-delta; A=1-b*delta
# C strictly within (A/theta,1/A). B strictly within (A, min(1/C,C*theta)).
C=(A/theta+1/A)/2
B=(A+min(1/C,C*theta))/2
eta=F(1,10000)
g=nu*(A*(1-eta)-theta)-(1-theta)
check={
 '0<theta<A<B<1':0<theta<A<B<1,
 'nu(A-theta)>1-theta':nu*(A-theta)>1-theta,
 'C>1':C>1,
 'B<1/C':B<1/C,
 'B<Ctheta<1':B<C*theta<1,
 'A²<theta':A*A<theta,
 'g>0':g>0,
 'CB<1':C*B<1,
 'Ctheta/B>1':C*theta/B>1,
 'B/A>1':B/A>1,
}
assert all(check.values()),check
print('Rational parameter witness:',dict(nu=str(nu),theta=str(theta),A=str(A),B=str(B),C=str(C),eta=str(eta),g=str(g)))
print('Parameter inequalities:',check)

# Rank test from the prior report: an intentionally invalid sufficient-condition case.
# Exact rank rechecked separately in prior 2026-10-23 log.
print('STATUS: scoped identities and finite parameter feasibility PASS. Not an interpolation theorem proof.')

# A-E is represented as a positive combination of A-(1+σ)E (nef)
# and aA-E (ample), per interpolation.tex around lines 525-534.
a,sigma,HH,EE=sp.symbols('a sigma HH EE', real=True)
den=a*(1+sigma)-1
convex_rhs=(a-1)/den*(HH-(1+sigma)*EE)+sigma/den*(a*HH-EE)
assert sp.cancel(convex_rhs-(HH-EE))==0
print('Blow-up A-E numerical identity: exact symbolic zero difference; coefficients positive if a>1, sigma>0.')
