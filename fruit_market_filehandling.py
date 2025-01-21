from user_define_fruit_file_handling import fruit_market
def role():
  print(""" WELCOME TO FRUIT MARKET
          
          1.Manager
          2.Customer
      """)

def manager():
    print(""" FRUIT MARKET MANAGER
          
          1.Add Fruit Stock
          2.View Fruit Stock
          3.Update Fruit Stock
         """)
def customer():
      print(""" CUSTOMER FRUIT ORDER
                 
            1.add cart and bill
            2.exit

            """)
fruit={}  
status=True
while status:
    role()
    user=int(input("enter your choice:"))
#============================================== manager =================================
    if user==1:
        goto=True
        while goto:
            manager()
            manager_choice=int(input("enter tha choice:"))
#=========================================add fruit=======================================            
            if manager_choice==1:
                name=input("enter the fruit:")
                qty=int(input("enter the quantity(1kg):"))
                price=int(input("enter the price:"))
                fruit_qyt_price={}

                fruit_qyt_price['qty']=qty
                fruit_qyt_price['price']=price

                fruit[name]=fruit_qyt_price
                fruit_market(f"who is using:manager \n fruit:{name} \n qty:{qty}kg \n price:{price}")
                print(fruit)

                choice_for_fruit=input("do you like to add,view and update fruit yes for y no for n:")
                if choice_for_fruit=='n':
                    goto=False
#=====================================view fruit============================
            elif manager_choice==2:
                print("fruit | qty | price")
                for k,v in fruit.items():
                    print(f"{k} | {v['qty']} | {v['price']}")
                    fruit_market("manager view the stock")
                print(fruit)

                choice_for_fruit=input("do you like to add,view and update fruit yes for y no for n:")
                if choice_for_fruit=='n':
                    goto=False
#======================================update fruit=============================
            elif manager_choice==3: 
                name=input("enter the name update:")
                if name in fruit:
                    qty=int(input("enter the update quantity:"))
                    price=int(input("enter the update price: "))
                    fruit[name]['qty']=qty
                    fruit[name]['price']=price
                    print(fruit)
                    fruit_market(f"who is using:manager \n fruit:{name} \n qty:{qty}kg \n price:{price}")
                    fruit_market("new update value")
                else:
                    print(f"{name} not in stock")
                    choice_for_fruit=input("do you like to add,view and update fruit yes for y no for n:")
                    if choice_for_fruit=='n':
                      goto=False
#========================================end manager=========================================

#====================================customer=======================================
    elif user==2:
            print("welcome to customer")
            customer()
            customer_choice=int(input("enter the choice:"))
            dict={}
            l1=[]
            if customer_choice==1:
                        stat=True
                        while stat:
                             print("===========add cart and bill==========")
                             name=input("enter the fruit name:")
                             if name in fruit:
                                qty=int(input("enter the quantity:"))
                                total=qty * fruit[name]['price']
                                key={}
                                l1.append(total)
                                key['qty']=qty
                                key['price']=total
                                dict[name]=key
                                print(dict)
                                for k,v in dict.items():
                                    print("==== total cart =====")
                                    print(f"{k} | {v['qty']} | {v['price']}")
                                print("total bill:-",sum(l1))
                                fruit_market(f"who is using:customer \n fruit:{name} \n qty:{qty}kg \n price:{price}")
                                fruit_market(f"who is using:add bill in cart {sum(l1)}")
                                
                             else:
                                print("not in stock")
                                fruit_market(f"who is using:customer \n not in stock")


                             choice_for_fruit=input("do you like to purchase fruit yes for y no for n:")
                             if choice_for_fruit=='n':
                               stat=False
    elif customer_choice==2:
        print("thank you for visiting")
        fruit_market("exit")

    
        


            
            

