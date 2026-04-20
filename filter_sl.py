import sys

def filter_threshold(lst, threshold):
    return [x for x in lst if x >= threshold]

args = sys.argv[1:]

# 引数チェック
if len(args) < 2:
    print("Usage: python script.py <threshold> <num1> <num2> ...")
    sys.exit(1)

try:
    threshold = int(args[0])
    nums = [int(x) for x in args[1:]]
except ValueError:
    print("Error: All arguments must be integers.")
    sys.exit(1)

print(filter_threshold(nums, threshold))
