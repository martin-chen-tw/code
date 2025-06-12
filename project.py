import numpy as np
import random as rd # tmp, use numpy instead
import tkinter as tk
import re
import hashlib
from tkinter import messagebox as mb
from enum import Enum
TEST_MODE = True
class Snake:
    bodies = []
    def __init__(self, gameconfig):
        if TEST_MODE: print(f"Creating snake name {self}...")
        self._direction = tk.IntVar()
        is_first_time = True
        len = gameconfig.snake_ini_len
        self.bodies.append([gameconfig.snack_rng.randint(1+1, gameconfig.block_number[0]-1), gameconfig.snack_rng.randint(1+1, gameconfig.block_number[1]-1)])
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
        if TEST_MODE: print(f"Snake {self} created successfully with bodies: {self.bodies} ")

    def move_ (self):
        pass
    def set_direction_U(self):
        self._direction.set(Dir.up.value) if self._direction.get() != Dir.down.value else None
    def set_direction_D(self):
        self._direction.set(Dir.down.value) if self._direction.get() != Dir.up.value else None
    def set_direction_L(self):
        self._direction.set(Dir.left.value) if self._direction.get() != Dir.right.value else None
    def set_direction_R(self):
        self._direction.set(Dir.right.value) if self._direction.get() != Dir.left.value else None
    def change_color(self):
        pass

