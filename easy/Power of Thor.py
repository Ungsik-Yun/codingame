import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in raw_input().split()]

# game loop
while 1:
    E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    X_shift_direction = TX - LX
    Y_shift_direction = TY - LY
    
    direction = ""
    
    if Y_shift_direction != 0:
        if Y_shift_direction > 0:
            direction += "N"
            TY = TY - 1
        elif Y_shift_direction < 0 :
            direction += "S"
            TY = TY + 1
            
    if X_shift_direction != 0:
        if X_shift_direction > 0:
            direction += "W"
            TX = TX - 1
        elif X_shift_direction < 0:
            direction += "E"
            TX = TX + 1
            
    print >> sys.stderr, "%d %d %s" % (X_shift_direction,  Y_shift_direction,direction)
        
    print direction