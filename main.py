def withdraw(amt_to_withdraw):
    if amt_to_withdraw > int(amount):
        print("Insufficient balance")
    elif amt_to_withdraw <= 0:
        print("Amount should be greater than 0")
    else:
        new_amount1 = int(amount) - amt_to_withdraw
        newdat1 = the_data.replace(amount, str(new_amount1))
        c = open('User_Data', 'w')
        c.write(newdat1)


def deposit(amt_to_deposit):
    if amt_to_deposit <= 0:
        print("Amount should be greater than 0")
    else:
        new_amount2 = int(amount) + amt_to_deposit
        newdat2 = the_data.replace(amount, str(new_amount2))
        d = open('User_Data', 'w')
        d.write(newdat2)


def balance():
    print("Your current balance is: ", amount)


def pin_change(newpin):
    print("Here is your new pin: ", str(newpin))
    choice2 = input("Are you sure you want to change the pin?(y/n): ")
    if choice2 == "y":
        newdat3 = the_data.replace(pin, newpin)
        e = open('User_Data', 'w')
        e.write(newdat3)


#def money_sending():
#newamount = int(dict1[account_number]) + int(transfer_money)
#newdat4 = the_data.replace(amount, str(newamount))
#f = open('User_Data', 'w')
#f.write(newdat4)
dict1 = {}
a = open('User_Data', 'r')
the_data = a.read()
stringofthedata = str(the_data)
print((stringofthedata))
print("Welcome to the Bank of Nivi. Enter your details below.\n")
user_account = input("Enter your account number: ")
user_pin = input("Enter your pin number: ")
checkforaccount = False
checkforpin = False
for i in stringofthedata.splitlines():

    person = i.split("-")  #its a list
    print(person)
    account_number = person[0]
    pin = person[1]
    amount = person[2]
    dict1[account_number] = amount

    if account_number == user_account:  #we cant use because here each number of the loop is taken and we are asking questions about it. we need to ask question and match, not iterate and find the match
        checkforaccount = True
        if pin == user_pin:
            checkforpin = True  #elseattheend
            while True:  #here while used not for infinite loop but for only executing in particular conditions. when true has reached we immediatley break out of the loop. the flag is set to true hence and no other message will be printed. but if true is never reached then flag is false. so flag  false condition messsages are printed
                if pin == user_pin:

                    choice1 = input(
                        "Enter your preferred action (1/2/3): 1.Withdraw 2. Deposit  3.Balance 4.Change pin 5. Exit: ")
                    if choice1 == "1":
                        amt_to_withdraw = int(input("Enter the amount to withdraw: "))
                        withdraw(amt_to_withdraw)
                    elif choice1 == "2":
                        amt_to_deposit = int(input("Enter the amount to be deposited: "))
                        deposit(amt_to_deposit)
                    elif choice1 == "3":
                        balance()

                    elif choice1 == "4":
                        newpin = input("Enter your new 3 digit pin: ")
                        pin_change(newpin)
                    elif choice1 == "5":
                        exiting = input("Are you sure you want to exit? (Y/N): ")
                        if exiting == "Y" or exiting == "y":
                            break
                    #elif choice1 == "6":
                    #transfer_account = input("Enter the account number: ")
                    #transfer_money = input("Enter the amt")
                    #if transfer_account in dict1:
                    #money_sending()
                    else:
                        print("Invalid action")
                break
if checkforaccount == False:
    print("Invalid account number")
elif checkforpin == False:
    print("Invalid PIN number")
print("Thanks for using Nivi's ATM")
