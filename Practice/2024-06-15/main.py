import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')
"""
N = int(input())
students = list(map(int, input().split()))
answers = [0 for _ in range(N)]
for i in range(N):
    place = students[students[i] - 1]
    answers[place - 1] += students[i]
print(* answers)
"""

def make_value_even(numbers):
    new_numbers = []
    for i in range(0, len(numbers), 2):
        new_numbers.append(int(((numbers[i] + numbers[i + 1]) / 2)))
    new_numbers.sort()
    return new_numbers

def make_value_odd(numbers):
    new_numbers = []
    for i in range(0, len(numbers) - 1, 2):
        new_numbers.append(int(((numbers[i] + numbers[i + 1]) / 2)))
    new_numbers.sort()
    new_numbers[-1] += numbers[-1]
    new_numbers[-1] = int(new_numbers[-1] / 2)
    new_numbers.sort()
    return new_numbers
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

while len(numbers) != 1:
    if len(numbers) % 2 == 0:
        numbers = make_value_even(numbers)
    else: # 例えば5の時, 前半4つをmake valueして終わったら1 1 残り となる　並び替えてもう一度
        numbers = make_value_odd(numbers)
print(*numbers)