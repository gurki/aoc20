from itertools import combinations

fin = open( "input.txt" )
xmas = list( map( int, fin ) )

def isPrevSum( vals, pre, curr ):
    return any( map(
        lambda x: x[0] + x[1] == vals[curr],
        combinations( vals[ curr - pre : curr ], 2 )
    ))

def validate( vals, pre ):
    return [ vals[ curr ] for curr in range( pre, len( vals ) ) if not isPrevSum( vals, pre, curr ) ]

print( validate( xmas, 25 ) )
magic = 15690279

def findContiguousFrom( vals, index, magic ):
    total = 0
    offset = 0
    while total < magic:
        total += vals[ index + offset ]
        offset += 1
    if total == magic and offset > 1:
        return min( vals[ index : index + offset ] ) + max( vals[ index : index + offset ] )
    return 0

def findContiguous( vals, magic ):
    return list( filter( lambda x: x > 0, [ findContiguousFrom( vals, i, magic ) for i in range( len( vals ) - 1 ) ] ))

print( findContiguous( xmas, magic ) )
