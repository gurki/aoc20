import re
from functools import reduce


fin = open( "input.txt" )
regex = re.compile( r"(\d+)-(\d+)\s(\w):\s(\w*)" )


def verifyLine( line, fn ):
    match = regex.fullmatch( line.strip() )
    return fn(
        int( match.group( 1 ) ),
        int( match.group( 2 ) ),
        match.group( 3 ),
        match.group( 4 )
    )


def verify( min, max, letter, string ):
    count = string.count( letter )
    return ( count >= min ) and ( count <= max )


def verifyToboggan( fst, snd, letter, string ):
    count = ( string[ fst - 1 ] == letter ) + ( string[ snd - 1 ] == letter )
    return ( count == 1 )


countA = reduce( lambda count, line: count + verifyLine( line, verify ), fin, 0 )
print( countA )

fin.seek( 0, 0 )

countB = reduce( lambda count, line: count + verifyLine( line, verifyToboggan ), fin, 0 )
print( countB )