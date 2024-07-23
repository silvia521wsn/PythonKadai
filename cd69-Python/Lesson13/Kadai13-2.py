"""
プログラム名:Kadai13-2.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Lunchset:
    drink = '紅茶'
    food = 'スコーン'
    tanka = 700
    goukei = 0
    otsuri = 0
    def kaiten(self):
        print('Welcome!')
    def kaikei(self,ninzu):
        self.goukei = self.tanka * ninzu
    def kaikei2(self,azukari):
        self.otsuri = azukari - self.goukei

lunch = Lunchset()
lunch.kaiten()
print(f'ティーセット内容：{lunch.drink}、{lunch.food}')

cyumon = int(input('注文数>>'))
lunch.kaikei(cyumon)
print(f'注文数:{cyumon} 個、合計:{lunch.goukei} 円')

azukari = int(input('お預かり金額>>'))
lunch.kaikei2(azukari)
print(f'おつりは {lunch.otsuri} 円です')