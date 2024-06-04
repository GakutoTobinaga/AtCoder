import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
A, B = list(map(int, input().split()))
if 13 <= A:
    print(B)
elif 6 <= A:
    print(int(B / 2))
else:
    print(0)
# 計算したらintを適用しよう
# https://atcoder.jp/contests/abc355/tasks/abc127_c