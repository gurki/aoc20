fin = open( "input.txt" )

joltages = sorted( [ 0 ] + list( map( int, fin ) ))
joltages.append( max( joltages ) + 3 )

# part 1

diffs = list( map( lambda x: x[1] - x[0], zip( joltages, joltages[1:] )))
diffMul = diffs.count( 1 ) * diffs.count( 3 )
print( "part1:", diffMul )

#  part 2

counts = list( map( lambda x: 0, joltages ) )

def countCombinations( jolts, fromId, counts ):
    if fromId < 0:
        return
    val0 = jolts[ fromId ]
    for index in range( fromId + 1, len( jolts ) - 1 ):
        if jolts[ index ] - val0 > 3:
            break
        counts[ fromId ] += counts[ index ]

for index in range( len( joltages ) - 2, len( joltages ) ):
    counts[ index ] = 1

for index in range( len( joltages ) - 3, -1, -1 ):
    countCombinations( joltages, index, counts )

print( "part2: ", counts[ 0 ] )