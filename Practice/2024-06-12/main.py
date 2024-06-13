import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')
"""
N = int(input())
numbers = map(int,input().split())
alice = 0
bob = 0

sorted_numbers = sorted(numbers, reverse=True)

for i in range(1, N + 1):
    biggest_number = sorted_numbers.pop(0)
    if i % 2 != 0:
        alice += biggest_number
    else:
        bob += biggest_number
print(alice - bob)

multipliers = []
N = int(input())
for i in range(1, 8):
    multipliers.append(2 ** i)
if N == 1:
    print(1)
elif N in multipliers:
    print(N)
else:
    for i in range(len(multipliers) - 1):
        if multipliers[i] <= N and N < multipliers[i + 1]:
            print(multipliers[i])
"""
