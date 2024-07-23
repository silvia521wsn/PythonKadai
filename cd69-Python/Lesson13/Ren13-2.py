"""
プログラム名:Ren13-2.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Chara:
    name = '諸岡'
    cm = 166.6
    def syoukai(self):
        print(f'{self.name}さんは身長{self.cm}cm')
    def syoukai2(self,name2,cm2):
        print(f'{name2}さんは身長{cm2}cm')

jinbutu = Chara()
jinbutu.syoukai()
jinbutu.syoukai2('山本',199.8)