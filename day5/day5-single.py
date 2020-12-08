from functools import reduce 
print( max( map( lambda line: int( line.strip().translate( str.maketrans( { 'B': '1', 'F': '0', 'R': '1', 'L': '0' } )), 2 ), open( "input.txt" ) )))

seta = set( range( 128 * 8 ) )
setb = map( 
    lambda line: int( line.strip().translate( str.maketrans( { 'B': '1', 'F': '0', 'R': '1', 'L': '0' } )), 2 ), 
    open( "input.txt" ) 
)

print( list( seta.intersection( setb ) )[ 1 ] )