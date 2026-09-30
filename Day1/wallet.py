class User:

    def __init__(self, name, phone_number, transactions=None, balance=0):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.transactions = [] if transactions is None else transactions

    def register_number(self, numeber):
        pass

    @staticmethod
    def normalise_phone(raw):
        raw = raw.strip()
        raw = raw.replace(" ", "").replace("-", "")

        if raw.startswith("+254"):
            raw = "0" + raw[4:]
        elif raw.startswith("254"):
            raw = "0" + raw[3:]

        if len(raw) != 10 or not raw.isdigit() or not raw.startswith(("07", "01")):
            return None

        return raw

    def send_money(self):
        pass

    def widthraw_amount(self):
        pass


print(User.normalise_phone("0712345678"))
print(User.normalise_phone("+254712345678"))
print(User.normalise_phone("254712345678")) 
print(User.normalise_phone("071 234 5678"))
print(User.normalise_phone("07123"))
print(User.normalise_phone("abc"))
print(User.normalise_phone("0812345678"))
print(User.normalise_phone("0712345"))













# def main():
#         while True:
#             print("*/ -- Mini - M-Pesa SYS")
#             print("1.Regiser Number:")
#             print("2.Send Money:")
#             print("3.Widthraw Cash:")
#             print("4.Exit")

#             choice = input("Choose an Option:")

#             if choice == '1':
#                 (input("Enter Phone to register: "))
#                 print("Registration Succesful")
#             elif choice == '2':
#                 float(input("Enter Amount to send: "))
#                 print("Amount sent succesfully")
#             elif choice == '3':
#                 float(input("Enter Amount to widthraw: "))
#                 print("Amount widtrawal succesfull")
#             elif choice == '4':
#                 break
#             else:
#                 print("Choose a valid Operation")





    