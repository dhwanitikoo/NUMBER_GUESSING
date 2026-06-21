import math as m
import random as r
import time
print("*******************************************NUMBER GUESSING GAME*************************************")
print("You get 100 points to play with in starting , -5 for every hint which is given with every attempt of yours")
print("LEVELS :")
print("1.EASY")
print("2.MEDIUM")
print("3.HARD")
level=int(input("ENTER NUMBER ACCORDING TO THE LEVEL YOU WANT TO CHOOSE : "))

def easy_high():
    f=open("easy_high_score.txt","r")
    highsc=f.read()
    f.close()
    if(score>int(highsc)):
        f=open("easy_high_score.txt","w")
        print("********YOU SET THE NEW HIGH SCORE IN EASY LEVEL**********")
        f.write(str(score))
        f.close()
    
def med_high():
    f=open("med_high_score.txt","r")
    highsc=f.read()
    f.close()
    if(score>int(highsc)):
        f=open("med_high_score.txt","w")
        print("********YOU SET THE NEW HIGH SCORE IN MEDIUM LEVEL**********")
        f.write(str(score))
        f.close()
    
def hard_high():
    f=open("hard_high_score.txt","r")
    highsc=f.read()
    f.close()
    if(score>int(highsc)):
        f=open("hard_high_score.txt","w")
        print("********YOU SET THE NEW HIGH SCORE IN HARD LEVEL**********")
        f.write(str(score))
        f.close()
    
def easy():
    global score
    score=100
    count=0
    choice='Y'
    random_num=r.randint(0,10)
    print("ENTER A NUMBER BETWEEN 1 to 10")
    start_time = time.time()
    while(choice=='Y'or choice=='y'):
        guess=int(input("ENTER YOUR GUESS : "))
        if (guess==random_num):
            print("*********HURRAY YOU WON***********")
            print("NUMBER OF ATTEMPTS TAKEN : ",count)
            print("YOUR SCORE : ",score)
            easy_high()
            choice=input("ENTER YOU CHOICE Y/N")
            random_num=r.randint(0,10)
            count=0
            score=100
        elif(guess>random_num):
            print("LOWER NUMBER PLEASE")
            count+=1
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")
        elif(guess<random_num):
            print("HIGHER NUMBER PLEASE")
            count+=1
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")
        
        
        
def medium():
    global score
    score=100
    count=0
    choice='Y'
    random_num=r.randint(0,50)
    print("ENTER A NUMBER BETWEEN 1 to 50")
    start_time = time.time()
    while(choice=='Y'or choice=='y'):
        guess=int(input("ENTER YOUR GUESS : "))
        if (guess==random_num):
            print("*********HURRAY YOU WON******")
            print("NUMBER OF ATTEMPTS TAKEN : ",count)
            print("YOUR SCORE : ",score)
            med_high()
            choice=input("ENTER YOU CHOICE Y/N")
            random_num=r.randint(0,50)
            count=0
            score=100
        elif(guess>random_num):
            print("LOWER NUMBER PLEASE")
            count+=1
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")
        elif(guess<random_num):
            count+=1
            print("HIGHER NUMBER PLEASE")
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")
        
        
def hard():
    global score
    score=100
    count=0
    choice='Y'
    random_num=r.randint(0,100)
    print("ENTER A NUMBER BETWEEN 1 to 100")
    start_time = time.time()
    while(choice=='Y'or choice=='y'):
        guess=int(input("ENTER YOUR GUESS : "))
        if (guess==random_num):
            print("*********HURRAY YOU WON******")
            print("NUMBER OF ATTEMPTS TAKEN : ",count)
            print("YOUR SCORE : ",score)
            hard_high()
            choice=input("ENTER YOU CHOICE Y/N")
            random_num=r.randint(0,100)
            count=0
            score=100
        elif(guess>random_num):
            print("LOWER NUMBER PLEASE")
            count+=1
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")
        elif(guess<random_num):
            print("HIGHER NUMBER PLEASE")
            count+=1
            score-=5
            endtime = time.time() - start_time
            if (endtime - start_time) > 10:
                print("Too slow! You took more than 10 seconds.")

        
        

if level==1:
    easy()
elif level==2:
    medium()
elif level==3:
    hard()
else:
    print("invalid choice")