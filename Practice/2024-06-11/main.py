import sys

input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

N = int(input())
K = int(input())
balls = list(map(int, input().split()))
A_robot = 0
B_robot = K
total = 0
for i in range(N):
    if abs(balls[i] - 0) > abs(balls[i] - K):
        total += abs(balls[i] - K) * 2

    else:
        total += abs(balls[i] - 0) * 2
print(total)