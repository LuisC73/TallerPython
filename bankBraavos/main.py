from Client import Client
from Account import Account
info = 0
while info != 7:

    menu = "¨*** Bank of Braavos ***\n"
    menu += "1. Register new client\n"
    menu += "2. See information of the client\n"
    menu += "3. Register new account\n"
    menu += "4. Remove money in your account\n"
    menu += "5. Enter money in your account\n"
    menu += "6. Consult balance of your account\n"
    menu += "7. Exit"
    print(menu)

    info = int(input('Enter the option: '))

    if info == 1:
        name = input("Please, enter your name: ")
        lastName = input("Please, enter your last name: ")
        nroDocument = input("Please, enter your document: ")
        client = Client(name, lastName, nroDocument)
    elif info == 2:
        client.seeInformation()
    elif info == 3:
        nroAccount = input('Please, enter your number of account: ')
        balance = int(input('Please, enter your balance of account: '))
        account = Account(nroAccount, balance)
    elif info == 4:
        amount = int(input('Please, enter the amount for remove of your account: '))
        account.changeBalance(amount, 'remove')
    elif info == 5:
        amount = int(input('Please, enter the amount for enter of your account: '))
        account.changeBalance(amount, 'enter')
    elif info == 6:
        account.consultBalance()
    else:
        print("Goodbye!!")
