
import time

print("please insert your CARD")
time.sleep(5)

password = 1989
balance = 7800

pin = int(input("enter your pin "))

if pin == password:
    while True:
        print('''
        1 == balance
        2 == withdraw balance
        3 == deposit balance
        4 == exit
        ''')

        try:
            option = int(input("enter your option "))
        except ValueError:
            print("please enter a valid option")
            continue

        if option == 1:
            print(f"your current balance is {balance}")
        elif option == 2:
            withdraw_amount = int(input("please enter withdraw amount "))
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"your current balance is {balance}")
        elif option == 3:
            deposit_amount = int(input("please enter deposit amount "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your current balance is {balance}")
        elif option == 4:
            print("thank you")
            break
        else:
            print("Invalid option")
else:
    print("incorrect pin")
