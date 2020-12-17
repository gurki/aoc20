from itertools import product
import numpy as np
import plotly.express as px
import keyboard


def parseGrid( grid ):
    voxels = set()
    rows = len( grid )
    for idy, line in enumerate( grid ):
        for idx, val in enumerate( line ):
            if val == '.': continue
            voxels.add( ( idx, rows - idy - 1, 0 ) )
    return voxels

def drawVoxels( voxels ):
    points = np.array( list( map( list, voxels ) ) )
    fig = px.scatter_3d( points, x=0, y=1, z=2 )
    fig.show()

def activeNeighbourCount( v, curr ):
    count = 0
    for off in product( [-1, 0, 1 ], repeat=3 ):
        if off == ( 0, 0, 0 ): continue
        w = ( v[0] + off[0], v[1] + off[1], v[2] + off[2] )
        if w in curr:
            count += 1
    return count

def gatherInactiveNeighbours( v, curr, inactive ):
    for off in product( [-1, 0, 1 ], repeat=3 ):
        if off == ( 0, 0, 0 ): continue
        w = ( v[0] + off[0], v[1] + off[1], v[2] + off[2] )
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
    grid = open( "input.txt" ).read().split("\n")
    voxels = parseGrid( grid )
    print( voxels )

    for i in range(6):
        voxels = updateCycle( voxels )
        drawVoxels( voxels )
        print( i, len( voxels ) )

partA()
