"""
プログラム名:Ren12-1.py
作成日:2024年7月16日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def kake(x,y):
    answer = x * y
    return answer
def wari(x,y):
    answer = x / y
    return answer

print('計算を行います')
key = input('かけ算は a または A、わり算は b または B を入力>>')
a = int(input('1 つめのオペランド>>'))
b = int(input('2 つめのオペランド>>'))

if key == 'a' or key == 'A':
    w_answer = kake(a,b)
    print(f'かけ算の答え：{w_answer}')
else:
    w_answer = wari(a,b) 
    print(f'わり算の答え：{w_answer}') 