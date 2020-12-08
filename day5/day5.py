import numpy as np

fin = open( "input.txt" )
seats = np.zeros( ( 127, 8 ) )
maxSid = -1
rowTrans = str.maketrans( { 'B': '1', 'F': '0' } )
colTrans = str.maketrans( { 'R': '1', 'L': '0' } )
trans = str.maketrans( { 'B': '1', 'F': '0', 'R': '1', 'L': '0' } )

for line in fin:
    row = int( line[0:7].translate( rowTrans ), 2 )
    col = int( line[7:10].translate( colTrans ), 2 )
    seats[ row ][ col ] = 1
    maxSid = max( row * 8 + col, maxSid )


print( maxSid )
hot = False

for row, col in np.ndindex(( 127, 8 )):
    if seats[ row ][ col ]: 
        hot = True; continue
    elif hot:
        print( row * 8 + col ); exit()