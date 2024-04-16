"7. Какой самый популярный цвет товаров среди всех продаж?"

import csv

# Функция map: извлекает цвет товара из строки и возвращает пару (цвет, 1)
def map_color_sales(row):
    color = row['colour']  # Получаем цвет товара из строки данных
    if color == 'NOT-CAPTURED':  # Проверяем, если цвет не указан
        return None  # Пропускаем такие строки
    return (color, 1)  # Возвращаем пару (цвет, 1)

# Функция reduce: агрегирует данные, считая количество упоминаний каждого цвета
def reduce_color_sales(mapped_data):
    result = {}
    for key, value in mapped_data:
        if key:  # Убедимся, что ключ не None
            if key in result:
                result[key] += value  # Увеличиваем счетчик для цвета
            else:
                result[key] = value  # Инициализируем счетчик для нового цвета
    return result

# Основная функция для выполнения MapReduce
def main():
    with open('data_2022.csv', mode='r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        mapped_data = []
        for row in reader:
            result = map_color_sales(row)  # Применяем функцию map к каждой строке
            if result:  # Добавляем результат только если он не None
                mapped_data.append(result)
        reduced_data = reduce_color_sales(mapped_data)  # Применяем функцию reduce к результатам маппинга
        # Находим самый популярный цвет
        most_popular_color = max(reduced_data, key=reduced_data.get) if reduced_data else None
        if most_popular_color:
            print(f"The most popular color is: {most_popular_color} with {reduced_data[most_popular_color]} sales.")
        else:
            print("No valid color data available.")

if __name__ == '__main__':
    main()

"""

Чтение данных: 
Скрипт начинает работу с чтения файла dataset.csv, который должен содержать данные о цветах товаров.

Функция Map (map_color_sales): 
Для каждой строки данных функция извлекает значение цвета из столбца colour. 
Если цвет не указан или маркирован как "NOT-CAPTURED", строка пропускается. 
Если цвет указан, функция возвращает пару (цвет, 1), где 1 указывает на одну продажу товара данного цвета.

Сбор данных: 
Все результаты, возвращенные функцией Map и не являющиеся None, собираются в список mapped_data.

Функция Reduce (reduce_color_sales): 
Данные, собранные в mapped_data, обрабатываются функцией Reduce. 
Эта функция агрегирует данные по ключам, где каждый ключ — это цвет товара. 
Для каждого цвета подсчитывается общее количество продаж.

Поиск самого популярного цвета и вывод результатов: 
После обработки всех данных функция Reduce возвращает словарь, где ключи — это цвета, а значения — количество продаж. 
Скрипт находит цвет с максимальным количеством продаж и выводит его в консоль.
"""