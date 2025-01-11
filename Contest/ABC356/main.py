import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

# ここから通常のコード
N, L, R = list(map(int, input().split()))
listFirst = []
list3 = list(range(L, R + 1))
for i in range(1, N + 1):
    if not i in list3:
        listFirst.append(i)
sortedList3 = sorted(list3, reverse=True)
final = listFirst[:L - 1] + sortedList3 + listFirst[L - 1:]
print(final)
