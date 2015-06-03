import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of temperatures to analyse
TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526

str_l = TEMPS.split()
int_l = [int(i) for i in str_l]

if N == 0:
    print 0
elif N == 1:
    print int_l[0]
else:
    int_l.sort(cmp=lambda x,y: abs(x) - abs(y))
    print >> sys.stderr, int_l
    
    if abs(int_l[0]) == abs(int_l[1]) and int_l[0] < int_l[1]:
        print int_l[1]
    else:
        print int_l[0]