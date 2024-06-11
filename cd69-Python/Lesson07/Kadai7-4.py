"""
プログラム名:Kadai7-4.py
作成日:2024年6月11日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
tosi = int(input('年齢入力>>'))
if tosi < 10 :
    tukisoi = int(input('付き添い(有:1、無:0)>>'))
    if tukisoi == 1:
        print('このアトラクションは利用可能です。')
    else:
        print('このアトラクションは利用できません。')
    
else:  
    print('このアトラクションは利用可能です。') 