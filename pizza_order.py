total_soft_drink=0
total_bruchetta =0
total_brownie=0
total_order=[]
total_of_pizza=[]
total_of_pasta=[]
class pizza:

     print("1 large pizza=10.99 AUD \n""2 large pizza=20.99 AUD \n""3 large pizza=29.99 AUD")
     print("=====================================================")
     print("byu 4 and more pizza get 1.5lt of soft drink free \n")
     pizza=10.99

    #  def _init_(self):
         #self.total_pizza=0
        #  self.total_pizza_cost=0
         
#============================================calculation for pasta======================================
     def calculate(self):
         global total_soft_drink
         global total_order
         global total_of_pizza
         self.total_pizza=int(input("enter the number of pizza you want:"))
         self.total_pizza_cost=self.pizza * self.total_pizza
         total_order.append(self.total_pizza)
         total_of_pizza.append(self.total_pizza_cost)
         print(f"pizza cost= {self.total_pizza_cost}AUD")
     
         
         if self.total_pizza>=4:
             print("offer available:- congratulation!! 1.5L soft drink")
             total_soft_drink +=1
             
       
         
         
class pasta:
      print("1 large pasta=9.5 AUD \n""2 large pasta=17.00 AUD \n""3 large pasta=27.50 AUD")
      print("=====================================================")
      print("buy 4 or more pasta get 2 bruchetta free \n")

      pasta=9.5
      
#======================================= calculation for pasta and bruchetta========================
      def calculate1(self):
         global total_bruchetta
         global total_order
         global total_of_pasta
         self.total_pasta=int(input("enter the number of pasta you want:"))
         self.total_pasta_cost=self.pasta * self.total_pasta
         total_order.append(self.total_pasta)
         total_of_pasta.append(self.total_pasta_cost)
         print(f"pasta cost= {self.total_pasta_cost}AUD")
         
         if self.total_pasta>=4:
             print("offer available are:- congratulation!! 2 bruchetta ")
             total_bruchetta +=2
        

class menu(pizza,pasta):
    print("Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.")
    def _init_(self):
        pizza._init_(self)
        pasta._init_(self)
        self.total_price=0
        self.net_amount=0
        #self.total_order=0

    def calculation(self):
        global total_brownie
        global total_order

        self.calculate()  # From Pizza
        self.calculate1()  # From Pasta

        # Calculate total price
        self.total_price = self.total_pizza_cost + self.total_pasta_cost

 #===========================both pizza and pasta==============================
        if self.total_pizza>=4 and self.total_pasta>=4:
            print("offer available are:- congratulation!! 2 choco brownie ice cream")
            total_brownie +=2

            #total amount pizza and pasta
            self.net_amount =self.total_pizza_cost +self.total_pasta_cost
            
            
        
        

    def pizza_pasta_bill(self):
        global total_bruchetta
        global total_soft_drink
        global total_brownie
        print(f"payment receive from pizza:{sum(total_of_pizza)}")
        print(f"payment receive from pasta:{sum(total_of_pasta)}")
        print(f"payment receive today:{sum(total_of_pasta+total_of_pizza)}")
        print(f"number of pizza and pasta sold in one shift:{sum(total_order)}")
        print(f"number of 1.5l soft drink bottle given:{total_soft_drink}")
        print(f"number of bruschetta given to customer:{total_bruchetta}")
        print(f"number of choco brownie ice cream given to customer:{total_brownie}")

    def asking_order(self):
        status=True
        while status:
            choice=int(input("enter your choice::press 1:order menu and press 2:exit:-"))
            if choice==2:
                print("thank you")
                break
            elif choice==1:
                customer_name=input("enter your name:")
                print(f"welcome,{customer_name}")
                self.calculation()

                while status:
                   customer_choice=input("Do you want to enter order from another customer yes for y and no for n:")
                   if customer_choice=='n':
                      self.pizza_pasta_bill()
                      print("thank you for visiting my shop")
                      return
                   elif customer_choice == 'y':
                       break
          
m=menu()
m.asking_order()


#this is multiple inheritance