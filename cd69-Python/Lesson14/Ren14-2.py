"""
プログラム名:Ren14-2.py
作成日:2024年09月03日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
import math

print('べき乗を行います')
a = int(input('元の値>>'))
b = int(input('何乗しますか>>'))
ans = math.pow(a,b)
print(f'{a} の {b} 乗は {ans} です')
c = float(input('小数入力>>'))
print(f'小数点以下切り捨て後：{math.floor(c)}')
print(f'小数点以下切り上げ後：{math.ceil(c)}')