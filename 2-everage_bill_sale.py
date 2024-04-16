"2. Какая средняя скидка по всем счетам?"

import csv

def map_discount(row):
    bill_id = row['bill_id']
    try:
        discount = float(row['bill_discount'])
    except ValueError:
        return None  # Возвращаем None для некорректных данных и пропускаем их
    return (bill_id, discount)

def reduce_discount(mapped_data):
    total_discount = 0
    count = 0
    for _, discount in mapped_data:
        if discount is not None:
            total_discount += discount
            count += 1
    if count == 0:
        return None  # Избегаем деления на ноль
    return total_discount / count

def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_discount(row)
            if result:  # Добавляем в список только корректные данные
                mapped_data.append(result)
        average_discount = reduce_discount(mapped_data)
        if average_discount is not None:
            print(f"Средняя скидка по всем счетам: {average_discount:.2f}")
        else:
            print("Нет информации о скидках.")

if __name__ == '__main__':
    main()

"""
Функция map_discount: Извлекает скидку из каждой строки, преобразуя её в число. В случае ошибки в данных возвращает None и такие строки пропускаются.
Функция reduce_discount: Суммирует все скидки и подсчитывает количество корректных записей для вычисления средней скидки. Проверяет на случай, если все данные некорректны, чтобы избежать деления на ноль.
Основная функция main: Читает данные, применяет функцию map к каждой строке, а затем функцию reduce к результатам, и выводит среднюю скидку.
"""