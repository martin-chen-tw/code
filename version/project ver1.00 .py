# NAME: snack game
# AUTHOR: MING-HAO CHEN
# VERSION: 1.00
# DATE: 20250614

import numpy as np
import time
import random as rd 
import tkinter as tk
import re
import hashlib
import sys
from tkinter import messagebox as mb
from enum import Enum
TEST_MODE = True
class Snake:
    def __init__(self, gameconfig):
        if TEST_MODE: print("[INFO] Initializing snake class...")

        self.bodies = []
        self._direction = tk.IntVar()

        directions = [
            (1, 0, Dir.left), 
            (-1, 0, Dir.right), 
            (0, 1, Dir.up), 
            (0, -1, Dir.down)
        ]

        max_attempts = 100
        attempts = 0

        while attempts < max_attempts:
            attempts += 1
            if TEST_MODE: print(f"[INFO] Attmpt{attempts:03X}")
            # randomly place the snake's head
            head_x = int(gameconfig.snake_rng.integers(2, gameconfig._block_number[0] - 1))
            head_y = int(gameconfig.snake_rng.integers(2, gameconfig._block_number[1] - 1))
            self.bodies = [[head_x, head_y]]

            success = True
            while len(self.bodies) < gameconfig._snake_ini_len:
                last_body = self.bodies[-1]
                rd.shuffle(directions)
                
                #if the direction is placed
                is_placed = False

                for dx, dy, direction in directions:
                    new_x = last_body[0] + dx
                    new_y = last_body[1] + dy

                    if (1 <= new_x <= gameconfig._block_number[0] and
                        1 <= new_y <= gameconfig._block_number[1] and
                        [new_x, new_y] not in self.bodies):
                        
                        self.bodies.append([new_x, new_y])
                        if len(self.bodies) == 2:
                            self._direction.set(direction.value)
                        is_placed = True
                        break  # successful placement, break out of direction loop

                if not is_placed:
                    success = False
                    break  # couldn't find a spot, break to retry head placement

            if success:
                break  # successfully initialized snake
        
        if attempts >= max_attempts:
            if TEST_MODE: print("[ERROR] Failed to initialize snake within maximum attempts.")

        if TEST_MODE: print(f"[INFO] Snake successfully created: {self.bodies}")

    def create_new_head(self, dir, current_loc):
        directions = {
            Dir.left.value: (-1, 0),
            Dir.right.value: (1, 0),
            Dir.up.value: (0, -1),
            Dir.down.value: (0, 1)
        }

        x, y = current_loc[0][0], current_loc[0][1]

        dx, dy = directions[dir.get()]
        new_x = x + dx
        new_y = y + dy

        return new_x, new_y


    def set_direction_U(self):
        if gamectl._can_change_dir == False: return
        if self._direction.get() == Dir.up.value:
            if TEST_MODE: print(f"[INFO] direction {Dir.up.name} doesn't change!")
        elif self._direction.get() != Dir.down.value:
            if TEST_MODE: print(f"[INFO] change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.up.name}")
            gamectl._can_change_dir = False
            self._direction.set(Dir.up.value)
        else:
            if TEST_MODE: print(f"[BAD] cannot change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.up.name}")

    def set_direction_D(self):
        if gamectl._can_change_dir == False: return
        if self._direction.get() == Dir.down.value:
            if TEST_MODE: print(f"[INFO] direction {Dir.down.name} doesn't change!")
        elif self._direction.get() != Dir.up.value:
            if TEST_MODE: print(f"[INFO] change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.down.name}")
            gamectl._can_change_dir = False
            self._direction.set(Dir.down.value)
        else:
            if TEST_MODE: print(f"[BAD] cannot change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.down.name}")

    def set_direction_L(self):
        if gamectl._can_change_dir == False: return
        if self._direction.get() == Dir.left.value:
            if TEST_MODE: print(f"[INFO] direction {Dir.left.name} doesn't change!")
        elif self._direction.get() != Dir.right.value:
            if TEST_MODE: print(f"[INFO] change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.left.name}")
            gamectl._can_change_dir = False
            self._direction.set(Dir.left.value)
        else:
            if TEST_MODE: print(f"[BAD] cannot change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.left.name}")

    def set_direction_R(self):
        if gamectl._can_change_dir == False: return
        if self._direction.get() == Dir.right.value:
            if TEST_MODE: print(f"[INFO] direction {Dir.right.name} doesn't change!")
        elif self._direction.get() != Dir.left.value:
            if TEST_MODE: print(f"[INFO] change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.right.name}")
            gamectl._can_change_dir = False
            self._direction.set(Dir.right.value)
        else:
            if TEST_MODE: print(f"[BAD] cannot change direction from {self.change_num_to_emun(self._direction.get())} to {Dir.right.name}")

    def change_num_to_emun (self, num):
        match num:
            case 1: return Dir.up.name
            case 2: return Dir.down.name
            case 3: return Dir.left.name
            case 4: return Dir.right.name
    
