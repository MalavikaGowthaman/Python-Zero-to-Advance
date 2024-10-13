class AtmMachine:
    # constructor for self call (its a special function)
    
    def __init__(self): # self will denote the AtmMachine
        # data part
        self.pin =""
        self.balance = 0
        self.menu()
        
    
    def menu(self):
        user_input = input(
        """
        Hi... How can I help you?
        
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Press Anything to Exit
        """
        )
        
        if user_input == "1":
            # create pin
            self.create_pin()
            
        elif user_input == "2":
            # change pin
            self.change_pin()
        elif user_input == "3":
            # check balance
            self.check_balance()
        elif user_input == "4":
            #withdraw 
            pass
        else:
            exit()
            
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin
        
        user_balance = int(input("Enter balance: "))
        self.balance = user_balance
        
        print("Pin created sucessfully!")
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin changed successfully!")
            self.menu()
        else:
            print("Invalid Pin!")
            self.menu()
            
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}")

        else:
            print("Your pin is incorrect, please try again")
        self.menu()

    
    def withdraw_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            #allow to withdraw
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"You have withdrawn {amount}. Your new balance is {self.balance}")
            
            else:
                print("Insufficient balance!")
                
        else:
            print("Your pin is incorrect, please try again")
        self.menu()

            
    
    