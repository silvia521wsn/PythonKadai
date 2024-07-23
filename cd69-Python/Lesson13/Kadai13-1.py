"""
プログラム名:Kadai13-1.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Teisyoku:
    soup = '味噌汁'
    food = '白米'
    side = 'お漬物'
    tanka = 600
    goukei = 0
    def eigyoucyu(self):
        print('へい、らっしゃい！！')
    def kanjou(self,kosu):
        self.goukei = self.tanka * kosu

meal = Teisyoku()
meal.eigyoucyu()
print(f'定食には{meal.soup}と{meal.food}、{meal.side}がつきます')

cyumon = int(input('定食の注文数>>'))
meal.kanjou(cyumon)
print(f'{cyumon} 食注文で合計 {meal.goukei} 円です')