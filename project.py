import random as rd
import tkinter as tk
from tkinter import messagebox as mb
from enum import Enum
TEST_MODE = True
class Snake:
    bodies = []
    def __init__(self, gameconfig):
        self._direction = tk.IntVar()
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
                        self.direction.set(Dir.left.value)
                case 2:
                    new_body = [last[0] - 1, last[1]]
                    new_body = [last[0] + 1, last[1]]
                    if (first_create_body_after_hand):
                        self.direction.set(Dir.right.value)
                case 3:
                    new_body = [last[0], last[1] + 1]
                    if (first_create_body_after_hand):
                        self.direction.set(Dir.down.value)
                case 4:
                    new_body = [last[0], last[1] - 1]
                    if (first_create_body_after_hand):
                        self.direction.set(Dir.up.value)
            first_create_body_after_hand = False
            
            if 1 <= new_body[0] <= gameconfig.block_number[0] and 1 <= new_body[1] <= gameconfig.block_number[1]:
                if new_body not in self.bodies:
                    self.bodies.append(new_body)
                    success_create_body_count += 1
    def move_ (self):
        pass
    def set_direction_U(self):
        self.__direction.set(Dir.up.value)
    def set_direction_D(self):
        self.__direction.set(Dir.down.value)
    def set_direction_L(self):
        self.__direction.set(Dir.left.value)
    def set_direction_R(self):
        self.__direction.set(Dir.right.value)
    def change_color(self):
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
        global gameconfig
        root.geometry('800x600')
        self.clear_canvas()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.create_text( 400, 32, text='Snake', anchor='center', fill=f'#{0x000000:06X}', font=('Times New Roman', 42, 'bold'))
        self.canvas.create_text( 400, 75, text='Created by MING-HAO CHIN 20250613', anchor='center', fill='black', font=('Times New Roman', 17))
        self.canvas.create_text( 400, 100, text='DO NOT USE FOR ANY OTHER PURPOSE EXCEPT ', anchor='center', fill='#303030', font=('Times New Roman', 10, 'bold'))
        self.canvas.create_text( 400, 115, text='NCCU_1132_207047001_Computer Programming Group1 Final Project', anchor='center', fill='#303030', font=('Times New Roman', 10))
        self.canvas.create_line( 10, 127, 790, 127, fill='black', width=2)

        self.canvas.create_text( 400, 147, text='Screen Display ', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        self.light_button = tk.Radiobutton(self.root, text='light mode', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                      ,variable=gameconfig.dark_mod, value=False)
        self.dark_button = tk.Radiobutton(self.root, text='dark mode', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                      ,variable=gameconfig.dark_mod, value=True)
        self.light_button.place(x=250, y=175, anchor='center')
        self.dark_button.place(x=550, y=175, anchor='center')

        self.canvas.create_text( 400, 200, text='Map Configeration', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        
        self.large_size_button = tk.Radiobutton(self.root, text='large size', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.size, value=Size.large.value, command=lambda: gameconfig.update_size(Size.large))
        self.medium_size_button = tk.Radiobutton(self.root, text='medium size', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                 ,variable=gameconfig.size, value=Size.medium.value, command=lambda: gameconfig.update_size(Size.medium))
        self.small_size_button = tk.Radiobutton(self.root, text='small size', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.size, value=Size.small.value, command=lambda: gameconfig.update_size(Size.small))
        
        self.large_size_button.place(x=600, y=235, anchor='center')
        self.medium_size_button.place(x=400, y=235, anchor='center')
        self.small_size_button.place(x=200, y=235, anchor='center')
        
        #---

        self.canvas.create_text( 400, 270, text='Game Speed', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        self.fast_speed_button = tk.Radiobutton(self.root, text='fast', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.speed, value=Speed.fast.value)
        self.medium_speed_button = tk.Radiobutton(self.root, text='medium', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                 ,variable=gameconfig.speed, value=Speed.medium.value)
        self.slow_speed_button = tk.Radiobutton(self.root, text='slow', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.speed, value=Speed.slow.value)
        self.fast_speed_button.place(x=600, y=305, anchor='center')
        self.medium_speed_button.place(x=400, y=305, anchor='center')
        self.slow_speed_button.place(x=200, y=305, anchor='center')

        #---
        
        def clear_focus(event):
            widget = event.widget
            if isinstance(widget, tk.Entry):
                return
            root.focus_set()
            
        root.bind_all('<Button-1>', clear_focus, add='+')
        
        def select_default_len():
            self.customized_ini_body_len_entry.config(state='normal')
            self.customized_ini_body_len_entry.insert(0, '3')
            self.customized_ini_body_len_entry.delete(1, 'end')
            self.customized_ini_body_len_entry.config(state='disabled')
            gameconfig.snake_ini_len.set(3)

        def select_customized_len():
            self.customized_ini_body_len_entry.config(state='normal')
            
        def ini_len_vcmd(x):
            if x.isdigit() and 3 <= int(x) <= 15:
                return True
            else:
                return False
            
        def ini_len_ivcmd(x):
            if not x.isdigit():
                message = "THe lengh must be a integer"
                self.customized_ini_body_len_entry.insert(0, '3')
                self.customized_ini_body_len_entry.delete(1, 'end')
            elif int(x) < 3:
                self.customized_ini_body_len_entry.insert(0, '3')
                self.customized_ini_body_len_entry.delete(1, 'end')
                message = "The lengh is too small (should longer than 3)"
            elif int(x) > 15:
                self.customized_ini_body_len_entry.delete(0, 'end')
                self.customized_ini_body_len_entry.insert(0, '15')
                self.customized_ini_body_len_entry.delete(2, 'end')
                message = "The lengh is too long (should shorter than 15)"
            mb.showerror("Wrong lengh value configeration",message, )
                
        len_vcmd = (self.root.register(ini_len_vcmd), '%P')
        len_ivcmd =(self.root.register(ini_len_ivcmd), '%P')
        self.canvas.create_text( 400, 340, text='Snake Configeration', anchor='center', fill='#202020', 
                                font=('Times New Roman', 19, 'bold'))
        self.default_ini_body_len_button = tk.Radiobutton(self.root, text='default initial lengh (3)', anchor='center', 
                                                          fg='#404040', font=('Times New Roman', 15, 'bold'),variable=gameconfig.is_customized_body_len,value=False) 
        self.customized_ini_body_len_button = tk.Radiobutton(self.root, text='customized initial lengh', anchor='center', 
                                                             fg='#404040', font=('Times New Roman', 15, 'bold'),variable=gameconfig.is_customized_body_len,value=True)
        self.customized_ini_body_len_entry = tk.Entry(self.root, width=3, font=('Times New Roman', 12, 'bold'), fg='#404040', bg='#f0f0f0',
                                                      state='normal',validate='focusout', validatecommand=len_vcmd,invalidcommand=len_ivcmd)
        self.customized_ini_body_len_entry.insert(0, '3')
        self.customized_ini_body_len_entry.config(state='disabled')
        self.default_ini_body_len_button.config(command=lambda: select_default_len())
        self.customized_ini_body_len_button.config(command=lambda: select_customized_len())

        self.default_ini_body_len_button.place(x=210, y=375, anchor='center')
        self.customized_ini_body_len_button.place(x=540, y=375, anchor='center')
        self.customized_ini_body_len_entry.place(x=680, y=375, anchor='center')

        #---

        self.default_body_color_button = tk.Radiobutton(self.root, text='default body color', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                        ,variable=gameconfig.snake_color)
        self.customized_body_color_button = tk.Radiobutton(self.root, text='customized body color', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                        ,variable=gameconfig.snake_color, value=0x000000)
        self.customized_body_color_entry = tk.Entry(self.root, width=10, font=('Times New Roman', 15, 'bold'), fg='#404040', bg='#f0f0f0')
        self.customized_body_color_entry.insert(0, '#000000')
        self.discoloration_button = tk.Checkbutton(self.root, text='discoloration', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                                    ,variable=gameconfig.discoloration, onvalue=True, offvalue=False)
        
        # self.default_body_color_button.place(x=600, y=375, anchor='center')
        # self.customized_body_color_button.place(x=600, y=405, anchor='center')
        # self.customized_body_color_entry.place(x=600, y=435, anchor='center')
        # self.discoloration_button.place(x=400, y=375, anchor='center')
        # gameconfig.snake_ini_len.set(int(self.customized_ini_body_len_entry.get()) if gameconfig.is_customized_body_len.get() else 3)
        # create a Save button as a test way
        self.save_config_button = tk.Button(self.root, text='save config', anchor='center', fg='#404040', font=('Times New Roman', 15, 'bold')
                                            ,command=lambda: saving_config()).place(x=400, y=580, anchor='center')
        
        self.canvas.pack()
        
        def saving_config():
            pass

    
        
    def gaming_page(self):
        root.geometry() #TBD
        self.clear_canvas()

    def rank_score_and_info_page(self):
        root.geometry('800x600') 
        self.clear_canvas()
        

class Gameconfig:
    def __init__(self):
        self.size = tk.StringVar(value=Size.small.value)
        self._block_number = [10, 10]
        # 10x10 20x20 50x30
        self._screen_size = [200,250]
        # 200x250 400x450 1000x650
        self.is_customized_body_len = tk.BooleanVar(value=False)
        self.snake_ini_len = tk.IntVar(value=3)
        self.snake_color = tk.IntVar(value=0x5ff26a)
        self.discoloration = tk.BooleanVar(value=True)
        self.dark_mod = tk.BooleanVar(value=False)
        self.speed = tk.StringVar(value=Speed.slow.value)
        self.random_generated_mod = tk.BooleanVar(value=True)
        self.random_seed = tk.IntVar()
        
    def update_size(self ,new_size):
        self.size.set(new_size.value)
        match self.size:
            case Size.small:
                self.block_number = [10, 10]
                self.screen_size = [200, 250]
            case Size.medium:
                self.block_number = [20, 20]
                self.screen_size = [400, 450]
            case Size.large:
                self.block_number = [50, 30]
                self.screen_size = [1000, 650]
        
class Last_Record:
    # when editing the variable type, change tk value declare functon type as well
    pass

class Best_Record:
    # when editing the variable type, change tk value declare functon type as well
    pass

class Size(Enum):
    # when editing the variable type, change tk value declare functon type as well
    small = 'small'
    medium = 'medium'
    large = 'large'

class Dir(Enum):
    # when editing the variable type, change tk value declare functon type as well
    up = 1
    down = 2
    left = 3
    right = 4

class Speed(Enum):
    # when editing the variable type, change tk value declare functon type as well
    fast = 'fast'
    medium = 'medium'
    slow = 'slow'
    

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
    global canvam
    global root
    global snake
    root = tk.Tk()
    root.title("Snake io game")
    root.geometry("800x600")
    root.resizable(False, False)
if False: #tmp disable
    root.bind('<Up>', lambda event: snake.set_direction_U())
    root.bind('<Down>', lambda event: snake.set_direction_D())
    root.bind('<Left>', lambda event: snake.set_direction_L())
    root.bind('<Right>', lambda event: snake.set_direction_R())
    root.bind('<w>', lambda event: snake.set_direction_U())
    root.bind('<s>', lambda event: snake.set_direction_D())
    root.bind('<a>', lambda event: snake.set_direction_L())
    root.bind('<d>', lambda event: snake.set_direction_R()) 

def start_game():
    pass

def go_to_main_page():
    canvam.main_page()  

def go_to_info_page():
    pass

# Main function is here
if __name__ == "__main__":
    window_setting()
    gameconfig = Gameconfig()
    menu_setting(root)
    canvam = CanvaManager(root)
    go_to_main_page()
    root.mainloop()


#note
    # We can't just write '#f{0x000000}' as '#000000' because it turns out to be '#0', we should add ':06X' after the text to declare a fixed output format 
    # so 'black'equals to '#000000' and f'#{0x000000:06X}'
    # Use 'x' when lowercase English letters in hexadecimal are expected
    # hex_str = '0x123456'
    # hex_num = int(hex_str, 16) --> hex_num = 0x123456