class Apple:
    global gameconfig
    def __init__(self,snake):
        self._position = []
        while True:
            apple_x = int(gameconfig.apple_rng.integers(low=1, high=gameconfig._block_number[0]))
            apple_y = int(gameconfig.apple_rng.integers(low=1, high=gameconfig._block_number[1]))
            if [apple_x, apple_y] not in snake.bodies:
                self._position = [apple_x, apple_y]
                if TEST_MODE:print(f'[GOOD] apple is generated in [{self._position}]')
                break
    def change_position(self, snake):
        x,y = None,None
        while True:
            apple_x = int(gameconfig.apple_rng.integers(low=1, high=gameconfig._block_number[0]))
            apple_y = int(gameconfig.apple_rng.integers(low=1, high=gameconfig._block_number[1]))
            if [apple_x, apple_y] not in snake.bodies:
                self._position = [apple_x, apple_y]
                if TEST_MODE:print(f'[GOOD] apple is generated in [{self._position}]')
                break
            

    def draw_apple(self, loc):
        x, y = loc[0]*30, loc[1]*30 + 100

        # Main apple body (rounder)
        canvam.canvas.create_oval(x + 4, y + 9, x + 26, y + 31, fill='#d62828', outline='')

        # White highlight (smaller and softer)
        canvam.canvas.create_oval(x + 8, y + 13, x + 11, y + 16, fill='#ffffff', outline='')

        # Bottom shadow (less pronounced)
        canvam.canvas.create_oval(x + 9, y + 22, x + 21, y + 29, fill='#a4161a', outline='')

        # Stem (thinner)
        canvam.canvas.create_rectangle(x + 14, y + 4, x + 16, y + 10, fill='#6c584c', outline='')

        # Leaf (smaller and rounder)
        canvam.canvas.create_oval(x + 17, y + 2, x + 25, y + 9, fill='#52b788', outline='')

        # Top shine (gentler)
        canvam.canvas.create_oval(x + 10, y + 6, x + 19, y + 14, fill='#c1121f', outline='')

        # Secondary highlight (tiny)
        canvam.canvas.create_oval(x + 6, y + 11, x + 8, y + 13, fill='#f8edeb', outline='')

        # Leaf depth (smaller)
        canvam.canvas.create_oval(x + 18, y + 3, x + 23, y + 7, fill='#40916c', outline='')

        # Stem shadow
        canvam.canvas.create_line(x + 15, y + 4, x + 15, y + 10, fill='#3d3d3d', width=1)

        # Bottom sparkle (smaller)
        canvam.canvas.create_oval(x + 17, y + 26, x + 19, y + 28, fill='#ffffff', outline='')


