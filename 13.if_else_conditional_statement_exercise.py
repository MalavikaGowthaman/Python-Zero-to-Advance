
"""Exercise 2

From 3 numbers find the Minimum number

Get 3 input from user and find the minimum number"""

# get input from the user

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1<num2 and num1<num3:
    print("The Minimum number is: ", num1)
    
elif num2<num1 and num2<num3:
    print("The Minimum number is: ", num2)
    
else:
    print("The Minimum number is: ",num3)



"""Exercise - 3

ATM Menu

1. Choose your Language 
2. Account type
3. Pin change
4. Balance check
5. Withdraw Money
6. Deposit
7. Exit

"""


Menu = int(input("""
            Welcome To ATM....
            1. Enter 1 to Choose your Language 
            2. Enter 2 for Selecting Account Type
            3. Enter 3 for Pin Change
            4. Enter 4 for Balance Check
            5. Enter 5 for Withdraw Money
            6. Enter 6 for Deposit
            7. Enter 7 for Exit
            
            Thank you for using....
            """))


if Menu == 1:
    lang_choosen = int(input("Choose Your Language (1 for English and 2 for Tamil): "))
    if lang_choosen == 1:
        print("English")
    else:
        print("Tamil")
        
elif Menu ==2:
    acc_type = int(input("Choose 1 for Savings account and 2 for Current account: "))
    if acc_type == 1:
        print("Saving account")
    else:
        print("Current account")
    
elif Menu ==3:
    print("pin change")
elif Menu == 4:
    print('Balance Check')
elif Menu == 5:
    print('withdraw money')
elif Menu == 6:
    print('Money Deposit')
elif Menu ==7:
    print("Press Exit")
else: 
    print('Thank you are using ATM ')
        
       

"""Exercise - 4

Calculator 

Get two input from user if they press + perform add, - perform sub, * perform Mul, / perform division"""

# get input from user

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
operator = input("Enter the Arithmetic operator sign: ")


if operator == '+':
    print("The addition of two number is: ", number1+number2)
    
elif operator == '-':
    print("The subraction of two number is: ", number1-number2)

elif operator == '*':
    print("The Multiplication of two number is: ", number1*number2)

else: 
    print("The division of two number is: ", number1/number2)
   

    
    
    


