from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def circle1(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor(0,25,160,215)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle2(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def square_pemotong():
    glBegin(GL_QUADS)
    glColor(255,255,255)
    glVertex2f(250,100)
    glVertex2f(250,400)
    glVertex2f(400,400)
    glVertex2f(400,100)
    glEnd()

def square():
    glBegin(GL_QUADS)
    glColor(0,25,160,215)
    glVertex2f(250,270)
    glVertex2f(340,270)
    glVertex2f(340,230)
    glVertex2f(250,230)
    glVertex2f(340,175)
    glVertex2f(340,230)
    glVertex2f(300,230)
    glVertex2f(300,175)
    glEnd()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    circle1(250,250,100,360)
    circle2(250,250,60,360)
    square_pemotong()
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Muhammad Afif Ma'ruf")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()