class Apple:
    global snake, gameconfig
    _position = []
    def __init__(self ):
        is_first_time = True
        while self._position in snake.bodies and is_first_time:
            is_first_time = False
            self._position = [gameconfig.apple_rng.integers(low=1, high=gameconfig.block_number[0]), gameconfig.apple_rng.integers(low=1,high= gameconfig.block_number[1])]
    def change_position(self):
        pass
    def draw_apple(x, y):
        # Main apple body (red)
        gameconfig.canvas.create_oval(x + 5, y + 10, x + 25, y + 30, fill='#d62828', outline='')
        # White highlight
        gameconfig.gameconfig.canvas.create_oval(x + 8, y + 14, x + 12, y + 18, fill='#ffffff', outline='')
        # Bottom shadow (dark red)
        gameconfig.canvas.create_oval(x + 10, y + 22, x + 20, y + 28, fill='#a4161a', outline='')
        # Stem (brown rectangle)
        gameconfig.canvas.create_rectangle(x + 14, y + 2, x + 16, y + 10, fill='#6c584c', outline='')
        # Leaf (green oval)
        gameconfig.canvas.create_oval(x + 16, y + 0, x + 26, y + 10, fill='#52b788', outline='')
        # Top shine (brighter red)
        gameconfig.canvas.create_oval(x + 10, y + 5, x + 20, y + 15, fill='#c1121f', outline='')
        # Secondary highlight
        gameconfig.canvas.create_oval(x + 6, y + 12, x + 9, y + 15, fill='#f8edeb', outline='')
        # Leaf depth (darker green overlay)
        gameconfig.canvas.create_oval(x + 18, y + 2, x + 24, y + 8, fill='#40916c', outline='')
        # Stem shadow (dark line)
        gameconfig.canvas.create_line(x + 15, y + 2, x + 15, y + 10, fill='#3d3d3d', width=1)
        # Bottom sparkle
        gameconfig.canvas.create_oval(x + 18, y + 26, x + 20, y + 28, fill='#ffffff', outline='')


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
                                                ,variable=gameconfig.size, value=Size.large.value)
        self.medium_size_button = tk.Radiobutton(self.root, text='medium size', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                 ,variable=gameconfig.size, value=Size.medium.value)
        self.small_size_button = tk.Radiobutton(self.root, text='small size', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.size, value=Size.small.value)
        self.large_size_button.place(x=600, y=235, anchor='center')
        self.medium_size_button.place(x=400, y=235, anchor='center')
        self.small_size_button.place(x=200, y=235, anchor='center')
        #--- Game Speed

        self.canvas.create_text( 400, 270, text='Game Speed', anchor='center', fill='#202020', font=('Times New Roman', 19, 'bold'))
        self.fast_speed_button = tk.Radiobutton(self.root, text='fast', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold')
                                                ,variable=gameconfig.speed, value=Speed.fast.value)
        self.medium_speed_button = tk.Radiobutton(self.root, text='medium', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold') ,variable=gameconfig.speed, value=Speed.medium.value)
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
            self.customized_ini_body_len_entry.config(state='normal')
            
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
        self.customized_ini_body_len_entry = tk.Entry(self.root, width=3, font=('Times New Roman', 12, 'bold'), fg='#363636', 
                                                        bg='#f0f0f0', state='normal',validate='focusout', validatecommand=len_vcmd,invalidcommand=len_ivcmd)
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

        self.default_body_color_button = tk.Radiobutton(self.root, text='default body color', anchor='center', fg='#363636', font=('Times New Roman', 15,'bold'),variable=gameconfig.is_customized_color,value=False,command=lambda: select_default_color())
        self.customized_body_color_button = tk.Radiobutton(self.root, text='customized body color', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold'),variable=gameconfig.is_customized_color, value=True, command=lambda: select_customized_color())
        self.customized_body_color_entry = tk.Entry(self.root, width=10, font=('Times New Roman', 12, 'bold'), fg='#363636', bg='#f0f0f0', validate='focusout',validatecommand=col_vcmd, invalidcommand=col_ivcmd)
        self.customized_body_color_entry.insert(0, '#5FF26A')
        self.customized_body_color_entry.config(state='disabled')
        self.discoloration_button = tk.Checkbutton(self.root, text='discoloration', anchor='center', fg='#363636', font=('Times New Roman', 15, 'bold') ,variable=gameconfig.is_discoloration, state='normal', onvalue=True, offvalue=False)
        
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
        self.start_game_button = tk.Button(self.root, text='Start Game', anchor='center', fg='#000000', font=('Times New Roman', 19, 'bold'),command=lambda: (check_customized()))
        self.start_game_button.place(x=400, y=545, anchor='center')
        
        #--- 
        def check_customized():
            is_sure = mb.askyesno("Confirm Game Start", "Custom parameters may cause unexpected bugs or crashes in the game.\nDo you wish to proceed?") if gameconfig.is_customized_body_len.get() is True or gameconfig.is_customized_color.get() is True else True
            if is_sure: gamectl.ready_to_start_game()
        #--- 
        self.canvas.pack()

    def gaming_page(self):
        x,y = 0, 1
        dp = 100 # dp = Displacement in y-axis
        root.geometry(gameconfig.screen_size)
        if TEST_MODE: print(f"Setting window size to {gameconfig.screen_size}") 
        self.clear_canvas_and_widget()
        self.canvas = tk.Canvas(self.root, width=gameconfig._block_number[x]*30, height=gameconfig._block_number[y]*30 + dp, bg=gameconfig.canvas_color)

    def rank_score_and_info_page(self):
        root.geometry('800x600') 
        self.clear_canvas_and_widget()
    
    def draw_snake_d(canvas, snake_coords, snake_color, bg_color, unit_size=30):
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        def rgb_to_hex(rgb_color):
            return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

        def gradient_color(start_color, end_color, factor):
            return tuple(int(s + (e - s) * factor) for s, e in zip(start_color, end_color))

        snake_rgb = hex_to_rgb(snake_color)
        bg_rgb = hex_to_rgb(bg_color)

        total_segments = len(snake_coords)

        for i in range(total_segments):
            factor = i / (total_segments - 1)
            segment_color = rgb_to_hex(gradient_color(snake_rgb, bg_rgb, factor))

            x, y = snake_coords[i]
            x1, y1 = x * unit_size, y * unit_size
            x2, y2 = x1 + unit_size, y1 + unit_size

            canvas.create_rectangle(x1, y1, x2, y2, fill=segment_color, outline=segment_color)
        

class GameCtl:

    def ready_to_start_game(self):
        gameconfig.update_complex_var()
        gameconfig.activate_wasd()
        gameconfig.copy_gameconfig(gameconfig_m)
        self.gaming()
        last_record = Score_Record()
        self.speed = gameconfig.speed.get()
    def gaming(self):
        global snake, apple, gameconfig, gamectl
        canvam.gaming_page()


        root.after(gameconfig.speed, self.game_loop)
    def game_over(self):
        pass


class Gameconfig:
    def __init__(self):
        # Screen size and color
        self.size = tk.StringVar(value=Size.small.value)
        self._block_number = [10, 10]
            # 10x10 20x20 50x30
        self.screen_size = '300x400'
            # 300x400 600x700 1500x1300 (x*30, y*30+100)
        self.is_dark_mod =      tk.BooleanVar(value=False)
        self._screen_color = '#FAFAFA'
        self._text_color = '#272727'
        # Snake len and color
        self.is_customized_body_len = tk.BooleanVar(value=False)
        self.snake_ini_len =    tk.IntVar(value=3)
        self.is_customized_color = tk.BooleanVar(value=False)
        self.snake_color =      tk.StringVar(value="#5FF26A")
        self.is_discoloration = tk.BooleanVar(value=True)
        # Game control
        self.speed =            tk.IntVar(value=Speed.slow.value)
        self.is_random_mod =       tk.BooleanVar(value=True)
        self.random_seed =      tk.IntVar()
        #Others
        self.bind_ids = {}
        self._is_activated_bind = False
    
    def copy_gameconfig(myself, other):
        # Screen size and color
        myself.size.set(other.size.get())
        myself._block_number = other._block_number[:]
        myself.screen_size = other.screen_size[:]
        myself.is_dark_mod.set(other.is_dark_mod.get())
        myself._screen_color = other._screen_color
        myself._text_color = other._text_color
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

    def update_complex_var(self):
        def sha256_decimal(input_value):
            input_str = str(input_value) 
            # calculate SHA-256 hash value
            sha256_hash = hashlib.sha256(input_str.encode()).hexdigest()
            
            # change the hash value in hexadecimal to decimal format
            decimal_hash = int(sha256_hash, 16)
            
            return decimal_hash
        new_size = self.size.get()
        match new_size:
            case Size.small:
                self.block_number = [10, 10]
                self.screen_size = '300x400'
            case Size.medium:
                self.block_number = [20, 20]
                self.screen_size = '600x700'
            case Size.large:
                self.block_number = [50, 30]
                self.screen_size = '1500x1300'
        if self.is_dark_mod.get():
            self.canvas_color = '#0D1117'
            self.text_color = '#E0E0E0'
        else:
            self.canvas_color = '#FAFAFA'
            self.text_color = '#272727'
        if self.is_customized_body_len.get() is not True:
            self.snake_ini_len.set(3)
        if self.is_customized_color.get() is not True:
            self.snake_color.set("#5FF26A")
        if self.is_random_mod.get() is not True:
            main_rng = np.random.default_rng(rd.randint(0, 65535))
        else:
            main_rng = np.random.default_rng(self.random_seed.get())
        self.snake_rng = np.random.default_rng(sha256_decimal(main_rng.integers(low=0, high=65535)))
        self.apple_rng = np.random.default_rng(sha256_decimal(main_rng.integers(low=0, high=65535)))
        

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
        if self._is_activated_bind is False:
            self._is_activated_bind = True
            if TEST_MODE: print("WASD keys activated")

    def deactivate_wasd(self):
        if self.bind_ids is None:
            for key, bind_id in self.bind_ids.items():
                root.unbind(key, bind_id)
        if self._is_activated_bind is True:
            self._is_activated_bind = False
            if TEST_MODE: print("WASD keys deactivated")
        
class Score_Record:
    def __init__(self):
        self._score = 0
        self._apple_count = 0
        self._max_len = gameconfig.snake_ini_len.get()
        if TEST_MODE: print(f"Score_Record initialization done")
    def add_score(self, score):
        self._score += score
        if TEST_MODE: print(f"Score added: {score}, Total score: {self._score}")
    def add_apple(self):
        self._apple_count += 1
        if TEST_MODE: print(f"Apple count increased: {self._apple_count}")
    def add_len(self, len):
        self._max_len += len
        if TEST_MODE: print(f"Snake length increased: {self._max_len}")
    def copy_score_record(myself, other):
        myself.add_apple(other._apple_count)
        myself.add_score(other._score) 
        myself.add_len(other._max_len)
        if TEST_MODE: print(f"Score_Record copied from myself to other")


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
    fast = 30
    medium = 60
    slow = 90
    

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
    gameconfig_m = Gameconfig()
    gamectl = GameCtl()
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