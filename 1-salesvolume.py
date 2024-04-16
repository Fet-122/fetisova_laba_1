"1. Какой общий объем продаж по каждому магазину за весь период?"

import csv


def map_store_sales(row):
    store_name = row['store_name']
    try:
        amount = float(row['line_item_amount'])
    except ValueError:
        return None  # Возвращаем None для некорректных данных и пропускаем их
    return (store_name, amount)

def reduce_store_sales(mapped_data):
    result = {}
    for key, value in mapped_data:
        if key and value is not None:  # Проверяем, что данные не None
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_store_sales(row)
            if result:  # Добавляем в список только корректные данные
                mapped_data.append(result)
        reduced_data = reduce_store_sales(mapped_data)
        for store, total_sales in reduced_data.items():
            print(f"Магазин: {store}, Общий объем продаж: {total_sales}")

if __name__ == '__main__':
    main()
