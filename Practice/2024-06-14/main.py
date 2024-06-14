import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

N, K = map(int, input().split())
trials = [N]
current = N

while True:
    next_value = abs(current - K)
    if next_value in trials:
        break
    else:
        trials.append(next_value)
        current = next_value

print(trials)
