import pgzrun
WIDTH=600
HEIGHT=600
list4enemies=[]
list4bullets=[]
spaceship=Actor("shotterspaceship")
alien=Actor("shooteralien")
spaceship.pos=(300,550)
gameover=False
win=False

for i in range(4):
    for j in range(4):
      list4enemies.append(Actor("shooteralien"))
      list4enemies[-1].x=50+i*50
      list4enemies[-1].y=80+j*50
      
    

def draw():
   screen.fill((20,0,50))
   spaceship.draw()
   for i in list4enemies:
      i.draw()
   for i in list4bullets:
       i.draw()
   if gameover:
       screen.draw.text("You lost:(",(300,300))

   elif win:
       screen.draw.text("YOU WOOONN",(300,300))


def on_key_down(key):
    if key==keys.SPACE:
        list4bullets.append(Actor("bullet"))
        list4bullets[-1].x=spaceship.x
        list4bullets[-1].y=spaceship.y-20

direction=1
godownnn=False
def update():
 global godownnn, direction, list4enemies, gameover, win
 if len(list4enemies)>0 and (list4enemies[-1].x>590 or list4enemies[0].x<10):
         godownnn=True
         direction*=-1
 for hi in list4enemies:
      hi.x+=5*direction
      if godownnn:
          hi.y+=10
      if hi.y==600:
          gameover=True
      for i in list4bullets:
          if hi.colliderect(i):
              list4enemies.remove(hi)
              list4bullets.remove(i)
              if len(list4enemies)==0:
                  win=True
 godownnn=False

 if keyboard.left and spaceship.x>0:
        spaceship.x-=10
 if keyboard.right and spaceship.x<601:
        spaceship.x+=10
 
 for i in list4bullets: 
    if i.y==0:
        list4bullets.remove(i)
    else:
        i.y-=35
    

pgzrun.go()