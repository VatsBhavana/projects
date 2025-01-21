"""
player 1:
player 2:


press 1 for play game and press '2' for exit

1
shuffle tickets
(1-100 randomly 12 tickets genrate)

ticket genrated

23 88 66 54 72 45 81 65 35 5 7 2

player1:66 54 72 81 65 23
player2:88 45 5  7  2  35 

enter(input())
lucky number is :88

enter

player1 66 54 72 81 65 23
player2 45 5  7  2  35

enter (input())
lucky number is :72

player1 66 54 81 65 23
player2 45 5  7  2  35
"""
"""

use to this method:-
#suppose single element add krne he toh append method ka use krte he

l2=[1,2,3,4]
l2.append([5,6,7,8])
print(l2)

#suppose koi element remove krna he toh remove method use krte he

l1=[1,2,3,4,5] #ticket_genrate
l1.remove(3) #list me se number remove krne he player1 ya  player2 me se number delete krna he toh
print(l1)



"""





import random 
 

print("\nWelcome to the Housie Game!")
print("Press 1 to play the game or 2 to exit")

choice = int(input("Enter your choice: "))
if choice != 1:
    print("Exit the game.")
else:

     
        player1 = []  # Initialize empty list for player1 tickets
        player2 = []  # Initialize empty list for player2 tickets
       
        ticket = []
    # Generate 12 random tickets and assign the first 6 to player1, last 6 to player2
        count=0
        while count!=12: #this condition ieterate 12 times
            gen_ticket = random.randint(1, 100) #randomly genrate
            if gen_ticket not in ticket: #suppose genrate number is present in ticket then do this conditon tiwill not append the same element
                ticket.append(gen_ticket)
                count+=1

        #list slicing
        player1 = ticket[:6]  # First 6 tickets for player1
        player2 = ticket[6:]
        
        print("tickets:",ticket)
        print()
        print("Player 1 tickets:", player1)
        print("Player 2 tickets:", player2)
       
        while ticket!=[]:
            input("Enter ...")
            lucky_number = random.choice(ticket)
            print("Lucky number is:", lucky_number)

    
            if lucky_number in player1: 
                player1.remove(lucky_number)# remove lucky number in player1 list
            if lucky_number in player2:
                player2.remove(lucky_number)# remove lucky number in player2 list

            ticket.remove(lucky_number)

            print("Player 1 tickets:", player1)
            print("Player 2 tickets:", player2)
            
            if  player1 ==[]:
                print("Player 1 wins the game!")
                break
            if player2 == []:
                print("player 2 win the game!")
                break

choice =input("do you want to play again press 'y' for yes and press 'n' for no:")  
if choice=='n' and choice=='no':
        status =False   
        





































































































