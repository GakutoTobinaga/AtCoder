import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')
P, R, Q = list(map(int, input().split()))
airport_distance = [P, R, Q]
airport_distance_sorted = sorted(airport_distance)
print(airport_distance_sorted[0] + airport_distance_sorted[1])
# https://atcoder.jp/contests/abc129/tasks/abc129_a