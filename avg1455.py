import sys

def avg_v3(lst):
    total = 0
    count = 0
    for x in lst:
        if x % 3 == 0:
            total +=x
            count +=1
    if count == 0:
       return 0
    return total / count
    return total / count

# コマンドライン引数を取得
args = sys.argv[1:]

# 文字列 → 数値に変換
nums = [int(x) for x in args]

# 実行
print(avg_3(nums))
