import tkinter as tk

root = tk.Tk()
root.title("Snake Head")

canvas = tk.Canvas(root, width=30, height=30, bg='white')
canvas.pack()


canvas.create_oval(5, 2, 25, 28, fill='#D2B48C', outline='')

canvas.create_polygon(8, 20, 15, 29, 22, 20, fill='#A0522D', outline='')


canvas.create_oval(9, 8, 12, 12, fill='black', outline='')


canvas.create_oval(18, 8, 21, 12, fill='black', outline='')


canvas.create_oval(13, 4, 14, 5, fill='#8B4513', outline='')
canvas.create_oval(16, 4, 17, 5, fill='#8B4513', outline='')


canvas.create_oval(13, 14, 17, 17, fill='#C19A6B', outline='')
canvas.create_oval(11, 16, 15, 19, fill='#C19A6B', outline='')
canvas.create_oval(15, 16, 19, 19, fill='#C19A6B', outline='')
canvas.create_oval(9, 18, 13, 21, fill='#C19A6B', outline='')
canvas.create_oval(17, 18, 21, 21, fill='#C19A6B', outline='')

root.mainloop()
