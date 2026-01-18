class Laboratory: 
    def __init__(self, substances, reactions=None): 
        self.substances = list(set(substances))
        self.stock = {name: 0.0 for name in substances} 
        
        self.reactions = reactions or {}
        
        for product, ingredients in self.reactions.items():
            for quantity, substance in ingredients:
                if substance not in self.substances:
                    raise ValueError(f"la substance est inconnue dans la réaction: {substance}")

        for product in self.reactions:
            self.stock[product] = 0.0
        
    def getQuantity(self, substance): 
        
        if not isinstance(substance, str):
            raise TypeError("Le nom de la substance doit être une chaîne de caractères.")
        
        substance = substance.rstrip("s")
        
        if substance not in self.stock:
            raise ValueError(f"La substance demandée est inconnue: {substance}")
        return self.stock[substance]
    
    def add(self, substance, quantity):
        
        if substance not in self.stock:
            raise ValueError(f"La substance demandée est inconnue: {substance}")
        
        if quantity < 0:
            raise ValueError("La quantité de la subastance que vous souhaitez ajouter ne peut pas être négative")
        
        if not isinstance(quantity, (int, float)):
            raise TypeError("La quantité doit être un nombre")
    
        self.stock[substance] += quantity