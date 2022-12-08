from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import OpenGL.GLUT as glut
import os
# try:
#     del os.environ['DISPLAY']
# except:
#     pass

# Object
x_pos_object = -270
y_pos_object = -60

# Character
x_pos_char = -210
y_pos_char = -60
onfloor = False

# Game
play = False
game_over = False
hp = 3
point = 0
level = 1

collision = 0

def draw_text(text,xpos,ypos,color):
    font_style = glut.GLUT_BITMAP_TIMES_ROMAN_24
    glColor3ub(color[0],color[1],color[2])
    line = 0
    glRasterPos2f(xpos, ypos)
    for i in text:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def drawText1(text,xpos,ypos,color):
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(text):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def drawTextBold(text,xpos,ypos,color):
    glPushMatrix()
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in text:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

# Question
number1 = 0
number2 = 0
wrong_answer = 0
correct_answer = 0
choice1 = 0
choice2 = 0
range_num1 = 1
range_num2 = 5
state_quest = True
show_answer_left = False
show_answer_right = False

# Color
black = 55,37,56
white = 255,255,255
orange = 255,209,171
pink = 224,166,179
brown = 130,42,67
blue = 197,224,253
red = 254,0,0
black1 = 0,0,0

log1 = 53,41,24
log2 = 103,83,53
log3 = 84,65,36
log4 = 65,50,30

sun1 = 253,221,127
sun2 = 250,209,86

tree1 = 10,84,9
tree2 = 9,113,9
tree3 = 121,73,3
tree4 = 140,85,3

def quest():
    global state_quest,level,range_num2
    if onfloor == True and x_pos_object <= -120:
        lompat(0)
    if point == 100:
        level=2
        range_num2=10
    elif point == 200:
        level=3
        range_num2=15
    elif point == 300:
        level=4
        range_num2=20

def refresh_quest():
    global number1,number2,choice1,choice2,wrong_answer,correct_answer
    # refresh number
    rand_num1 = random.randrange(range_num1,range_num2)
    number1 = rand_num1
    rand_num2 = random.randrange(range_num1,range_num2)
    number2 = rand_num2

    # refresh answer
    wrong_answer = number1+number1
    correct_answer = number1+number2

    # random answer
    choices = [wrong_answer,correct_answer]
    rand_idx = random.randint(0,1)
    choice1 = choices[rand_idx]
    choices.pop(rand_idx)
    choice2 = choices[0]

def panda():
    global x_pos_char,y_pos_char,x_pos_object,y_pos_object,collision,hp
    glPushMatrix()
    glTranslated(x_pos_char,y_pos_char,0)
    if x_pos_char == x_pos_object and y_pos_object-1<=y_pos_char<=y_pos_object:
        print("terkena ndase",collision)
        collision+=1
        hp-=1

    # body
    square(0,0,40,45,white)
    square(-18,0,40,13,pink)
    square(3,-8,3,29,pink)
    square(3,15,3,7,black)
    square(-11,-17,3,10,pink)
    square(-11,-14,3,5,pink)
    square(-14,25,10,11,pink)
    square(2,24,10,25,white)
    square(18,21,3,5,white)
    # eye
    square(3,4,15,29,pink)
    square(4,2,12,25,orange)
    square(3,12,3,33,black)
    square(3,-5,3,29,black)
    square(18,4,15,3,black)
    square(-12,4,15,3,black)
    square(12,4,7,3,black) #mata kiri
    square(-4,4,7,3,black) #mata kanan
    square(4,2,3,7,black) #mulut

    square(3,22.5,7,8,pink)
    square(11.5,21.5,10,10,black)
    square(-5.5,21.5,10,10,black)
    square(-4,21.5,5.5,2.5,white)
    square(10,21.5,5.5,2.5,white)

    # Outline
    # Feet
    square(24,0,40,3,black)
    square(-23,0,40,3,black)
    square(0.5,-20,4,45,black)
    square(-20,-17,3,8,black)
    square(21,-17,3,6,black)
    square(-13,-23,3,12,black)
    square(-13,-26,3,8,black)
    square(14,-23,3,12,black)
    square(14,-26,3,8,black)

    # Head
    square(-20,25,13,3,black)
    square(-17,28,12,3,black)
    square(-14,29.5,9,3,black)
    square(2,29,3,30,black)
    square(21,21,4,3,black)
    square(18,28,12,3,black)
    square(21,29,8,3,black)
    square(-11,31,2,4,black)
    square(12,31,2,4,black)
    square(15,28,12,3,black)
    square(-17,27,3,3,brown)
    square(17,28,3,3,pink)

    # Hand
    square(-15,-5,5,3,black)
    square(-18,-5,12,3,black)
    square(-21,-5,18,3,black)
    square(-25,-6.5,15,3,black)
    square(-27,-6.5,12,3,black)

    square(26,-6.5,15,3,black)
    square(28,-6.5,12,3,black)
    glPopMatrix()

