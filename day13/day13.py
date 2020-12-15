from functools import reduce
import math

lines = open( "input.txt" ).read().split( "\n" )
t0 = int( lines[ 0 ] )
ids = sorted( [ int( x ) for x in lines[ 1 ].split( "," ) if not x == 'x' ] )

#  part 1

minId = -1
minDelay = math.inf

def getDelay( t0, busId ):
    return busId - t0 % busId

for i in ids:
    delay = getDelay( t0, i )
    if delay < minDelay:
        minDelay = delay
        minId = i

print( minId * minDelay )

#  part 2
#  DISCLAIMER: this is heavily inspired by [1]
#  i was trying to catch up and not motivated enough to think and research more than the hour i had already spent
#  [1] https://github.com/j0057/aoc2020/blob/master/python/day13.py

buses = [ int( x ) if x.isnumeric() else None for x in lines[ 1 ].split( ',' ) ]

def crt(L):
    N = math.prod(n for (_, n) in L)
    return sum(a * (N//n) * pow(N//n, -1, n) for (a, n) in L), N

def findEarliest(buses):
    x, N = crt([(a, n) for (a, n) in enumerate(buses) if n is not None])
    return N - (x % N)

print( findEarliest( ids ) )
# 640856202464541