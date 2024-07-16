"""
プログラム名:Code6-3.py
作成日:2024年7月16日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
userinfo = input('名前と血液型をカンマで区切って１行で入力>>')
[name,blood] =userinfo.split(',')
blood = blood.upper().strip()
print(f'{name}さんは{blood}型なので大吉です')