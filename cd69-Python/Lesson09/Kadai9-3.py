"""
プログラム名:Kadai9-3.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
data = [22, 34, 56, 33, 42, 83, 27, 18, 25, 89]
print(data)
start = int(input('どこから>>'))
end = int(input('どこまで>>'))
total = 0
for i in range(start,end+1):
    total += data[i]
print(f'{start} 番めから {end} 番めまでの合計は {total} です')