import re
from functools import reduce

fin = open( "input.txt" )
regex = re.compile( r"(\d+)-(\d+)\s(\w):\s(\w*)" )

def verifyLine( line ):
    stripped = line.strip()
    match = regex.fullmatch( stripped )
    return verify(
        int( match.group( 1 ) ),
        int( match.group( 2 ) ),
        match.group( 3 ),
        match.group( 4 )
    )

def verify( min, max, letter, string ):
    count = string.count( letter )
    return ( count >= min ) and ( count <= max )

count = reduce( lambda count, line: count + verifyLine( line ), fin, 0 )
print( count )