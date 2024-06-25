"""
プログラム名:Code4-10.py
作成日:2024年6月25日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
ages = [28,50,8,20,78,25,22,10,27,33]
num = 5
samples = list()
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples) 