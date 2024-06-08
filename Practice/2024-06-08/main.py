import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

"""
N = int(input())
ans = -1
for i in range(1, N + 1):
    if int(i * 1.08) == N:
        ans = i
if ans != -1:
    print(ans)
else:
    print(":(")
"""
"""
N, M, C = map(int, input().split())
Bs = list(map(int, input().split()))
ans = 0
for _ in range(N):
    As = list(map(int, input().split()))
    A_ans = 0
    for i in range(M):
        A_ans += As[i] * Bs[i]
        if i == M - 1:
            A_ans += C
            if A_ans > 0:
                ans += 1
print(ans)
"""

H, W = map(int, input().split())
X = H * W
if H == 1 or W == 1:
    print(1)
elif X % 2 == 0:
    print(int(X / 2))
else:
    X -= 1
    Y = X / 2
    print(int(Y + 1))