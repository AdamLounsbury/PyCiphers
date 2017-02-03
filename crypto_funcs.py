#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

# These are functions are used in the affine cipher


def gcd(a, b):
    """Calculate the greatest common divisor for two numbers."""

    while a != 0:
        a, b = b % a, a
    return b


def mod_inverse(a, m):
    """Determine the mod inverse of a number using the extended Euclidean algorithm."""

    if gcd(a, m) != 1:
        return None

    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, m

    while y3 != 0:
        q = x3 // y3
        y1, y2, y3, x1, x2, x3 = (x1 - q * y1), (x2 - q * y2), (x3 - q * y3), y1, y2, y3

    return x1 % m
