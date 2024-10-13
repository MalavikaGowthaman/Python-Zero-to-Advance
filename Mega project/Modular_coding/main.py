# this code is for modular coding concept 
# 
from Modular_coding.atm_machine import AtmMachine


atm = AtmMachine()
if __name__ == "__main__":
    atm.create_pin()
    atm.check_balance()