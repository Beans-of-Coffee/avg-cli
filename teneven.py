import sys
def teneven(lst):
    count=0
    for x in lst:
        if x >=10 and x % 2 ==0:
            count +=1
    return count

args = sys.argv[1:]
nums = [int(x) for x in args]
print(teneven(nums))
