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