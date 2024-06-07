import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')
# bootcamp 3
N, A, B = list(map(int, input().split()))
B_counter = 0
qualified = 0
S = input()
S_list = list(S)

for i in range(len(S)):
    if S_list[i] == "c":
        print("No")
    elif (qualified) >= (A + B):
        print("No")
    else:
        if S_list[i] == "a":
            qualified += 1
            print("Yes")
        else:
            B_counter += 1
            if B_counter <= B:
                qualified += 1
                print("Yes")
            else:
                print("No")