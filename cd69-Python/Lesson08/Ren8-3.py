"""
プログラム名:Ren8-3.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
atai1 = '10'
atai2 = '20'
print(f'1 つめの値={atai1}、2 つめの値={atai2} ')
check = int(input('入力区分(絶対値計算:1/文字連結:2)>>'))
if check == 1:
    atai3 = int(atai1) - int(atai2)
    if atai3 > 0:
        print(f'絶対値は {atai3} です')
    else:
        print(f'絶対値は {atai3*(-1)} です')
else:
    print('文字を連結すると' + atai1 + atai2 + 'です') 