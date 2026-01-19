class Laboratory: 
    def __init__(self, substances, reactions=None): 
        
        if not substances:
            raise ValueError("Le laboratoire doit contenir au moins une substance connue.")
        
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
        
    
    def make(self, product, quantity=1):
        
        if product not in self.reactions:
            raise ValueError(f"La réaction pour {product} est inconnue.")

        for qty_needed, substance in self.reactions[product]:
            if self.stock.get(substance, 0) < qty_needed * quantity:
                raise ValueError(f"Stock insuffisant pour {substance}")

        for qty_needed, substance in self.reactions[product]:
            self.stock[substance] -= qty_needed * quantity

        if product not in self.stock:
            self.stock[product] = 0.0
        self.stock[product] += quantity

        return quantity

