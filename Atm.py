# code for cLASS
class Atm:
    # constructor
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input("""
        hi how can i help you?
        1. press 1 to create pin
        2. press 2 to chenge pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. Anything else to exit
        """)
        if user_input=='1':
            # create pin
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
            # change pin
        elif user_input=='3':
            self.check_balance()
            # check balance
        elif user_input=='4':
            self.withdraw()
            # withdrawl
        else:
            exit()
    def create_pin(self):
        user_pin=input('enter the pin')
        self.pin=user_pin
        user_balance=int(input('enter balance'))
        self.balance=user_balance
        print('pin creating sucessfully')
        self.menu()
    def change_pin(self):
        old_pin=input('enter the old pin')
        if old_pin==self.pin:
            #let him change pin
            new_pin=input('enter new pin')
            self.pin=new_pin
            print('pin change successfully')
            self.menu()
        else:
            print('ni krne  de skta baba')
            self.menu()
    def check_balance(self):
        user_pin=input('ente your pin')
        if user_pin==self.pin:
            print('your balance is', self.balance)
        else:
            print('sir your pin is wrong')
            self.menu()
    def withdraw(self):
        user_pin=input('enter the pin')
        if user_pin==self.pin:
            # allow to withdral
            amount=int(input('enter the amount'))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print('with secessfull balance is',self.balance)
                self.menu()
            else:
                print('you are thief')
        else:
            print('you  have no amount')
        self.menu()
