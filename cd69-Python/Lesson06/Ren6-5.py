"""
プログラム名:Ren6-5.py
作成日:2024年6月4日
作成者:(CD69-3組 K024C2100 WANG SHINING
"""
uriage ={'kamata':65,'omori':110,'oimachi':50}
print(f'最初のディクショナリの内容:{uriage}')
uriage['kawasaki'] = 125
uriage['kamata'] = 70
del uriage['oimachi']
print(f'現在のディクショナリの内容:{uriage}') 
sum1 = sum(uriage.values()) 
print(f'3店舗合計:{sum1} 個') 