def log():
    global x_pos_object,y_pos_object,state_quest,show_answer_left,show_answer_right
    glPushMatrix()
    glTranslated(x_pos_object,y_pos_object,0)
    x_pos_object -= 1
    if -290 <= x_pos_object <= -280:
        x_pos_object = 270
        refresh_quest()
        state_quest=True
        show_answer_left=False
        show_answer_right=False

    square(0,0,40,40,log1)
    square(0,0,30,30,log2)
    square(0,0,20,20,log3)
    square(0,0,10,10,log2)
    square(0,0,5,5,log3)

    square(10,17.5,5,5,log4)
    square(-12.5,17.5,5,5,log4)
    square(-17.5,-17.5,5,5,log4)
    square(-17.5,2,5,5,log4)
    square(17.5,4,5,5,log4)
    square(17.5,-8,5,5,log4)
    square(0,-17.5,5,5,log4)

    square(-2,17.5,5,5,log3)
    square(10,-17.5,5,5,log3)
    square(17.5,17.5,5,5,log3)
    square(-17.5,10,5,5,log3)
    square(-10,-17.5,5,5,log3)
    square(-17.5,-8,5,5,log2)
    glPopMatrix()

def lompat(value):
    global y_pos_char,onfloor
    if onfloor==True:
        y_pos_char+=0.5
        glutTimerFunc(200,lompat,0)
        if y_pos_char >= 10:
            onfloor=False
    if onfloor==False and y_pos_char>=-60:
        y_pos_char-=0.25
        glutTimerFunc(200,lompat,0)

def jump(key, x, y):
    global onfloor,state_quest,show_answer_left,show_answer_right,point,play,game_over
    # if key == b'u':
    #     onfloor=True
    #     if onfloor==True:
    #         lompat(0)
    if play == True:
        if key == b'1' and state_quest == True:
            show_answer_left=True
            state_quest=False
            if choice1 == correct_answer:
                onfloor=True
                point+=10
        if key == b'2' and state_quest == True:
            show_answer_right=True
            state_quest=False
            if choice2 == correct_answer:
                onfloor=True
                point+=10
    if key == b'\r' and play == False:
        play=True
    if key == b'r' and game_over == True:
        play=False
        game_over=False

def square(x,y,height,width,color):
    glBegin(GL_POLYGON)
    glColor3ub(color[0],color[1],color[2])
    height = height/2
    width = width/2
    glVertex2f(-width+x,height+y)
    glVertex2f(width+x,height+y)
    glVertex2f(width+x,-height+y)
    glVertex2f(-width+x,-height+y)
    glEnd()

state_cloud = True
xpos_cloud = 0
ypos_cloud = 0

def cloud():
    global xpos_cloud,ypos_cloud,state_cloud
    glPushMatrix()
    glTranslated(xpos_cloud,ypos_cloud,0)
    if state_cloud == True:
        xpos_cloud -= 0.1
        if xpos_cloud <= -50:
            state_cloud = False
    if state_cloud == False:
        xpos_cloud += 0.1
        if xpos_cloud >= 50:
            state_cloud = True
    cloud1()
    cloud2()
    cloud3()
    cloud4()
    cloud5()
    glPopMatrix()

