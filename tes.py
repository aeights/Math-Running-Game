import random
angka1 = random.randint(1,10)
angka2 = random.randint(1,10)
answer = 0

question1 = angka1 + angka2
answer+=question1

choice1 = angka1+angka1

rand_choice = [choice1,answer]
rand_idx = random.randint(0,1)

print(rand_choice[rand_idx])
rand_choice.pop(rand_idx)
print(rand_choice[0])
print('index ke',rand_idx)
print('index 0',choice1)
print('index 1',answer)
# print(rand_idx)

number1 = 0
number2 = 0
state_quest = False
wrong_answer = number1+number1
correct_answer = number1+number2
choices = [wrong_answer,correct_answer]
rand_idx = random.randint(0,1)
choice1 = choices[rand_idx]
choices.pop(rand_idx)
choice2 = choices[0]

# def character():
#     global x_pos_char,y_pos_char,x_pos_object,y_pos_object,collision
#     glPushMatrix()
#     glTranslated(x_pos_char,y_pos_char,0)
#     if x_pos_char == x_pos_object and y_pos_object-1<=y_pos_char<=y_pos_object:
#         print("terkena ndase",collision)
#         collision+=1
#     # print('x character:',x_pos_char,'y character:',y_pos_char)
#     # print('x object:',x_pos_object,'y object:',y_pos_object)
#     glBegin(GL_POLYGON)
#     glColor3ub(60, 170, 205)
#     glVertex2d(xmin_char,ymax_char)
#     glVertex2d(xmin_char,ymin_char)
#     glVertex2d(xmax_char,ymin_char)
#     glVertex2d(xmax_char,ymax_char)
#     glEnd()
#     glPopMatrix()

# def rintangan():
#     global x_pos_object,y_pos_object,number1,number2
#     glPushMatrix()
#     glTranslated(x_pos_object,y_pos_object,0)
#     x_pos_object -= 0.5
#     if -280 <= x_pos_object <= -270:
#         x_pos_object = 230
#         refresh_quest()
#     glBegin(GL_POLYGON)
#     glColor3ub(60, 170, 205)
#     glVertex2d(xmin_object,ymax_object)
#     glVertex2d(xmin_object,ymin_object)
#     glVertex2d(xmax_object,ymin_object)
#     glVertex2d(xmax_object,ymax_object)
#     glEnd()
#     glPopMatrix()