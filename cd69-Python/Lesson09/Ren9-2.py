"""
プログラム名:Ren9-2.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
scores = [80,95,98,100]
print(scores)
total = sum(scores)
ave = total/len(scores)
print(f'平均点は {ave} 点です')
i = 1
for data in scores:
    if data >= ave:
        print(f'{i}組の得点は {data} 点で平均点以上です')
    else:
        print(f'{i}組の得点は {data} 点で平均点未満です')
    i += 1
