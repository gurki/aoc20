from functools import reduce
fin = open( "input.txt" )

program = [ [ line[:3], int( line[4:-1] ), False ] for line in fin ]


def runProgram( program, id ):
    for p in program:
        p[ 2 ] = False

    acc = 0
    lid = 0
    steps = 0

    while True:
        if lid < 0:
            break

        if lid + 1 > len( program ):
            print( 'eop' )
            break

        if program[ lid ][ 2 ]:
            break

        steps += 1
        cmd = program[ lid ]
        cmd[ 2 ] = True
        opp = cmd[ 0 ]

        # try swapping op code and see what happens
        if lid == id:
            opp = ( "nop" if opp == "jmp" else "jmp" )

        if opp == "nop":
            lid += 1
        elif opp == "acc":
            acc += cmd[ 1 ]
            lid += 1
        else:
            lid += cmd[ 1 ]

    return ( acc, lid, steps )

# find all lines that could be the issue
nums = [ lid for lid in range( len( program ) ) if program[ lid ][ 0 ] == "jmp" or program[ lid ][ 0 ] == "nop" ]

# bruteforce swapping one op at a time
for i in nums:
    print( runProgram( program, i ) )