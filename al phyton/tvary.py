import tkinter as tk

def draw_circles():
    root = tk.Tk()
    root.title("Soustředné kružnice")
    
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    center_x, center_y = 200, 200
    radii = [25, 50, 100, 150, 190]  

    for r in radii:
        canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, outline="black")

    root.mainloop()

draw_circles()