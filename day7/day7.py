import re

fin = open( "input.txt" )

rxTop = re.compile( r"(\w* \w*) bags contain (no other bags|.*)" )
rxSub = re.compile( r"(?:(?:(\d+) (\w+ \w+)) bag)+" )

rules = {}

for line in fin:
    matchTop = rxTop.match( line )
    contents = matchTop.group( 2 )

    if contents == "no other bags":
        continue

    matchSub = rxSub.findall( contents )
    container = matchTop.group( 1 )

    for item in matchSub:
        color = item[ 1 ]
        if not color in rules:
            rules[ color ] = []
        rules[ color ].append( container )

def containCount( color, options ):
    print( color, "/", options )
    if not color in rules:
        return
    options.update( rules[ color ] )
    for parent in rules[ color ]:
        containCount( parent, options )

# print( rules )

options = set()
containCount( "shiny gold", options )
print( len( options ) )
