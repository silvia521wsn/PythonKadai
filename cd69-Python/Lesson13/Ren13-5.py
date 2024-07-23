"""
プログラム名:Ren13-5.py
作成日:2024年7月23日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
class Teaset:
    eat = 'キッシュ'
    tea = 'ダージリンティー'
    tanka = 1000
    kei = 0
    def naiyou(self):
        print(f'ティーセットの内容は{self.eat}と{self.tea}です ')
    def kaikei(self,setsu):
        self.kei = self.tanka * setsu

tea_time = Teaset()
tea_time.naiyou()
tea_time.kaikei(3)
print(f'3 セットのご注文なので合計 {tea_time.kei} 円です')