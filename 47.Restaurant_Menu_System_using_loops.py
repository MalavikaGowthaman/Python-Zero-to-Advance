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

while True:

    item = input("Enter the food you want to order: ").capitalize()

    if item in menu:
        tot_price += menu[item]
    # print(tot_price)
        print(f"{item} ordered. Bill so far: {tot_price}")
    else:
        print(f"Invalid order {item} is not there in our menu. Please order a food which is there in the Menu.")
    
    another_order =  input("Do you want anythings else:(yes)/(no)").lower()

    if another_order == 'no':
        break

  
print(f"Your total bill amount is {tot_price}")     
