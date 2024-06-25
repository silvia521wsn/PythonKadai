"""
プログラム名:Kadai9-2.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
scores = []
for i in range(3):
    n = int(input(f'{i+1}回目の得点入力>>'))
    scores.append(n)
for a in range(3):
    if a == 0:
        print(f'{a+1} 回目 {scores[a]} 点')
    else:
        if scores[a] > scores[a-1]:
             print(f'{a+1} 回目 {scores[a]} 点 +{scores[a]-scores[a-1]}')
        else:
            print(f'{a+1} 回目 {scores[a]} 点 -{scores[a-1]-scores[a]}')

