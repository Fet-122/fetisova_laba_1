"3. Каково количество продаж по каждой категории товаров?"

import csv

# Функция map: извлекает категорию товара из строки и возвращает пару (категория, 1)
def map_category_sales(row):
    category = row['inventory_category']
    if category == '':  # Проверяем на пустую строку, предполагая что категория может быть не указана
        return None
    return (category, 1)

# Функция reduce: агрегирует данные, суммируя количество продаж по каждой категории
def reduce_category_sales(mapped_data):
    result = {}
    for key, value in mapped_data:
        if key:  # Убедимся, что ключ не None
            if key in result:
                result[key] += value  # Увеличиваем счетчик для категории
            else:
                result[key] = value  # Инициализируем счетчик для новой категории
    return result

# Основная функция для выполнения MapReduce
def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_category_sales(row)  # Применяем функцию map к каждой строке
            if result:  # Добавляем результат только если он не None
                mapped_data.append(result)
        reduced_data = reduce_category_sales(mapped_data)  # Применяем функцию reduce к результатам маппинга
        for category, count in reduced_data.items():
            print(f"Category: {category}, Sales Count: {count}")  # Вывод результатов

if __name__ == '__main__':
    main()

"""
Чтение данных: 
Скрипт начинает работу с чтения файла dataset.csv, который должен содержать данные о продажах товаров, 
включая категории этих товаров. Файл читается с учетом указанной кодировки cp1251 и разделителя ;.

Функция Map (map_category_sales): 
Для каждой строки данных функция извлекает значение из колонки inventory_category. 
Если категория товара указана, возвращается пара (категория, 1). 
Если категория не указана или строка пустая, функция возвращает None, что позволяет пропустить такие строки при дальнейшей обработке.

Сбор данных: 
Все результаты, возвращенные функцией Map и не являющиеся None, собираются в список mapped_data.

Функция Reduce (reduce_category_sales): 
Данные, собранные в mapped_data, обрабатываются функцией Reduce. 
Здесь для каждой категории суммируется количество упоминаний (единицы из пар (категория, 1)), 
что позволяет подсчитать общее количество продаж по каждой категории.

Вывод результатов: 
После обработки всех данных функция Reduce возвращает словарь, где ключи — это категории товаров, 
а значения — количество продаж. Этот результат выводится в консоль.
"""