"""
プログラム名:Ren14-1.py
作成日:2024年09月03日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Character:
    name = 'ライオン'
    setumei = '百獣の王'
    def chara_print(self):
        print(f'当動物園でおすすめ：{self.name}')

print('処理科どうぶつえんへようこそ！')
animal = Character()
animal.chara_print()
print(f'PR ポイント：{animal.setumei}')