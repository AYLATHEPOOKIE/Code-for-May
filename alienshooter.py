import pgzrun
WIDTH=600
HEIGHT=800
list4enemies=[]
spaceship=Actor("shotterspaceship")
spaceship.pos=(300,700)
gamover=False

for i in range(4):
    for j in range(4):
      alien=Actor("shooteralien")
      list4enemies.append(alien)
      list4enemies[-1].x=50+i*50
      list4enemies[-1].y=200-j*50
      
    

def draw():
   screen.fill((20,0,50))
   for i in list4enemies:
      i.draw()
    
direction=1
godownnn=False
def update():
 global godownnn, direction, list4enemies, gameover
 if len(list4enemies)>0 and (list4enemies[0].x<10 or list4enemies[-1].x>590):
         godownnn=True
         direction*=-1
 for hi in list4enemies:
      hi.x+=5*direction
      if godownnn:
          hi.y+=10
          godownnn=False
      if hi.y==800:
          gameover=True
pgzrun.go()