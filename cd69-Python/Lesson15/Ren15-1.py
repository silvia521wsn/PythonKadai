"""
プログラム名:Ren15-1.py
作成日:2024年09月10日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
import requests 
response = requests.get('https://www.python.org/downloads/') 
text = response.text 
print(text) 