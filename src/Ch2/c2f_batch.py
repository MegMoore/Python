import sys
#python3 c2f_batch.py 100 0 -40

cstrings = sys.argv[1:]
for cstr in cstrings:
    c = float(cstr)
    F = ((9 * c) / 5) + 32

    print(F)
