class Laboratory: 
    def __init__(self, substances): 
        self.substances = substances 
        self.stock = {name: 0.0 for name in substances} 
    def getQuantity(self, substance): 
        return self.stock[substance]