#  creates a canvas with blue cells and a movable pink eraser that erases cells it touches as the mouse moves.
import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    mouse_x, mouse_y = event.x, event.y
    canvas.coords(eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
    for cell in cells:
        if canvas.bbox(cell):
            x1, y1, x2, y2 = canvas.bbox(cell)
            if intersects(mouse_x, mouse_y, x1, y1, x2, y2):
                canvas.itemconfig(cell, fill="white")

def intersects(mx, my, x1, y1, x2, y2):
    return not (mx + ERASER_SIZE < x1 or mx > x2 or my + ERASER_SIZE < y1 or my > y2)

root = tk.Tk()
root.title("Canvas Eraser")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

cells = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue')
        cells.append(cell)

eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

canvas.bind("<Motion>", erase)

root.mainloop()