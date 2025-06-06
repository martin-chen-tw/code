import random as rd
import tkinter as tk

root = tk.Tk()
root.title("This is a game manually created by MING-HAO CHEN")
root.geometry("800x600")
root.resizable(False, False)

# 設一個全域變數來保存目前顯示的 Canvas
current_canvas = None

def clear_canvas():
    global current_canvas
    if current_canvas is not None:
        current_canvas.destroy()
        current_canvas = None

def canva1():
    global current_canvas
    clear_canvas()
    current_canvas = tk.Canvas(root, width=300, height=300)
    current_canvas.create_text(10, 0, text='hello', anchor='nw')
    current_canvas.create_text(20, 20, text='world', anchor='nw', font=('Arial', 20))
    current_canvas.create_text(30, 40, text='I am\nOXXO', anchor='nw', fill='#f00', font=('Arial', 30, 'bold'))
    current_canvas.create_text(40, 110, text='測試1', anchor='nw', fill='#0a0', font=('Arial', 30, 'bold', 'italic', 'underline'))
    current_canvas.pack()

def canva2():
    global current_canvas
    clear_canvas()
    current_canvas = tk.Canvas(root, width=300, height=300)
    current_canvas.create_text(10, 0, text='hello', anchor='nw')
    current_canvas.create_text(20, 20, text='world', anchor='nw', font=('Arial', 20))
    current_canvas.create_text(30, 40, text='I am\nOXXO', anchor='nw', fill='#f00', font=('Arial', 30, 'bold'))
    current_canvas.create_text(40, 110, text='測試2', anchor='nw', fill='#0a0', font=('Arial', 30, 'bold', 'italic', 'underline'))
    current_canvas.pack()

# 選單設計
menu = tk.Menu(root)
munubar_1 = tk.Menu(menu, tearoff=0)
munubar_1.add_command(label='canva1', command=canva1)
munubar_1.add_command(label='canva2', command=canva2)
munubar_1.add_command(label='canva3')  # 尚未實作
menu.add_cascade(label='option', menu=munubar_1)
root.config(menu=menu)

root.mainloop()