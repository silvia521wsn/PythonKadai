"""
プログラム名:Kadai8-1.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
keisan = int(input('計算しますか？(する:1/しない:0)>>'))
if keisan == 1:
    num1 = int(input('１つめのオペランド>>'))
    enzansi = input('演算子>>')
    num2 = int(input('2つめのオペランド>>'))
    if enzansi == '+':
        print(f'答えは {num1 + num2}')
    elif enzansi == '-':
        print(f'答えは {num1 - num2}')
    elif enzansi == '*':
        print(f'答えは {num1 * num2}')
    elif enzansi == '/':
        print(f'答えは {num1 / num2}')
    else:
        print('計算できません')
else:
    print('計算希望なしなので終了します') 