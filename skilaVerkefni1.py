import math

#dæmi 2

def summa(n):
    if n == 1:
        return n
    else:

        return n**2 + summa(n-1)
print(summa(5))

#dæmi 3

def runa(m):
    if m == 1:
        print(m)
    else:
        runa(m - 1)
        print(m*(m+1)/2)
runa(5)

#dæmi4




#dæmi5

def samnefnari(n,m):
    if n==0 or m==0:
        return 0
    else:
        return math.gcd(n,m)
print(samnefnari(8,12))
