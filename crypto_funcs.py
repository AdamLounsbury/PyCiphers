#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

# These are functions are used in the affine cipher and RSA cipher

import math
import random


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True  # loop did not find a factor


def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s //= 2
        t += 1

    for i in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            j = 0
            while v != (num - 1):
                if j == t - 1:
                    return False
                else:
                    j += 1
                    v = (v ** 2) % num
    return True


def is_prime(num):
    if num < 2:
        return False  # negative numbers, 0, and 1 are not primes

    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                  139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                  229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                  317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                  421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
                  521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
                  619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
                  733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                  839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
                  953, 967, 971, 977, 983, 991, 997]

    if num in low_primes:
        return True

    for prime in low_primes:  # check if any low primes can divide num
        if num % prime == 0:
            return False

    return rabin_miller(num)  # if none of the above works, call rabin miller algorithm


def generate_prime(key_size=1024):
    while True:
        num = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if is_prime(num):
            return num
