class Account:

    def __init__(self, nroAccount, balance) -> None:
        self.nroAccount = nroAccount
        self.balance = balance

    def consultBalance(self):
        return print(f'your balance is {self.balance}')

    def changeBalance(self, amount, type):
        if type == "enter":
            self.balance = self.balance + amount
            print(f'Your new balance is {self.balance}')
        elif type == "remove":
            self.balance = self.balance - amount
            print(f'Your new balance is {self.balance}')
        else:
            print("ERROR")
