"""
プログラム名:Ren8-2.py
作成日:2024年6月18日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
score = int(input('点数を入力してください>>'))
if score < 0:
    print('点数は 0 以上 100 の範囲で入力してください') 
elif score < 60:
    print('評価は D です')
elif score < 70:
    print('評価は C です')
elif score < 80:
    print('評価は B です')
elif score < 90:
    print('評価は A です')
elif score <= 100:
    print('評価は S です')
else:
    print('点数は 0 以上 100 の範囲で入力してください') 