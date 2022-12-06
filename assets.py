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
yellow = 245,255,97
red = 254,0,0

log1 = 53,41,24
log2 = 103,83,53
log3 = 84,65,36
log4 = 65,50,30

sun1 = 253,221,127
sun2 = 250,209,86

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

def log():
    global log1,log2,log3
    glScaled(5,5,0)
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

def panda():
    global black,white,orange,pink,brown
    # glTranslated(100,100,0)
    glScaled(5,5,0)
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

def cloud():
    global black,white,blue
    glScaled(3,3,0)
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

def hp():
    glScaled(4,4,0)
    # square(0,0,40,40,orange)
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


def sun():
    glScaled(4,4,0)
    # Color
    square(0,0,50,100,yellow)
    square(0,0,100,50,yellow)

    # square(0,0,100,100,blue)
    square(50,0,50,3,black)
    square(-50,0,50,3,black)
    square(0,50,3,50,black)
    square(0,-50,3,50,black)

    square(47,29,8,3,black)
    square(44,37,8,3,black)
    square(42,42,3,3,black)#tengah
    square(29,47,3,8,black)
    square(37,44,3,8,black)

    square(-47,29,8,3,black)
    square(-44,37,8,3,black)
    square(-42,42,3,3,black)
    square(-29,47,3,8,black)
    square(-37,44,3,8,black)

    square(-47,-29,8,3,black)
    square(-44,-37,8,3,black)
    square(-42,-42,3,3,black)
    square(-29,-47,3,8,black)
    square(-37,-44,3,8,black)

    square(47,-29,8,3,black)
    square(44,-37,8,3,black)
    square(42,-42,3,3,black)
    square(29,-47,3,8,black)
    square(37,-44,3,8,black)

def sun_new():
    # glScaled(2,2,0)
    # square(0,0,100,100,blue)
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
    # log()
    # cloud()
    # sun()
    # sun_new()
    hp()
    # square(0,0,2,2,[255,160,112])
    # square(0,0,50,50,blue)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Muhammad Afif Ma'ruf")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()