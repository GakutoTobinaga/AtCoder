import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
N, A = list(map(int, input().split()))
Ts = list(map(int, input().split()))
total_time = 0
# これと比べてでかいかどうか
for i in range(N):
    if total_time <= Ts[i]:
        total_time += Ts[i]
        total_time += A
        print(total_time, "This")
    elif total_time > Ts[i]:
        print(total_time)
        total_time += Ts[i]