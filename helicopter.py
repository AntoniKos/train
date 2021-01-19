
from graph import *
windowSize(700, 700)
canvasPos(5, 5)
canvasSize(690, 690)

def helicopter(x,y):
  global a, obj1, obj4
  hel_body=[(x+10, y-23), (x+13, y-10),\
            (x+13, y+10), (x+5, y+20),\
            (x, y+45), (x-5, y+20),\
            (x-13, y+10), (x-13, y-10),\
            (x-10, y-23), (x+10, y-23)]
  """корпус вертолета"""
  brushColor("yellow")
  penSize(2)
  obj1=polygon(hel_body)
  """лыжи"""
  obj2=line(x+15, y-20, x+15, y+20)
  obj3=line(x-15, y-20, x-15, y+20)
  """пропеллер"""
  brushColor("white")
  penSize(1)
  obj4=circle(x,y,20)
  brushColor("black")
  obj5=circle(x,y,2)
  obj6=line(x,y,x+20,y)
  obj7=line(x,y,x,y+20)
  """малый пропеллер"""
  obj8=line(x,y+45,x+5,y+45)
  obj9=line(x+5,y+40,x+5,y+50)
  a=[obj1, obj2, obj3, obj9, obj5, obj6, obj7, obj8, obj4]
 
def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -5; dy = 0
  elif event.keycode == VK_RIGHT:
    dx = 5; dy = 0
  elif event.keycode == VK_UP:
    dx = 0; dy = -5
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 5
  elif event.keycode == VK_SPACE:
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close()
    
def update():
  dx1=dx
  dy1=dy
  for i in a:
      x_coord = coords(obj4)[0]
      if x_coord <= 0:
        if dx < 0: dx1 = 0
        elif dx >= 0: dx1 = dx; dy1 = dy
        moveObjectBy(i, dx1, dy1)
      elif x_coord >= 650:
        if dx > 0: dx1 = 0
        elif dx <= 0: dx1 = dx; dy1 = dy
        moveObjectBy(i, dx1, dy1)
      else:
        moveObjectBy(i, dx, dy)
 
    
dx = 0;  dy = 0

obj=helicopter(345,345)

onKey(keyPressed)
onTimer(update, 50)

run()
