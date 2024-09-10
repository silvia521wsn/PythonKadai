"""
プログラム名:Kadai15-1.py
作成日:2024年09月10日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
import tkinter as tk 
root = tk.Tk() 
root.geometry('300x200') 
root.title('(任意課題15-1)会員ツール') 
button1 = tk.Button(root,text='会員登録',width=20, height=2)
button2 = tk.Button(root,text='検索',width=20, height=2)  
button1.pack(pady=40)
button2.pack()  
root.mainloop() 