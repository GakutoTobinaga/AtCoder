import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

cookies = list(map(int, input().split()))
already = [cookies[0], cookies[1], cookies[2]]
already_cookies = [already]
count = 0
while True:
    new_cookies = []
    new_cookies = [int(int(cookies[1]) / 2 + int(cookies[2]) / 2),
                int(int(cookies[0]) / 2 + int(cookies[2]) / 2),
                int(int(cookies[0]) / 2 + int(cookies[1]) / 2)]
    count += 1
    if new_cookies[0] % 2 == 0 and new_cookies[1] % 2 == 0 and new_cookies[0] % 2 == 0:
        already_cookies.append(new_cookies)
        new_cookies.clear
    else:
        if new_cookies in already_cookies:
            print(count)
            break
        else:
            new_cookies.clear