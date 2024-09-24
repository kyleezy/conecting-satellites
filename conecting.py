import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE='space'
total=5
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
    for satellite in satellites:
       satellite.draw() 
def update():
    pass









pgzrun.go()  
