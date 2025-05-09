import pgzrun,random
WIDTH=800
HEIGHT=600
TITLE="mothers dayyyyyyyyyyy"
score=0

questionrect=Rect(10,100,670,150)
answerrect1=Rect(10,290,335,115)
answerrect2=Rect(350,290,335,115)
answerrect3=Rect(10,415,335,115)
answerrect4=Rect(350,415,335,115)
answerrect=[answerrect1,answerrect2,answerrect3,answerrect4]

person=Actor("bottle")
person.pos=(400,500)

def draw():
    screen.fill((50,0,35))
    screen.draw.filled_rect(questionrect,(41,2,25))
    screen.draw.filled_rect(answerrect1,(107,4,45))
    screen.draw.filled_rect(answerrect2,(107,4,45))
    screen.draw.filled_rect(answerrect3,(107,4,45))
    screen.draw.filled_rect(answerrect4,(107,4,45))
    person.draw()


def update():
    for i in answerrect:
        i.y+=5
    if keyboard.left and person.x>0:
        person.x-=5
    if keyboard.right and person.x<801:
        person.x+=5

pgzrun.go()