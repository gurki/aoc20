from itertools import product
import numpy as np

layout = np.array( list( map( list, open( "input.txt" ).read().split( "\n" ))))

def isOccupied( layout, idx ):
    if idx[ 0 ] < 0 or idx[ 0 ] >= layout.shape[ 0 ]:
        return False
    if idx[ 1 ] < 0 or idx[ 1 ] >= layout.shape[ 1 ]:
        return False
    return layout[ idx ] == "#"


def findFirstOccupied( layout, idx, offs ):
    if idx[ 0 ] < 0 or idx[ 0 ] >= layout.shape[ 0 ]:
        return False
    if idx[ 1 ] < 0 or idx[ 1 ] >= layout.shape[ 1 ]:
        return False
    if layout[ idx ] == ".":
        return findFirstOccupied( layout, ( idx[ 0 ] + offs[ 0 ], idx[ 1 ] + offs[ 1 ] ), offs )
    return layout[ idx ] == "#"


def occupiedNeighbours( layout, idx ):
    count = 0
    for offs in product( [ -1, 0, 1 ], repeat=2 ):
        if offs == ( 0, 0 ): continue
        count += isOccupied( layout, ( idx[ 0 ] + offs[ 0 ], idx[ 1 ] + offs[ 1 ] ))
    return count


def occupiedSight( layout, idx ):
    count = 0
    for offs in product( [ -1, 0, 1 ], repeat=2 ):
        if offs == ( 0, 0 ): continue
        count += findFirstOccupied( layout, ( idx[ 0 ] + offs[ 0 ], idx[ 1 ] + offs[ 1 ] ), offs )
    return count


def update( prev ):
    curr = prev.copy()
    for idx, x in np.ndenumerate( layout ):
        if x == ".": continue
        occ = occupiedSight( layout, idx )
        if x == "L" and occ == 0:
            curr[ idx ] = "#"
        if x == "#" and occ >= 5:
            curr[ idx ] = "L"
    return curr


curr = []
anyChange = True

print( "initial:\n", layout )
print( "\n" )

iter = 0
while anyChange:
# for iter in range( 10 ):
    iter += 1
    print( "iter", iter )
    curr = update( layout )
    print( "curr:\n", curr )
    anyChange = not np.array_equal( curr, layout )
    layout = curr.copy()
    print( "\n" )

print( np.count_nonzero( layout == "#" ) )