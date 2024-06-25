"""
プログラム名:Kadai9-4.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
data = [73, 59, 92, 83, 75, 52, 95, 70, 69, 80]
gusu = [] 
kisu = [] 
for i in range(10):
    if i % 2 == 0:  
        gusu.append(data[i])
    else: 
        kisu.append(data[i])
print(data)
print(gusu)
print(kisu)
