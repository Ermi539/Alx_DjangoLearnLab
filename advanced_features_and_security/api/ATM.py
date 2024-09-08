password = 4080
amount = 10000
new_amount = 0
def login():
    password = "4080"
    while True:
        user_input = input('''                             Enter your password
                                      ''')
        if user_input == password:
            print("Login successful!")
            break  # Exit the loop if password is correct
        else:
            print("Incorrect password. Please try again.")

def cas():
    cash = int(input('''
                               how mach do you need ?
                                         '''))
    new_amount = amount-cash
    if cash <= amount:
        print(f'''
            your current amount is {new_amount} birr . thanks for use this service.''')
    else:
        print(f'''
            your current amount is {amount} birr . We're unable to access this service at the moment.enter other amount !''')
        cas()
def transf():
    transfer = input('''enter accpter bank account ?
                                    ''')
    am_transfer = int(input('''enter the amount of transfer ?
                                           '''))
    new_amount = amount - am_transfer
    if len(transfer) == 5:
        if am_transfer <= amount:
            print(f'''Transfer done seccessfully.
            you are transfer {am_transfer} birr to this bank account {transfer}
            your current amount is {new_amount} .thanks for use this service.''')
        else:
            print(f'''your current amount is {amount} birr . We're unable to access this service at the moment.
                   enter other amount !''')
            transf()
    else :
        print(f"plase enter the correct bank account")
        transf()
def deposit():
    dipos = int(input("enter your deposit ? "))
    new_amount = amount + dipos
    print(f'''
            your current amount is {new_amount} birr . thanks for use this service.''')
def main():
        use = input('''
                                 What do you need
        (1)cash withdrawal                                      (2) balance
        (3)transfer                                             (4)deposit






        ''')
        if use == "2":
             print(f'your current amount is {amount} birr .thanks for use this service.')
        elif use == '1':
             cas()
        elif use =="3":
             transf()
        elif use =="4":
             deposit()
        else:
            print('''
                                      WRONG KEY
                                plase enter the correct key''')
        main()

print('''
                                  NEGUS BANK
                                  ''')
    
login()
print(f'''
                         your current amount {amount} birr''')
main()

