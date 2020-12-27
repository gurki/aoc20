import operator

lines = [ line.replace(' ', '') for line in open( "input.txt" ).read().split( "\n" ) ]
# print(lines)

tree = {}

def parse( line ):
    # print( line )
    res = 0
    nextOp = None
    carry = None
    depth = 0

    for idx, x in enumerate( line ):
        if x == '(': 
            if depth == 0: 
                carry = parse( line[ idx+1: ] )
            depth += 1
        elif x == ')':
            depth -= 1
            if depth < 0: return res
        
        if depth > 0:
            continue

        if x.isnumeric():
            carry = int( x ) 
        elif x == '+':
            nextOp = operator.add
        elif x == '*': 
            nextOp = operator.mul

        if carry:
            if nextOp: 
                res = nextOp( carry, res )
                nextOp = None
            else: 
                res = carry
            carry = None
    return res
    
def convertLine( line ):
    return '(' + line.replace( '(', '((' ).replace( ')', '))' ).replace( '*', ')*(' ) + ')'

print( sum( list( map( parse, lines ))))
print( sum( list( map( parse, map( convertLine, lines ) ))))