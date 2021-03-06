import numpy as np


def rotate( v, deg ):
    rad = np.radians( deg )
    s = np.sin( rad )
    c = np.cos( rad )
    return np.array( [ v[0] * c - v[1] * s, v[0] * s + v[1] * c ] )

cmds = list( map(
    lambda line: ( line[ 0 ], int( line[ 1: ] ) ),
    open( "input.txt" ).read().split( "\n" )
))

pos = np.array( [ 0.0, 0.0 ] )
anc = np.array( [ 10.0, 1.0 ] )

dirs = {
    "N": np.array( [  0.0, 1.0 ] ),
    "S": np.array( [  0.0,-1.0 ] ),
    "E": np.array( [  1.0, 0.0 ] ),
    "W": np.array( [ -1.0, 0.0 ] )
}

for act, val in cmds:
    if act in dirs:
        anc += val * dirs[ act ]
    else:
        if act == "L": anc = rotate( anc, val )
        elif act == "R": anc = rotate( anc,-val )
        else: pos += val * anc
    print( pos, anc )

print( np.sum( np.abs( pos ) ))