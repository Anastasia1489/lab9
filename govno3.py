import csv


input_file = input()
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    sm = 0
    for row in reader:
        sm += row['Количество'] * row['Цена']
        print(row['Продукт'] + '-' + str(row['Количество']) + 'шт. за' + row['Цена'] + 'руб.')

    print('Итоговая сумма:' + sm + 'руб.')

