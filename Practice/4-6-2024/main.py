import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
A, P = list(map(int, input().split()))
L = (A * 3) + P
print(int(L / 2))
# 商のみを考慮すれば良かったのでOK。
# https://atcoder.jp/contests/abc128/tasks/abc128_a