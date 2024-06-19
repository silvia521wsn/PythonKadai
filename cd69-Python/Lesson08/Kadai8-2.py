"""
プログラム名:Kadai8-2.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
atai1 = input('1 つめの値>>')
atai2 = input('2 つめの値>>')
flg = int(input('入力データ区分(数値:1/文字:2)>>'))
if flg == 1:
    print('入力値が数値のため大小比較します')
    if int(atai1) == int(atai2):
        print('2 つの値は同じです')
    elif int(atai1) > int(atai2):
        print('１つめの値の方が大きいです')
    else:
        print('2 つめの値の方が大きいです')
else:
    print('入力値が文字のため文字連結します')
    print(atai1 + atai2)