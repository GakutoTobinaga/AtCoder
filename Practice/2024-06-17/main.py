import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

N, x = list(map(int, input().split()))
a = list(map(int, input().split()))
sort_a = sorted(a)
count = 0
for i in range(N):
    if i == (N - 1) and x > 0:
        if x == sort_a[i]:
            count += 1
        else:
            pass
    elif sort_a[i] <= x:
        x -= sort_a[i]
        count += 1
print(count)