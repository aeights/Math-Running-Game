from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

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
gravity =  0.5

# Cloud
xpos_cloud = 0
ypos_cloud = 90
collision = 0


def character():
    global x_pos_char,y_pos_char,x_pos_object,y_pos_object,collision
    glPushMatrix()
    glTranslated(x_pos_char,y_pos_char,0)
    if x_pos_char == x_pos_object and y_pos_object-1<=y_pos_char<=y_pos_object:
        print("terkena ndase",collision)
        collision+=1
    # if y_pos_char >= -60:
    #     y_pos_char -= gravity
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
    global x_pos_object,y_pos_object
    glPushMatrix()
    glTranslated(x_pos_object,y_pos_object,0)
    x_pos_object -= 0.5
    if -280 <= x_pos_object <= -270:
        x_pos_object = 230
    glBegin(GL_POLYGON)
    glColor3ub(60, 170, 205)
    glVertex2d(xmin_object,ymax_object)
    glVertex2d(xmin_object,ymin_object)
    glVertex2d(xmax_object,ymin_object)
    glVertex2d(xmax_object,ymax_object)
    glEnd()
    glPopMatrix()

onfloor = False

def lompat(value):
    global y_pos_char,onfloor
    if onfloor==True:
        y_pos_char+=1
        glutTimerFunc(5,lompat,0)
        if y_pos_char >= 0:
            onfloor=False
    if onfloor==False and y_pos_char>=-60:
        y_pos_char-=gravity
        glutTimerFunc(5,lompat,0)

def jump(key, x, y):
    global y_pos_char,onfloor,gravity,time_keeper
    if key == b'u':
        onfloor=True
        if onfloor==True:
            lompat(0)


def timer_jump(value):
    glutTimerFunc(100,timer_jump,0)

def cloud():
    global xpos_cloud,ypos_cloud
    glPushMatrix()
    glTranslated(xpos_cloud,ypos_cloud,0)
    # xpos_cloud-=1
    if xpos_cloud <= -450:
        xpos_cloud = 450
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-145, y+10)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-170, y-5)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-150, y-8)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-130, y-5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+20, y+35)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+20, y+15)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x, y+20)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+40, y+20)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+155, y+10)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+160, y-8)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+180, y+-5)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+140, y-5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-90, y+100)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-90, y+80)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-110, y+85)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x-80, y+85)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+80, y+125)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+80, y+105)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+100, y+110)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(195,195,195)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x+65, y+110)
    glEnd()
    glPopMatrix()

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
    sun()
    # cloud()
    ground()

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