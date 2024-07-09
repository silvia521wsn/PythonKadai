"""
プログラム名:Ren11-4.py
作成日:2024年7月09日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
def heikin_ver2(w_cd69):
    avg = sum(w_cd69)/len(w_cd69)
    return avg

print('クラス平均表示プログラム Ver.2')    
cd69 = list()
for num in range(4): 
    ten = int(input(f'{num+1}組の点数>>'))  
    cd69.append(ten) 
kekka = heikin_ver2(cd69)
print(f'4クラス平均:{kekka} 点')