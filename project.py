import numpy as np
import random as rd # tmp, use numpy instead
import tkinter as tk
import re
from tkinter import messagebox as mb
from enum import Enum
TEST_MODE = True
class Snake:
    bodies = []
    def __init__(self, gameconfig):
        self._direction = tk.IntVar()
        is_first_time = True
        len = gameconfig.snake_ini_len
        self.bodies.append([rd.randint(1+1, gameconfig.block_number[0]-1), rd.randint(1+1, gameconfig.block_number[1]-1)])
        while next in self.bodies or is_first_time:
            is_first_time = False
            first_create_body_after_hand = True
            success_create_body_count = 1
            while success_create_body_count < gameconfig.snake_ini_len:
                judge_number = rd.randint(1, 4)
                last = self.bodies[success_create_body_count - 1]
                match judge_number:
                    case 1:
                        new_body = [last[0] + 1, last[1]]
                        if (first_create_body_after_hand):
                            self.direction.set(Dir.left.value)
                        next = [last[0] - 1, last[1]]
                    case 2:
                        new_body = [last[0] - 1, last[1]]
                        new_body = [last[0] + 1, last[1]]
                        if (first_create_body_after_hand):
                            self.direction.set(Dir.right.value)
                        next = [last[0] + 1, last[1]]
                    case 3:
                        new_body = [last[0], last[1] + 1]
                        if (first_create_body_after_hand):
                            self.direction.set(Dir.down.value)
                        next = [last[0], last[1] - 1]
                    case 4:
                        new_body = [last[0], last[1] - 1]
                        if (first_create_body_after_hand):
                            self.direction.set(Dir.up.value)
                        next = [last[0] + 1, last[1] ]
                first_create_body_after_hand = False
            if success_create_body_count >= gameconfig.snake_ini_len:
                first_create_body_after_hand = True
                success_create_body_count = 1
            
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
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.main_page_widgets = ["start_game_button","light_button","dark_button","large_size_button","medium_size_button","small_size_button",
    "fast_speed_button","medium_speed_button","slow_speed_button","default_ini_body_len_button","customized_ini_body_len_button","default_body_color_button",
    "customized_body_color_button","random_mod_button","fixed_mod_button","discoloration_button","customized_ini_body_len_entry","customized_body_color_entry",
    "random_seed_entry"]
       
        for name in self.main_page_widgets:
            setattr(self.canvas, name, None)

    def clear_canvas_and_widget(self):
        if self.canvas is not None:
            if TEST_MODE: print("Clearing canvas...")
            try:
                self.canvas.delete("all")
                for widget in self.canvas.winfo_children():
                    widget.destroy()
                self.canvas.pack_forget()
                self.canvas.destroy()
            except Exception as e:
                if TEST_MODE: print(f"Failed to clear canvas: {e}")
            finally:
                if TEST_MODE: print("Clearing canvas done")
                self.canvas = None
        for name in self.main_page_widgets:
            widget = getattr(self, name, None)
            try:
                if widget:
                    widget.destroy()
                    setattr(self, name, None)  
                    if TEST_MODE: print(f"Destroyed canvas widget: {name}")
            except Exception as e:
                if TEST_MODE: print(f"Failed to clear canvas: {e}")
        
    def main_page(self):
        #--- Initialization
        global root, gameconfig, snake
        gameconfig.deactivate_wasd()
        root.geometry('800x600')
        self.clear_canvas_and_widget()

        #--- Title and information
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.create_text( 400, 32, text='Snake', anchor='center', fill=f'#{0x000000:06X}', font=('Times New Roman', 42, 'bold'))
        self.canvas.create_text( 400, 75, text='Created by MING-HAO CHIN 20250613', anchor='center', fill='black', font=('Times New Roman', 17))
        self.canvas.create_text( 400, 100, text='DO NOT USE FOR ANY OTHER PURPOSE EXCEPT ', anchor='center', fill='#303030', font=('Times New Roman', 10, 'bold'))
        self.canvas.create_text( 400, 115, text='NCCU_1132_207047001_Computer Programming Group1 Final Project', anchor='center', fill='#303030', font=('Times New Roman', 10))
        self.canvas.create_line( 10, 127, 790, 127, fill='black', width=2)
        
        #--- Screen Display

        self.canvas.create_text( 400, 147, text='Screen Display ', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        self.light_button = tk.Radiobutton(self.root, text='light mode', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                      ,variable=gameconfig.is_dark_mod, value=False)
        self.dark_button = tk.Radiobutton(self.root, text='dark mode', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                      ,variable=gameconfig.is_dark_mod, value=True)
        self.light_button.place(x=250, y=175,anchor='center')
        self.dark_button.place(x=550, y=175, anchor='center')

        #--- Map Configeration

        self.canvas.create_text( 400, 200, text='Map Configeration', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        
        self.large_size_button = tk.Radiobutton(self.root, text='large size', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.size, value=Size.large.value, command=lambda: gameconfig.update_size(Size.large))
        self.medium_size_button = tk.Radiobutton(self.root, text='medium size', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                 ,variable=gameconfig.size, value=Size.medium.value, command=lambda: gameconfig.update_size(Size.medium))
        self.small_size_button = tk.Radiobutton(self.root, text='small size', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.size, value=Size.small.value, command=lambda: gameconfig.update_size(Size.small))
        self.large_size_button.place(x=600, y=235, anchor='center')
        self.medium_size_button.place(x=400, y=235, anchor='center')
        self.small_size_button.place(x=200, y=235, anchor='center')
        #--- Game Speed

        self.canvas.create_text( 400, 270, text='Game Speed', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        self.fast_speed_button = tk.Radiobutton(self.root, text='fast', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.speed, value=Speed.fast.value)
        self.medium_speed_button = tk.Radiobutton(self.root, text='medium', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                 ,variable=gameconfig.speed, value=Speed.medium.value)
        self.slow_speed_button = tk.Radiobutton(self.root, text='slow', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.speed, value=Speed.slow.value)
        self.fast_speed_button.place(x=600, y=305, anchor='center')
        self.medium_speed_button.place(x=400, y=305, anchor='center')
        self.slow_speed_button.place(x=200, y=305, anchor='center')
        
        #--- Snake Configeration (lengh)
        
        def clear_focus(event):
            widget = event.widget
            if isinstance(widget, tk.Entry):
                return
            root.focus_set()
            
        root.bind_all('<Button-1>', clear_focus, add='+')
        
        def select_default_len():
            self.canvas.customized_ini_body_len_entry.config(state='normal')
            self.canvas.customized_ini_body_len_entry.insert(0, '3')
            self.canvas.customized_ini_body_len_entry.delete(1, 'end')
            self.canvas.customized_ini_body_len_entry.config(state='disabled')
            gameconfig.snake_ini_len.set(3)

        def select_customized_len():
            self.canvas.customized_ini_body_len_entry.config(state='normal')
            
        def ini_len_vcmd(x):
            if x.isdigit() and 3 <= int(x) <= 15:
                return True
            else:
                return False
            
        def ini_len_ivcmd(x):
            if not x.isdigit():
                message = "THe lengh must be a integer"
                self.canvas.customized_ini_body_len_entry.insert(0, '3')
                self.canvas.customized_ini_body_len_entry.delete(1, 'end')
            elif int(x) < 3:
                self.canvas.customized_ini_body_len_entry.insert(0, '3')
                self.canvas.customized_ini_body_len_entry.delete(1, 'end')
                message = "The lengh is too small (should longer than 3)"
            elif int(x) > 15:
                self.canvas.customized_ini_body_len_entry.delete(0, 'end')
                self.canvas.customized_ini_body_len_entry.insert(0, '15')
                self.canvas.customized_ini_body_len_entry.delete(2, 'end')
                message = "The lengh is too long (should shorter than 15)"
            mb.showerror("Wrong lengh value configeration",message)
                
        len_vcmd = (self.root.register(ini_len_vcmd), '%P')
        len_ivcmd =(self.root.register(ini_len_ivcmd), '%P')

        self.canvas.create_text( 400, 340, text='Snake Configeration', anchor='center', fill='#202020', 
                                font=('Times New Roman', 19, 'bold'))
        self.default_ini_body_len_button = tk.Radiobutton(self.root, text='default initial lengh (3)', anchor='center', 
                                                          fg='#363636', font=('Times New Roman', 15, 'bold'),variable=gameconfig.is_customized_body_len,value=False) 
        self.customized_ini_body_len_button = tk.Radiobutton(self.root, text='customized initial lengh', anchor='center', 
                                                             fg='#363636', font=('Times New Roman', 15, 'bold'),variable=gameconfig.is_customized_body_len,value=True)
        self.customized_ini_body_len_entry = tk.Entry(self.root, width=3, font=('Times New Roman', 12, 'bold'), fg='#363636', bg='#f0f0f0',
                                                      state='normal',validate='focusout', validatecommand=len_vcmd,invalidcommand=len_ivcmd)
        self.customized_ini_body_len_entry.insert(0, '3')
        self.customized_ini_body_len_entry.config(state='disabled')
        self.default_ini_body_len_button.config(command=lambda: select_default_len())
        self.customized_ini_body_len_button.config(command=lambda: select_customized_len())

        self.default_ini_body_len_button.place(x=210, y=380, anchor='center')
        self.customized_ini_body_len_button.place(x=540, y=380, anchor='center')
        self.customized_ini_body_len_entry.place(x=680, y=380, anchor='center')

        #--- Snake Configeration (color)

        def select_default_color():
            self.customized_body_color_entry.config(state='normal')
            self.customized_body_color_entry.insert(0, "#5FF26A")
            self.customized_body_color_entry.delete(7, 'end')
            self.customized_body_color_entry.config(state='disabled')
            self.discoloration_button.config(state='normal')
            gameconfig.snake_color.set("#5FF26A")

        def select_customized_color():
            self.customized_body_color_entry.config(state='normal')
            gameconfig.is_discoloration.set(False)
            self.discoloration_button.config(state='disabled')
            
        # Regular expression for hex color code    
        col_pattern = r'^#(?:[0-9A-F]){6}$'  
        def ini_col_vcmd(x):
            return re.fullmatch(col_pattern, x) is not None
        
        def ini_col_ivcmd(x):
            if re.fullmatch(col_pattern, x ,flags=re.IGNORECASE) is not None:
                new = self.customized_body_color_entry.get()
                new = '#' + new if (new[0] != '#') else new
                new = new.upper()
                self.customized_body_color_entry.insert(0, new)
                self.customized_body_color_entry.delete(7, 'end')
            else:
                self.customized_body_color_entry.insert(0, "#5FF26A")
                self.customized_body_color_entry.delete(7, 'end')
                message = "The color code is invalid\n Please follow HTML color code format \n Using the format '#RRGGBB' or 'RRGGBB' (case insensitive)"
                mb.showerror("Wrong value configeration",message)

        col_vcmd = (self.root.register(ini_col_vcmd), '%P')
        col_ivcmd =(self.root.register(ini_col_ivcmd), '%P')

        self.default_body_color_button = tk.Radiobutton(self.root, text='default body color', anchor='center', fg='#363636', font=('Times New Roman', 
                                                            15,'bold'),variable=gameconfig.is_customized_color,value=False,command=lambda: select_default_color())
        self.customized_body_color_button = tk.Radiobutton(self.root, text='customized body color', anchor='center', fg='#363636', font=('Times New Roman', 
                                                        15, 'bold'),variable=gameconfig.is_customized_color, value=True, command=lambda: select_customized_color())
        self.customized_body_color_entry = tk.Entry(self.root, width=10, font=('Times New Roman', 12, 'bold'), fg='#363636', bg='#f0f0f0', 
                                                    validate='focusout',validatecommand=col_vcmd, invalidcommand=col_ivcmd)
        self.customized_body_color_entry.insert(0, '#5FF26A')
        self.customized_body_color_entry.config(state='disabled')
        self.discoloration_button = tk.Checkbutton(self.root, text='discoloration', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                    ,variable=gameconfig.is_discoloration, state='normal', onvalue=True, offvalue=False)
        
        self.default_body_color_button.place(x=170, y=420, anchor='center')
        self.customized_body_color_button.place(x=500, y=420, anchor='center')
        self.customized_body_color_entry.place(x=670, y=420, anchor='center')
        self.discoloration_button.place(x=280, y=420, anchor='center')

        #---


        def select_default_rng():
            rn = str(rd.randint(0, 65535))
            self.random_seed_entry.insert(0, rn)
            self.random_seed_entry.delete(len(rn)-1, 'end')
            self.random_seed_entry.config(state='disabled')

        def select_customized_rng():
            self.random_seed_entry.config(state='normal')

        def ini_rng_vcmd(x):
            return x.isdigit() and 0 <= int(x) <= 65535
        
        def ini_rng_ivcmd(x):
            rn = str(rd.randint(0, 65535))
            self.random_seed_entry.insert(0, rn)
            self.random_seed_entry.delete(len(rn)-1, 'end')
            message = "The RNG seed must be a integer"
            mb.showerror("Wrong value configeration",message)

        rng_vcmd = (self.root.register(ini_rng_vcmd), '%P')
        rng_ivcmd =(self.root.register(ini_rng_ivcmd), '%P')


        self.canvas.create_text( 400, 455, text='Random Number Generator (RNG)', anchor='center', fill='#202020', 
                                font=('Times New Roman', 19, 'bold'))
        self.random_mod_button = tk.Radiobutton(self.root, text='random mode', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.is_random_mod, state='normal',value=True, command=lambda: select_default_rng())
        self.fixed_mod_button = tk.Radiobutton(self.root, text='fixed mode', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.is_random_mod, state='normal',value=False, command=lambda: select_customized_rng())

        self.random_seed_entry = tk.Entry(self.root, width=10, font=('Times New Roman', 15, 'bold'), fg='#363636', bg='#f0f0f0',
                                          validate='focusout', validatecommand=rng_vcmd, invalidcommand=rng_ivcmd)
        self.random_seed_entry.config(state='disabled')

        self.random_mod_button.place(x=250, y=495, anchor='center')
        self.fixed_mod_button.place(x=550, y=495, anchor='center')
        self.random_seed_entry.place(x=670, y=495, anchor='center')

        #--- Start Game Button

        def ready_to_start_game():
            #save gameconfig
            gameconfig.update_size(gameconfig.size.get())

        def start_game():
            ready_to_start_game()
            self.main_page()

        self.start_game_button = tk.Button(self.root, text='Start Game', anchor='center', fg='#000000', font=('Times New Roman', 19, 'bold')
                                            ,command=lambda: (start_game(),self.gaming_page()))
        self.start_game_button.place(x=400, y=545, anchor='center')
        
        #--- 

        self.canvas.pack()
    
        
    def gaming_page(self):
        root.geometry('800x600') #TBD
        self.clear_canvas_and_widget()

    def rank_score_and_info_page(self):
        root.geometry('800x600') 
        self.clear_canvas_and_widget()
        

class Gameconfig:
    def __init__(self):
        # Screen size and color
        self.size = tk.StringVar(value=Size.small.value)
        self._block_number = [10, 10]
            # 10x10 20x20 50x30
        self._screen_size = [300,400]
            # 300x400 600x700 1500x1300 (x*30, y*30+100)
        self.is_dark_mod =      tk.BooleanVar(value=False)
        # Snake len and color
        self.is_customized_body_len = tk.BooleanVar(value=False)
        self.snake_ini_len =    tk.IntVar(value=3)
        self.is_customized_color = tk.BooleanVar(value=False)
        self.snake_color =      tk.StringVar(value="#5FF26A")
        self.is_discoloration = tk.BooleanVar(value=True)
        # Game control
        self.speed =            tk.StringVar(value=Speed.slow.value)
        self.is_random_mod =       tk.BooleanVar(value=True)
        self.random_seed =      tk.IntVar()
        #Others
        self.bind_ids = {}
    
    def copy_from(myself, other):
        # Screen size and color
        myself.size.set(other.size.get())
        myself._block_number = other._block_number[:]
        myself._screen_size = other._screen_size[:]
        myself.is_dark_mod.set(other.is_dark_mod.get())
        # Snake len and color
        myself.is_customized_body_len.set(other.is_customized_body_len.get())
        myself.snake_ini_len.set(other.snake_ini_len.get())
        myself.is_customized_color.set(other.is_customized_color.get())
        myself.snake_color.set(other.snake_color.get())
        myself.is_discoloration.set(other.is_discoloration.get())
        # Game control
        myself.speed.set(other.speed.get())
        myself.is_random_mod.set(other.is_random_mod.get())
        myself.random_seed.set(other.random_seed.get())

    def update_size(self ,new_size):
        match new_size:
            case Size.small:
                self.block_number = [10, 10]
                self.screen_size = [200, 250]
            case Size.medium:
                self.block_number = [20, 20]
                self.screen_size = [400, 450]
            case Size.large:
                self.block_number = [50, 30]
                self.screen_size = [1000, 650]

    def activate_wasd(self):
        global root, snake
        self.bind_ids['<Up>']    = root.bind('<Up>',    lambda e: snake.set_direction_U(), add='+')
        self.bind_ids['<Down>']  = root.bind('<Down>',  lambda e: snake.set_direction_D(), add='+')
        self.bind_ids['<Left>']  = root.bind('<Left>',  lambda e: snake.set_direction_L(), add='+')
        self.bind_ids['<Right>'] = root.bind('<Right>', lambda e: snake.set_direction_R(), add='+')
        self.bind_ids['<w>']     = root.bind('<w>',     lambda e: snake.set_direction_U(), add='+')
        self.bind_ids['<s>']     = root.bind('<s>',     lambda e: snake.set_direction_D(), add='+')
        self.bind_ids['<a>']     = root.bind('<a>',     lambda e: snake.set_direction_L(), add='+')
        self.bind_ids['<d>']     = root.bind('<d>',     lambda e: snake.set_direction_R(), add='+')

    def deactivate_wasd(self):
        if self.bind_ids is None:
            for key, bind_id in self.bind_ids.items():
                root.unbind(key, bind_id)
        
class GameData_Record:
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

    # using numpy to create a random number generator with independent seed
    # rng = np.random.default_rng(42)
    # rng.random(5)
    # rng.integers(1, 10)
    # rng.standard_normal(5)