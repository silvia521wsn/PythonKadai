"""
プログラム名:Kadai10-4.py
作成日:2024年7月02日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def sankaku():
    kigou = input('表示記号>>')
    gyo = int(input('三角形の高さ>>'))
    while gyo > 0:
        print(f'{kigou}'*gyo)
        gyo -= 1

print('***花文字プログラム(逆三角形表示)***')
sankaku()