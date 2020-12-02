fin = open( "input.txt" )
expenses = list( map( int, fin ) )

for x in expenses:
    if x > 2020:
        continue
    for y in expenses:
        if x + y > 2020:
            continue
        for z in expenses:
            if x + y + z != 2020:
                continue
            print( x, y, z, x*y*z )
            exit()