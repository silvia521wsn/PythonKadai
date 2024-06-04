"""
プログラム名:Kadai6-3.py
作成日:2024年6月4日
作成者:(CD69-3組 K024C2100 WANG SHINING
"""
it_college = {'CD':69,'IS':18,'NT':28}
print(f'追加前：{it_college}')
code = str(input('新しい学科コード(半角英字)>>'))
key = str(input('新しい学科の期(半角数字)>>'))
it_college[code] = key
print(f'追加後:{it_college}') 