try:
    # for Python2
    from Tkinter import *  
except ImportError:
    # for Python3
    from tkinter import * 
import random
tkGUI = Tk()
tkGUI.title("Bounce It")
tkGUI.wm_attributes("-topmost", 1)
tkGUI.resizable(0, 0)
canvasObject = Canvas(tkGUI, bg ="black", width=800, height=600, bd=0, highlightthickness=5)
canvasObject.pack()
tkGUI.update()
class pongBall:
    def __init__(self, canvas, color):
        array = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        random.shuffle(array)
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 35, 35, fill = color)
        self.canvas.move(self.id, 250, 200)
        self.x = array[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            location = self.canvas.coords(self.id)
            if location[0] <= 0:
                self.x = 4
            if location[1] <= 0:
                self.y = 4
            if location[2] >= self.canvas_width:
                self.x = -4
            if location[3] >= self.canvas_height:
                self.y = -4
            self.canvas.after(12, self.draw)
ball = pongBall(canvasObject, "red")
def BallBounce(event):
    ball.draw()
canvasObject.bind_all("<Button-1>", BallBounce)
tkGUI.mainloop()