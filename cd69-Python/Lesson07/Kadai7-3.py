"""
プログラム名:Kadai7-3.py
作成日:2024年6月11日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
score1 = int(input('1 人目の点数：'))
score2 = int(input('2 人目の点数：'))
score3 = int(input('3 人目の点数：'))
ten = [score1,score2,score3]
total = sum(ten)
avg = total/len(ten)
print(f'合計は{total}点です')
print(f'平均は {avg} 点です') 
if score1 >= avg:
    kekka = '以上'
else:
    kekka = '未満'
print(f'1 人目の点数は {score1} 点、平均点{kekka}です。')
if score2 >= avg:
    kekka = '以上'
else:
    kekka = '未満'
print(f'2 人目の点数は {score2} 点、平均点{kekka}です。')
if score3 >= avg:
    kekka = '以上'
else:
    kekka = '未満'
print(f'2 人目の点数は {score3} 点、平均点{kekka}です。')