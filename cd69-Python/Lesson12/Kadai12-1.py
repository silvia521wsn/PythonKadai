"""
プログラム名:Kadai12-1.py
作成日:2024年7月16日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class watasi:
    name = 'ねね'
    money = 200
    def cyokin(self,add):
        print(f'{self.name}は{add}万円儲かった!')
        self.money += add

print('私の秘密を紹介します')
wk = watasi()
wk.cyokin(1000)
print(f'{wk.name}の貯金は現在{wk.money}万円です')