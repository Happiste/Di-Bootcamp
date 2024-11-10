#EXCERCICE XP NINJA

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.message = []

    def call(self, other_phone):
        call = (f"{other_phone} called {self.phone_number}")
        self.call_history.append(call)
        print(f"{other_phone} called {self.phone_number}")

    def show_call_history(self):
        print(f"CALL HISTORY of {self.phone_number}:\n")
        for call in self.call_history:
            print(call)
        print("---------")

    def send_message(self, other_phone, msg):
        new_msg = {"to": other_phone.phone_number, "from": self.phone_number, "content" : msg}
        self.message.append(new_msg)
        other_phone.message.append(new_msg)

    
    def show_outgoing_message(self):
        print(f"Outgoing MSG of {self.phone_number}: ")
        count = 1
        for msg in self.message:
            if msg["from"] == self.phone_number:
                print(f"msg numero {count}: {msg}")
                count += 1
        print("--------")
    
    def show_incoming_message(self):
        print(f"Incoming MSG of {self.phone_number}: ")
        count = 1
        for msg in self.message:
            if msg["to"] == self.phone_number:
                print(f"msg numero {count}: {msg}")
                count += 1
        print("--------")


my_phone = Phone(13)
yael_phone = Phone(5)
naomi_phone = Phone(47)

my_phone.call(yael_phone.phone_number)
yael_phone.call(my_phone.phone_number)
my_phone.call(naomi_phone.phone_number)
my_phone.show_call_history()
yael_phone.show_call_history()
my_phone.send_message(yael_phone, "Salut commen tu vas ?")
my_phone.show_outgoing_message()
yael_phone.send_message(my_phone, "Je vais trés bien et toi ??")
yael_phone.show_outgoing_message()
my_phone.send_message(yael_phone, "Tu fais quoi pour Shabbat ?")
my_phone.show_outgoing_message()
my_phone.show_incoming_message()