import numpy as np
import re
from itertools import permutations
import itertools


maskre = re.compile( r"mask = (.+)" )
memre = re.compile( r"mem\[(\d+)\] = (\d+)" )

fin = open( "input.txt" ).read().split( "\n" )

mem = {}
orMask = 0
ftMask = 0
andMask = 0

def parseMask( text ):
    global orMask, ftMask, andMask
    orMask = int( ''.join( [ '1' if x == '1' else '0' for x in text ] ), 2 )
    ftMask = ''.join( [ '1' if x == 'X' else '0' for x in text ] )
    andMask = int( ''.join( [ '0' if x == 'X' else '1' for x in text ] ), 2 )

def mergeMaskedBits( a, b, mask ):
    return a ^ ( ( a ^ b) & mask )

def setMemory( address, value ):
    addr = ( address | orMask ) & andMask
    print( ftMask )
    xCount = ftMask.count( '1' )
    lst = ftMask.split( '1' )
    for i in range( pow( 2, xCount )):
        b = list( format( i, '036b' ) )[ -xCount: ] + [ '' ]
        curr = lst + b
        curr[::2] = lst
        curr[1::2] = b
        mask = int( ''.join( curr ), 2 )
        mem[ addr | mask ] = value

    return

for line in fin:
    m1 = maskre.fullmatch( line )
    if m1:
        parseMask( m1.group( 1 ) )
        continue
    m2 = memre.fullmatch( line )
    if m2:
        setMemory( int( m2.group( 1 ) ), int( m2.group( 2 ) ) )

print( sum( mem.values() ) )