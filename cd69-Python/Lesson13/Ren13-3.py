"""
プログラム名:Ren13-3.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Keisan:
    name = 'ねね'
    tosi = 26
    tosi2 = 0
    def kasan(self,after):
        self.tosi2 = self.tosi + after 

obj = Keisan()
nensu = 2030 - 2024
obj.kasan(nensu)
print(f'現在{obj.tosi}歳の{obj.name}は、2030年には{obj.tosi2}歳になります。')
