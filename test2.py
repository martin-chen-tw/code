import tkinter as tk

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

def gradient_color(start_color, end_color, factor):
    return tuple(int(s + (e - s) * factor) for s, e in zip(start_color, end_color))

def draw_gradient_snake(canvas, snake_coords, snake_color, bg_color, unit_size=30):
    canvas.delete("all")

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

# example test
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Gradient Snake")

    canvas = tk.Canvas(root, width=400, height=400, bg='#000000')
    canvas.pack()

    snake_coords = [
        [1, 1], [2, 2], [3, 3], [4, 4],
        [5, 5], [6, 6], [7, 7]
    ]

    draw_gradient_snake(canvas, snake_coords, snake_color='#00FF00', bg_color='#000000', unit_size=30)

    root.mainloop()
