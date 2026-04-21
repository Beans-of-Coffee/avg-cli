import sys

def get_lengths(lst):
    total = []
    for x in lst:
        total.append(len(x))
    return total

args = sys.argv[1:]

print(get_lengths(args))
