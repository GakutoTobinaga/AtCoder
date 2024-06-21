import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

S = input()
numbers = []
for i in range(len(S) - 2):
    number = abs(753 - int(S[i] + S[i + 1] + S[i + 2]))
    numbers.append(number)
print(min(numbers))