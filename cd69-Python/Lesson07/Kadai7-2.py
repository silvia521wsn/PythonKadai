"""
プログラム名:Kadai7-2.py
作成日:2024年6月11日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
height_cm = float(input('身長(cm)>>'))
weight = float(input('体重(kg)>>'))
height_m = height_cm/100
BMI = int(weight/height_m/height_m)
print(f'BMI={BMI}')
if BMI >= 25:
    print('肥満')
else:
    print('正常') 