from itertools import product
from functools import reduce
import operator
import re

sections = [ section.split( '\n' ) for section in open( "input.txt" ).read().split( "\n\n" ) ]
sections[1] = sections[1][1:]
sections[2] = sections[2][1:]

reField = re.compile( r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)")

fields = {
    m.group( 1 ) : [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]
    for m in [ reField.fullmatch( field ) for field in sections[0] ]
}

myticket = [ int(val) for val in sections[1][0].split( ',' ) ]
tickets = [ [ int(val) for val in ticket.split( ',' ) ] for ticket in sections[2] ]


################################################################################
#  part a

def validField( ranges, val ):
    return any( [ a <= val and val <= b for a, b in ranges ] )

def hasValidField( val ):
    return any( [ validField( ranges, val ) for key, ranges in fields.items() ] )

err = sum ( [ val for ticket in tickets for val in ticket if not hasValidField( val ) ] )
print( err )


################################################################################
#  part b

# discard invalid tickets
def validTicket( ticket ):
    return all( [ hasValidField( val ) for val in ticket ] )

validTickets = list( filter( validTicket, tickets ) )

# collect which fields are invalid
def gatherInvalidOptions( val ):
    return set( [ fieldId for fieldId, ranges in fields.items() if not validField( ranges, val ) ] )

invalidOptions = { i : set() for i in range( len( validTickets ) ) }
for ticket, i in product( validTickets, range( len( myticket ) )):
    invalidOptions[ i ].update( gatherInvalidOptions( ticket[ i ] ))

# deduce actual fields by process of elimination
fieldIds = set( fields.keys() )
unavailable = set()
assignment = {}

def identifyField():
    for pos, options in invalidOptions.items():
        valids = fieldIds.difference( options.union( unavailable ) )
        if not len( valids ) == 1: continue
        unavailable.update( valids )
        ( assignment[ pos ], ) = valids

for i in range( len( fieldIds ) ):
    # it is guaranteed that each run identifies at least one item
    identifyField()

# count departures
prod = reduce( operator.mul, [ myticket[ pos ] for pos, fieldId in assignment.items() if fieldId.startswith( "departure" ) ])
print( prod )
