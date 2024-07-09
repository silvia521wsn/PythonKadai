"""
プログラム名:Ren11-5.py
作成日:2024年7月09日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def in_ninzu(it):
    print(f'{it}の各人数を入力します')
    zaiseki = int(input('在籍数>>'))
    goukaku = int(input('基本情報試験合格者数>>'))
    ninzu = [zaiseki,goukaku]
    return ninzu
def wariai_keisan(ninzu):
    ritu = ninzu[1] / ninzu[0] * 100
    return ritu
def out_ritu(it,ritu):
    print(f'{it}の FE 合格率は {ritu}%')

cd_ninzu = in_ninzu('情報処理科') 
is_ninzu = in_ninzu('IT スペシャリスト科') 
cd_ritu = wariai_keisan(cd_ninzu) 
is_ritu = wariai_keisan(is_ninzu) 
out_ritu('情報処理科',cd_ritu) 
out_ritu('IT スペシャリスト科',is_ritu)