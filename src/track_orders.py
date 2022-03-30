class TrackOrders:
    def __init__(self):
        self.orders = []
        self.dishes = set()
        self.working_days = set()
        self.days_counter = {}
        self.busiest_day_counter = 0
        self.busiest_day = ""
        self.least_busy_day_counter = 999
        self.least_busy_day = ""

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def count_day(self, day):
        self.working_days.add(day)
        if day not in self.days_counter:
            self.days_counter[day] = 1
        else:
            self.days_counter[day] += 1

        if self.days_counter[day] >= self.busiest_day_counter:
            self.busiest_day_counter = self.days_counter[day]
            self.busiest_day = day

        if self.days_counter[day] <= self.least_busy_day_counter:
            self.least_busy_day_counter = self.days_counter[day]
            self.least_busy_day = day

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})
        self.dishes.add(order)
        self.count_day(day)

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
        went_days = set()
        for order in self.orders:
            if order["customer"] == customer:
                went_days.add(order["day"])
        return self.working_days.difference(went_days)

    def get_busiest_day(self):
        return self.busiest_day

    def get_least_busy_day(self):
        return self.least_busy_day
