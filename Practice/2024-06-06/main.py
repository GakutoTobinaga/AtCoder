import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

A, B = list(map(int, input().split()))

N = 0
T = 0
while N < B:
    N += A
    T += 1
    if N < B:
        N -= 1
print(T)