#import library
import random
import OpenGL.GLUT as glut
# from Truck import truk
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

play = False
y_rintangan = 50 # digunakan untuk pergerakan rintangan ke bawah
tr = 500
cek_lev = 1

# PLAYER 1
x_player1 = 120
y_player1 = 0
grid_player1 = [100,300,0,500]
# Logika player 1
y = 500
kecepatan = 10
cek_point = 30
cek_y = 50
cek_kecepatan = 5000
#collison
crash_wal_player1 = False # True ketika menabrak
# score
score_player1 = 0
fix_score_player1 = 0
# rintangan
x_r_player1 = random.randrange(150,250,10)
tingkatan1 = 1 # for level counting

# PLAYER 2
x_player2 = 420
y_player2 = 0
grid_player2 = [400,600,0,500]
# Logika player 2
y2 = 500
kecepatan2 = 10
cek_point2 = 30
cek_y2 = 50
cek_kecepatan2 = 5000
#collison
crash_wal_player2 = False
# score
score_player2 = 0 # for score counting
fix_score_player2 = 0
x_r_player2 = random.randrange(450,550,10)
tingkatan2 = 1 # for level counting

#draw text
def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()
       
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

# Rintangan
def rintangan(x):
    glPushMatrix()
    # glTranslate(0,y_rintangan,0)
    glPointSize(30)
    glBegin(GL_POINTS)
    glColor3ub(37, 188, 143) 
    glVertex2f(x, 450+y_rintangan) # Plyaer1 =x[150, 200, 250]
    glEnd()
    glPopMatrix()
    
# Kendaraan

