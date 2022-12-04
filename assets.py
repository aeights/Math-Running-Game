from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

black = 55,37,56
white = 255,255,255
orange = 255,209,171
pink = 224,166,179
brown = 130,42,67
blue = 197,224,253

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

def panda():
    global black,white,orange,pink,brown
    # glTranslated(100,100,0)
    glScaled(5,5,0)
    # body
    square(0,0,50,50,white)
    square(-18,0,50,15,pink)
    square(3,-5,3,29,pink)
    square(3,18,3,7,black)
    # eye
    square(3,7,15,29,pink)
    square(4,5,12,25,orange)
    square(3,15,3,33,black)
    square(3,-2,3,29,black)
    square(18,7,15,3,black)
    square(-12,7,15,3,black)
    square(12,7,7,3,black) #mata kiri
    square(-4,7,7,3,black) #mata kanan
    square(4,5,3,7,black) #mulut

def cloud():
    global black,white,blue
    glScaled(3,3,0)
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
    square(38,29,5,15,black)

def sun():
    pass

def backup():
    global black,white,orange,pink,brown
    # glTranslated(100,100,0)
    glScaled(5,5,0)
    # body
    square(0,0,50,50,white)
    square(18,0,50,15,pink)
    square(-3,-5,3,29,pink)
    square(-3,18,3,7,black)
    # eye
    square(-3,7,15,29,pink)
    square(-4,5,12,25,orange)
    square(-3,15,3,33,black)
    square(-3,-2,3,29,black)
    square(-18,7,15,3,black)
    square(12,7,15,3,black)
    square(-12,7,7,3,black) #mata kiri
    square(4,7,7,3,black) #mata kanan
    square(-4,5,3,7,black) #mulut

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    square(0,0,500,500,[255,160,112])
    # panda()
    cloud()
    square(0,0,2,2,[255,160,112])
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Muhammad Afif Ma'ruf")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()