import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# https://atcoder.jp/contests/abc126/tasks/abc126_a
N, K = list(map(int ,input().split()))
S = input()
new_s = []
for i in range(N):
    if i == K - 1:
        lower_alp = S[i].lower()
        new_s.append(lower_alp)
    else:
        new_s.append(S[i])
print("".join(new_s))