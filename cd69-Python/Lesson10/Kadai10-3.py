"""
プログラム名:Kadai10-3.py
作成日:2024年7月02日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def out_syori(num):
    shou = num // 7
    amari = num % 7
    while shou > 0:
        print('*******')
        shou -= 1
    print('*'*amari)

print('1 行あたり 7 個づつ表示します')
num1 = int(input('＊をいくつ表示しますか>>'))
out_syori(num1)