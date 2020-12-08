import re

fin = open( "input.txt" )

rxTop = re.compile( r"(\w* \w*) bags contain (no other bags|.*)" )
rxSub = re.compile( r"(?:(?:(\d+) (\w+ \w+)) bag)+" )

rules = {}
counts = {}

for line in fin:
    matchTop = rxTop.match( line )
    contents = matchTop.group( 2 )

    if contents == "no other bags":
        continue

    matchSub = rxSub.findall( contents )
    container = matchTop.group( 1 )

    if not container in counts:
        counts[ container ] = {}

    for item in matchSub:
        color = item[ 1 ]
        if not color in rules:
            rules[ color ] = []
        rules[ color ].append( container )
        counts[ container ][ color ] = int( item[ 0 ] )


def containCount( color, options ):
    if not color in rules:
        return
    options.update( rules[ color ] )
    for parent in rules[ color ]:
        containCount( parent, options )


def bagCount( color ):
    if not color in counts:
        return 0
    total = 0
    for key, value in counts[ color ].items():
        total += value + value * bagCount( key )
    return total

options = set()
containCount( "shiny gold", options )
print( len( options ) )

totalBagCount = bagCount( "shiny gold" )
print( totalBagCount )