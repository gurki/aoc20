import re


reValid = re.compile( r"(?:(?:(\w{3}):([\w\d#]+))[\s\n]?)" )
reHeight = re.compile( r"(\d+)(cm|in)" )
reColor = re.compile( r"#[0-9a-f]{6}" )
reEye = re.compile( r"amb|blu|brn|gry|grn|hzl|oth" )
rePid = re.compile( r"^\d{9}$" )

targets = set([ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ])


def validHeight( height ):
    hgtMatch = reHeight.match( height )
    if not hgtMatch: return False

    hgt = int( hgtMatch.group( 1 ) )
    hgtUnit = hgtMatch.group( 2 )
    if hgtUnit == "cm" and ( hgt < 150 or hgt > 193 ): return False
    if hgtUnit == "in" and ( hgt < 59 or hgt > 76 ): return False

    return True


def validate( line ):
    match = dict( reValid.findall( line ) )
    keys = match.keys()

    if not targets.issubset( keys ): return False

    byr = int( match[ "byr" ] )
    iyr = int( match[ "iyr" ] )
    eyr = int( match[ "eyr" ] )

    if byr < 1920 or byr > 2002: return False
    if iyr < 2010 or iyr > 2020: return False
    if eyr < 2020 or eyr > 2030: return False
    if not validHeight( match[ "hgt" ] ): return False
    if not reColor.match( match[ "hcl" ] ): return False
    if not reEye.match( match[ "ecl" ] ): return False
    if not rePid.match( match[ "pid" ] ): return False

    return True


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