"""
プログラム名:Kadai10-2.py
作成日:2024年7月02日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def kakezan(w_ope1,w_ope2,w_ope3):
    print(f'{w_ope1} × {w_ope2} × {w_ope3} = {w_ope1*w_ope2*w_ope3}')

print('3値の掛け算プログラム')
ope1 = int(input('1 つめの値>>'))
ope2 = int(input('2 つめの値>>'))
ope3 = int(input('3 つめの値>>'))

kakezan(ope1,ope2,ope3)