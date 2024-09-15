# create menu

menu ={
    "Idly":20,
    "Dosa":30,
    "Pongal":60,
    "Poori":100,
    "Coffee":10,
    "Tea":12
}

print("""
      Welcome to Tasty Mess....
      
      Here you have out Menu
      
      Idly  = 20
      Dosa = 30
      Pongal = 60
      Poori = 100
      Coffee = 10
      Tea = 12
    
      """)
tot_price =0 

item1 = input("Enter the food you want to order: ").capitalize()

if item1 in menu:
  tot_price += menu[item1]
  # print(tot_price)

  print(f"You ordered {item1}. Your total bill amount is {tot_price}")
else:
  print(f"Invalid order {item1} is not there in our menu. Please order a food which is there in the Menu.")
  
another_order =  input("Do you want anythings else:(yes)/(no)").lower()

if another_order == 'yes':
  item2 = input("Enter the food you want to order: ").capitalize()

if item2 in menu:
  tot_price += menu[item2]
  # print(tot_price)

  print(f"You ordered {item2}. Your total bill amount is {tot_price}")
else:
  print(f"Invalid order {item2} is not there in our menu. Please order a food which is there in the Menu.")

  
print(f"Your total bill amount is {tot_price}")     