class CanvaManager:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.main_page_widgets = ["start_game_button","light_button","dark_button","large_size_button","medium_size_button","small_size_button",
    "fast_speed_button","medium_speed_button","slow_speed_button","default_ini_body_len_button","customized_ini_body_len_button","default_body_color_button",
    "customized_body_color_button","random_mod_button","fixed_mod_button","discoloration_button","customized_ini_body_len_entry","customized_body_color_entry",
    "random_seed_entry"]
       
        for name in self.main_page_widgets:
            setattr(self, name, None)

    def clear_canvas_and_widget(self):
        if self.canvas is not None:
            # if TEST_MODE: print("[INFO]Clearing canvas...")
            try:
                self.canvas.delete("all")
                for widget in self.canvas.winfo_children():
                    widget.destroy()
                self.canvas.pack_forget()
                self.canvas.destroy()
            except Exception as e:
                if TEST_MODE: print(f"[ERROR]Failed to clear canvas: {e}")
            finally:
                # if TEST_MODE: print("[INFO]Clearing canvas done")
                self.canvas = None
        for name in self.main_page_widgets:
            widget = getattr(self, name, None)
            try:
                if widget:
                    widget.destroy()
                    setattr(self, name, None)  
                    if TEST_MODE: print(f"[INFO]Destroyed canvas widget: {name}")
            except Exception as e:
                if TEST_MODE: print(f"[ERROR]Failed to clear canvas: {e}")
        
    def main_page(self):
        #--- Initialization
        if TEST_MODE: print(f"[INFO]Initializing main page...")
        global root, gameconfig, snake
        gameconfig.deactivate_wasd()
        root.geometry('800x600')
        self.clear_canvas_and_widget()
        if TEST_MODE: print(f"[INFO]Creating main page...")
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
            rn = int(rd.randint(0, 65535))
            self.random_seed_entry.insert(0, rn)
            self.random_seed_entry.delete(len(rn)-1, 'end')
            self.random_seed_entry.config(state='disabled')
            self.random_seed_entry.set(rn)

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
        self.random_seed_entry.insert(0,'0')
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
        if TEST_MODE: print(f"[INFO]Creating main page done")

    def gaming_page(self):
        match gameconfig._screen_size: # 300x400 600x700 1500x1300
            case '300x400':
                title_size = 25
                text_size = 16
                dx = 10
            case '600x700':
                title_size = 32
                text_size = 23
                dx = 30
            case '1200x1000':
                title_size = 35
                text_size = 26
                dx = 45   
        x,y = 0, 1
        fx,fy =gameconfig._block_number[x]*30,gameconfig._block_number[y]*30+100
        dy = 100 # dp = Displacement in y-axis
        root.geometry(gameconfig._screen_size)
        if TEST_MODE: print(f"[INFO]Setting window size to {gameconfig._screen_size}") 
        self.clear_canvas_and_widget()
        self.canvas = tk.Canvas(self.root, width=fx, height=fy, bg=f'{str(gameconfig._canvas_color)}')
        self.canvas.create_text( fx/2, 23,text='Snake', anchor='center', fill=gameconfig._text_color, font=('Times New Roman', title_size, 'bold'))
        self.canvas.create_text( fx-dx, 83,text=f'Apple: {gamectl.last_record._apple_count}', anchor='e', fill=gameconfig._text_color, font=('Times New Roman', text_size, 'bold'))
        self.canvas.create_text( fx/2, 83,text=f'Score: {gamectl.last_record._score}', anchor='center', fill=gameconfig._text_color, font=('Times New Roman', text_size, 'bold'))
        self.canvas.create_text( dx, 83,text=f'Lengh: {gamectl.last_record._max_len}', anchor='w', fill=gameconfig._text_color, font=('Times New Roman', text_size, 'bold'))
        self.canvas.create_line( 0,100,fx,100, fill=gameconfig._text_color, width=2)
        self.canvas.pack()

    def rank_score_and_info_page(self):
        root.geometry('800x600') 
        self.clear_canvas_and_widget()
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_color):
        return '#{:02X}{:02X}{:02X}'.format(*rgb_color)

    def gradient_color(self, start_color, end_color, factor):
        return tuple(int(s + (e - s) * factor) for s, e in zip(start_color, end_color))
    
    def draw_snake_d(self,canvas, snake_coords, snake_color, bg_color, unit_size=30):

        snake_rgb = self.hex_to_rgb(snake_color.get())
        bg_rgb = self.hex_to_rgb(bg_color)

        total_segments = len(snake_coords)

        for i in range(total_segments):
            factor = i / (total_segments )
            segment_color = self.rgb_to_hex(self.gradient_color(snake_rgb, bg_rgb, factor))

            x, y = snake_coords[i]
            x1, y1 = x * unit_size, y * unit_size +100
            x2, y2 = x1 + unit_size, y1 + unit_size

            canvas.create_rectangle(x1, y1, x2, y2, fill=segment_color, outline=segment_color)
        

