"""
プログラム名:Kadai9-1.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
print('****掛け算練習プログラム****')
dan = int(input('いくつの段を練習しますか？1～9 を入力>>'))
for i in range(9):
    ans = int(input(f"{dan}*{i+1}は？"))
    if ans == dan*(i+1):
        print('正解です')
    else:
        print(f'不正解。答えは {dan*(i+1)} でした')