def cloud1():
    glPushMatrix()
    glTranslated(0,100,0)
    # Color
    square(0,16,20,99,white)
    square(0,30,15,41,white)
    square(-1.5,45,15,28,white)
    square(35.5,29,6,28,white)
    square(35,34.5,6,19,white)
    square(-38,25,5,15,white)

    # Color
    square(0,5,5,100,blue)
    square(-45,10,5,10,blue)
    square(-47,17,10,5,blue)

    square(-15,10,5,10,blue)
    square(-18,17,10,5,blue)
    square(-23,24,5,5,blue)

    square(10,10,5,10,blue)
    square(15,17,11,5,blue)
    square(20,25,5,5,blue)

    square(45,10,5,10,blue)
    square(47,17,10,5,blue)

    # Outline
    square(0,0,5,100,black)
    square(52,15,25,5,black)
    square(-52,12,20,5,black)
    square(-47,24,5,5,black)
    square(-28,24,5,5,black)
    square(-38,29,5,15,black)
    square(-23,32,11,5,black)
    square(-18,43,11,5,black)

    square(47,30,5,5,black)
    square(42,35,5,5,black)
    square(35,40,5,10,black)
    square(28,35,5,5,black)
    square(23,30,5,5,black)
    square(18,35,5,5,black)
    square(15,43,11,5,black)
    square(10,50,5,5,black)
    square(-13,50,5,5,black)
    square(-2,52,5,19,black)
    glPopMatrix()

def cloud2():
    glPushMatrix()
    glTranslated(150,80,0)
    # Color
    square(0,16,20,99,white)
    square(0,30,15,41,white)
    square(-1.5,45,15,28,white)
    square(35.5,29,6,28,white)
    square(35,34.5,6,19,white)
    square(-38,25,5,15,white)

    # Color
    square(0,5,5,100,blue)
    square(-45,10,5,10,blue)
    square(-47,17,10,5,blue)

    square(-15,10,5,10,blue)
    square(-18,17,10,5,blue)
    square(-23,24,5,5,blue)

    square(10,10,5,10,blue)
    square(15,17,11,5,blue)
    square(20,25,5,5,blue)

    square(45,10,5,10,blue)
    square(47,17,10,5,blue)

    # Outline
    square(0,0,5,100,black)
    square(52,15,25,5,black)
    square(-52,12,20,5,black)
    square(-47,24,5,5,black)
    square(-28,24,5,5,black)
    square(-38,29,5,15,black)
    square(-23,32,11,5,black)
    square(-18,43,11,5,black)

    square(47,30,5,5,black)
    square(42,35,5,5,black)
    square(35,40,5,10,black)
    square(28,35,5,5,black)
    square(23,30,5,5,black)
    square(18,35,5,5,black)
    square(15,43,11,5,black)
    square(10,50,5,5,black)
    square(-13,50,5,5,black)
    square(-2,52,5,19,black)
    glPopMatrix()

def cloud3():
    glPushMatrix()
    glTranslated(-150,90,0)
    # Color
    square(0,16,20,99,white)
    square(0,30,15,41,white)
    square(-1.5,45,15,28,white)
    square(35.5,29,6,28,white)
    square(35,34.5,6,19,white)
    square(-38,25,5,15,white)

    # Color
    square(0,5,5,100,blue)
    square(-45,10,5,10,blue)
    square(-47,17,10,5,blue)

    square(-15,10,5,10,blue)
    square(-18,17,10,5,blue)
    square(-23,24,5,5,blue)

    square(10,10,5,10,blue)
    square(15,17,11,5,blue)
    square(20,25,5,5,blue)

    square(45,10,5,10,blue)
    square(47,17,10,5,blue)

    # Outline
    square(0,0,5,100,black)
    square(52,15,25,5,black)
    square(-52,12,20,5,black)
    square(-47,24,5,5,black)
    square(-28,24,5,5,black)
    square(-38,29,5,15,black)
    square(-23,32,11,5,black)
    square(-18,43,11,5,black)

    square(47,30,5,5,black)
    square(42,35,5,5,black)
    square(35,40,5,10,black)
    square(28,35,5,5,black)
    square(23,30,5,5,black)
    square(18,35,5,5,black)
    square(15,43,11,5,black)
    square(10,50,5,5,black)
    square(-13,50,5,5,black)
    square(-2,52,5,19,black)
    glPopMatrix()

