"""
プログラム名:Kadai10-1.py
作成日:2024年7月02日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
scores = [30, 59, 100, 48, 60]
def list_make():
    ng_scores = []
    for ten in scores:
        if ten < 60:
            ng_scores.append(ten)
    print(f'不合格者の得点：{ng_scores}')

print(f'全員の得点：{scores}')
list_make()