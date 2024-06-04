"""
プログラム名:Kadai6-1.py
作成日:2024年6月4日
作成者:(CD69-3組 K024C2100 WANG SHINING
"""
it = [88,90,95,100,99,92]
print(f'CD69期、IS18期の全点数={it}')
print(f'うち CD69期の点数={it[0:4]}')
print(f'うち IS18期の点数={it[4:]}') 
sum1 = sum(it[0:4])
avg1 = sum1/len(it[0:4])
print(f'CD69期:合計{sum1}点、平均{avg1}点')
sum2 = sum(it[4:])
avg2 = sum2/len(it[4:])
print(f'IS18期:合計{sum2}点、平均{avg2}点')