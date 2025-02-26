import tkinter as tk

root = tk.Tk()
root.title("kreslení kruhu")

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

canvas.create_oval(100, 100, 800, 800)

root.mainloop()