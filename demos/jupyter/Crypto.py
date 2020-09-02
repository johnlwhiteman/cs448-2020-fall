import math
import random
import re

def genLcg(seed, a, c, m, n=None, stopOnDup=True):
    genLcg.state = 'active'
    genLcg.count = 0
    x = int(seed)
    tracker = {x: 1}
    while True:
        x = ((x * a) + c) % m
        yield x
        genLcg.count += 1
        if not n is None and genLcg.count >= n:
            genLcg.state = 'stopped'
            break
        if stopOnDup:
            if x in tracker:
                genLcg.state = 'duplicate'
                break
            else:
                tracker[x] = 1

def genMsm(seed, length=None, n=None, stopOnDup=True):
    genMsm.state = 'active'
    genMsm.count = 0
    x = str(seed)
    tracker = {x: 1}
    if None is length:
        length = len(x)
    r = math.ceil(length / 2)
    while True:
        x = str(int(x)**2)[r:length+r].rjust(length, "0")
        yield x
        genMsm.count += 1
        if 0 == int(x):
            genMsm.state = 'converged'
            break
        if not n is None and genMsm.count >= n:
            genMsm.state = 'stopped'
            break
        if stopOnDup:
            if x in tracker:
                genMsm.state = 'duplicate'
                break
            else:
                tracker[x] = 1

def getBinStr(c):
    return re.sub('0b', '', bin(ord(c))).rjust(8,'0')

def getDivisors(n):
    divisors = [i for i in range(1, n // 2 + 1) if 0 == n % i]
    divisors.append(n)
    return divisors

def getGCD(n1, n2):
    if n1 == n2:
        return n1
    if n1 > n2:
        tmp = n2
        n2 = n1
        n1 = tmp
    divisors = getDivisors(n1)
    if divisors is None:
        return None
    divisors.reverse()
    for divisor in divisors:
        if 0 == n2 % divisor:
            return divisor
    return None

def getRandomNumber(min, max):
    return random.randint(min, max)

def isCoprime(n1, n2):
    return (1 == getGCD(n1, n2))

def isPrime(n):
   if n < 2 or 0 == n % 2:
        if n == 2:
            return True
        return False
   for i in range(2, n // 2):
      if 0 == n % i:
         return False
   return True

def isRelativelyPrime(n1, n2):
    return (isCoprime(n1, n2))

if __name__ == "__main__":
    n = []
    for i in range(0, 12):
       n.append(getRandomNumber(1, 6))
    #print(n)