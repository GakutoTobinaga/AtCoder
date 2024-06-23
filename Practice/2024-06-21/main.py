import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

"""
S = input()
numbers = []
for i in range(len(S) - 2):
    number = int(S[i] + S[i + 1] + S[i + 2])
    numbers.append(number)
    print(i,"は", S[i:i+3])
    print(numbers)
# print(min(numbers))

S = input()
already = []
for i in range(len(S)):
  if S[i] in already:
    print("no")
    break
  else:
    already.append(S[i])
    if i == len(S) - 1:
      print("yes")


N = int(input())
S = input()
x = 0
xs = [0]
for i in range(N):
    if S[i] == "I":
        x += 1
        xs.append(x)
    else:
        x -= 1
        xs.append(x)
print(max(xs))
"""

A, B = list(map(int, input().split()))
S = input()
x = 0
if (A + B + 1) != len(S):
    print("No")
else:
    for i in range(A):
        if 1 <= int(S[i]) <= 9:
            x += 1
        else:
            pass
    if x == A and S[A + B] == "-":
        x += 1
        for j in range(A, A + B + 1):
            if 1 <= int(S[j]) <= 9:
                x += 1
            else:
                pass
    else:
        print("No")
if x == (A + B + 1):
    print("Yes")