def cloud4():
    glPushMatrix()
    glTranslated(100,180,0)
    # Color
    square(0,16,20,99,white)
    square(0,30,15,41,white)
    square(-1.5,45,15,28,white)
    square(35.5,29,6,28,white)
    square(35,34.5,6,19,white)
    square(-38,25,5,15,white)

    # Color
    square(0,5,5,100,blue)
    square(-45,10,5,10,blue)
    square(-47,17,10,5,blue)

    square(-15,10,5,10,blue)
    square(-18,17,10,5,blue)
    square(-23,24,5,5,blue)

    square(10,10,5,10,blue)
    square(15,17,11,5,blue)
    square(20,25,5,5,blue)

    square(45,10,5,10,blue)
    square(47,17,10,5,blue)

    # Outline
    square(0,0,5,100,black)
    square(52,15,25,5,black)
    square(-52,12,20,5,black)
    square(-47,24,5,5,black)
    square(-28,24,5,5,black)
    square(-38,29,5,15,black)
    square(-23,32,11,5,black)
    square(-18,43,11,5,black)

    square(47,30,5,5,black)
    square(42,35,5,5,black)
    square(35,40,5,10,black)
    square(28,35,5,5,black)
    square(23,30,5,5,black)
    square(18,35,5,5,black)
    square(15,43,11,5,black)
    square(10,50,5,5,black)
    square(-13,50,5,5,black)
    square(-2,52,5,19,black)
    glPopMatrix()

def cloud5():
    glPushMatrix()
    glTranslated(-120,160,0)
    # Color
    square(0,16,20,99,white)
    square(0,30,15,41,white)
    square(-1.5,45,15,28,white)
    square(35.5,29,6,28,white)
    square(35,34.5,6,19,white)
    square(-38,25,5,15,white)

    # Color
    square(0,5,5,100,blue)
    square(-45,10,5,10,blue)
    square(-47,17,10,5,blue)

    square(-15,10,5,10,blue)
    square(-18,17,10,5,blue)
    square(-23,24,5,5,blue)

    square(10,10,5,10,blue)
    square(15,17,11,5,blue)
    square(20,25,5,5,blue)

    square(45,10,5,10,blue)
    square(47,17,10,5,blue)

    # Outline
    square(0,0,5,100,black)
    square(52,15,25,5,black)
    square(-52,12,20,5,black)
    square(-47,24,5,5,black)
    square(-28,24,5,5,black)
    square(-38,29,5,15,black)
    square(-23,32,11,5,black)
    square(-18,43,11,5,black)

    square(47,30,5,5,black)
    square(42,35,5,5,black)
    square(35,40,5,10,black)
    square(28,35,5,5,black)
    square(23,30,5,5,black)
    square(18,35,5,5,black)
    square(15,43,11,5,black)
    square(10,50,5,5,black)
    square(-13,50,5,5,black)
    square(-2,52,5,19,black)
    glPopMatrix()

def sun():
    glPushMatrix()
    # glBegin(GL_POLYGON)
    # glColor3ub(245,255,97)
    # glColor3ub(sun1[0],sun1[1],sun1[2])
    # for i in range(360):
    #     theta= 2 *3.1415926*i/360
    #     x = 50 * math.cos(theta)
    #     y = 50 * math.sin(theta)
    #     glVertex2f(x-20, y+180)
    # glEnd()
    glScaled(0.8,0.8,0)
    glTranslated(-20,230,0)
    square(50,0,90,10,sun2)
    square(-50,0,90,10,sun2)
    square(0,50,10,90,sun2)
    square(0,-50,10,90,sun2)

    square(0,0,90,90,sun1)
    square(40,40,10,10,white)

    square(60,60,10,10,sun2)
    square(-60,60,10,10,sun2)
    square(60,-60,10,10,sun2)
    square(-60,-60,10,10,sun2)

    square(0,70,10,40,sun2)
    square(0,80,10,10,sun2)
    square(0,70,10,10,sun1)

    square(0,-70,10,40,sun2)
    square(0,-80,10,10,sun2)
    square(0,-70,10,10,sun1)

    square(-70,0,40,10,sun2)
    square(-80,0,10,10,sun2)
    square(-70,0,10,10,sun1)

    square(70,0,40,10,sun2)
    square(80,0,10,10,sun2)
    square(70,0,10,10,sun1)
    glPopMatrix()

def tree():
    tree_1()
    tree_2()
    tree_3()
    tree_4()
    tree_5()

xpos_tree1 = -250
xpos_tree2 = -125
xpos_tree3 = 0
xpos_tree4 = 125
xpos_tree5 = 250

