"""
プログラム名:Kadai8-5.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
data = [22,34,56,33,42,83,27,18,25,89]
min_index = 0
min_atai = data[0]
cnt = 1

while cnt < len(data):
    if data[cnt] < min_atai:
        min_atai = data[cnt]
        min_index = cnt
    cnt += 1

print(data)
print(f'data[{min_index}]が最小で最小値は {min_atai} です')