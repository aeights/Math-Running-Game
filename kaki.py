from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1000, 1000

def warna():
    glBegin(GL_POLYGON)
    glColor3ub(100, 500, 250)
    glVertex2d(100, 0)#a
    glVertex2d(140, 0)#b

    glVertex2d(140, 0)#b
    glVertex2d(140, 50)#c

    glVertex2d(140, 50)#c
    glVertex2d(100, 50)#L
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(100, 100, 200)
    glVertex2d(140, 50)#C
    glVertex2d(140, 100)#d

    glVertex2d(140, 100)#d
    glVertex2d(100, 100)#m

    glVertex2d(100, 100)#m
    glVertex2d(100, 50)#l
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(100, 100, 200)
    glVertex2d(140, 100)#D
    glVertex2d(250, 100)#e

    glVertex2d(250, 100)#e
    glVertex2d(300, 100)#n

    glVertex2d(300, 100)#n
    glVertex2d(300, 180)#j

    glVertex2d(300, 180)#j
    glVertex2d(100, 180)#k

    glVertex2d(100, 180)#k
    glVertex2d(100, 100)#m
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(100, 100, 200)
    glVertex2d(250, 100)#e
    glVertex2d(250, 50)#f

    glVertex2d(250, 50)#f
    glVertex2d(300, 50)#i

    glVertex2d(300, 50)#i
    glVertex2d(300, 100)#n

    glVertex2d(300, 100)#n
    glVertex2d(250, 100)#e
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(100, 500, 250)
    glVertex2d(250, 50)#f
    glVertex2d(250, 0)#g

    glVertex2d(250, 0)#g
    glVertex2d(300, 0)#h

    glVertex2d(300, 0)#h
    glVertex2d(300, 50)#i
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, w, -500, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    
    warna()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()