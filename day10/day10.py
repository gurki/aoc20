fin = open( "input.txt" )

joltages = sorted( [ 0 ] + list( map( int, fin ) ))
joltages.append( max( joltages ) + 3 )

diffs = list( map( lambda x: x[1] - x[0], zip( joltages, joltages[1:] )))
diffMul = diffs.count( 1 ) * diffs.count( 3 )
print( diffMul )