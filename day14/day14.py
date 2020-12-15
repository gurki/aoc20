import numpy as np
import re

maskre = re.compile( r"mask = (.+)" )
memre = re.compile( r"mem\[(\d+)\] = (\d+)" )

fin = open( "input.txt" ).read().split( "\n" )

mem = {}
mask = 0
maskedBits = 0

def parseMask( text ):
    global maskedBits
    global mask
    maskedBits = int( ''.join( [ '0' if x == 'X' else x for x in text ] ), 2 )
    mask = int( ''.join( [ '0' if x == 'X' else '1' for x in text ] ), 2 )

def mergeMaskedBits( a, b, mask ):
    return a ^ ( ( a ^ b) & mask )

def setMemory( address, value ):
    mem[ address ] = mergeMaskedBits( value, maskedBits, mask )

for line in fin:
    m1 = maskre.fullmatch( line )
    if m1:
        parseMask( m1.group( 1 ) )
        continue
    m2 = memre.fullmatch( line )
    if m2:
        setMemory( int( m2.group( 1 ) ), int( m2.group( 2 ) ) )

print( sum( mem.values() ) )