class GameCtl:

    def ready_to_start_game(self):
        if TEST_MODE:print ('[INFO] prepare for starting game...')
        
        gameconfig.update_tkinput_var()
        gameconfig.update_complex_var()
        gameconfig.activate_wasd()
        gameconfig.copy_gameconfig(gameconfig_m)
        #self._can_change_dir = False
        try:
            self.last_record = Score_Record()
            self.snake = Snake(gameconfig)
            self.apple = Apple(self.snake)
        except tk.TclError as e:
            if TEST_MODE:print(f"[ERROR] unable to create calss snake or score_record: {e}")
        self.speed = gameconfig._speed
        if TEST_MODE:print ('[INFO] ready for starting game')
        self._first = True
        self.game_loop()
        
    def game_loop(self):
        # if TEST_MODE:print ('[INFO]game loop start')
        global gameconfig
        canvam.gaming_page()
        canvam.draw_snake_d(canvam.canvas, self.snake.bodies, gameconfig.snake_color, gameconfig._canvas_color, unit_size=30)
        self.apple.draw_apple(self.apple._position)
        #if self._first:
        #    root.after(300, self.game_loop)
        #    self._first = False
        self._can_change_dir = True
        new_x,new_y = self.snake.create_new_head(self.snake._direction, self.snake.bodies)
        apple_loc = self.apple._position
        if [new_x,new_y] ==  apple_loc:
            self.last_record.add_apple()
            self.last_record.add_len(1)
            self.last_record.add_score(100)
            self.snake.bodies.insert(0, [new_x, new_y])
            self.apple.change_position(self.snake)
            if TEST_MODE:print ('[INFO] eat apple!')
        elif (0 <= new_x < int(gameconfig._block_number[0])) is not True:
            if TEST_MODE:print ('[INFO] invaild x-axis value, game over!')
            self.game_over()
            return
        elif (0 <= new_y < int(gameconfig._block_number[1])) is not True:
            if TEST_MODE:print ('[INFO] invaild y-axis value, game over!')
            self.game_over()
            return
        elif [new_x,new_y] in self.snake.bodies:
            if TEST_MODE:print ('[INFO] hit body, game over!')
            self.game_over()
            return
        else:
            if TEST_MODE:print ('[INFO] normal move!')
            self.snake.bodies.insert(0, [new_x, new_y])
            self.snake.bodies.pop()
             #tmp
        root.after(self.speed, self.game_loop)
    def game_over(self):
        # root.free()
        # sys.exit(0)
        pass


