import tkinter as tk
from tkinter import *

class circle:

    def __init__(self, xc, yc, r):
        self.xc = xc
        self.yc = yc
        self.r = r
 
    def draw_circle(self):
        test_canvas.create_oval(self.xc - self.r, self.yc + self.r, self.xc + self.r, self.yc - self.r)

root = Tk()

r = 100
canvas_width = 2000
canvas_height = 2000
test_canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
test_canvas.pack()

for k in range(0, int(canvas_width / (2 * r))):
    for j in range(0, int(canvas_width / (2 * r))):
        for i in range(1, int(canvas_width / r)):
            x_orig = canvas_width / 2 + r * (j - k)
            y_orig = canvas_height / 2 + r * (j - k)
            circle_orig = circle(x_orig, y_orig, r)
            circle_orig.draw_circle()
            circle_orig = circle(x_orig + r * i, y_orig, r)
            circle_orig.draw_circle()
            circle_orig = circle(x_orig - r * i, y_orig, r)
            circle_orig.draw_circle()
            circle_orig = circle(x_orig, y_orig + r * i, r)
            circle_orig.draw_circle()
            circle_orig = circle(x_orig, y_orig - r * i, r)
            circle_orig.draw_circle()

root.mainloop()

