import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

N = int(input())
students = list(map(int, input().split()))
answers = [0 for _ in range(N)]
for i in range(N):
    place = students[students[i] - 1]
    answers[place - 1] += students[i]
print(* answers)