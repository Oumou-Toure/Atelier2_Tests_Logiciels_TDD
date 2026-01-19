class Laboratory:
    def __init__(self, substances, reactions=None):
        if not substances:
            raise ValueError("Le laboratoire doit contenir au moins une substance connue.")

        self.substances = list(set(substances))
        self.stock = {name: 0.0 for name in self.substances}

        self.reactions = reactions or {}
        self._validate_reactions()

        for product in self.reactions:
            self.stock[product] = 0.0

    def _validate_reactions(self):
        all_valid_names = set(self.substances) | set(self.reactions.keys())
        for product, ingredients in self.reactions.items():
            for quantity, substance in ingredients:
                if substance not in all_valid_names:
                    raise ValueError(f"La substance est inconnue dans la réaction: {substance}")


    def _get_stock(self, name):
        return self.stock.get(name, 0.0)


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

        if not isinstance(quantity, (int, float)):
            raise TypeError("La quantité doit être un nombre")

        if quantity < 0:
            raise ValueError("La quantité de la substance que vous souhaitez ajouter ne peut pas être négative")

        self.stock[substance] += quantity


    def make(self, product, quantity=1):
        if product not in self.reactions:
            raise ValueError(f"La réaction pour {product} est inconnue.")

        if not isinstance(quantity, int):
            raise TypeError("quantity doit être un entier")
        if quantity <= 0:
            raise ValueError("quantity doit être positif")

        max_possible = float('inf')
        for qty_needed, substance in self.reactions[product]:
            if qty_needed == 0:
                continue
            max_units = self._get_stock(substance) / qty_needed
            max_possible = min(max_possible, max_units)

        qty_to_make = int(min(quantity, max_possible))

        if qty_to_make == 0:
            raise ValueError(f"Stock insuffisant pour fabriquer {product}")

        for qty_needed, substance in self.reactions[product]:
            self.stock[substance] -= qty_needed * qty_to_make

        if product not in self.stock:
            self.stock[product] = 0.0
        self.stock[product] += qty_to_make

        return qty_to_make
