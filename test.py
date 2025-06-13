import tkinter as tk

def draw_snake_head(canvas, x, y, direction='up', size=30):
    def rotate_coords(coords, angle, cx, cy):
        from math import radians, sin, cos
        rad = radians(angle)
        rotated = []
        for i in range(0, len(coords), 2):
            px, py = coords[i], coords[i+1]
            qx = cx + cos(rad) * (px - cx) - sin(rad) * (py - cy)
            qy = cy + sin(rad) * (px - cx) + cos(rad) * (py - cy)
            rotated.extend([qx, qy])
        return rotated

    angle_map = {'up': 0, 'right': 90, 'down': 180, 'left': 270}
    angle = angle_map.get(direction, 0)
    cx, cy = x + size / 2, y + size / 2

    # Head shape
    head_coords = [x+size*0.5, y, x+size*0.8, y+size*0.2, x+size*0.9, y+size*0.6,
                   x+size*0.5, y+size, x+size*0.1, y+size*0.6, x+size*0.2, y+size*0.2]
    rotated_head = rotate_coords(head_coords, angle, cx, cy)
    canvas.create_polygon(rotated_head, fill='#5FF26A', outline='black')

    # Eyes
    eye_offset = size * 0.15
    left_eye = [cx - eye_offset, cy - eye_offset]
    right_eye = [cx + eye_offset, cy - eye_offset]

    left_eye_rotated = rotate_coords([left_eye[0], left_eye[1]], angle, cx, cy)
    right_eye_rotated = rotate_coords([right_eye[0], right_eye[1]], angle, cx, cy)

    canvas.create_oval(left_eye_rotated[0]-size*0.05, left_eye_rotated[1]-size*0.08,
                       left_eye_rotated[0]+size*0.05, left_eye_rotated[1]+size*0.08,
                       fill='black')
    canvas.create_oval(right_eye_rotated[0]-size*0.05, right_eye_rotated[1]-size*0.08,
                       right_eye_rotated[0]+size*0.05, right_eye_rotated[1]+size*0.08,
                       fill='black')

    # Nostril
    nostril_offset = size * 0.07
    left_nostril = [cx - nostril_offset, cy + size*0.1]
    right_nostril = [cx + nostril_offset, cy + size*0.1]

    left_nostril_rotated = rotate_coords(left_nostril, angle, cx, cy)
    right_nostril_rotated = rotate_coords(right_nostril, angle, cx, cy)

    canvas.create_oval(left_nostril_rotated[0]-2, left_nostril_rotated[1]-2,
                       left_nostril_rotated[0]+2, left_nostril_rotated[1]+2,
                       fill='black')
    canvas.create_oval(right_nostril_rotated[0]-2, right_nostril_rotated[1]-2,
                       right_nostril_rotated[0]+2, right_nostril_rotated[1]+2,
                       fill='black')

    # Scales
    scale_coords = [[cx, cy + size*0.3], [cx - size*0.1, cy + size*0.35], [cx + size*0.1, cy + size*0.35]]
    for sx, sy in scale_coords:
        scale_rotated = rotate_coords([sx, sy], angle, cx, cy)
        canvas.create_arc(scale_rotated[0]-5, scale_rotated[1]-3,
                          scale_rotated[0]+5, scale_rotated[1]+3,
                          start=0, extent=180, style='arc', outline='black')

# Test
root = tk.Tk()
root.title("Detailed Snake Head")
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

draw_snake_head(canvas, 85, 85, direction='up', size=30)

root.mainloop()