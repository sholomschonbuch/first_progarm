class categorie:
    def __init__(self, name):
        self.name = name
        self.initial_total = []
        self.amount = []
        self.date = []
        self.paid = []
        self.paid_date = []
        
    def add(self, amount, date):
        #user_input = float(input("How much do you owe? "))
        #input_date = input("What is the date? ")
        self.amount.append(amount)
        self.date.append(date)
    def add_paid(self, amount, date):
        #user_input = float(input("How much did you pay? "))
        #input_date = input("What is the date? ")
        self.paid.append(amount)
        self.paid_date.append(date)
    def total(self):
        total_amount = 0
        for money in self.amount:
            total_amount += money
        return total_amount
    def total_paid(self):
        total_amount = 0
        for money in self.paid:
            total_amount += money
        return total_amount
    def __str__(self):
        return f"Name: {self.name} \ntotal: {self.total()} \nowe: {self.total() - self.total_paid()}"
    
        