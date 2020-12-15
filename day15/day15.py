nums = [ int(x) for x in open( "input.txt" ).read().split( ',' ) ]

spokenTurns = {}
spoken = -1

for turn in range( 1, 30000001 ):
    if turn <= len( nums ):
        spoken = nums[ turn - 1 ]
        spokenTurns[ spoken ] = [ turn ]
        continue
    if spoken in spokenTurns:
        turns = spokenTurns[ spoken ]
        if len( turns ) == 1:
            spoken = 0
            if not spoken in spokenTurns: spokenTurns[ spoken ] = []
            spokenTurns[ spoken ].append( turn )
            spokenTurns[ spoken ] = spokenTurns[ spoken ][ -2: ]
        else:
            spoken = turns[ -1 ] - turns[ -2 ]
            if not spoken in spokenTurns: spokenTurns[ spoken ] = []
            spokenTurns[ spoken ].append( turn )
            spokenTurns[ spoken ] = spokenTurns[ spoken ][ -2: ]
    else:
        spokenTurns[ spoken ] = [ turn ]
        spoken = 0
    if turn % 1000 or turn > 30000001 - 1000:
        print(  turn / 30000001, ":", spoken )