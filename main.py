#Indroduce the game and it's rules
print("Welcome to the multiplication game. You will have three seconds to answer the multiplication question or you FAIL!")

user_answer=input("Are you ready to start, please enter yes or no: ")
print(user_answer)
score=-1
if(user_answer=="yes"):
  print("Ok then good luck")
  import time
  for y in range(3,0,-1):
    print(y)
    time.sleep(1)
  import random
  
  
  '''
  cpt_number1=random.randint(0,12)
  cpt_number2=random.randint(0,12)
  correct_answer= cpt_number1 * cpt_number2
 # print("Computer number 1 is: " + str(cpt_number1))
  #print("Computer number 2 is: " + str(cpt_number2))
  #print("The right answer is: " + str(correct_answer))
  start_time=time.time()
  user_answer=int(input("What is the answer " + str(cpt_number1) + "*" + str(cpt_number2) + ": "))
  finish_time=time.time()
  return_time=finish_time-start_time
  print("You answered " + str(user_answer) + " and you took " + str(return_time) + " seconds.")
  '''
  
  correct_answer=1
  user_answer=1

  while(user_answer == correct_answer):
    cpt_number1=random.randint(0,12)
    cpt_number2=random.randint(0,12)
    correct_answer= cpt_number1 * cpt_number2
    #print("Computer number 1 is: " + str(cpt_number1))
    # print("Computer number 2 is: " + str(cpt_number2))
    # print("The right answer is: " + str(correct_answer))
    start_time=time.time()
    user_answer=int(input("What is the answer " + str(cpt_number1) + "*" + str(cpt_number2) + ": "))
    finish_time=time.time()
    return_time=finish_time-start_time
    print("You answered " + str(user_answer) + " and you took " + str(return_time) + " seconds.")
    score+=1
  else:
    print("Sorry incorrect answer the game is over, and your score is: " + str(score)) 
else:
  print("Sorry thanks for trying")
  

  