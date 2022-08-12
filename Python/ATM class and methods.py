# create new class

class ATM:
    pass
 


class ATM:
    def __init__(self,branch,branchcode,bank):
        self.branch = branch
        self.branchcode = branchcode
        self.bank = bank

    def __str__ (self) :
        return f"Nawarat Bank ATM Branch : {self.branch} {self.branchcode}. Please insert ATM card."
        
    def atmpin(self):
        correct_pin = card['atm_pin']
        c = 0
        while c <5:
            user_pin = input("enter your ATM Pin Number: ")
            if user_pin == correct_pin:
                print("Please select transaction option")
                break
            else:
                print("Incorrect PIN")
                c += 1


    def check_bal(self):
        print(f"Your account balance is {card['balance']} bahts.")
           

    def deposit (self):
        print("Please insert banknotes")

        deposit_amount = int(input("amount of money: "))
       
        print(f"Amount of {deposit_amount} bahts is successfully deposited.")

        card['balance'] += deposit_amount

        print(f"Current account balance: {card['balance']}")

        

    def withdraw (self):
        print("Please enter the withdrawal amount.")

        withdrawal_amount = int(input("withdrawal amount: "))
       
        if card['balance'] - withdrawal_amount >= 0:
       
            print(f"Amount of {withdrawal_amount} bahts is withdrawn. Please collect the cash.")

            card['balance'] -= withdrawal_amount

            print(f"Current account balance: {card['balance']}")
        else:
            print("Insufficient account balance")

    def transfer(self):
        print("Please select the destination bank and Enter the destination account number.")
        des_acc = input("Destination account number: ")
        trans_amt = int(input("Transfer amount: "))

        if card['balance'] - trans_amt >= 0:
            print(f"Amount of {trans_amt} bahts is transferred to account no. {des_acc}")

            card['balance'] -= trans_amt

            print(f"Current account balance: {card['balance']}")

        else:
            print("Insufficient account balance")


            
card = {
    "card_num":"1996",
    "owner":"Nawarat A",
    "balance":596000000,
    "atm_pin":"1212312121"
}







atm1 = ATM("Bangkae", 10160, "nawarat")


print(atm1)


atm1.atmpin()

atm1.check_bal()

atm1.deposit()

atm1.withdraw()

atm1.transfer()





