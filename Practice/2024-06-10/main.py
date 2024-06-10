import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

a, b = input().split()
c = int(a + b)
isTrue = False
for i in range(c):
    if i ** 2 == c:
        isTrue = True
    else:
        pass

if isTrue:
    print("Yes")
else:
    print("No")