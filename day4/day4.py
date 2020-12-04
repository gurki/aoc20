import re

regex = re.compile( r"(?:(?:(\w{3}):[\w\d#]+)[\s\n]?)" )
targets = set([ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ])

def validate( line ):
    match = set( regex.findall( line ) )
    return targets.issubset( match )

def validateBatch():
    fin = open( "input.txt" )
    curr = ""
    count = 0

    for line in fin:
        if line == "\n":
            count += validate( curr )
            curr = ""
        else:
            curr += " " + line.strip()

    print( count )

validateBatch()