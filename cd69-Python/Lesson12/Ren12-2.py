"""
プログラム名:Ren12-2.py
作成日:2024年7月16日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
IT = 'ITスペシャリスト科'
def it_print():
    global IT
    IT = '情報処理科'   

print(f'変更前のグローバル変数 IT の内容：{IT}')
it_print()
print(f'変更後のグローバル変数 IT の内容：{IT}')