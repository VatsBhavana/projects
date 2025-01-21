#game computer to user 


import random

total_score=0
level1=True
while level1:
    computer_guess=random.randint(1,50)
    for i in range(1,11):
        user_guess=int(input("enter the number:"))
        points=10  #user add points
        if computer_guess==user_guess:
            total_score +=points
            print("you win level1.....")
            print("number genrate by compter is",computer_guess)
            print("your total score",total_score) #if you win then 2nd level
            break
        elif i==10 and computer_guess!=user_guess:
             print("you are out...you will try next time")
             print("computer gerate the number:",computer_guess)
             exit()
        else:
            if user_guess>computer_guess:
                print("hint:guess lower number")
            elif user_guess<computer_guess:
                print("hint:guess upper number")
    level1=False #level1 is stop


    print("start the 2nd level..........................")

    level2=True
    while level2:
        computer_guess=random.randint(1,100)
        for i in range(1,11):
            user_guess=int(input("enter the number:"))
            points=10
            if computer_guess==user_guess:
                total_score +=points
                print("you win level2.....")
                print("number genrate by compter is",computer_guess)
                print("your total score",total_score)
                break
            elif i==10 and computer_guess!=user_guess:
                print("you are out...you will try next time")
                print("computer gerate the number:",computer_guess)
                exit()
            else:
                if user_guess>computer_guess:
                    print("hint:guess lower number")
                elif user_guess<computer_guess:
                    print("hint:guess upper number")
        level2=False #levele2 is stop

        print("start the 3rd level............................")

        level3=True
        while level3:
            computer_guess=random.randint(1,150)
            for i in range(1,11):
                user_guess=int(input("enter the number:"))
                points=10
                if computer_guess==user_guess:
                    total_score +=points
                    print("you win level3.....")
                    print("number genrate by compter is",computer_guess)
                    print("your total score",total_score)
                    break
                elif i==10 and computer_guess!=user_guess:
                    print("you are out...you will try next time")
                    print("computer gerate the number:",computer_guess)
                    exit()
                else:
                    if user_guess>computer_guess:
                        print("hint:guess lower number")
                    elif user_guess<computer_guess:
                        print("hint:guess upper number")
            level3=False #level3 is stop

            print("start the 4th level.................................")

            level4=True
            while level4:
                computer_guess=random.randint(1,200)
                for i in range(1,11):
                    user_guess=int(input("enter the number:"))
                    points=10
                    if computer_guess==user_guess:
                        total_score +=points
                        print("you win level4.....")
                        print("number genrate by compter is",computer_guess)
                        print("your total score",total_score)
                        break
                    elif i==10 and computer_guess!=user_guess:
                        print("you are out...you will try next time")
                        print("computer gerate the number:",computer_guess)
                        exit()
                    else:
                        if user_guess>computer_guess:
                            print("hint:guess lower number")
                        elif user_guess<computer_guess:
                            print("hint:guess upper number")
                level4=False #level4 is stop

                print("start the 5th level.............................")

                level5=True
                while level5:
                    computer_guess=random.randint(1,100)
                    for i in range(1,11):
                        user_guess=int(input("enter the number:"))
                        points=10
                        if computer_guess==user_guess:
                            total_score +=points
                            print("you win level5.....")
                            print("number genrate by compter is",computer_guess)
                            print("your total score",total_score)
                            print("Congratulations, You have won all the level :) ")
                            break
                        elif i==10 and computer_guess!=user_guess:
                            print("you are out...you will try next time")
                            print("computer gerate the number:",computer_guess)
                            exit()
                        else:
                            if user_guess>computer_guess:
                                print("hint:guess lower number")
                            elif user_guess<computer_guess:
                                print("hint:guess upper number")
                    level5=False #levele5 is stop
                    print("are you king/queen of the game")



