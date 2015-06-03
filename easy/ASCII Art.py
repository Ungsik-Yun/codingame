import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

W = int(input())
H = int(input())
T = input()

N = 27

out_msg = [ "" for i in range(H)]
al_numbers = list(range(N))
al_dict = {}
al_relations = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    '?':27,
    }

for i in range(1, N + 1):
    al_dict[i] = list()

for i in range(H):
    ROW = input()
    for j in range(1,N+1):
        al_dict[ j ].append( ROW[ W*(j-1) : W*j ] )
        
for char in T:
    tgt = char.lower()
    # print(al_dict[al_relations[tgt]], file=sys.stderr)
    for i in range(H):
        if tgt in al_relations:
            out_msg[i] += al_dict[al_relations[tgt]][i]
        else:
            out_msg[i] += al_dict[al_relations['?']][i]

# print(out_msg, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for i in range(H):
    print (out_msg[i])