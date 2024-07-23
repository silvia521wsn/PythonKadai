"""
プログラム名:Ren13-4.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Cafe:
    soup = 'ポタージュ'
    meal = 'ナポリタン'
    def omise_open(self):
        print('Welcome!')

set_menu = Cafe()
set_menu.omise_open()
print(f'セットメニューは{set_menu.soup}と{set_menu.meal}です')