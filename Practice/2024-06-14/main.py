import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

N = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers)

center = int(N / 2)

if sorted_numbers[center - 1] == sorted_numbers[center]:
    print(0)
else:
    between_number = sorted_numbers[center] - sorted_numbers[center - 1]
    print(between_number)