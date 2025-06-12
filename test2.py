import tkinter as tk


root = tk.Tk()
root.geometry('300x150')
canvas = tk.Canvas(root, bg='lightblue', width=300, height=150)
w =canvas.create_window(150, 75, window=tk.Label(canvas, text='123123', bg='lightblue'))
r = tk.Canvas.create_rectangle(canvas, 1,1,30,30, fill='red', outline='black')
canvas.pack()
root.mainloop()