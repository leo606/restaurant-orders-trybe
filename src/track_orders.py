class TrackOrders:
    def __init__(self):
        self.orders = []
        self.dishes = set()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})
        self.dishes.add(order)

    def get_most_ordered_dish_per_customer(self, customer):
        ordered_dishes = {}
        most_ordered_counter = 0
        most_ordered_dish = ""
        for order in self.orders:
            if order["customer"] == customer:
                if not order["order"] in ordered_dishes:
                    ordered_dishes[order["order"]] = 1
                else:
                    ordered_dishes[order["order"]] += 1
                    if ordered_dishes[order["order"]] > most_ordered_counter:
                        most_ordered_counter = ordered_dishes[order["order"]]
                        most_ordered_dish = order["order"]
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        ordered_dishes = set()
        for order in self.orders:
            if order["customer"] == customer:
                ordered_dishes.add(order["order"])
        return self.dishes.difference(ordered_dishes)

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
