import json
import random
import string
from pathlib import Path


class Bank:
    def __init__(self):
        self.database = "data.json"
        self.data = []

        try:
            if Path(self.database).exists():
                with open(self.database, "r") as fr:
                    self.data = json.load(fr)
        except Exception:
            self.data = []

    def update(self):
        with open(self.database, "w") as fw:
            json.dump(self.data, fw, indent=4)

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

    def create_account(self, name, email, age, pin):

        accountNo = self.createAccountNo()

        info = {
            "name": name,
            "age": age,
            "email": email,
            "accountNo": accountNo,
            "pin": pin,
            "balance": 0
        }

        self.data.append(info)
        self.update()

        return accountNo

    def deposit(self, accNo, pin, amount):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:
                user["balance"] += amount
                self.update()
                return True, user["balance"]

        return False, "Account not found"

    def withdraw(self, accNo, pin, amount):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:

                if amount > user["balance"]:
                    return False, "Insufficient Balance"

                user["balance"] -= amount
                self.update()

                return True, user["balance"]

        return False, "Account not found"

    def check_balance(self, accNo, pin):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:
                return True, user["balance"]

        return False, "Account not found"

    def send_money(self, senderAcc, senderPin, receiverAcc, amount):

        sender = None
        receiver = None

        for user in self.data:

            if user["accountNo"] == senderAcc and user["pin"] == senderPin:
                sender = user

            if user["accountNo"] == receiverAcc:
                receiver = user

        if sender is None:
            return False, "Sender not found"

        if receiver is None:
            return False, "Receiver not found"

        if amount > sender["balance"]:
            return False, "Insufficient Balance"

        sender["balance"] -= amount
        receiver["balance"] += amount

        self.update()

        return True, "Transfer Successful"

    def update_name(self, accNo, pin, new_name):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:
                user["name"] = new_name
                self.update()
                return True

        return False

    def update_pin(self, accNo, pin, new_pin):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:
                user["pin"] = new_pin
                self.update()
                return True

        return False

    def update_email(self, accNo, pin, new_email):

        for user in self.data:
            if user["accountNo"] == accNo and user["pin"] == pin:
                user["email"] = new_email
                self.update()
                return True

        return False

    def delete_account(self, accNo, pin):

        for index, user in enumerate(self.data):

            if user["accountNo"] == accNo and user["pin"] == pin:
                self.data.pop(index)
                self.update()
                return True

        return False