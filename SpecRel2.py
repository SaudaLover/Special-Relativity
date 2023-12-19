import turtle as trtl
import formulas
import numpy as np
import scipy.constants as spc
import time


#ask for values
while True:
    vel = float(input("What Factor of the speed of light do you want to go at?: "))
    length = float(input("What is the height of our einsteins: "))
    if vel > 0 and vel < 1:
        break
    else:
            print("Put it inbetween 0 and 1 please")
    
print("Values:")
print("Shrinking Value: ", formulas.shrink_factor(vel))
print("Separation Distance: ", formulas.length_contraction(vel))
print("Time Dilation: ", formulas.time_dilation(vel))
print("EInstein height contraction: ", formulas.length_einstein_contraction(vel, length))


#window setup
wn=trtl.Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

wn.setup(1200,675)
wn.bgcolor('black')
wn.title('if you see this, hi!')



c=spc.speed_of_light

twin1=trtl.Turtle()
twin1.hideturtle()
twin1.speed(0)
twin1.shape('turtle')
twin1.turtlesize(5,5)
twin1.color('blue')
twin1.penup()
twin1.goto(-450,100)
twin1.left(180)


twin2=trtl.Turtle()
twin2.hideturtle()
twin2.speed(0)
twin2.shape('turtle')
twin2.turtlesize(5,5)
twin2.color('red')
twin2.penup()
twin2.goto(450,100)
twin2.left(180)

clock1 = trtl.Turtle()
clock1.hideturtle()
clock1.speed(0)
clock1.color('white')
clock1.pencolor('white')
clock1.penup()
clock1.goto(-450,-25)
clock1.pendown()
clock1.circle(35)

clock2 = trtl.Turtle()
clock2.hideturtle()
clock2.speed(0)
clock2.color('white')
clock2.pencolor('white')
clock2.penup()
clock2.goto(450,-25)
clock2.pendown()
clock2.circle(35)




titletext = ['Trial ','1',': Non-Relativistic Speed']
titletext.pop(1)
titletext.insert(1,'1')
strtitletext=''.join(titletext)

title=trtl.Turtle()
title.hideturtle()
title.speed(0)
title.penup()
title.goto(0,275)
title.pendown()
title.pencolor('white')
title.write(strtitletext,False,"center",("Arial",24,"normal"))


captiontext1 = ['Shrinking Factor: ','Negligible']
captiontext2 = ['Separation Distance: ','100000 meters']
captiontext3 = ['Apparent Heights: ','1.9 meters']
captiontext4 = ['Time Dilation: ','Negligible']



caption=trtl.Turtle()
caption.hideturtle()
caption.speed(0)
caption.pencolor('white')

def caption_reset():
    while True:
        if len(captiontext1) > 1:
             captiontext1.pop()
        else:
             break
    while True:
        if len(captiontext2) > 1:
             captiontext2.pop()
        else:
             break
    while True:
        if len(captiontext3) > 1:
             captiontext3.pop()
        else:
             break
    while True:
        if len(captiontext4) > 1:
             captiontext4.pop()
        else:
             break

def caption_write():

    strcaptiontext1 = ''.join(captiontext1)
    strcaptiontext2 = ''.join(captiontext2)
    strcaptiontext3 = ''.join(captiontext3)
    strcaptiontext4 = ''.join(captiontext4)
    caption.penup()
    caption.goto(-500,-100)
    caption.pendown()
    caption.write(strcaptiontext1,False,"left",("Arial",20,"normal"))
    caption.penup()
    caption.goto(-500,-150)
    caption.pendown()
    caption.write(strcaptiontext2,False,"left",("Arial",20,"normal"))
    caption.penup()
    caption.goto(-500,-200)
    caption.pendown()
    caption.write(strcaptiontext3,False,"left",("Arial",20,"normal"))
    caption.penup()
    caption.goto(-500,-250)
    caption.pendown()
    caption.write(strcaptiontext4,False,"left",("Arial",20,"normal"))



caption_write()

twin1.showturtle()
twin2.showturtle()


laser=trtl.Turtle()
laser.penup()
laser.pencolor('red')
laser.hideturtle()
laser.speed(0)
laser.goto(450,100)
laser.pendown()
laser.shape('arrow')
laser.speed(6)
laser.goto(-450,100)

def clock_setup():
    clock1.pencolor('white')
    clock1.penup()
    clock1.goto(-450,-25)
    clock1.pendown()
    clock1.circle(35)
    clock2.pencolor('white')
    clock2.penup()
    clock2.goto(450,-25)
    clock2.pendown()
    clock2.circle(35)

n=-25
m=-450
for i in range (0,5):
    
    clock1.pencolor('white')
    clock2.pencolor('white')
    clock1.goto(m,n)
    clock2.goto(m+900,n)
    time.sleep(1)
    clock1.pencolor('black')
    clock2.pencolor('black')
    clock1.goto(-450,10)
    clock2.goto(450,10)
    if i%4==0:
        n=45
        m=-450
    if i%4 == 1:
        n=10
        m=-415
    if i%4 == 2:
        n=-25
        m=-450
    if i%4 == 3:
        n=10
        m=-485

def clock(delay):

    for i in range (0,5):
        if i%4==0:
            n=45
            m=-450
        if i%4 == 1:
            n=10
            m=-415
        if i%4 == 2:
            n=-25
            m=-450
        if i%4 == 3:
            n=10
            m=-485
        clock1.pencolor('white')
        clock2.pencolor('white')
        clock1.goto(m,n)
        clock2.goto(m+900,n)
        time.sleep(delay)
        clock1.pencolor('black')
        clock2.pencolor('black')
        clock1.goto(-450,10)
        clock2.goto(450,10)
        
        


    
   
    
         




