"""
プログラム名:Code4-4.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f'ひつじが{count}匹')
    key = input('もう眠りそうですか？(y/n)>>')
    if key == 'y':
        is_awake = False
print('おやすみなさい')