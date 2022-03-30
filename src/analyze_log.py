from classes.CsvReader import CsvReader


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


def analyze_log(path_to_file):
    restaurant_data = CsvReader.read_file(path_to_file)
    maria_info = most_ordered(restaurant_data, 'maria')
    arnaldo_info = most_ordered(restaurant_data, 'arnaldo')

    print(maria_info[0])
    print(arnaldo_info[1]['hamburguer'])


path = 'data/orders_1.csv'


analyze_log(path)
