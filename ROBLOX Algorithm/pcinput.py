def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "Not a float -- Please try again." )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "Not an integer -- Please try again." )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()

def getLetter( prompt ):
    while True:
        line = input( prompt )
        line = line.strip()
        line = line.upper()
        if len( line ) != 1:
            print( "Give precisely ONE letter." )
            continue
        if line < 'A' or line > 'Z':
            print( "Please give a letter from the alphabet." )
            continue
        return line
