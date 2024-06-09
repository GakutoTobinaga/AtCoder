import sys
import copy
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

def make_diagonal_ans_1(bingo, number):
    diagonal_ans = []
    for i in range(int(number)):
        diagonal_ans.append(bingo[i][i])
    return diagonal_ans

bingo = [list(map(int, input().split())) for _ in range(3)]
ans = copy.copy(bingo)
ans.append(make_diagonal_ans_1(bingo, 3))
ans.append([bingo[0][2], bingo[1][1], bingo[2][0]])

ans.append([bingo[0][0], bingo[1][0], bingo[2][0]])
ans.append([bingo[0][1], bingo[1][1], bingo[2][1]])
ans.append([bingo[0][2], bingo[1][2], bingo[2][2]])

answ = 0
N = int(input())
input_numbers = []
for i in range(N):
    num = int(input())
    input_numbers.append(num)


for j in range(9):
    set_ans = set(ans[j - 1])
    print(set_ans)
    if set_ans in input_numbers:
        print(set_ans)
        answ += 1

if answ > 0:
    print("Yes")
else:
    print("No")

print(input_numbers)