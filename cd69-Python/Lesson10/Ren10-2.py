"""
プログラム名:Ren10-2.py
作成日:2024年7月02日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
dan = int(input('いくつの段を練習しますか？1～9 を入力>>'))
for i in range(9):
    print(f'{dan} × {i+1} = {dan*(i+1)}')
    