def tamiya(x,y):
    glColor3ub(150, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(8+x, 38+y)
    glVertex2f(6+x, 38+y)
    glVertex2f(8+x, 40+y)
    glVertex2f(10+x, 42+y)
    glVertex2f(20+x, 42+y)
    glVertex2f(22+x, 40+y)
    glVertex2f(24+x, 38+y)
    glVertex2f(22+x, 38+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(8+x, 38+y)
    glVertex2f(22+x, 38+y)
    glVertex2f(20+x, 36+y)
    glVertex2f(10+x, 36+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 36+y)
    glVertex2f(20+x, 36+y)
    glVertex2f(20+x, 30+y)
    glVertex2f(10+x, 30+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 30+y)
    glVertex2f(10+x, 30+y)
    glVertex2f(10+x, 20+y)
    glVertex2f(20+x, 20+y)
    glEnd()

    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 20+y)
    glVertex2f(24+x, 16+y)
    glVertex2f(24+x, 10+y)
    glVertex2f(22+x, 10+y)
    glVertex2f(22+x, 16+y)
    glVertex2f(20+x, 18+y)
    glEnd()

    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(6+x, 16+y)
    glVertex2f(6+x, 10+y)
    glVertex2f(8+x, 10+y)
    glVertex2f(8+x, 16+y)
    glVertex2f(10+x, 18+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(10+x, 18+y)
    glVertex2f(10+x, 12+y)
    glVertex2f(12+x, 14+y)
    glVertex2f(12+x, 18+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(12+x, 18+y)
    glVertex2f(18+x, 18+y)
    glVertex2f(20+x, 20+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 20+y)
    glVertex2f(20+x, 18+y)
    glVertex2f(20+x, 12+y)
    glVertex2f(18+x, 14+y)
    glVertex2f(18+x, 18+y)
    glEnd()

def truk(x,y):
    glPushMatrix()
    #BADAN
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(x, y)
    glVertex2f(x + 30, y + 0)
    glVertex2f(x + 30, y + 35)
    glVertex2f(x + 30-5, y + 50)
    glVertex2f(x + 5, y + 50)
    glVertex2f(x , y + 35)
    glVertex2f(x , y + 0)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3ub(0,0,0)
    glVertex2f(x , y + 5)
    glVertex2f(x + 15 , y + 10)
    glVertex2f(x + 30 , y + 5)
    glEnd()
    
    #belakang kaca
    glBegin(GL_QUADS)
    glColor3ub(16, 35, 110)
    glVertex2f(x + 5 , y + 15)
    glVertex2f(x + 25 , y + 15)
    glVertex2f(x + 25 , y + 30)
    glVertex2f(x + 5 , y + 30)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2f(x + 5 , y + 15)
    glVertex2f(x + 15 , y + 25)
    glVertex2f(x + 25 , y + 15)
    glEnd()
    
    # KACA
    glBegin(GL_POLYGON)
    glColor3ub(16, 35, 110)
    glVertex2f(x , y + 30)
    glVertex2f(x + 30 , y + 30)
    glVertex2f(x + 25 , y + 35)
    glVertex2f(x + 25 , y + 37)
    glVertex2f(x + 20 , y + 40)
    glVertex2f(x + 10 , y + 40)
    glVertex2f(x + 5 , y + 37)
    glVertex2f(x + 5, y + 35)
    glEnd()
    
    #lampu
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(238, 255, 0)
    glVertex2f(x + 7, y + 47)
    glEnd()
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(238, 255, 0)
    glVertex2f(x + 23 , y + 47)
    glEnd()
    
    glPopMatrix()

def mobil():
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(37, 188, 143)
    glVertex2f(x_player1 , y_player1      + 0)
    glVertex2f(x_player1 + 30 , y_player1 + 0)
    glVertex2f(x_player1 + 30 , y_player1 + 50)
    glVertex2f(x_player1 , y_player1      + 50)
    glEnd()
    glPopMatrix()
    
def mobil2():
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(37, 188, 143)
    glVertex2f(x_player2 , y_player2 + 0)
    glVertex2f(x_player2 + 30 , y_player2 + 0)
    glVertex2f(x_player2 + 30 , y_player2 + 50)
    glVertex2f(x_player2 , y_player2 + 50)
    glEnd()
    glPopMatrix()
    
# Membuat bentuk jalan
#JALAN RAYA
def jalan(jln):
    glPushMatrix()
    glBegin(GL_QUADS) 
    glColor3ub(0,0,0) #hitam
    glVertex2f(jln - 100, 500)
    glVertex2f(jln - 100, 0)
    glVertex2f(jln + 100, 0)
    glVertex2f(jln + 100, 500)
    glEnd()
    glPopMatrix()

def tepi(tp):
    glPushMatrix()
    glColor3ub(255, 255, 255) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(tp, 0) 
    glVertex2f(tp, 500)
    glEnd()
    glPopMatrix()

def kotak_coll(kcx):
    glPushMatrix()
    glColor3ub(14,15,20)
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(kcx, 0) 
    glVertex2f(kcx, 500)
    glEnd()
    glPopMatrix()

def garis_mid(gmx,gmy):
    glPushMatrix()
    glTranslated(0,y,0)
    glColor3ub(255, 255, 255) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(gmx, gmy) 
    glVertex2f(gmx, gmy+50)
    glEnd()
    glPopMatrix()

#Logik
def background(x):
    glPushMatrix()
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(100+x, 0) 
    glVertex2f(300+x, 0)
    glVertex2f(300+x, 500)
    glVertex2f(100+x, 500) 
    glEnd()
    glPopMatrix()

def key_player1(key,x,y):
    global x_player1, y_player1, crash_wal_player1, play, crash_wal_player2
    # Untuk mengubah posisi kotak
    if ord(key) == ord('w'):
        if y_player1+50 > 500:
            y_player1 += 0
        else:
            y_player1 += 0
    elif ord(key) == ord('s'):
        if y_player1-5 < 0:
            y_player1 -= 0
        else:
            y_player1 -= 0
    elif ord(key) == ord('d'):
        if crash_wal_player1 == False:
            if x_player1+50 > grid_player1[1]:
                x_player1 +=0
                crash_wal_player1 = True
            else:
                x_player1 += 10
        else:
            x_player1 +=0
    elif ord(key) == ord('a'):
        if crash_wal_player1 == False:
            if x_player1-20 < grid_player1[0]:
                x_player1 +=0
                crash_wal_player1 = True
            else:
                x_player1 -= 10
        else:
            x_player1 -= 0
    elif ord(key) == ord(b'\r'):
        play = False
        crash_wal_player1 = False
        crash_wal_player2 = False
        
def key_player2(key,x,y):
    global x_player2, y_player2, crash_wal_player2
    # Untuk mengubah posisi karakter
    if key == GLUT_KEY_UP:
        if y_player2+50 > 500:
            y_player2 += 0
        else:
            y_player2 += 0
    elif key == GLUT_KEY_DOWN:
        if y_player2-5 < 0:
            y_player2 -= 0
        else:
            y_player2 -= 0
    elif key == GLUT_KEY_RIGHT:
        if crash_wal_player2 == False:
            if x_player2+50 > grid_player2[1]:
                x_player2 +=0
                crash_wal_player2 = True
            else:
                x_player2 += 10
        else:
            x_player2 += 0
    elif key == GLUT_KEY_LEFT:
        if crash_wal_player2 == False:
            if x_player2-20 < grid_player2[0]:
                x_player2 +=0
                crash_wal_player2 = True
            else:
                x_player2 -= 10    
        else:
            x_player2-=0

def mouse_play_game(button, state, x, y):
    global play
    if button == GLUT_LEFT_BUTTON:
        if (x >= 280 and x <= 480) and (y >= 220 and y <=280):
            play = True

#play
def play_player1():
    jalan(200)
    tepi(100) #kiri
    tepi(300) #kanan
    kotak_coll(200) #ditengah
    gmy = 20 # y pertama dari garis mid
    for i in range(7): #garis mid dibentuk sebanyak 7 menggunakan perulangan for
        garis_mid(200,gmy)
        gmy += 70 #memberikan jarak setiap garis_mid
    # mobi
    truk(x_player1 , y_player1)
    drawText('SCORE 1: ',15,460,0,0,0) #player 1
    drawTextNum(score_player1,25,440,0,0,0) # player 1
    drawText('LEVEL : ',15,420,0,0,0)
    drawTextNum(tingkatan1,25,400,0,0,0)
        
def play_player2():
    jalan(500)
    tepi(400)
    tepi(600)
    kotak_coll(500)
    gmy = 20
    for i in range(7):
        garis_mid(500,gmy)
        gmy += 70
    tamiya(x_player2,y_player2)
    drawText('SCORE 2: ',640,460,0,0,0) #player 2
    drawTextNum(score_player2,650,440,0,0,0) # player 2
    drawText('LEVEL : ',640,420,0,0,0)
    drawTextNum(tingkatan2,650,400,0,0,0)

def play_game():
    if crash_wal_player1 == False:
        play_player1()
        rintangan(x_r_player1)
    else:
        background(0)
        drawText('YOUR FINAL SCORE: ',110,450,255,255,255) #player 1
        drawTextNum(fix_score_player1,180,430,255,255,255) # player 1
        drawText('HIGHEST LEVEL : ',110,400,255,255,255) #player 1
        drawTextNum(tingkatan1,270,400,255,255,255) # player 1
        
    if crash_wal_player2 == False:
        play_player2()
        rintangan(x_r_player2)
    else:
        background(300)
        drawText('YOUR FINAL SCORE: ',410,450,255,255,255) #player 2
        drawTextNum(fix_score_player2,480,430,255,255,255) # player 2
        drawText('HIGHEST LEVEL : ',410,400,255,255,255) #player 1
        drawTextNum(tingkatan2,570,400,255,255,255) # player 1
    
    if (crash_wal_player1 and crash_wal_player2)==True:
        bg_text(-40,0)
        drawTextBold("G A M E O V E R",260,255)
        drawText("Enter To Play",280,236,38, 33, 98)
        
def start_game():
    glPushMatrix()
    glColor3b(36, 150, 127)
    glBegin(GL_QUADS)
    glVertex2f(280, 220)
    glVertex2f(480, 220)
    glVertex2f(480, 280)
    glVertex2f(280, 280)
    glEnd()
    glColor3ub(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, 220)
    glVertex2f(480, 220)
    glVertex2f(480, 280)
    glVertex2f(280, 280)
    glEnd()
    glPopMatrix()
    drawTextBold("P L A Y G A M E",295,250)

#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    if play == False:
        start_game()
    else:
        play_game()
    glutSwapBuffers() #utk membersihkan layar, double buffering
    
def timer_rintangan(value):
    global y_rintangan, tr, x_r_player1, x_r_player2, cek_lev,crash_wal_player1,crash_wal_player2
    if play == True:
        y_rintangan -= 20
        if crash_wal_player1==False or crash_wal_player2 == False:
        # print(x_r_player1,x_player1) # 390 collison, x = 140
            if y_rintangan < -450:
                cek_lev += 1
                y_rintangan = 100
                x_r_player1 = random.randrange(150,250,10)
                x_r_player2 = random.randrange(450,550,10)
            if (cek_lev %2) == 0:
                tr-=100
            if tr <100:
                tr = 100 
            if (x_player1 in range(x_r_player1-50,x_r_player1+20))and(y_rintangan < -390):
                crash_wal_player1 = True
            if (x_player2 in range(x_r_player2-50,x_r_player2+20))and(y_rintangan < -390):
                crash_wal_player2 = True
            
    #timer rintangan awal = 500, berkurang hingga mencapai 100
    glutTimerFunc(tr,timer_rintangan,0)

def timer(value):
    global y, kecepatan, score_player1, cek_point, cek_y, cek_kecepatan, tingkatan1, fix_score_player1
    if play==True:
        if crash_wal_player1 == False:
            y -= kecepatan  
            if y < value :
                # 50 adalah tingkatan awal.... berkurang 5 hingga tingkatan akhir menjadi 20
                y = cek_y
            score_player1 += kecepatan 
            if score_player1 % cek_kecepatan == 0 :
                tingkatan1 += 1
                cek_y -= 5
                cek_point -= 5
                cek_kecepatan += 10000

            if cek_y < 20:
                cek_y = 20
                
            if cek_point < 10:
                cek_point = 10
        else:
            fix_score_player1 = score_player1
    #timer awal = 30, berkurang sebanyak 5 hingga mencapai 10
    glutTimerFunc(cek_point,timer,0)

def timer2(value):
    global y2, kecepatan2, score_player2, cek_point2, cek_y2, cek_kecepatan2, tingkatan2, fix_score_player2
    if play==True:
        if crash_wal_player2 == False:
            y2 -= kecepatan2  
            if y2 < value :
                # 50 adalah tingkatan awal.... berkurang 5 hingga tingkatan akhir menjadi 20
                y2 = cek_y2
            score_player2 += kecepatan2 
            if score_player2 % cek_kecepatan2 == 0 :
                tingkatan2 += 1
                cek_y2 -= 5
                cek_point2 -= 5
                cek_kecepatan2 += 10000

            if cek_y2 < 20:
                cek_y2 = 20
                
            if cek_point2 < 10:
                cek_point2 = 10
        else:
            fix_score_player2 = score_player2
    #timer awal = 30, berkurang sebanyak 5 hingga mencapai 10
    glutTimerFunc(cek_point2,timer2,0)

def init():
    glClearColor(2,1,0, 2.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def main ():   
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(600, 500) #utk mengatur ukuran window
    glutInitWindowPosition(100,100) #utk mengatur letak window
    glutCreateWindow("2D Car Racing Game") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    glutKeyboardFunc(key_player1)
    glutSpecialFunc(key_player2)
    glutMouseFunc(mouse_play_game)
    timer_rintangan(0)
    timer(0)
    timer2(0)
    init()
    glutMainLoop() #fungsi yang akan memulai keseluruhan program

main()