from itertools import product
import numpy as np
import plotly.express as px


def printVoxels( voxels ):
    lsts = list( zip( *voxels ) )
    lower = list( map( min, lsts ) )
    upper = list( map( max, lsts ) )

    coordsZW = [ (z,w)
        for z in range(lower[2], upper[2]+1)
        for w in range(lower[3], upper[3]+1)
    ]

    for zw in coordsZW:
        print( "z=" + str( zw[0] ) + ", w=" + str( zw[1] ) )

        for x in range(upper[0],lower[0]-1,-1):
            for y in range(lower[1], upper[1]+1):
                v = (y,x,zw[0],zw[1])
                if v in voxels:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')

    return

def parseGrid( grid ):
    voxels = set()
    rows = len( grid )
    for idy, line in enumerate( grid ):
        for idx, val in enumerate( line ):
            if val == '.': continue
            voxels.add( ( idx, rows - idy - 1, 0, 0 ) )
    return voxels

def drawVoxels( voxels ):
    points = np.array( list( map( list, voxels ) ) )
    fig = px.scatter_3d( points, x=0, y=1, z=2 )
    fig.show()

def activeNeighbourCount( v, curr ):
    count = 0
    for off in product( [-1, 0, 1 ], repeat=4 ):
        if off == ( 0, 0, 0 ): continue
        w = ( v[0] + off[0], v[1] + off[1], v[2] + off[2], v[3] + off[3] )
        if w in curr:
            count += 1
    return count

def gatherInactiveNeighbours( v, curr, inactive ):
    for off in product( [-1, 0, 1 ], repeat=4 ):
        if off == ( 0, 0, 0 ): continue
        w = ( v[0] + off[0], v[1] + off[1], v[2] + off[2], v[3] + off[3] )
        if w in curr: continue
        inactive.add( w )

def updateActive( v, curr, next ):
    count = activeNeighbourCount( v, curr )
    if count >= 2 and count <= 3:
        next.add( v )

def updateInactive( v, curr, next ):
    count = activeNeighbourCount( v, curr )
    if count == 3:
        next.add( v )

def updateCycle( voxels ):
    next = set()
    inactive = set()

    for v in voxels:
        updateActive( v, voxels, next )
        gatherInactiveNeighbours( v, voxels, inactive )
    for v in inactive:
        updateInactive( v, voxels, next )

    return next


def partA():
    grid = open( "example.txt" ).read().split("\n")
    voxels = parseGrid( grid )
    printVoxels( voxels )
    # print( voxels )

    for i in range(1):
        voxels = updateCycle( voxels )
        print( i, len( voxels ) )
        # drawVoxels( voxels )
        printVoxels( voxels )



partA()