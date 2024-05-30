import sys
# https://atcoder.jp/contests/abc002/tasks/abc002_2
# input.txt を読み込む
input_file = 'input.txt'
with open(input_file, 'r') as f:
    input_data = f.read()

# 標準入力から読み込んだように処理する
sys.stdin = open(input_file, 'r')
# ここから通常のコード
n = input()
vowel = 'aeiouAEIOU'
name = 'Torvalds'
cname = ''.join(s for s in n if s not in vowel)
print(cname)  # Trvlds
# ユーザーから入力を受け取る

# make transとtranslateを使ってみると...
# 母音を削除するための変換マッピングを作成
vowel = 'aeiouAEIOU'
translation_table = str.maketrans('', '', vowel)

# 変換テーブルの内容を表示
print("Translation Table:", translation_table)

# 文字列を変換
cn = n.translate(translation_table)
# 2つの数値を足す無名関数
# lambda 引数1, 引数2, ... : 式
add = lambda x, y: x + y
print(add(3, 5))  # 出力: 8

# 結果を出力
print("Result:", cn)

# 処理例

# python3 main.py