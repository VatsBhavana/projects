from tkinter import *
import random

desktop=Tk()
desktop.geometry("500x500")
desktop.title("Stone Paper Scissor Game")

user_selction_tk=StringVar()
computer_selection_tk=StringVar()
result_tk=StringVar()

user_selction_tk.set("")
computer_selection_tk.set("")
result_tk.set("")

user_score_tk=IntVar()
computer_score_tk=IntVar()

user_score_tk.set(0)
computer_score_tk.set(0)

user_score=0
computer_score=0

l1=["Rock","Paper","Scissor"]

def game(user_choice):
    global user_score,computer_score
    user_selction_tk.set(user_choice)
    computer_choice=random.choice(l1)
    computer_selection_tk.set(computer_choice)

    if computer_choice==user_choice:
        result_tk.set("its tie")
    elif user_choice=="Rock" and computer_choice=="Scissor" or user_choice=="Paper" and computer_choice=="Rock" or user_choice=="Scissor" and computer_choice=="Paper":
        user_score+=1
        user_score_tk.set(user_score)
        result_tk.set("user win")
    elif computer_choice=="Rock" and user_choice=="Scissor" or computer_choice=="Paper"and user_choice=="Rock"or computer_choice=="Scissor"and user_choice=="Paper":
        computer_score+=1
        computer_score_tk.set(computer_score)
        result_tk.set("computer win")
    
            

    


#==============================create button=============================
btn1=Button(desktop,text="Rock",font=("times of roman",20,"bold"),command=lambda:game("Rock"))
btn1.place(x=10,y=20)

btn1=Button(desktop,text="Paper",font=("times of roman",20,"bold"),command=lambda:game("Paper"))
btn1.place(x=120,y=20)

btn1=Button(desktop,text="Scissor",font=("times of roman",20,"bold"),command=lambda:game("Scissor"))
btn1.place(x=240,y=20)
#==============================end button=============================
#============================user==================================
user=Label(desktop,text="USER:",font=("times of roman",20,"bold"))
user.place(x=20,y=150)

btn1=Button(desktop,textvariable=user_selction_tk,font=("times of roman",20,"bold"))
btn1.place(x=250,y=150)

btn1=Button(desktop,textvariable=user_score_tk,font=("times of roman",20,"bold"))
btn1.place(x=450,y=150)
#==============================end user=============================
#=============================computer===================================
comp=Label(desktop,text="COMPUTER:",font=("times of roman",20,"bold"))
comp.place(x=20,y=250)

btn1=Button(desktop,textvariable=computer_selection_tk,font=("times of roman",20,"bold"))
btn1.place(x=250,y=250)

btn1=Button(desktop,textvariable=computer_score_tk,font=("times of roman",20,"bold"))
btn1.place(x=450,y=250)

#==============================end computer=================================

labl=Entry(desktop,textvariable=result_tk,font=("times of roman",20,"bold"))
labl.place(x=200,y=350)


desktop.mainloop()