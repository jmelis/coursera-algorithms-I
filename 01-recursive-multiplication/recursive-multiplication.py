#!/usr/bin/env python2

import sys

from random import randint
from math import ceil

def multiply(a,b):
    a_len = len(str(a))
    b_len = len(str(b))

    m = max(a_len, b_len)

    if m == 1:
        return a*b

    m_h = int(ceil(float(m)/2))

    a_str = str(a).zfill(m)
    b_str = str(b).zfill(m)

    a0, a1 = int(a_str[:m-m_h]), int(a_str[-m_h:])
    b0, b1 = int(b_str[:m-m_h]), int(b_str[-m_h:])

    a0_b0 = multiply(a0,b0)
    a0_b1 = multiply(a0,b1)
    a1_b0 = multiply(a1,b0)
    a1_b1 = multiply(a1,b1)

    return (10**(2*m_h)*a0_b0 + 10**m_h*(a0_b1+a1_b0) + a1_b1)

args = len(sys.argv)

if args == 2:
    n = m = int(sys.argv[1])
elif args == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
else:
    n = m = 3

a = randint(10**(n-1), 10**n-1)
b = randint(10**(m-1), 10**m-1)

print "a =",a
print "b =",b
print "m =",a*b

recursive_m = multiply(a,b)

if a*b == recursive_m:
    print "correct"
else:
    print "wrong(%i)"
    print "r =",recursive_m
