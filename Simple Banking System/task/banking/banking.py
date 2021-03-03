# Write your code here
import random
import sqlite3
import logging

conn = sqlite3.connect('card.s3db')
c = conn.cursor()
try:
    c.execute("""
                CREATE TABLE card(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT UNIQUE,
                pin TEXT,
                balance INTEGER DEFAULT 0)
              """)
except sqlite3.OperationalError:
    pass

complete_created = """
Your card has been created
Your card number:
{}
Your card PIN:
{}
"""

bank_menu = """
1. Create an account
2. Log into account
0. Exit
"""

login_menu = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""

transfer_description = """
Transfer
Enter card number:
"""


class BankSystem:
    def __init__(self):
        self.current_account = None
        self.is_login = False

    def generate_card_number(self):
        row_data = "400000" + self.generate_customer_account()
        temp = []
        for i in range(len(row_data)):
            temp.append(int(row_data[i]) * 2 if i % 2 == 0 else int(row_data[i]))
        remainder = sum([x - 9 if x > 9 else x for x in temp]) % 10
        return row_data + str(10 - (remainder if remainder != 0 else 10))

    def generate_customer_account(self):
        return "".join([str(random.randint(0, 9)) for _ in range(9)])

    def generate_pin(self):
        return "".join([str(random.randint(0, 9)) for _ in range(4)])

    def generate_complete(self):
        card_number = self.generate_card_number()
        pin = self.generate_pin()
        # ------ store data into database --------
        c.execute(f"""
                    INSERT INTO card(number, pin)
                    VALUES ({card_number}, {pin})
        """)
        conn.commit()

        # ------ Print Card Information ------
        print(complete_created.format(card_number, pin))

        # ------ Create Credit Card Instance ------
        card = CreditCard()
        card.card_number = card_number
        card.PIN = pin
        return card

    def load_account_info(self, account):
        c.execute(f"""
                    SELECT  *
                    FROM    card
                    WHERE   number={account}
                """)
        return c.fetchone()

    def login_bank_system(self, account, pin):
        account_info = self.load_account_info(account)
        if account_info is not None:
            account_pin = account_info[2]
            account_pin = account_pin.zfill(4)
            if account_pin == pin and account_info[1] == account:
                self.current_account = account
                self.is_login = True
                print("You have successfully logged in!")
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")

    def valid_card_check_sum(self, card_number):
        temp = list(card_number[:15])
        for i in range(len(temp)):
            temp[i] = int(temp[i]) * 2 if i % 2 == 0 else int(temp[i])
        remainder = sum([x - 9 if x > 9 else x for x in temp]) % 10
        return card_number[-1] == str(10 - (remainder if remainder != 0 else 10))


class CreditCard:
    def __init__(self, card_number="", PIN="", balance=0):
        self.card_number = card_number
        self.PIN = PIN
        self.balance = balance


bank_system = BankSystem()
while True:
    if bank_system.is_login:
        service = input(login_menu)
        if service == "1":
            c.execute(f"""
                        SELECT  balance
                        FROM    card
                        WHERE   number={bank_system.current_account}
                        """)
            print("Balance:", c.fetchone()[0])
        elif service == "2":
            income = input("Enter income:")
            c.execute(f"""
                        UPDATE card
                        SET balance = balance + {income}
                        WHERE number={bank_system.current_account}
                        """)
            conn.commit()
            print("Income was added!")
        elif service == "3":
            transfer_account = input(transfer_description)
            if not bank_system.valid_card_check_sum(transfer_account):
                print("Probably you made mistake in card number. Please try again!")
            else:
                transfer_account = bank_system.load_account_info(transfer_account)
                if transfer_account is None:
                    print("Such a card does not exist.")
                else:
                    transfer_number = int(input("Enter how much money you want to transfer:"))
                    c.execute(f"""
                                SELECT  balance
                                FROM    card
                                WHERE   number={bank_system.current_account}
                                """)
                    if c.fetchone()[0] < transfer_number:
                        print("Not enough money!")
                    else:
                        c.execute(f"""
                                    UPDATE card
                                    SET balance = balance - {transfer_number}
                                    WHERE number={bank_system.current_account}
                                    """
                                  )
                        c.execute(f"""
                                    UPDATE card
                                    SET balance = balance + {transfer_number}
                                    WHERE number={transfer_account[1]}
                                    """
                                  )
                        conn.commit()
                        print("Success!")

        elif service == "4":
            c.execute(f"""
                        DELETE FROM card
                        WHERE number={bank_system.current_account}
                        """
                      )
            conn.commit()
            bank_system.current_account = None
            print("The account has been closed!")
        elif service == "5":
            bank_system.is_login = False
            bank_system.current_account = None
            print("You have successfully logged out!")
        if service == "0":
            print("Bye!")
            break
    else:
        status = input(bank_menu)
        if status == '1':
            bank_system.generate_complete()
        if status == '2':
            bank_system.login_bank_system(input("Enter your card number:"), input("Enter your PIN:"))
        if status == '0':
            print("Bye!")
            break
