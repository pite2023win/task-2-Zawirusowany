# - allow for money transfer from client to client

class Client:
    def __init__(self, name, money_amount):
        self.name = name
        self.money_amount = money_amount
class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
    def withdraw_money(self, client, amount):
        client.money_amount -= amount
    def input_money(self, client, amount):
        client.money_amount += amount
    def show_funds(self, client):
        print(f'Funds in {client.name} account: {client.money_amount}')
    def transfer_money(self, client1, client2, amount):
        pass

client1 = Client('Will Smith', 1000)
bank_1 = Bank('PKO')
bank_1.add_client(client1)
bank_1.show_funds(client1)
bank_1.withdraw_money(client1, 400)
bank_1.show_funds(client1)
client2 = Client('Adam Nowak', -200)
bank_1.show_funds(client2)






