fin = open( "example.txt" )

joltages = sorted( [ 0 ] + list( map( int, fin ) ))
joltages.append( max( joltages ) + 3 )

diffs = list( map( lambda x: x[1] - x[0], zip( joltages, joltages[1:] )))
diffMul = diffs.count( 1 ) * diffs.count( 3 )
print( "part1:", diffMul, "\n" )

counted = set()
print( joltages )

def countArrangements( joltages ):
    print( joltages )
    if len( joltages ) < 2:
        return 0
    if joltages[ 0 ] in counted:
        return 0
    counted.add( joltages[ 0 ] )
    diff = joltages[ 1 ] - joltages[ 0 ]
    if diff > 3:
        return countArrangements( joltages[ 1: ] )
    else:
        opt1 = countArrangements( joltages[ 1: ] )
        opt2 = countArrangements( [ joltages[0] ] + joltages[ 2: ] )
        return 1 + opt1 + opt2

totalCount = countArrangements( joltages )

print( totalCount )


# [0 4] 5 6 7
#   [4 5] 6 7
#     [4 6] 7
#       [4 7]
#       [6 7]
#     [5 6] 7
#         [6 7]
#         [5 7]