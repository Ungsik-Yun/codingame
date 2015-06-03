import sys, math, binascii

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

encoded_msg = ""

for c in MESSAGE:
    e = bin(int.from_bytes(c.encode(), 'big'))[2:]
    encoded_msg = encoded_msg + e.zfill(7)


print(encoded_msg, file=sys.__stderr__)

prev = -1
r = ""

for c in encoded_msg:
    print(c, file=sys.__stderr__)
    
    if c == "1" and (prev == 0 or prev == -1):
        # switch 0 to 1 or start
        if prev != -1:
            r = r + " "
        r = r + "0 0"
        prev = 1
    elif c == "1" and prev == 1:
        # continue from prev 1
        r = r + "0"
        prev = 1

    elif c == "0" and (prev == 1 or prev == -1):
        # swith 1 to 0 or start
        if prev != -1:
            r = r + " "
        r = r + "00 0"
        prev = 0
    elif c == "0" and prev == 0:
        # continue from prev 0
        r = r + "0"
        prev = 0

    
    
print(r)
# print("answer")