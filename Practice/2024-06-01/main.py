import sys

input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

# ここから通常のコード
N, T = list(map(int, input().split()))
bingoList1 = [i for i in range(1, N + 1)]
bingoList2 = [1] + [1 + i*N for i in range(1, N)]
bingoList3 = [1] + [1 + (i + i*N) for i in range(1, N)] 
bingoList4 = [N * N - i for i in range(N)]
print(bingoList1)
print(bingoList2)
print(bingoList3)
print(bingoList4)
bingoList5 = [1] + [i * N for i in range(1, N)]
print(bingoList5)
# https://atcoder.jp/contests/abc355/tasks/abc355_c