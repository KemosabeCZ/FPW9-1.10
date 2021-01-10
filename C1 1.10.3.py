class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

client1 = Client(name = 'Иван Петров', balance = 50)
print ('Клиент','"',client1.name,'"', 'Баланс = ', client1.balance)