def trial_1():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    laser.clear()
    clock1.clear()
    clock2.clear()
    clock_setup
    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.append('Trial 1: Non-Relativistic Speed')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5)
    twin2.turtlesize(5,5)
    twin1.goto(-450,100)
    twin2.goto(450,100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))


    captiontext1.append('Negligible')
    captiontext2.append('100000 meters')
    captiontext3.append('1.9 meters')
    captiontext4.append('Negligible')
    
    caption_write()


    twin1.showturtle()
    twin2.showturtle()

    laser.speed(0)
    laser.penup()
    laser.goto(450,100)
    laser.pendown()
    laser.speed(6)
    laser.goto(-450,100)

    clock(1)

    


def trial_2c():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    laser.clear()
    
    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.append('Custom Trial 2: ')
    titletext.append(str(vel/2))
    titletext.append(' times the speed of light')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5*formulas.shrink_factor(vel/2))
    twin2.turtlesize(5,5*formulas.shrink_factor(vel/2))
    twin1.goto(-450*formulas.shrink_factor(vel/2),100)
    twin2.goto(450*formulas.shrink_factor(vel/2),100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))


    captiontext1.append(str(formulas.shrink_factor(vel/2)))
    captiontext2.append(str(formulas.length_contraction(vel/2)))
    captiontext2.append(' meters')
    captiontext3.append(str(formulas.length_einstein_contraction(vel/2,length)))
    captiontext3.append(' meters')
    captiontext4.append(str(formulas.time_dilation(vel/2)))
    captiontext4.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()

    laser.speed(0)
    laser.penup()
    laser.goto(450*formulas.shrink_factor(vel/2),100)
    laser.pendown()
    laser.speed(6)
    laser.goto(-450*formulas.shrink_factor(vel/2),100)

    clock(1/formulas.shrink_factor(vel/2))



    
    


def trial_3c():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    laser.clear()

    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.insert(1,'Custom Trial 3: ')
    titletext.append(str(vel))
    titletext.append(' Times the Speed of Light')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5*formulas.shrink_factor(vel))
    twin2.turtlesize(5,5*formulas.shrink_factor(vel))
    twin1.goto(-450*formulas.shrink_factor(vel),100)
    twin2.goto(450*formulas.shrink_factor(vel),100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))

    captiontext1.append(str(formulas.shrink_factor(vel)))
    captiontext2.append(str(formulas.length_contraction(vel)))
    captiontext2.append(' meters')
    captiontext3.append(str(formulas.length_einstein_contraction(vel,length)))
    captiontext3.append(' meters')
    captiontext4.append(str(formulas.time_dilation(vel)))
    captiontext4.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()

    laser.speed(0)
    laser.penup()
    laser.goto(450*formulas.shrink_factor(vel),100)
    laser.pendown()
    laser.speed(6)
    laser.goto(-450*formulas.shrink_factor(vel),100)

    clock(1/formulas.shrink_factor(vel))

   


def trial_2():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    laser.clear()
    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.append('Trial 2: 0.50 Times the Speed of Light')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5*formulas.shrink_factor(.5))
    twin2.turtlesize(5,5*formulas.shrink_factor(.5))
    twin1.goto(-450*formulas.shrink_factor(.5),100)
    twin2.goto(450*formulas.shrink_factor(.5),100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))


    captiontext1.append(str(formulas.shrink_factor(.5)))
    captiontext2.append(str(formulas.length_contraction(.5)))
    captiontext2.append(' meters')
    captiontext3.append(str(formulas.length_einstein_contraction(.5,length)))
    captiontext3.append(' meters')
    captiontext4.append(str(formulas.time_dilation(.5)))
    captiontext4.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()

    laser.speed(0)
    laser.penup()
    laser.goto(450*formulas.shrink_factor(.5),100)
    laser.pendown()
    laser.speed(6)
    laser.goto(-450*formulas.shrink_factor(.5),100)

    clock(1/formulas.shrink_factor(.5))

   


def trial_3():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    laser.clear()
    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.append('Trial 3: 0.99 Times the Speed of Light')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5*formulas.shrink_factor(.99))
    twin2.turtlesize(5,5*formulas.shrink_factor(.99))
    twin1.goto(-450*formulas.shrink_factor(.99),100)
    twin2.goto(450*formulas.shrink_factor(.99),100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))


    captiontext1.append(str(formulas.shrink_factor(.99)))
    captiontext2.append(str(formulas.length_contraction(.99)))
    captiontext2.append(' meters')
    captiontext3.append(str(formulas.length_einstein_contraction(.99,length)))
    captiontext3.append(' meters')
    captiontext4.append(str(formulas.time_dilation(.99)))
    captiontext4.append(' seconds')

    caption_write()


    twin1.showturtle()
    twin2.showturtle()

    laser.speed(0)
    laser.penup()
    laser.goto(450*formulas.shrink_factor(.99),100)
    laser.pendown()
    laser.speed(6)
    laser.goto(-450*formulas.shrink_factor(.99),100)

    clock(1/formulas.shrink_factor(.99))

   
    

wn.onkeypress(trial_1,"1")
wn.onkeypress(trial_2,"2")
wn.onkeypress(trial_3,"3")

wn.onkeypress(trial_2c,"4")
wn.onkeypress(trial_3c,"5")
   

wn.listen()
wn.mainloop()
