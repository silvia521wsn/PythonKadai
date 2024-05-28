"""
プログラム名:Ren5-4.py
作成日:2024年5月28日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
tatemono = ['地下1階','1階', '2階', '3階', '4階']
print('現在の建物のフロア状況\n' + str(tatemono) + '\n')
tatemono.append('屋上')
print('屋上が完成しました\n' + str(tatemono) + '\n')
tatemono.remove('地下1階')
print('地下1階を閉鎖しました\n' + str(tatemono) + '\n')
tatemono[2] = 'M2階'
print('3階をM2階に改装しました\n' + str(tatemono) + '\n') 