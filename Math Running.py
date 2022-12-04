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
xmin_object = -10
xmax_object = 20
ymin_object = -20
ymax_object = 20 
x_pos_object = 230
y_pos_object = -60

# Character
xmin_char = -10
xmax_char = 10
ymin_char = -20
ymax_char = 20
x_pos_char = -210
y_pos_char = -60
onfloor = False

# Game
crash = False
hp = 3
point = 10
level = 1

collision = 0

def draw_text(text,xpos,ypos,r,b,g):
    color = (r, b, g)
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

# Question
number1 = random.randrange(1,10)
number2 = random.randrange(1,10)
wrong_answer = number1+number1
correct_answer = number1+number2
choice1 = wrong_answer
choice2 = correct_answer

def quest():
    if onfloor == True and x_pos_object <= -160:
        lompat(0)

def refresh_quest():
    global number1,number2,choice1,choice2,wrong_answer,correct_answer
    # refresh number
    rand_num1 = random.randrange(1,10)
    number1 = rand_num1
    rand_num2 = random.randrange(1,10)
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

def character():
    global x_pos_char,y_pos_char,x_pos_object,y_pos_object,collision
    glPushMatrix()
    glTranslated(x_pos_char,y_pos_char,0)
    if x_pos_char == x_pos_object and y_pos_object-1<=y_pos_char<=y_pos_object:
        print("terkena ndase",collision)
        collision+=1
    # print('x character:',x_pos_char,'y character:',y_pos_char)
    # print('x object:',x_pos_object,'y object:',y_pos_object)
    glBegin(GL_POLYGON)
    glColor3ub(60, 170, 205)
    glVertex2d(xmin_char,ymax_char)
    glVertex2d(xmin_char,ymin_char)
    glVertex2d(xmax_char,ymin_char)
    glVertex2d(xmax_char,ymax_char)
    glEnd()
    glPopMatrix()

def rintangan():
    global x_pos_object,y_pos_object,number1,number2
    glPushMatrix()
    glTranslated(x_pos_object,y_pos_object,0)
    x_pos_object -= 0.5
    if -280 <= x_pos_object <= -270:
        x_pos_object = 230
        refresh_quest()
    glBegin(GL_POLYGON)
    glColor3ub(60, 170, 205)
    glVertex2d(xmin_object,ymax_object)
    glVertex2d(xmin_object,ymin_object)
    glVertex2d(xmax_object,ymin_object)
    glVertex2d(xmax_object,ymax_object)
    glEnd()
    glPopMatrix()

def lompat(value):
    global y_pos_char,onfloor
    if onfloor==True:
        y_pos_char+=0.5
        glutTimerFunc(180,lompat,0)
        if y_pos_char >= 10:
            onfloor=False
    if onfloor==False and y_pos_char>=-60:
        y_pos_char-=0.5
        glutTimerFunc(180,lompat,0)

def jump(key, x, y):
    global x_pos_object,onfloor,gravity,choice1,choice2
    # if key == b'u':
    #     onfloor=True
    #     if onfloor==True:
    #         lompat(0)
    if key == b'1':
        if choice1 == correct_answer:
            onfloor=True
    if key == b'2':
        if choice2 == correct_answer:
            onfloor=True


def cloud():
    pass

def sun():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(245,255,97)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 50 * math.cos(theta)
        y = 50 * math.sin(theta)
        glVertex2f(x-20, y+180)
    glEnd()    
    glPopMatrix()

def ground():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(60, 0, 205)
    glVertex2d(-250,-80)
    glVertex2d(250,-80)
    glVertex2d(250,-250)
    glVertex2d(-250,-250)
    glEnd()
    glPopMatrix()

def start():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(60, 170, 205)
    glVertex2d(-100,30)
    glVertex2d(100,30)
    glVertex2d(100,-30)
    glVertex2d(-100,-30)
    glEnd()
    glPopMatrix()

def decorates():
    global number1,number2,choice1,choice2
    ground()
    sun()
    quest()
    draw_text(f"{number1} + {number2}",-20,-120,255,255,255)
    draw_text(f'{choice1}',-60,-180,255,255,255)
    draw_text(f'{choice2} ',40,-180,255,255,255)

def playgame():
    character()
    rintangan()

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
    # start()
    decorates()
    playgame()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Muhammad Afif Ma'ruf")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(jump)
glutMainLoop()