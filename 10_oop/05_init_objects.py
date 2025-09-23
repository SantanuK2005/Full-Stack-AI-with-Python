class chaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size =  size

    def summary(self):
        return f"{self.size} ml of {self.type} chai"
    
order = chaiOrder("green tea", 100)
print(order.summary())

order_two = chaiOrder("masala chai", 200)
print(order_two.summary())