class Gameconfig:
    def __init__(self):
        # Screen size and color
        self.size = tk.StringVar(value=Size.small.value)
        self._size = Size.small.value
        self._block_number = [10, 10]
            # 10x10 20x20 50x30
        self._screen_size = '300x400'
            # 300x400 600x700 1500x1300 (x*30, y*30+100)
        self.is_dark_mod =      tk.BooleanVar(value=False)
        self._is_dark_mod = False
        self._screen_color = '#FAFAFA'
        self._text_color = '#272727'
        # Snake len and color
        self.is_customized_body_len = tk.BooleanVar(value=False)
        self._is_customized_body_len = False
        self.snake_ini_len =    tk.IntVar(value=3)
        self._snake_ini_len = 3
        self.is_customized_color = tk.BooleanVar(value=False)
        self._is_customized_color = False
        self.snake_color =      tk.StringVar(value="#5FF26A")
        self._snake_color = "#5FF26A"
        self.is_discoloration = tk.BooleanVar(value=True)
        self._is_discoloration = True
        # Game control
        self.speed =            tk.IntVar(value=Speed.slow.value)
        self._speed = Speed.slow.value
        self.is_random_mod =       tk.BooleanVar(value=True)
        self._is_random_mod = True
        self.random_seed =      tk.IntVar(value=0)
        self._random_seed = 0
        #Others
        self.bind_ids = {}
        self._is_activated_bind = False

    
    def copy_gameconfig(myself, other):
        # Screen size and color
        other._size = myself._size
        other._block_number = myself._block_number 

    def update_tkinput_var (self):
        attrs = [
        ('_size', self.size),
        ('_is_dark_mod', self.is_dark_mod),
        ('_is_customized_body_len', self.is_customized_body_len),
        ('_snake_ini_len', self.snake_ini_len),
        ('_is_customized_color', self.is_customized_color),
        ('_snake_color', self.snake_color),
        ('_is_discoloration', self.is_discoloration),
        ('_speed', self.speed),
        ('_is_random_mod', self.is_random_mod),
        ('_random_seed', self.random_seed),
    ]
        if TEST_MODE:print(f'[INFO]Update tkinter input var to static var...')
        for attr_name, attr_var in attrs:
            
            try:
                setattr(self, attr_name, attr_var.get())
                if TEST_MODE:print(f'[INFO]update gameconfig.{attr_name} = [{attr_var.get()}]')
            except tk.TclError as e:
                print(f"[ERROR]error occurs when try to get var of {attr_name} :{e}")
        if TEST_MODE:print(f'[INFO]Update tkinter input var done')

    def update_complex_var(self):
        if TEST_MODE:print(f'[INFO]Update complex type of vars...')

        def sha256_decimal(input_value):
            input_str = str(input_value) 
            # calculate SHA-256 hash value
            sha256_hash = hashlib.sha256(input_str.encode()).hexdigest()
            
            # change the hash value in hexadecimal to decimal format
            decimal_hash = int(sha256_hash, 16)
            
            return decimal_hash
        
        match self._size:
            case Size.small.value:
                self._block_number = [10, 10]
                self._screen_size = '300x400'
            case Size.medium.value:
                self._block_number = [20, 20]
                self._screen_size = '600x700'
            case Size.large.value:
                self._block_number = [40, 30]
                self._screen_size = '1200x1000'
        if TEST_MODE:print(f'[INFO]update _block_number = {self._block_number}')
        if TEST_MODE:print(f'[INFO]update _screen_size = [{self._screen_size}]')

        if self._is_dark_mod:
            self._canvas_color = '#0D1117'
            self._text_color = '#E0E0E0'
        else:
            self._canvas_color = '#FAFAFA'
            self._text_color = '#272727'
        if TEST_MODE:print(f'[INFO]update _canvas_color = [{self._canvas_color}]')
        if TEST_MODE:print(f'[INFO]update _text_color = [{self._text_color}]')
        if self._is_customized_body_len is not True:
            self._snake_ini_len = 3
        if TEST_MODE:print(f'[INFO]update _snake_ini_len = [{self._snake_ini_len}]')
        if self._is_customized_color is not True:
            self._snake_color="#5FF26A"
        if TEST_MODE:print(f'[INFO]update _snake_color = [{self._snake_color}]')
        if self._is_random_mod:
            main_rng = np.random.default_rng(sha256_decimal(rd.randint(0, 65535)))
        else:
            self.main_rng = np.random.default_rng(sha256_decimal(self._random_seed))
        self.snake_rng = np.random.default_rng(sha256_decimal(main_rng.integers(low=0, high=65535)))
        self.apple_rng = np.random.default_rng(sha256_decimal(main_rng.integers(low=0, high=65535)))
        if TEST_MODE:print(f'[INFO]create RNG of self.main_rng')
        if TEST_MODE:print(f'[INFO]create RNG of self.snake_rng')
        if TEST_MODE:print(f'[INFO]create RNG of self.apple_rng')
        if TEST_MODE:print(f'[INFO]Update complex type of vars done')
        

    def activate_wasd(self):
        global root ,gamectl
        self.bind_ids['<Up>']    = root.bind('<Up>',    lambda e: gamectl.snake.set_direction_U(), add='+')
        self.bind_ids['<Down>']  = root.bind('<Down>',  lambda e: gamectl.snake.set_direction_D(), add='+')
        self.bind_ids['<Left>']  = root.bind('<Left>',  lambda e: gamectl.snake.set_direction_L(), add='+')
        self.bind_ids['<Right>'] = root.bind('<Right>', lambda e: gamectl.snake.set_direction_R(), add='+')
        self.bind_ids['<w>']     = root.bind('<w>',     lambda e: gamectl.snake.set_direction_U(), add='+')
        self.bind_ids['<s>']     = root.bind('<s>',     lambda e: gamectl.snake.set_direction_D(), add='+')
        self.bind_ids['<a>']     = root.bind('<a>',     lambda e: gamectl.snake.set_direction_L(), add='+')
        self.bind_ids['<d>']     = root.bind('<d>',     lambda e: gamectl.snake.set_direction_R(), add='+')
        if self._is_activated_bind is False:
            self._is_activated_bind = True
            if TEST_MODE: print("[INFO]WASD keys activated")

    def deactivate_wasd(self):
        if self.bind_ids is None:
            for key, bind_id in self.bind_ids.items():
                root.unbind(key, bind_id)
                if TEST_MODE: print(f"key {key} unbind {bind_id}")
        if self._is_activated_bind is True:
            self._is_activated_bind = False
            if TEST_MODE: print("[INFO]WASD keys deactivated")
        
class Score_Record:
    def __init__(self):
        self._score = 0
        self._apple_count = 0
        self._max_len = gameconfig.snake_ini_len.get()
        if TEST_MODE: print(f"[INFO]Score_Record initialization done")
    def add_score(self, step):
        self._score += step
        pass
        if TEST_MODE: print(f"[INFO]Score added: {step}, Total score: {self._score}")
    def add_apple(self):
        self._apple_count += 1
        if TEST_MODE: print(f"[INFO]Apple count increased: {self._apple_count}")
    def add_len(self, len):
        self._max_len += len
        if TEST_MODE: print(f"[INFO]Snake length increased: {self._max_len}")
    def copy_score_record(myself, other):
        myself.add_apple(other._apple_count)
        myself.add_score(other._score) 
        myself.add_len(other._max_len)
        if TEST_MODE: print(f"[INFO]Score_Record copied from myself to other")


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
    fast = 120
    medium = 150
    slow = 200
    

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
    pass

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
    canvam.main_page()  
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