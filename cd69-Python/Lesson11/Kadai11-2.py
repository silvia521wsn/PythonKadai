"""
プログラム名:Kadai11-2.py
作成日:2024年7月09日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def max_syori(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
def min_syori(num1,num2):
    if num1 < num2:
        return num1
    else:
        return num2
def kagen_syori(num1,num2):
    if num1 > num2:
        ans = num1 + num2
    else:
        ans = num2 - num1
    return ans

w_num1 = int(input('1 つめの値>>'))
w_num2 = int(input('2 つめの値>>'))
max_num = max_syori(w_num1,w_num2)
min_num = min_syori(w_num1,w_num2)
kagen = kagen_syori(w_num1,w_num2)

print(f'{w_num1} と {w_num2} では {max_num} が大きいです')
print(f'{w_num1} と {w_num2} では {min_num} が小さいです')
print('1 番目が大きい時は和、2 番目が大きい時は差を求めます')
print(f'値は {kagen} です')