def tree_1():
    global xpos_tree1
    glPushMatrix()
    glTranslated(xpos_tree1,-51,0)
    xpos_tree1-=0.2
    if xpos_tree1 <= -300:
        xpos_tree1 = 300
    # Color
    square(0,-14,10,35,tree2)
    square(15,-14,10,3,tree1)

    square(0,-3,12,30,tree2)
    square(12,-3,12,3,tree1)

    square(0,6,7,26,tree2)
    square(9,6,7,3,tree1)

    square(0,15,12,21,tree2)
    square(6,15,12,3,tree1)

    square(0,26,10,15,tree2)
    square(3,26,10,3,tree1)

    square(0,35,8,9,tree2)

    square(0,-23,8,10,tree3)
    square(0,-25,4,10,tree4)

    # Outline
    square(0,40,3,3,black1)
    square(3,35,8,3,black1)
    square(-3,35,8,3,black1)

    square(6,26,10,3,black1)
    square(-6,26,10,3,black1)
    
    square(9,15,12,3,black1)
    square(-9,15,12,3,black1)
    
    square(12,6,7,3,black1)
    square(-12,6,7,3,black1)

    square(15,-3,12,3,black1)
    square(-15,-3,12,3,black1)

    square(18,-14,10,3,black1)
    square(-18,-14,10,3,black1)

    square(10.5,-20.5,3,12,black1)
    square(-10.5,-20.5,3,12,black1)

    square(6,-23,8,3,black1)
    square(-6,-23,8,3,black1)
    square(0,-28,3,9,black1)
    glPopMatrix()

def tree_2():
    global xpos_tree2
    glPushMatrix()
    glTranslated(xpos_tree2,-60,0)
    glScaled(0.7,0.7,0)
    xpos_tree2-=0.2
    if xpos_tree2 <= -300:
        xpos_tree2 = 300
    # Color
    square(0,-14,10,35,tree2)
    square(15,-14,10,3,tree1)

    square(0,-3,12,30,tree2)
    square(12,-3,12,3,tree1)

    square(0,6,7,26,tree2)
    square(9,6,7,3,tree1)

    square(0,15,12,21,tree2)
    square(6,15,12,3,tree1)

    square(0,26,10,15,tree2)
    square(3,26,10,3,tree1)

    square(0,35,8,9,tree2)

    square(0,-23,8,10,tree3)
    square(0,-25,4,10,tree4)

    # Outline
    square(0,40,3,3,black1)
    square(3,35,8,3,black1)
    square(-3,35,8,3,black1)

    square(6,26,10,3,black1)
    square(-6,26,10,3,black1)
    
    square(9,15,12,3,black1)
    square(-9,15,12,3,black1)
    
    square(12,6,7,3,black1)
    square(-12,6,7,3,black1)

    square(15,-3,12,3,black1)
    square(-15,-3,12,3,black1)

    square(18,-14,10,3,black1)
    square(-18,-14,10,3,black1)

    square(10.5,-20.5,3,12,black1)
    square(-10.5,-20.5,3,12,black1)

    square(6,-23,8,3,black1)
    square(-6,-23,8,3,black1)
    square(0,-28,3,9,black1)
    glPopMatrix()

def tree_3():
    global xpos_tree3
    glPushMatrix()
    glTranslated(xpos_tree3,-53,0)
    glScaled(0.9,0.9,0)
    xpos_tree3-=0.2
    if xpos_tree3 <= -300:
        xpos_tree3 = 300
    # Color
    square(0,-14,10,35,tree2)
    square(15,-14,10,3,tree1)

    square(0,-3,12,30,tree2)
    square(12,-3,12,3,tree1)

    square(0,6,7,26,tree2)
    square(9,6,7,3,tree1)

    square(0,15,12,21,tree2)
    square(6,15,12,3,tree1)

    square(0,26,10,15,tree2)
    square(3,26,10,3,tree1)

    square(0,35,8,9,tree2)

    square(0,-23,8,10,tree3)
    square(0,-25,4,10,tree4)

    # Outline
    square(0,40,3,3,black1)
    square(3,35,8,3,black1)
    square(-3,35,8,3,black1)

    square(6,26,10,3,black1)
    square(-6,26,10,3,black1)
    
    square(9,15,12,3,black1)
    square(-9,15,12,3,black1)
    
    square(12,6,7,3,black1)
    square(-12,6,7,3,black1)

    square(15,-3,12,3,black1)
    square(-15,-3,12,3,black1)

    square(18,-14,10,3,black1)
    square(-18,-14,10,3,black1)

    square(10.5,-20.5,3,12,black1)
    square(-10.5,-20.5,3,12,black1)

    square(6,-23,8,3,black1)
    square(-6,-23,8,3,black1)
    square(0,-28,3,9,black1)
    glPopMatrix()

