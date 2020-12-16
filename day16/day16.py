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

myticket = [ int(val) for val in sections[1][0].split( ',' ) ]
tickets = [ [ int(val) for val in ticket.split( ',' ) ] for ticket in sections[2] ]


#  part a

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


# part b

def validTicket( ticket ):
    return all( [ hasValidField( val ) for val in ticket ] )

validTickets = list( filter( validTicket, tickets ) )
invalidOptions = {}

for i in range( len( ticket ) ):
    invalidOptions[ i ] = set()

for ticket in validTickets:
    for i in range( len( ticket ) ):
        val = ticket[ i ]
        for fieldId, ranges in fields.items():
            if not validField( ranges, val ):
                invalidOptions[ i ].add( fieldId )

fieldIds = set( fields.keys() )
unavailable = set()
assignment = {}

for i in range( len( fieldIds ) ):
    for pos, options in invalidOptions.items():
        valids = fieldIds.difference( options.union( unavailable ) )
        if len( valids ) != 1: continue
        unavailable.update( valids )
        assignment[ pos ] = list( valids )[ 0 ]

prod = 1
for pos, fieldId in assignment.items():
    if not fieldId.startswith( "departure" ): continue
    prod *= myticket[ pos ]

print( prod )
