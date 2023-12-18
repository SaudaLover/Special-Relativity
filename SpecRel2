import turtle as trtl
import formulas
import numpy as np
import scipy.constants as spc


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
print("Length Contraction: ", formulas.length_contraction(vel))
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


twin2=trtl.Turtle()
twin2.hideturtle()
twin2.speed(0)
twin2.shape('turtle')
twin2.turtlesize(5,5)
twin2.color('red')
twin2.penup()
twin2.goto(450,100)

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
captiontext2 = ['Length Contraction: ','Negligible']
captiontext3 = ['Time Dilation: ','Negligible']


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

def caption_write():

    strcaptiontext1 = ''.join(captiontext1)
    strcaptiontext2 = ''.join(captiontext2)
    strcaptiontext3 = ''.join(captiontext3)
    caption.penup()
    caption.goto(-500,-25)
    caption.pendown()
    caption.write(strcaptiontext1,False,"left",("Arial",20,"normal"))
    caption.penup()
    caption.goto(-500,-75)
    caption.pendown()
    caption.write(strcaptiontext2,False,"left",("Arial",20,"normal"))
    caption.penup()
    caption.goto(-500,-125)
    caption.pendown()
    caption.write(strcaptiontext3,False,"left",("Arial",20,"normal"))



caption_write()

twin1.showturtle()
twin2.showturtle()


def trial_1():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
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
    captiontext2.append('Negligible')
    captiontext3.append('Negligible')
    
    caption_write()


    twin1.showturtle()
    twin2.showturtle()


def trial_2c():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
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
    captiontext3.append(str(formulas.time_dilation(vel/2)))
    captiontext3.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()


def trial_3c():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
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
    captiontext3.append(str(formulas.time_dilation(vel)))
    captiontext3.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()


def trial_2():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
    while True:
        if len(titletext) > 0:
             titletext.pop()
        else:
             break
    titletext.append('Trial 2: 0.45 Times the Speed of Light')
    strtitletext=''.join(titletext)
    twin1.turtlesize(5,5*formulas.shrink_factor(.5))
    twin2.turtlesize(5,5*formulas.shrink_factor(.5))
    twin1.goto(-450*formulas.shrink_factor(.5),100)
    twin2.goto(450*formulas.shrink_factor(.5),100)
    title.write(strtitletext,False,"center",("Arial",24,"normal"))


    captiontext1.append(str(formulas.shrink_factor(.5)))
    captiontext2.append(str(formulas.length_contraction(.5)))
    captiontext2.append(' meters')
    captiontext3.append(str(formulas.time_dilation(.5)))
    captiontext3.append(' seconds')

    caption_write()

    twin1.showturtle()
    twin2.showturtle()


def trial_3():
    twin1.hideturtle()
    twin2.hideturtle()
    title.clear()
    caption.clear()
    caption_reset()
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
    captiontext3.append(str(formulas.time_dilation(.99)))
    captiontext3.append(' seconds')

    caption_write()


    twin1.showturtle()
    twin2.showturtle()


wn.onkeypress(trial_1,"1")
wn.onkeypress(trial_2,"2")
wn.onkeypress(trial_3,"3")

wn.onkeypress(trial_2c,"4")
wn.onkeypress(trial_3c,"5")
   

wn.listen()
wn.mainloop()
