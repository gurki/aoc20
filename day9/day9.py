from itertools import combinations

fin = open( "input.txt" )
xmas = list( map( int, fin ) )

def isPrevSum( vals, pre, curr ):
    return any( map(
        lambda x: x[0] + x[1] == vals[curr],
        combinations( vals[ curr - pre : curr ], 2 )
    ))

def validate( vals, pre ):
    for curr in range( pre, len( vals ) ):
        print( vals[ curr ], isPrevSum( vals, pre, curr ) )

validate( xmas, 25 )