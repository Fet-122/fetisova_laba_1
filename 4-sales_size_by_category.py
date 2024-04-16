"4. Как распределены продажи по размерам внутри каждой категории товаров?"

import csv
import re

# Функция map: извлекает категорию и размер товара из строки и возвращает пару ((категория, размер), 1)
def map_category_size_sales(row):
    description = row['description']
    # Извлекаем последний элемент описания, который, как предполагается, является размером
    # Разделяем описание по пробелам и берем последний элемент
    size = description.split()[-1] if description else 'NOT-CAPTURED'
    category = row['inventory_category']
    if category == '' or size == 'NOT-CAPTURED':  # Проверяем на пустую строку в категории или размере
        return None
    return ((category, size), 1)

# Функция reduce: агрегирует данные, суммируя количество продаж по каждой паре (категория, размер)
def reduce_category_size_sales(mapped_data):
    result = {}
    for key, value in mapped_data:
        if key:  # Убедимся, что ключ не None
            if key in result:
                result[key] += value  # Увеличиваем счетчик для категории и размера
            else:
                result[key] = value  # Инициализируем счетчик для новой пары категория-размер
    return result

# Основная функция для выполнения MapReduce
def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_category_size_sales(row)  # Применяем функцию map к каждой строке
            if result:  # Добавляем результат только если он не None
                mapped_data.append(result)
        reduced_data = reduce_category_size_sales(mapped_data)  # Применяем функцию reduce к результатам маппинга
        for (category, size), count in reduced_data.items():
            print(f"Category: {category}, Size: {size}, Sales Count: {count}")  # Вывод результатов

if __name__ == '__main__':
    main()


"""
Чтение данных: 
Скрипт начинает работу с чтения файла dataset.csv. Файл должен содержать данные, включая категории и размеры товаров. 
Считывание происходит с учетом кодировки cp1251 и разделителя ;.

Функция Map (map_category_size_sales): 
Для каждой строки данных функция извлекает значения из колонок inventory_category и size. 
Если одно из этих значений пустое, функция возвращает None, что позволяет пропустить такие строки при дальнейшей обработке. 
В противном случае, функция возвращает пару ((категория, размер), 1), где 1 указывает на одну продажу данного товара в данном размере.

Сбор данных: 
Все результаты, возвращенные функцией Map и не являющиеся None, собираются в список mapped_data.

Функция Reduce (reduce_category_size_sales): 
Данные, собранные в mapped_data, обрабатываются функцией Reduce. 
Эта функция агрегирует данные по ключам, где каждый ключ это пара (категория, размер). 
Для каждой такой пары подсчитывается общее количество продаж.

Вывод результатов: 
После обработки всех данных функция Reduce возвращает словарь, где ключи — это пары (категория, размер), 
а значения — количество продаж. Эти результаты выводятся в консоль.
"""