def tree_4():
    global xpos_tree4
    glPushMatrix()
    glTranslated(xpos_tree4,-57,0)
    glScaled(0.8,0.8,0)
    xpos_tree4-=0.2
    if xpos_tree4 <= -300:
        xpos_tree4 = 300
    # Color
    square(0,-14,10,35,tree2)
    square(15,-14,10,3,tree1)

    square(0,-3,12,30,tree2)
    square(12,-3,12,3,tree1)

    square(0,6,7,26,tree2)
    square(9,6,7,3,tree1)

    square(0,15,12,21,tree2)
    square(6,15,12,3,tree1)

    square(0,26,10,15,tree2)
    square(3,26,10,3,tree1)

    square(0,35,8,9,tree2)

    square(0,-23,8,10,tree3)
    square(0,-25,4,10,tree4)

    # Outline
    square(0,40,3,3,black1)
    square(3,35,8,3,black1)
    square(-3,35,8,3,black1)

    square(6,26,10,3,black1)
    square(-6,26,10,3,black1)
    
    square(9,15,12,3,black1)
    square(-9,15,12,3,black1)
    
    square(12,6,7,3,black1)
    square(-12,6,7,3,black1)

    square(15,-3,12,3,black1)
    square(-15,-3,12,3,black1)

    square(18,-14,10,3,black1)
    square(-18,-14,10,3,black1)

    square(10.5,-20.5,3,12,black1)
    square(-10.5,-20.5,3,12,black1)

    square(6,-23,8,3,black1)
    square(-6,-23,8,3,black1)
    square(0,-28,3,9,black1)
    glPopMatrix()

def tree_5():
    global xpos_tree5
    glPushMatrix()
    glTranslated(xpos_tree5,-51,0)
    xpos_tree5-=0.2
    if xpos_tree5 <= -300:
        xpos_tree5 = 300
    # Color
    square(0,-14,10,35,tree2)
    square(15,-14,10,3,tree1)

    square(0,-3,12,30,tree2)
    square(12,-3,12,3,tree1)

    square(0,6,7,26,tree2)
    square(9,6,7,3,tree1)

    square(0,15,12,21,tree2)
    square(6,15,12,3,tree1)

    square(0,26,10,15,tree2)
    square(3,26,10,3,tree1)

    square(0,35,8,9,tree2)

    square(0,-23,8,10,tree3)
    square(0,-25,4,10,tree4)

    # Outline
    square(0,40,3,3,black1)
    square(3,35,8,3,black1)
    square(-3,35,8,3,black1)

    square(6,26,10,3,black1)
    square(-6,26,10,3,black1)
    
    square(9,15,12,3,black1)
    square(-9,15,12,3,black1)
    
    square(12,6,7,3,black1)
    square(-12,6,7,3,black1)

    square(15,-3,12,3,black1)
    square(-15,-3,12,3,black1)

    square(18,-14,10,3,black1)
    square(-18,-14,10,3,black1)

    square(10.5,-20.5,3,12,black1)
    square(-10.5,-20.5,3,12,black1)

    square(6,-23,8,3,black1)
    square(-6,-23,8,3,black1)
    square(0,-28,3,9,black1)
    glPopMatrix()

def draw_hp(x=130):
    global xpos_hp
    glPushMatrix()
    glTranslated(x,30,0)
    # Color
    square(9.5,15,4,10,red)
    square(-9.5,15,4,10,red)
    square(0,8.5,10,40,red)
    square(0,1,25,11,red)
    square(8,0,11,7,red)
    square(-8,0,11,7,red)
    square(11,2,4,7,red)
    square(-11,2,4,7,red)

    square(-9.5,13,3,5,white)
    square(-12,10,3,5,white)
    square(-13,8,5,3,white)

    # Outline
    square(0,12,3,3,black)
    square(3,15,3,3,black)
    square(-3,15,3,3,black)

    square(9.5,18,3,10,black)
    square(-9.5,18,3,10,black)
    square(16,15,3,3,black)
    square(-16,15,3,3,black)
    square(19,8.5,10,3,black)
    square(-19,8.5,10,3,black)

    square(16,2,3,3,black)
    square(-16,2,3,3,black)
    square(13,-1,3,3,black)
    square(-13,-1,3,3,black)
    square(10,-4,3,3,black)
    square(-10,-4,3,3,black)
    square(7,-7,3,3,black)
    square(-7,-7,3,3,black)
    square(4,-10,3,3,black)
    square(-4,-10,3,3,black)
    square(1,-13,3,3,black)
    square(-1,-13,3,3,black)
    glPopMatrix()

