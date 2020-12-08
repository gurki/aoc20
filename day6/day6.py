from functools import reduce
print( reduce( lambda count, group: count + len( set( list( group.replace( "\n", '' ) ))), open( "input.txt" ).read().split( "\n\n" ), 0 ))
print( reduce( lambda count, group: count + len( reduce( lambda s, entry: s.intersection( set( list( entry ))), group.split( "\n" ), set( list( group.replace( "\n", '' ) )))),  open( "input.txt" ).read().split( "\n\n" ), 0 ))