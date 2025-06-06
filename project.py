import random as rd
import tkinter as tk
from enum import Enum

class Snake:
    bodies = []
    direction = None
    global gameconfig
    global canvam
    def __init__(self, gameconfig):
        first_create_body_after_hand = True
        len = gameconfig.snake_ini_len
        self.bodies.append([rd.randint(1, gameconfig.block_number[0]), rd.randint(1, gameconfig.block_number[1])])
        success_create_body_count = 1
        while success_create_body_count < gameconfig.snake_ini_len:
            judge_number = rd.randint(1, 4)
            last = self.bodies[success_create_body_count - 1]
            match judge_number:
                case 1:
                    new_body = [last[0] + 1, last[1]]
                    if (first_create_body_after_hand):
                        self.direction = dir.left
                case 2:
                    new_body = [last[0] - 1, last[1]]
                    new_body = [last[0] + 1, last[1]]
                    if (first_create_body_after_hand):
                        self.direction = dir.right
                case 3:
                    new_body = [last[0], last[1] + 1]
                    if (first_create_body_after_hand):
                        self.direction = dir.down
                case 4:
                    new_body = [last[0], last[1] - 1]
                    if (first_create_body_after_hand):
                        self.direction = dir.up
            first_create_body_after_hand = False
            
            if 1 <= new_body[0] <= gameconfig.block_number[0] and 1 <= new_body[1] <= gameconfig.block_number[1]:
                if new_body not in self.bodies:
                    self.bodies.append(new_body)
                    success_create_body_count += 1
    def move_snake (self):
        pass
    def change_direction(self, gameconfig):
        pass
    def change_color(self , gaomeconfig , cnavamanager):
        pass

class CanvaManager:
    def __init__(self, root):
        self.root = root
        self.canvas = None

    def clear_canvas(self):
        if self.canvas is not None:
            self.canvas.destroy()
            self.canvas = None

    def main_page(self):
        root.geometry('800x600')
        self.clear_canvas()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.create_text( 400, 45, text='Snake Io Game', anchor='center', fill='#000000', font=('Times New Roman', 30, 'bold'))
        self.canvas.create_text( 400, 85, text='Created by MING-HAO CHIN', anchor='center', fill='#000000', font=('Times New Roman', 17))
        self.canvas.create_text( 400, 110, text='All Right Reserved', anchor='center', fill='#303030', font=('Times New Roman', 10))
        self.canvas.pack()
    def gaming_page(self):
        pass
        

class Gameconfig:
    def __init__(self):
        self.block_number = [10,10]
        self.screen_size = [200,230]
        self.snake_ini_len = 3
        
class dir(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

def menu_setting(root):
    global menu 
    menu = tk.Menu(root)

    menubar_1 = tk.Menu(menu)
    menubar_1.add_command(label='restart game', state='disabled', command=lambda: start_game())
    menubar_1.add_command(label='go to main page', state='disabled', command=lambda: go_to_main_page())
    menubar_1.add_command(label='informatin', state='active', command=lambda: go_to_info_page())
    menu.add_cascade(label='option', menu=menubar_1)

    root.config(menu=menu)

def window_setting():
    global root
    root = tk.Tk()
    root.title("Snake io game")
    root.geometry("800x600")
    root.resizable(False, False)

def start_game():
    pass

def go_to_main_page():
    canvam.main_page()  

def go_to_info_page():
    pass

# Main function is here
window_setting()
gameconfig = Gameconfig()
menu_setting(root)
canvam = CanvaManager(root)
go_to_main_page()
root.mainloop()
