def countTrees( dx, dy, fin ):
    fin.seek( 0, 0 )
    x = 0
    y = 0
    count = 0

    for line in fin:
        inactiveRow = ( y % dy )
        y += 1

        if inactiveRow:
            continue

        stripped = line.strip()
        env = stripped[x % len(stripped)]

        count += ( env == '#' )

        x += dx

    return count


slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

fin = open( "input.txt" )
totalCount = 1

for slope in slopes:
    count = countTrees( slope[0], slope[1], fin )
    print( slope, count )
    totalCount *= count

print( totalCount )
