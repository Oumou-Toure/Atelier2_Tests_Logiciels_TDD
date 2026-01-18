class Laboratory: 
    def __init__(self, substances): 
        self.substances = substances 
        self.stock = {name: 0.0 for name in substances} 
    def getQuantity(self, substance): 
        if not isinstance(substance, str):
            raise TypeError("Le nom de la substance doit être une chaîne de caractères.")
        
        substance = substance.rstrip("s")
        
        if substance not in self.stock:
            raise ValueError(f"La substance demandée est inconnue: {substance}")
        return self.stock[substance]