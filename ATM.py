import time
print("               Welcome to RBI \n\nPlease Insert Your ATM Card")

time.sleep(3)

password = 1234

pin = int(input("Enter Your Pin : "))


balance = 5000

if pin == password:
    while True:

        print("""
            1. Check Balance
            2. Withdraw Money
            3. Pin Change
            4. Deposite Money
            5. Exit
            """)
        
        try:
            option = int(input("Please Select One Option : "))

        except:
            print("Please Select Valid Option from 1 to 4")

        if option == 1:
            print("Your Current balance is:", balance)

        if option == 2:
            withdraw_amount = int(input("Please Enter Withdraw Amount: "))
            if withdraw_amount > balance:
                print("Insufficient Balance")
            else:
                print(f"{withdraw_amount} is Successfully Debited from your account")    
                balance = balance - withdraw_amount     
                print("Your Current Available Balance is: ", balance)

        if option == 3:
            new_pin = int(input("Enter New pin: "))
            conform_pin = int(input("Conform New pin: "))
            if new_pin == conform_pin:
                password = new_pin
                print("Pin Changed Successfully")
            else:
                print("Try Again Later")    

        if option == 4:
            deposite_amount = int(input("Enter Your Balance for Deposite: "))
            if deposite_amount < 0:
                print("Please Deposite More than 0.")
            else:
                balance = balance + deposite_amount
                print(f"{deposite_amount} is Successfully Credited to your account")
                print("Your Current Available Balance is: ", balance)

        if option == 5:
            break


else:
    print("Invalid Pin !! \n\n Please Try Again")
