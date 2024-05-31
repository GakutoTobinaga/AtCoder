import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
n = int(input())
a = list(map(int, input().split()))

# 処理例
print(sum(a))

# python3 main.py

N = int(input())
K = int(input())
print(int(N % K))