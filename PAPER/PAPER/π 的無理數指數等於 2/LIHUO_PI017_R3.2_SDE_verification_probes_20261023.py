#!/usr/bin/env python3
"""Small independent checks for LIHUO PAPER-017 R3.2 (NOT Lean proof verification).

Uses sympy for an intentionally invalid-premise interpolation negative control.
Do not mistake finite tests for proof of an asymptotic theorem.
"""
import math
import sympy as sp


def parameter_feasibility():
    nu, b, delta, eta = 2.2, 0.52, 0.01, 0.0001
    theta = 1 - delta
    A = 1 - b * delta
    C = (A/theta + 1/A) / 2
    B = (A + min(1/C, C*theta)) / 2
    g = nu * (A * (1 - eta) - theta) - (1 - theta)
    eps0 = min(g/2, .5)
    F0 = math.ceil(max(2/theta, 3*nu/eps0)) + 1
    tests = {
      'theta < A < B < 1': 0 < theta < A < B < 1,
      'A^2 < theta': A*A < theta,
      'C > 1': C > 1,
      'CB < 1': C*B < 1,
      'Ctheta/B > 1': C*theta/B > 1,
      'B/A > 1': B/A > 1,
      'g > 0': g > 0,
      'F0 > 2/theta': F0 > 2/theta,
      'nu/F0 < eps0/3': nu/F0 < eps0/3
    }
    print('Parameter existence probe | nu =',nu,'b =',b,'delta =',delta,'eta =',eta)
    print('theta %.12g A %.12g B %.12g C %.12g g %.12g F0 %d' % (theta,A,B,C,g,F0))
    for k,v in tests.items():print('  ',k,'=',v)
    assert all(tests.values())
    for m in (1000,100000,1000000):
        c=math.log(2)/4
        logcL = math.log(c)+2*math.log(eta)+m*math.log(B/A)-math.log(2*(m+1))
        print(' m =',m,'log(cL)=',round(logcL,6),'cL > 2:',logcL > math.log(2))


def deliberately_invalid_weight_negative_control():
    # Theorem's necessary volume inequalities: K*theta^m = 0.8 < 1,
    # K*(w0/v0)*theta^m = 0.4 < 1.
    # However w1=6 does not meet the theorem's successive separation
    # threshold. For sigma=0.01, m=1, L0=3, C*=600 and w1> C* v0=1200
    # is one explicit *sufficient* separation condition.
    H,w0,w1,v0,v1 = 16,1,6,2,15
    centers=[sp.Integer(0),sp.Integer(1)]
    t=sp.symbols('t')
    logt=sum(sp.Rational((-1)**(k+1),k)*t**k for k in range(1,8))
    columns=[(h,a) for a in range(H//w1+1) for h in range(H-w1*a+1)]
    rows=[(j,s,b) for j in range(len(centers))
          for b in range(2) for s in range(H//v0+1) if v0*s+v1*b<H]
    coefficients={}
    for j,c in enumerate(centers):
        for h,a in columns:
            for beta in range(min(a,1)+1):
                poly=sp.Poly((1+t)**h*(c+logt)**(a-beta),t)
                for s in range(8):
                    coefficients[(j,h,a,s,beta)] = sp.binomial(a,beta)*poly.nth(s)
    matrix=sp.Matrix([[coefficients.get((j,h,a,s,beta),0)
                       for h,a in columns] for j,s,beta in rows])
    rank=matrix.rank()
    print('Toy interpolation: K=2, m=1, theta=2/5, w0=1,v0=2,w1=6,v1=15,H=16')
    print(' volume inequalities satisfied: ',2*2/5<1,2*(1/2)*(2/5)<1)
    print(' strict separation fails: w1=6 is NOT > 600*v0=1200')
    print(' matrix shape',matrix.shape,'exact rational rank',rank,'surjective',rank==len(rows))
    assert (len(rows), len(columns), rank)==(18,33,17)
    print(' Interpretation: not a counterexample; admissibility and sufficiently large H are missing.')


if __name__=='__main__':
    parameter_feasibility()
    deliberately_invalid_weight_negative_control()
    print('PASS: probe scripts reproduced expected scoped checks. NOT a Lean kernel receipt.')
