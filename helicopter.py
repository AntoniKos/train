
import tkinter as tk


class Helicopter:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.hel_body = [(self.x + 10, self.y - 23), (self.x + 13, self.y - 10), \
                         (self.x + 13, self.y + 10), (self.x + 5, self.y + 20), \
                         (self.x, self.y + 45), (self.x - 5, self.y + 20), \
                         (self.x - 13, self.y + 10), (self.x - 13, self.y - 10), \
                         (self.x - 10, self.y - 23), (self.x + 10, self.y - 23)]


        self.obj1 = canvas.create_polygon(self.hel_body)

        self.obj2 = canvas.create_line(self.x + 15, self.y - 20, self.x + 15, self.y + 20)
        self.obj3 = canvas.create_line(self.x - 15, self.y - 20, self.x - 15, self.y + 20)

        self.obj4 = canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20)

        self.obj5 = canvas.create_oval(self.x-2, self.y-2, self.x+2, self.y+2)
        self.obj6 = canvas.create_line(self.x, self.y, self.x + 20, self.y)
        self.obj7 = canvas.create_line(self.x, self.y, self.x, self.y + 20)

        self.obj8 = canvas.create_line(self.x, self.y + 45, self.x + 5, self.y + 45)
        self.obj9 = canvas.create_line(self.x + 5, self.y + 40, self.x + 5, self.y + 50)
        self.a = [self.obj1, self.obj2, self.obj3, self.obj9, self.obj5, self.obj6, self.obj7, self.obj8, self.obj4]

    def move(self):
        self.dx1 = self.dx
        self.dy1 = self.dy
        self.x_coord = canvas.coords(self.obj4)[0]
        self.y_coord = canvas.coords(self.obj4)[1]
        if self.x_coord <= 0:
            if 5 < self.y_coord < 619:
                if self.dx < 0:
                    self.dx1 = 0
                elif self.dx >= 0:
                    self.dx1 = self.dx;
                    self.dy1 = self.dy

            elif self.y_coord <= 5:
                if self.dx < 0 or self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx > 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

            elif self.y_coord >= 619:
                if self.dx < 0 or self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx > 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

        elif self.x_coord >= 650:
            if 5 < self.y_coord < 619:
                if self.dx > 0:
                    self.dx1 = 0
                elif self.dx <= 0:
                    self.dx1 = self.dx;
                    self.dy1 = self.dy

            elif self.y_coord <= 5:
                if self.dx > 0 or self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx < 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

            elif self.y_coord >= 619:
                if self.dx > 0 or self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx < 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

        elif 0 < self.x_coord < 650 and self.y_coord <= 5:
            if self.dy < 0:
                self.dy1 = 0
            elif self.dy >= 0:
                self.dx1 = self.dx;
                self.dy1 = self.dy

        elif 0 < self.x_coord < 650 and self.y_coord >= 619:
            if self.dy > 0:
                self.dy1 = 0
            elif self.dy <= 0:
                self.dx1 = self.dx;
                self.dy1 = self.dy
        print(self.x_coord, self.y_coord)

    def show(self):
        for i in self.a:
            canvas.move(i, self.dx1, self.dy1)

def tick():
    obj.move()
    obj.show()
    root.after(50, tick)

root = tk.Tk()
root.geometry(str(700) + "x" + str(700))
canvas = tk.Canvas(root, width = 690, height = 690, bg = 'white')
canvas.pack(anchor="nw", fill=tk.BOTH)
obj = Helicopter(345, 345)
tick()


root.mainloop()
"""windowSize(700, 700)
canvasPos(5, 5)
canvasSize(690, 690)



class Helicopter:
    def __init__(self, x, y):
        global a, obj1, obj4
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.hel_body = [(self.x + 10, self.y - 23), (self.x + 13, self.y - 10), \
                    (self.x + 13, self.y + 10), (self.x + 5, self.y + 20), \
                    (self.x, self.y + 45), (self.x - 5, self.y + 20), \
                    (self.x - 13, self.y + 10), (self.x - 13, self.y - 10), \
                    (self.x - 10, self.y - 23), (self.x + 10, self.y - 23)]
     
        brushColor("yellow")
        penSize(2)
        self.obj1 = polygon(self.hel_body)
        
        self.obj2 = line(self.x + 15, self.y - 20, self.x + 15, self.y + 20)
        self.obj3 = line(self.x - 15, self.y - 20, self.x - 15, self.y + 20)
        
        brushColor("white")
        penSize(1)
        self.obj4 = circle(self.x, self.y, 20)
        brushColor("black")
        self.obj5 = circle(self.x, self.y, 2)
        self.obj6 = line(self.x, self.y, self.x + 20, self.y)
        self.obj7 = line(self.x, self.y, self.x, self.y + 20)
       
        self.obj8 = line(self.x, self.y + 45, self.x + 5, self.y + 45)
        self.obj9 = line(self.x + 5, self.y + 40, self.x + 5, self.y + 50)
        self.a = [self.obj1, self.obj2, self.obj3, self.obj9, self.obj5, self.obj6, self.obj7, self.obj8, self.obj4]

    def move(self):
        self.dx1 = self.dx
        self.dy1 = self.dy
        self.x_coord = coords(self.obj4)[0]
        self.y_coord = coords(self.obj4)[1]
        if self.x_coord <= 0:
            if 5 < self.y_coord < 619:
                if self.dx < 0:
                    self.dx1 = 0
                elif self.dx >= 0:
                    self.dx1 = self.dx;
                    self.dy1 = self.dy

            elif self.y_coord <= 5:
                if self.dx < 0 or self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx > 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

            elif self.y_coord >= 619:
                if self.dx < 0 or self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx > 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

        elif self.x_coord >= 650:
            if 5 < self.y_coord < 619:
                if self.dx > 0:
                    self.dx1 = 0
                elif self.dx <= 0:
                    self.dx1 = self.dx;
                    self.dy1 = self.dy

            elif self.y_coord <= 5:
                if self.dx > 0 or self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx < 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

            elif self.y_coord >= 619:
                if self.dx > 0 or self.dy > 0:
                    self.dx1 = 0;
                    self.dy1 = 0
                elif self.dy < 0:
                    self.dx1 = 0;
                    self.dy1 = self.dy
                elif self.dx < 0:
                    self.dx1 = self.dx;
                    self.dy1 = 0

        elif 0 < self.x_coord < 650 and self.y_coord <= 5:
            if self.dy < 0:
                self.dy1 = 0
            elif self.dy >= 0:
                self.dx1 = self.dx;
                self.dy1 = self.dy

        elif 0 < self.x_coord < 650 and self.y_coord >= 619:
            if self.dy > 0:
                self.dy1 = 0
            elif self.dy <= 0:
                self.dx1 = self.dx;
                self.dy1 = self.dy

    def show(self):
        for i in self.a:
            moveObjectBy(i, self.dx1, self.dy1)

    def keyPressed(self, event):
        if event.keycode == VK_LEFT:
            self.dx = -5;
            self.dy = 0
        elif event.keycode == VK_RIGHT:
            self.dx = 5;
            self.dy = 0
        elif event.keycode == VK_UP:
            self.dx = 0;
            self.dy = -5
        elif event.keycode == VK_DOWN:
            self.dx = 0;
            self.dy = 5
        elif event.keycode == VK_SPACE:
            self.dx = self.dy = 0
        elif event.keycode == VK_ESCAPE:
            close()

def tick():
    obj.move()
    obj.show()


obj = Helicopter(345, 345)

onKey(obj.keyPressed)
onTimer(tick, 50)

run()"""
