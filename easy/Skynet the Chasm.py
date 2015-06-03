import sys, math

def get_need_to_stop(X):
    return sum(range(1, X + 1))

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(input()) # the length of the road before the gap.
G = int(input()) # the length of the gap.
L = int(input()) # the length of the landing platform.

FULL = R + G + L
GAP_POS = R
GAP_POS_AFTER = R + G

is_jumped = False

# game loop
while 1:
    S = int(input()) # the motorbike's speed.
    X = int(input()) # the position on the road of the motorbike.
    
    left_to_jump = R - X
    after_jump = FULL - X
    
    print(R, G, L, file=sys.__stderr__)
    print(S, X, file=sys.__stderr__)
    print("after jump you need", get_need_to_stop(S),"to stop", file=sys.__stderr__)
    print("left to jump:", left_to_jump, file=sys.__stderr__)
    
    # Before jump
    if not is_jumped:
        if G < S and GAP_POS - X < S :
            is_jumped = True
            print("JUMP")
            
        if X < GAP_POS:
            if L < get_need_to_stop(S):
                print("SLOW")
            elif G < S:
                print("WAIT")
            else:
                print("SPEED")

    #After jump
    else:
        print("SLOW")
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # print("SPEED") # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.