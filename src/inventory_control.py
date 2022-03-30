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
        self.avaible_dishes = set(
            ingredient for ingredient in self.INGREDIENTS.keys()
        )
        self.dishes_by_ingredient = self.get_dishes_by_ingredient()

    def get_dishes_by_ingredient(self):
        dishes_by_ing_result = {}
        for ing in self.MINIMUM_INVENTORY.keys():
            dishes_by_ing_result[ing] = set(
                dish
                for dish, dish_ings in self.INGREDIENTS.items()
                if ing in dish_ings
            )
        return dishes_by_ing_result

    def update_inventory(self, order):
        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1
            if self.inventory[ingredient] < 1:
                self.avaible_dishes.difference_update(
                    self.dishes_by_ingredient[ingredient]
                )

    def add_new_order(self, customer, order, day):
        if order not in self.avaible_dishes:
            return False
        self.orders.append({"customer": customer, "order": order, "day": day})
        self.update_inventory(order)

    def get_quantities_to_buy(self):
        buy_list = {}
        for item, value in self.MINIMUM_INVENTORY.items():
            buy_list[item] = value - self.inventory[item]
        return buy_list

    def get_available_dishes(self):
        return self.avaible_dishes
