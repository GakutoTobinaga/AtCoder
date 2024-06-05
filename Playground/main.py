import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
# join, lowerについて
sample1 = "Gakuto"
sample2 = "$".join(sample1)
print(sample2)
sample3 = sample1.lower()
# lowerは元のやつは変えられない
print(sample3)

def gcp(x, y):
    if y == 0:
        return x
    else:
        return gcp(y, x%y)

print(gcp(234, 987))