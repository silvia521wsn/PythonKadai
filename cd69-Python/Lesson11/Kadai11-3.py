"""
プログラム名:Kadai11-3.py
作成日:2024年7月09日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def kaijo(n): 
    ans = 1 
    while n > 0:
        ans *= n 
        n -= 1
    return ans 

n = int(input('求めたい階乗 n を入力>>')) 
if n < 0:
    print(f'{n}の階乗は求められません。0 以上を入力してください。')
else: 
    ans = kaijo(n) 
    print(f'n = {n} のとき、n! = {ans}') 