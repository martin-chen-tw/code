import tkinter as tk

def clear_focus(event):
    # 如果目前點擊的 widget 不是 Entry，就清除焦點
    if not isinstance(event.widget, tk.Entry):
        root.focus_set()

def on_focus_out(event):
    print(f"{event.widget} 失去焦點")

root = tk.Tk()
root.geometry('300x150')

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
btn = tk.Button(root, text="我是按鈕")

entry1.pack(pady=5)
entry2.pack(pady=5)
btn.pack(pady=5)

# 綁定所有 entry 的 focus out 行為
entry1.bind('<FocusOut>', on_focus_out)
entry2.bind('<FocusOut>', on_focus_out)

# 全域滑鼠點擊事件，用於清除焦點
root.bind_all('<Button-1>', clear_focus, add='+')

root.mainloop()
