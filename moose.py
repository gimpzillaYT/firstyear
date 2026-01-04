import turtle 
import tkinter as tk

def main():
    t = turtle.Turtle()
    t.speed(0)
    moose_coords = [
    (0, 0), (20, 5), (40, 20), (45, 40),      # Nose and forehead
    (60, 60), (90, 80), (80, 50), (100, 70),  # Antler point 1
    (90, 40), (110, 50), (100, 30), (80, 25), # Antler point 2
    (50, 20), (40, 0), (70, -10), (100, -10), # Neck and back
    (110, -40), (105, -80), (95, -80),        # Back leg 1
    (90, -40), (70, -40), (65, -80), (55, -80),# Back leg 2
    (50, -30), (20, -30), (15, -80), (5, -80), # Front leg 1
    (0, -30), (-10, -80), (-20, -80),         # Front leg 2
    (-15, -20), (-30, -10), (-20, 0), (0, 0),   #chest and chin
    (-90, 40), (-110, 50), (-100, 30), (-80, 25),
    (-60, 60), (-90, 80), (-80, 50), (-100, 70)]  # secon antler guessed by warren

    t.up()
    t.goto(moose_coords[0])
    t.down()

    for each_xy in moose_coords:
        t.goto(each_xy)
    
    t.up()
    t.home()
    tk.mainloop()

main() 