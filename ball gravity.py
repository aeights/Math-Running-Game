from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def KB(Key, x, y):
    global pressed
    if Key == b"u":
        pressed = True
    else:
        pressed = False
    if Key == b"q":
        sys.exit()

yy = -0.07
dt = 0.0005
v_velocity = 3
xx = 0
max = False
pressed = False

def drw():
    global xx, max, v_velocity, dt, yy, pressed
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(xx, 0.4, 0)
    glBegin(GL_POLYGON)  # The Line
    glVertex2d(-0.8, 0.1)
    glVertex2d(-0.8, -0.1)
    glVertex2d(-0.2, -0.1)
    glVertex2d(-0.2, 0.1)
    glEnd()
    glColor(0, 1, 0)
    glBegin(GL_POLYGON)  # The Line
    glVertex2d(-0.2, 0.1)
    glVertex2d(-0.2, -0.1)
    glVertex2d(0.4, -0.1)
    glVertex2d(0.4, 0.1)
    glEnd()
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.4, 0.1)  # The Line
    glVertex2d(0.4, -0.1)
    glVertex2d(0.8, -0.1)
    glVertex2d(0.8, 0.1)
    glEnd()

    glLoadIdentity()
    glTranslate(0, yy, 0)
    glColor(0, 1, 0)
    glutSolidSphere(0.07, 25, 25)  # The ball

    # movement of the Line

    if xx > 1.5:
        max = True
    if xx < -1.5:
        max = False
    if max:
        xx -= 0.0005
    else:
        xx += 0.0005
    # ????? movement of the Ball  ???????
    if pressed:
        yy += 0.0007
    else:
        v_velocity = v_velocity - 9.8 * dt
        yy += v_velocity * dt

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Title")
glutDisplayFunc(drw)
glutKeyboardFunc(KB)
glutIdleFunc(drw)
glutMainLoop()