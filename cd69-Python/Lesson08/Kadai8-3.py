"""
プログラム名:Kadai8-3.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""

hani = int(input('範囲を指定：'))
cnt = 0
ans = 0
while cnt <= hani:
    ans += cnt
    cnt += 2
print(f'1～{hani} までの偶数の和は {ans} です') 