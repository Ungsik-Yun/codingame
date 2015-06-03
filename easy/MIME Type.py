import sys, math, re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # Number of elements which make up the association table.
Q = int(input()) # Number Q of file names to be analyzed.
ext_dict = dict()
for i in range(N):
    # EXT: file extension
    # MT: MIME type.
    EXT, MT = input().split()
    ext_dict[EXT.lower()] = MT
for i in range(Q):
    FNAME = input().lower() # One file name per line.
    # print(FNAME, file=sys.stderr)
    result = re.search("^.*\.(.*)$", FNAME)
    if result is not None:
        # print(result, file=sys.stderr)
        FEXT = result.groups()[0]
        if FEXT in ext_dict:
            print(ext_dict[FEXT])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
# Write an action using print
# print(ext_dict, file=sys.stderr)

 # For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.