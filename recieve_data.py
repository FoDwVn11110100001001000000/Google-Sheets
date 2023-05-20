import os
from collections import namedtuple

# Вместо "****" нужно вставить имя файла
def path():
    folder = os.path.dirname(__file__)
    filename = '*************************'
    file_path = os.path.join(folder, filename)
    return file_path


def str_to_float(list):
    result = []
    for i in list:
        if i[:-3].isdigit():
            result.append(float(i[:-3]))
        else:
            result.append(i)
    return result

# Функция получает данные из файла в формате "Drivers_name ","2371.00","1026.00","1345.00","1778.25","1237.00","0.00","0.00","0.00","0.00","300.01","225.01","0.00","0.00","0.00"
def opening():
    Driver = namedtuple('Driver', ['Водій',
                                'Валовий_дохід', 
                                'Валовий_дохід_з_платежів_через_додаток', 
                                'Валовий_дохід_готівкою', 
                                'Чистий_дохід', 
                                'Готівка_на_руках', 
                                'Чайові', 
                                'Бонуси', 
                                'Компенсації', 
                                'Плата_за_скасування', 
                                'Дохід_за_годину_валовий', 
                                'Дохід_на_годину_чистий',
                                'Платні_дороги',
                                'Плата_за_бронювання',
                                'Повернення_коштів_пасажирам'])
    with open(path(), 'r', encoding='utf-8') as data_file:
        driver = []
        for r in data_file:
            str_format =  [column.strip('"|₴\n\ufeff') for column in r.split(',')]
            if str_format[1] != '0.00': # выводит водителей с плюсовым валом
                converted_list = str_to_float(str_format)
                x = Driver._make(converted_list)
                driver.append(x)
        return driver


def sort_result():
    format_list = opening()
    sorted_data = sorted(format_list[1:], key=lambda x: x[-4], reverse=True)
    sorted_data.insert(0, format_list[0])
    return sorted_data


def main():
    compre = [[driver.Водій, driver.Дохід_на_годину_чистий, driver.Чайові, f'{driver.Дохід_на_годину_чистий+driver.Чайові}'] for driver in sort_result()]
    return compre

print(main())


