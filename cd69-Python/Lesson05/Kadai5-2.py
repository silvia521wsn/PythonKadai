"""
プログラム名:Kadai5-2.py
作成日:2024年5月28日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
ten = []
ten.append(int(input('1 人目の点数>>')))
ten.append(int(input('2 人目の点数>>')))
ten.append(int(input('3 人目の点数>>')))
print(f'合計は{sum(ten)}点です')
avg = sum(ten)/len(ten)
print(f'平均は{avg}点です')
print(f'1 人目の点数は{ten[0]}点、平均との差{ten[0]-avg}点')
print(f'2 人目の点数は{ten[1]}点、平均との差{ten[1]-avg}点')
print(f'3 人目の点数は{ten[2]}点、平均との差{ten[2]-avg}点')