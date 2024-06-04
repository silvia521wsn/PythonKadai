"""
プログラム名:Kadai6-2.py
作成日:2024年6月4日
作成者:(CD69-3組 K024C2100 WANG SHINING
"""
tannin = ['山本','清水','三嶌','藤本']
kumi = int(input('何組を表示しますか(半角数字を入力)>>'))
name = kumi-len(tannin)-1
print (f'{kumi}組担任は{tannin[name]}先生です')