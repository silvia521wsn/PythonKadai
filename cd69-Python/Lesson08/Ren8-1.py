"""
プログラム名:Ren8-1.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
number = int(input('整数を入力>>'))
amari = number % 2
if number >= 0 and amari == 0:
    print('偶数')
else:
    print('奇数か、または0以上ではありません') 