import re

sections = [ section.split( '\n' ) for section in open( "input.txt" ).read().split( "\n\n" ) ]
sections[1] = sections[1][1:]
sections[2] = sections[2][1:]

reField = re.compile( r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)")

fields = {}
for field in sections[0]:
    match = reField.fullmatch( field )
    fields[ match.group( 1 ) ] = [
        ( int(match.group(2)), int(match.group(3)) ),
        ( int(match.group(4)), int(match.group(5)) ),
    ]
# print( fields )

tickets = [ [ int(val) for val in ticket.split( ',' ) ] for ticket in sections[2] ]
# print( tickets )

def validField( ranges, val ):
    return any( [ a <= val and val <= b for a, b in ranges ] )

def hasValidField( val ):
    return any( [ validField( ranges, val ) for key, ranges in fields.items() ] )

err = 0
for ticket in tickets:
    for val in ticket:
        if hasValidField( val ): continue
        err += val

print( err )
