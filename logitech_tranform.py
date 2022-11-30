from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

xPosition = 0
yPosition = 0
xScale = 1
yScale = 1
rotate = 0

def logitech(cx,cy,num_segment):
    glTranslated(xPosition, yPosition, 0)
    glScaled(xScale,yScale,0)
    glRotated(rotate, 0, 0, 3)
    glBegin(GL_POLYGON)
    glColor(0,25,160,215)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 100 * math.cos(theta)
        y = 100 * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 60 * math.cos(theta)
        y = 60 * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    glVertex2f(0,150)
    glVertex2f(100,150)
    glVertex2f(100,-150)
    glVertex2f(0,-150)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,25,160,215)
    glVertex2f(0,20)
    glVertex2f(90,20)
    glVertex2f(90,-20)
    glVertex2f(0,-20)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,25,160,215)
    glVertex2f(50,-20)
    glVertex2f(90,-20)
    glVertex2f(90,-60)
    glVertex2f(50,-60)
    glEnd()

def position_scale(key, x, y):
    global xPosition
    global yPosition
    global xScale
    global yScale
    if key == GLUT_KEY_LEFT:
        xPosition -= 50
    elif key == GLUT_KEY_RIGHT:
        xPosition += 50
    elif key == GLUT_KEY_UP:
        yPosition += 50
    elif key == GLUT_KEY_DOWN:
        yPosition -= 50
    elif key == GLUT_KEY_PAGE_UP:
        xScale += .1
        yScale += .1
    elif key == GLUT_KEY_PAGE_DOWN:
        if xScale < 0.2 and yScale < 0.2:
            xScale -= 0
            yScale -= 0
        else:
            xScale -= .1
            yScale -= .1

def rotated(key, x, y):
    global rotate
    if key == b'.':
        rotate -= 2
    elif key == b',':
        rotate += 10

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
    logitech(0,0,360)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Muhammad Afif Ma'ruf")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(position_scale)
glutKeyboardFunc(rotated)
glutMainLoop()