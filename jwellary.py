
"""
TASK 3 : mini project : 

KALYAN JWELLERS : 

M 
>  65
purchase > 2lk - 3lk    20% 
purchase > 3lk - 5lk 	30% 
purchase > 5lk  	35% 


<65
purchase > 2lk - 3lk    10% 
purchase > 3lk - 5lk 	20% 
purchase > 5lk  	25% 



F
>  65
purchase > 2lk - 3lk    25% 
purchase > 3lk - 5lk 	35% 
purchase > 5lk  	40% 


<65
purchase > 2lk - 3lk    15% 
purchase > 3lk - 5lk 	25% 
purchase > 5lk  	30% 


------------------------------------------------------------
Enter your name : 
Enter gender : 
Enter age : 

Enter product : Ring 
Enter product gram : 20  
current gold price (1 grm) : 5752

-------------------------------------
TOTAL GOLD RATE :  XXXXX 

"""

print("...............Welcome To The Kalyan Jwellers................")

total_gold_amount=0
name=input("Enter The Name:")
gender=input("Enter The Gender:")
age=int(input("Enter The Age:"))
print("-"*40)

product=input("Enter The product:")
print("Product 1 Gram price:7543")
print("Making Charges of 1 gram:700")
gram=int(input("how much gram you want purchase:"))

print("-"*40)

gram1=7543
making_charges=700

make_charge_on_gram=making_charges* gram
purchase_gram = gram1* gram
purchase = make_charge_on_gram + purchase_gram
print("purchase:",purchase)
print(purchase)
print("-"*40)

if age >65 :
    if gender=="male":
      if purchase >200000 and purchase<=300000 :
         print("apply 20% discount")
         dis = 20
         discount=(purchase*dis)//100
         print("discount prioce:",discount)
         total_gold_amount=purchase-discount
         print("total gold amount:",total_gold_amount)

      elif purchase>300000 and purchase<=500000 :
         print("apply 30% discount")
         dis=30
         discount=(purchase*dis)/100
         print("discount price",discount)
         total_gold_amount=purchase-discount
         print("total gold amount:",total_gold_amount)

      elif purchase>500000:
         print("apply 35% discount")
         dis=35
         discount=(purchase*dis)//100
         print("discount price:",discount)
         total_gold_amount=purchase-discount
         print("total gold amount:",total_gold_amount)
      else:
         dis = 0
         discount = 0
         total_gold_amount = purchase
      
else:
   if age<65:
      if gender=="male":
         if purchase >200000 and purchase<=300000:
            print("apply 10% discount")
            dis=10
            discount=(purchase*dis)//100
            print("discount price",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)

         elif purchase >300000 and purchase<=500000:
            print("apply 20% discount")
            dis=20
            discount=(purchase*dis)//100
            print("discount price",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)

         elif purchase>500000:
            print("apply 25% discount")
            dis=25
            discount=(purchase*dis)//100
            print("discount price",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)
         else:
            dis = 0
            discount = 0
            total_gold_amount = purchase

if age>65:
 if gender=="female":
    if purchase>200000 and purchase<=300000:
      dis=25
      print("apply 25% discount ")
      discount=(purchase*dis)//100
      print("discount price:",discount)
      total_gold_amount=purchase-discount
      print("total gold amount:",total_gold_amount)

    elif purchase>300000 and purchase<=500000:
      print("apply 35% discount ")
      dis=35
      discount=(purchase*dis)//100
      print("discount price:",discount)
      total_gold_amount=purchase-discount
      print("total gold amount:",total_gold_amount)

    elif purchase>500000:
      print("apply 40% discount")
      dis=40
      discount=(purchase*dis)//100
      print("discount price:",discount)
      total_gold_amount=purchase-discount
      print("total gold amount:",total_gold_amount)
    else:
         dis = 0
         discount = 0
         total_gold_amount = purchase  

else:
   if age<65:
      if gender=="female":
         if purchase>200000 and purchase<=300000:
            print("apply 15% discount ")
            dis=15
            discount=(purchase*dis)//100
            print("discount price:",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)

         elif purchase>200000 and purchase<=300000:
            print("apply 25% discount ")
            dis=25
            discount=(purchase*dis)//100
            print("discount price:",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)

         elif purchase>200000 and purchase<=300000:
            print("apply 30% discount ")
            dis=30
            discount=(purchase*dis)//100
            print("discount price:",discount)
            total_gold_amount=purchase-discount
            print("total gold amount:",total_gold_amount)
         else:
            dis = 0
            discount = 0
            total_gold_amount = purchase

print("-"*40)

print("total gold amount:",total_gold_amount)
print("total making charges 1 gram:",make_charge_on_gram)
print("total amount:",purchase)

print("-"*40)

print(f"discount :{dis}%")
print(f"discount amount:{discount}")
print(f"TOTAL NET AMOUNT: {total_gold_amount}")
    






