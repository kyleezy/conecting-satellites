import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE='space'
total=5
target=1
lines=[]
satellites=[]
for i in range(5):
  space=Actor("st")
  x=random.randint(50,650)
  y=random.randint(50,550)
  space.pos=x,y
  satellites.append(space)
def draw():
    #screen.clear()
    screen.fill('red')
    number=1
    for satellite in satellites:
       satellite.draw() 
       screen.draw.text(str(number),(satellite.x,satellite.y+30))
       number=number+1
def on_mouse_down(pos):
  if satellites[target-1].collidepoint(pos):
    if target>1:
      lines.append((satellites[target-2].pos,satellites[target-1].pos))

def update():
    pass









pgzrun.go()  
