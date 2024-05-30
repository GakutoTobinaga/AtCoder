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
# 文字列を変換
cn = n.translate(translation_table)
# translateは受け取ったUnicode配列を使って文字列を置き換えていく関数。
# 結果を出力
print(cn)