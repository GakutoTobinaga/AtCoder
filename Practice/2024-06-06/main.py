import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')
"""
A, B = list(map(int, input().split()))

N = 0
T = 0
while N < B:
    N += A
    T += 1
    if N < B:
        N -= 1
print(T)
"""

N = int(input())
Xs = list(map(int, input().split()))
Xs_min = min(Xs)
Xs_max = max(Xs)

Answers = []
Xs_set = list(set(Xs))
for i in range(Xs_min, Xs_max + 1):
    #開催地を移動する
    total = 0
    for j in range(len(Xs)):
        #住人を一人ずつ今の開催地と計算して足す
        total += (Xs[j] - i) ** 2
    Answers.append(total)
print(min(Answers))