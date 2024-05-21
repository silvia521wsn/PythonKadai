"""
プログラム名:Kadai4-3.py
作成日:2024年5月21日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
a = int(input('変数 a を入力>>'))
b = int(input('変数 b を入力>>'))
print(f'入れ替え前 変数 a は\"{a}\" 変数 b は\"{b}\"')
c = a
a = b
b = c
print(f'入れ替え後 変数 a は\"{a}\" 変数 b は\"{b}\"')