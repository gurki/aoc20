from functools import reduce
import math

lines = open( "input.txt" ).read().split( "\n" )
t0 = int( lines[ 0 ] )
ids = sorted( [ int( x ) for x in lines[ 1 ].split( "," ) if not x == 'x' ] )

print( t0 )
print( ids )

minId = -1
minDelay = math.inf

for i in ids:
    delay = i - t0 % i
    if delay < minDelay:
        minDelay = delay
        minId = i

print( minId, minDelay, minId * minDelay )