def show_hp():
    global xpos_hp,game_over
    if hp == 3:
        draw_hp()
        draw_hp(175)
        draw_hp(220)
    elif hp == 2:
        draw_hp()
        draw_hp(175)
    elif hp == 1:
        draw_hp()
    elif hp == 0:
        game_over=True

def dirt():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(60, 0, 205)
    glColor3ub(log2[0],log2[1],log2[2])
    glVertex2d(-250,-80)
    glVertex2d(250,-80)
    glVertex2d(250,-250)
    glVertex2d(-250,-250)
    glEnd()
    glPopMatrix()

def grass():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(102,166,60)
    glVertex2d(-250,-80)
    glVertex2d(250,-80)
    glVertex2d(250,-110)
    glVertex2d(-250,-110)
    glEnd()
    glPopMatrix()

def start():
    glPushMatrix()
    square(0,0,500,500,blue)
    square(0,0,80,200,[89,206,143])
    square(0,45,10,200,log3)
    square(0,-45,10,200,log3)
    square(105,0,80,10,log3)
    square(-105,0,80,10,log3)
    drawTextBold("PLAY GAME",-50,0,black1)
    drawText1("PRESS ENTER TO PLAY GAME",-96,-25,[255,255,255])

    dirt()
    grass()
    sun()
    cloud1()
    cloud2()
    cloud3()
    cloud4()
    cloud5()
    glPopMatrix()

def end():
    glPushMatrix()
    square(0,0,500,500,black)
    square(0,0,80,200,[141,141,170])
    square(0,45,10,200,blue)
    square(0,-45,10,200,blue)
    square(105,0,80,10,blue)
    square(-105,0,80,10,blue)
    drawTextBold("GAME OVER",-58,10,black1)
    drawText1(f'YOUR FINAL SCORE: {point}',-80,-10,white)
    drawText1('PRESS "R" TO RESTART',-80,-30,white)
    glPopMatrix()

def decorates():
    global xpos_hp
    square(0,0,500,500,blue)
    dirt()
    grass()
    sun()
    cloud()
    tree()
    quest()
    show_hp()

    # Quest box
    square(0,-128,3,80,log1)
    square(0,-160,3,80,log1)
    square(40,-144,35,3,log1)
    square(-40,-144,35,3,log1)

    # Highlight answer
    if show_answer_left==True:
        square(-48,-203,35,50,log1)
    elif show_answer_right==True:
        square(47,-203,35,50,log1)

    # Answer box
    square(-48,-187,3,50,[102,166,60])
    square(-48,-219,3,50,[102,166,60])

    square(48,-187,3,50,[102,166,60])
    square(48,-219,3,50,[102,166,60])

    square(-72,-203,35,3,[102,166,60])
    square(-22,-203,35,3,[102,166,60])
    square(72,-203,35,3,[102,166,60])
    square(22,-203,35,3,[102,166,60])

    # Draw quest
    draw_text(f"{number1} + {number2}",-25,-150,[255,255,255])
    draw_text(f'{choice1}',-60,-210,[255,255,255])
    draw_text(f'{choice2} ',35,-210,[255,255,255])

    # Draw level and score
    drawText1("LEVEL:",-230,-200,[255,255,255])
    drawText1(f'{level}',-180,-200,[255,255,255])
    drawText1("SCORE:",-230,-225,[255,255,255])
    drawText1(f'{point}',-180,-225,[255,255,255])

def playgame():
    log()
    panda()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,1)
    glLoadIdentity()
    iterate()
    if play == False and game_over == False:
        start()
    elif play == True and game_over == False:
        decorates()
        playgame()
    elif play == True and game_over == True:
        end()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Math Running Game")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(jump)
glutMainLoop()