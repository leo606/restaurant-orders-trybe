from src.classes.CsvReader import CsvReader


def most_ordered(data, person):
    dishes_ordered = {}
    result = ''
    counter = 0
    for order in data:
        if order['name'] == person:
            if not order['dish'] in dishes_ordered:
                dishes_ordered[order['dish']] = 1
            else:
                dishes_ordered[order['dish']] += 1
                if dishes_ordered[order['dish']] > counter:
                    result = order['dish']
                    counter = dishes_ordered[order['dish']]
    return (result, dishes_ordered)


def dishes_never_ordered(data, person):
    all_dishes = set()
    person_dishes = set()

    for order in data:
        all_dishes.add(order['dish'])
        if order['name'] == person:
            person_dishes.add(order['dish'])

    return all_dishes.difference(person_dishes)


def days_never_went(data, person):
    all_days = set()
    person_went_days = set()

    for order in data:
        all_days.add(order['day'])
        if order['name'] == person:
            person_went_days.add(order['day'])

    return all_days.difference(person_went_days)


def save_file(data, path_name):
    with open(path_name, mode='w') as file:
        for row in data:
            file.write(f'{row}\n')


def analyze_log(path_to_file):
    restaurant_data = CsvReader.read_file(path_to_file)
    maria_info = most_ordered(restaurant_data, 'maria')
    arnaldo_info = most_ordered(restaurant_data, 'arnaldo')

    maria_most_ordered = maria_info[0]
    arnaldo_hamburger_orders = str(arnaldo_info[1]['hamburguer'])
    joao_never_ordered = str(dishes_never_ordered(restaurant_data, 'joao'))
    joao_never_went = str(days_never_went(restaurant_data, 'joao'))

    save_file(
        [maria_most_ordered, arnaldo_hamburger_orders,
         joao_never_ordered, joao_never_went],
        'data/mkt_campaign.txt'
    )
