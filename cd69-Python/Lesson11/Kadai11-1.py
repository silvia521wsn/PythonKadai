"""
プログラム名:Kadai11-1.py
作成日:2024年7月09日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def plus(x,y):
    answer = x + y
    return answer
def minus(x,y):
    answer = x - y
    return answer

choose = input('加算は 1、減算は 2 を入力してください>>')
a = int(input('1 つめのオペランド>>'))
b = int(input('2 つめのオペランド>>'))

if choose == '1':
    w_answer = plus(a,b)
    print(f'足し算の答えは {w_answer} です')
else:
    w_answer = minus(a,b)
    print(f'引き算の答えは {w_answer} です') 