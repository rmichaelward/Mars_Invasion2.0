class User:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

    def set_balance(self, balance):
        self.balance = balance

    def add_balance(self, add_balance):
        self.balance += add_balance    
    
    def get_info(self):
        return {"username":self.name, "balance": self.balance}
