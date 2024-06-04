import sys

# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def isContinuous(A, B):
    conListed = sorted(A + B)
    setA = set(A)
    for i in range(len(conListed) - 1):
        if conListed[i] in setA and conListed[i + 1] in setA:
            return True 
    return False

if isContinuous(A, B):
    print("Yes")
else:
    print("No")
# python3 main.py
# https://atcoder.jp/contests/abc355/tasks/abc355_b
# 初めてSetっちゅう概念を学んだ、こいつは重複を排除してくれたりしていい感じやな
