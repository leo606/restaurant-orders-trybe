class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def update_inventory(self, order):
        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})
        self.update_inventory(order)

    def get_quantities_to_buy(self):
        buy_list = {}
        for item, value in self.MINIMUM_INVENTORY.items():
            buy_list[item] = value - self.inventory[item]
        return buy_list
