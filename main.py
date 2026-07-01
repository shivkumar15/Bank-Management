import json
import random
from pathlib import Path
import string

class Bank:
    def __init__(self):
        self.database='data.json'
        self.data=[]

        try:
            if Path(self.database).exists():
                with open(self.database,"r") as fr:
                    self.data=json.load(fr)
            else:
                print("Such file does not exits ")
        except Exception as err:
            print(f"An error has occured {err}")

        print(
            """
            1. Press 1 to create account
            2. Press 2 to deposite money
            3. Press 3 to withdraw money
            4. Press 4 to check balance
            5. Press 5 to send money
            6. Press 6 to update details
            7. Press 7 to delete account
            """)
        
        self.val=int(input("How would you like to proceed ? "))

        if self.val==1:
            self.createAccount()
        elif self.val==2:
            self.deposite()
        elif self.val==3:
            self.withdraw()
        elif self.val==4:
            self.checkBalance()
        elif self.val==5:
            self.sendMoney()
        elif self.val==6:
            self.updateDetails()
        elif self.val==7:
            self.delAccount()

    

    def update(self):
        with open(self.database,"w") as fw:
            json.dump(self.data,fw,indent=4)

    def createAccountNo(self):
            while True:
                intVal = random.choices("0123456789", k=4)
                strVal = random.choices(string.ascii_letters, k=3)
                spChar = random.choices("!@#$%^&*", k=1)
                accNo = "".join(intVal + strVal + spChar)

                duplicate = False

                for account in self.data:
                    if accNo == account["accountNo"]:
                        duplicate = True
                        break
                if not duplicate:
                    return accNo

        
    
    def createAccount(self):
        self.name=input("Enter your name ")
        self.email=input("Enter your email ")
        self.age=input("Enter your age ")
        self.pin=input("Enter your Pin ")
        self.accountNo=self.createAccountNo()
        self.balance=0
        print("Account Successfully Created ")

        print(f'''
            Your info is \n Name : {self.name} \n Email : {self.email} \n Age : {self.age} \n Pin : {self.pin} \n Account No. : {self.accountNo} \n Balance : {self.balance}
            ''')
        
        print("Please Note you account number ")

        self.info={
            "name":self.name,
            "age":self.age,
            "email":self.email,
            "accountNo":self.accountNo,
            "pin":self.pin,
            "balance":self.balance
        }

        self.data.append(self.info)
        self.update()







    def deposite(self):
        accNo=input("Enter your Account Number")
        pin=input("Enter your pin ")
        
        
        for i in self.data:
            if i["accountNo"]==accNo and i["pin"]==pin:
                depAmt=int(input("How much you want to deposite ? "))
                i["balance"]=i["balance"]+depAmt
                self.update()
                print("Amount deposited successfully!!!")
                print(f"Your current balance is {i["balance"]}")
                break
            else:
                print("No user found!!!")


    def withdraw(self):
        accNo=input("Enter your Account Number")
        pin=input("Enter your pin ")

        for i in self.data:
            if i["accountNo"] == accNo and i["pin"]==pin:
                withdrawAmt=int(input("Enter how much you want to withdraw "))

                if withdrawAmt >i["balance"] or withdrawAmt < 0:
                    print("Invalid amount!! Enter a valid amount ")
                else:
                    i['balance']=i['balance']-withdrawAmt
                    self.update()
                    print("Amount withdrawn successfully ")
                    print(f"Your current balance is {i["balance"]}")
                break
            else:
                print("No account found!!!")


    def checkBalance(self):
        accNo=input("Enter your Account Number")
        pin=input("Enter your pin ")

        for i in self.data:
            if i["accountNo"] == accNo and i["pin"] == pin:
                print(f"Your currect banlance is {i["balance"]} ")



    def sendMoney(self):
        senderAcc=input("Enter the account no. of sender ")
        senderPw=input("Enter the pw of the sender ")

        receiverAcc=input("Enter the account no. of the receiver ")
       

        for i in self.data:
            if i["accountNo"]==senderAcc and i["pin"] ==senderPw:
                sendAmt=int(input("Amount to be send "))
                if sendAmt > i["balance"] or sendAmt < 0:
                    print("Invalid amount entered . Try Again!!")
                    break
                
                receiverFound = False

                for j in self.data:
                    if j["accountNo"] == receiverAcc:
                        i["balance"] -= sendAmt
                        j["balance"] += sendAmt

                        self.update()
                        print("Money transferred successfully")
                        receiverFound = True
                        break
                if not receiverFound:
                  print("Receiver not found!")
                break
            else:
                print("Sender not found ")


    def updateDetails(self):
        accNo=input("Enter your Account Number")
        pin=input("Enter your pin ")

        print(f"NOTE :- You cann't change 1.Age 2.Account Number 3.Balance")
        print(""" 1. Press 1 to change the name \n 2. Press 2 to change the pin \n 3.Press 3 to change the email id """)

        response=int(input("Enter your response "))

        if response == 1:
            newName=input("Enter New Name ")
            for i in self.data:
                if i["accountNo"]==accNo and i["pin"]==pin:
                    i["name"]=newName
                    self.update()
                    print("Name updated Successfully !!")
                    break
                else:
                    print('Account not found ')
        elif response == 2:
            newPin=input("Enter New Pin ")
            for i in self.data:
                if i["accountNo"]==accNo and i["pin"]==pin:
                    i["pin"]=newPin
                    self.update()
                    print("Pin updated Successfully !!")
                    break
                else:
                    print('Account not found ')
        elif response ==3:
            newEmail=input("Enter New Email ")
            for i in self.data:
                if i["accountNo"]==accNo and i["pin"]==pin:
                    i["Email"]=newEmail
                    self.update()
                    print("Email updated Successfully !!")
                    break
                else:
                    print('Account not found ')

        

    
    def delAccount(self):
        accNo=input("Enter your Account Number ")
        pin=input("Enter your pin ")

        print("Are you sure to delete the account ")
        response= input("Press Y for yes and Press N for avoid deletion ")

        if response =='Y' or response == 'y':
            for index,i in enumerate(self.data):
                if i['accountNo']==accNo and i['pin']==pin:
                    self.data.pop(index)
                    self.update()
                    print("Account deleted successfully")
                    return
                else:
                    print("No account found !")
                    return
        else:
            return
        

        

        

c1=Bank()