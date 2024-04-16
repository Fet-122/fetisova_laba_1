"5. Как изменяется средний размер скидки в течение года по месяцам?"
import csv
from datetime import datetime

def map_discount_by_month(row):
    try:
        # Проверяем формат даты и преобразуем её в объект datetime
        date = datetime.strptime(row['transaction_date'], '%d.%m.%Y')
        year = date.year
        month = date.month
        # Пытаемся преобразовать скидку в число
        discount = float(row['bill_discount'])
    except ValueError as e:
        # Проверяем, вызвана ли ошибка некорректным значением скидки
        if "could not convert string to float" in str(e):
            pass
        else:
            print(f"Error processing row {row}: {e}")
        return None
    return ((year, month), discount)

def reduce_discount_by_month(mapped_data):
    result = {}
    for (year_month, discount) in mapped_data:
        if year_month:
            if year_month in result:
                result[year_month]['total'] += discount
                result[year_month]['count'] += 1
            else:
                result[year_month] = {'total': discount, 'count': 1}
    for year_month in result:
        result[year_month] = result[year_month]['total'] / result[year_month]['count']
    return result

def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_discount_by_month(row)
            if result:
                mapped_data.append(result)
        if not mapped_data:
            print("No valid data to process.")
            return
        reduced_data = reduce_discount_by_month(mapped_data)
        if not reduced_data:
            print("No reductions to display.")
            return
        for year_month, avg_discount in reduced_data.items():
            print(f"Year: {year_month[0]}, Month: {year_month[1]}, Average Discount: {avg_discount:.2f}")

if __name__ == '__main__':
    main()


"""
Чтение данных: 
Скрипт начинает работу с чтения файла dataset.csv, который должен содержать данные о скидках и датах транзакций.

Функция Map (map_discount_by_month): 
Для каждой строки данных функция преобразует строку даты в объект datetime для извлечения года и месяца. 
Скидка также преобразуется в число. Если данные корректны, возвращается пара ((год, месяц), скидка). 
Если возникает ошибка в данных, возвращается None.

Сбор данных: 
Все результаты, возвращенные функцией Map и не являющиеся None, собираются в список mapped_data.

Функция Reduce (reduce_discount_by_month): 
Данные, собранные в mapped_data, обрабатываются функцией Reduce. 
Она агрегирует данные по ключам, где каждый ключ — это пара (год, месяц). 
Для каждой такой пары подсчитывается общая сумма скидок и их количество. 
Затем вычисляется средняя скидка для каждого месяца.

Вывод результатов: 
После обработки всех данных функция Reduce возвращает словарь, где ключи — это пары (год, месяц), 
а значения — средние скидки. Эти результаты выводятся в консоль.
"""