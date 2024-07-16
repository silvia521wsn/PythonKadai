"""
プログラム名:Ren12-3.py
作成日:2024年7月16日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Hero:
    name = 'モロロッケ'#属性
    hp = 100 #属性
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝た！')
        self.hp += hours

#ゲーム開始　
print('***処理科ファンタジーⅡ***')
h = Hero()
print(f'{h.name}のHPは現在{h.hp}です')
h.sleep(10) 
print(f'{h.name}のHPは現在{h.hp}です') 