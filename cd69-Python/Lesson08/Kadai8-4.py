"""
プログラム名:Kadai8-4.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
data = [22, 34, 56, 33, 42, 83, 27, 18, 25, 89]
max = data[0]  
cnt = 1

while cnt < len(data):
    if data[cnt] > max:
        max = data[cnt]
    cnt += 1

print(f'最大値：{max}')