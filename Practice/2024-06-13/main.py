import sys
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

sys.stdin = open(input_file, 'r')

cookies = list(map(int, input().split()))
already_cookies = [cookies]
count = 0
while True:
    new_cookies = [int(int(cookies[1]) / 2 + int(cookies[2]) / 2),
                   int(int(cookies[0]) / 2 + int(cookies[2]) / 2),
                   int(int(cookies[0]) / 2 + int(cookies[1]) / 2)]
    if new_cookies[0] % 2 != 0 or new_cookies[1] % 2 != 0 or new_cookies[0] % 2 != 0:
        print(new_cookies)
        count += 1
        print(count)
        exit()
    else:
        new_cookies_set = new_cookies
        print(new_cookies_set)
        if new_cookies_set in already_cookies:
            print(-1)
            exit()
        else:
            already_cookies.append(new_cookies)