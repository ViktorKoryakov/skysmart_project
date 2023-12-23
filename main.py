# -*- coding: utf-8 -*-
"""
:authors: mrvikor
:license: MIT License, see LICENSE file

:copyright: (c) 2023 mrvikor
"""

__author__ = 'mrvikor'
__version__ = '1.1'
__email__ = 'vityakoryakov@yandex.ru'

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Fraction: # (рус.: Дробь)
    """
    Набор функций для работы с дробями
    """

    # Инициализация начальных значений дроби
    def __init__(self, numerator: int | float, denominator: int | float) -> None: # При создании объекта от класса Fraction в скобочках ожидаются два параметра: 1 - числитель (int/float), 2 - знаменатель (int/float)
        try:
            self.numerator: int | float = float(numerator) # Задаём числитель
            self.denominator: int | float = float(denominator) # Задаём знаменатель
        except ValueError: 
            print('Не удалось конвертировать одно (оба) из чисел в дробное число. Попробуйте ещё раз.')
    
    # Сложение
    def addition(self, choosen_num: int, number: int | float) -> None:
        """
        Добавление number к числителю/знаменателю (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое добавляется к числителю/знаменателю
        :type number: int | float
        """

        try:
            choosen_num = int(choosen_num) # Преобразуем choosen_num в числовое значение # Преобразуем choosen_num в числовое значение
            number = float(number) # Преобразуем number в дробное числовое значение для выполнения операции

            if choosen_num == 1: # Если choosen_num = 1, то работаем с числителем дроби 
                self.numerator += number
                print(f'Успешно добавлено {number} к числителю. Текущее значение числителя: {self.numerator}')
            elif choosen_num == 2: # Иначе если choosen_num = 2, то работаем с знаменателем дроби 
                self.denominator += number
                print(f'Успешно добавлено {number} к знаменателю. Текущее значение знаменателя: {self.denominator}')
            else: # Если choosen_num not in [1, 2] (!= каждому из значений), то прекращаем работу
                print(f'Не распознана часть дроби, с которой требуется провести сложение (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
        except ValueError:
            print('Не удалось преобразовать какое-то из чисел в нужный тип (необходимо: choosen_num - int, number - int | float). Проверьте написание и попробуйте ещё раз')

    # Вычитание
    def substruct(self, choosen_num: int, number: int | float) -> None:
        """
        Вычитание number из числителя/знаменателя (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое вычитается у числителя/знаменателя
        :type number: int | float
        """

        try:
            choosen_num = int(choosen_num) # Преобразуем choosen_num в числовое значение
            number = float(number) # Преобразуем number в дробное числовое значение для выполнения операции

            if choosen_num == 1: # Если choosen_num = 1, то работаем с числителем дроби 
                self.numerator -= number
                print(f'Успешно вычтено {number} у числителя. Текущее значение числителя: {self.numerator}')
            elif choosen_num == 2: # Иначе если choosen_num = 2, то работаем с знаменателем дроби 
                self.denominator -= number
                print(f'Успешно вычтено {number} у знаменателя. Текущее значение знаменателя: {self.denominator}')
            else: # Если choosen_num not in [1, 2] (!= каждому из значений), то прекращаем работу
                print(f'Не распознана часть дроби, с которой требуется провести вычитание (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
        except ValueError:
            print('Не удалось преобразовать какое-то из чисел в нужный тип (необходимо: choosen_num - int, number - int | float). Проверьте написание и попробуйте ещё раз')
    
    def multi(self, choosen_num: int, number: int | float) -> None:
        """
        Умножение number на числитель/знаменатель (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое нужно умножить на числитель/знаменатель
        :type number: int | float
        """

        try:
            choosen_num = int(choosen_num) # Преобразуем choosen_num в числовое значение
            number = float(number) # Преобразуем number в дробное числовое значение для выполнения операции

            if choosen_num == 1: # Если choosen_num = 1, то работаем с числителем дроби 
                self.numerator = self.numerator * number
                print(f'Успешно умножено {number} на числитель. Текущее значение числителя: {self.numerator}')
            elif choosen_num == 2: # Иначе если choosen_num = 2, то работаем с знаменателем дроби 
                self.denominator = self.denominator * number
                print(f'Успешно умножено {number} на знаменатель. Текущее значение знаменателя: {self.denominator}')
            else: # Если choosen_num not in [1, 2] (!= каждому из значений), то прекращаем работу
                print(f'Не распознана часть дроби, с которой требуется провести умножение (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
        except ValueError:
            print('Не удалось преобразовать какое-то из чисел в нужный тип (необходимо: choosen_num - int, number - int | float). Проверьте написание и попробуйте ещё раз')

    def division(self, choosen_num: int, number: int | float) -> None:
        """
        Деление числителя/знаменателя на number (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: делитель
        :type number: int | float
        """

        try:
            choosen_num = int(choosen_num) # Преобразуем choosen_num в числовое значение
            number = float(number) # Преобразуем number в дробное числовое значение для выполнения операции

            if choosen_num == 1: # Если choosen_num = 1, то работаем с числителем дроби 
                self.numerator = self.numerator / number
                print(f'Успешно разделён числитель на {number}. Текущее значение числителя: {self.numerator}')
            elif choosen_num == 2: # Иначе если choosen_num = 2, то работаем с знаменателем дроби 
                self.denominator = self.denominator / number
                print(f'Успешно разделён знаменатель на {number}. Текущее значение знаменателя: {self.denominator}')
            else: # Если choosen_num not in [1, 2] (!= каждому из значений), то прекращаем работу
                print(f'Не распознана часть дроби, которая должна стать делимым (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
        except ValueError:
            print('Не удалось преобразовать какое-то из чисел в нужный тип (необходимо: choosen_num - int, number - int | float). Проверьте написание и попробуйте ещё раз')
        except ZeroDivisionError:
            print('Не удалось выполнить операцию. На ноль делить нельзя')
    
class ConvertTemperature:
    """
    Набор функций для конвертации мер температуры
    """

    # Конвертация градусов Фаренгейта в градусы Цельсия
    def fahrenheit_to_celsius(self, fahrenheit: int | float) -> int | float:
        """
        Конвертация градусов Фаренгейта в градусы Цельсия

        :param fahrenheit: градусы Фаренгейта
        :type fahrenheit: int | float

        :rtype: int | float
        """
        try:
            fahrenheit = float(fahrenheit) # Преобразуем градусы Фаренгейта в дробное число для выполнения операции
            return fahrenheit / 33,8 # 1°С = 33,8°F
        except ValueError:
            print('Не удалось преобразовать градусы Фаренгейта в дробное число. Проверьте написание и попробуйте ещё раз')
    
    # Конвертация градусов Цельсия в градусы Фаренгейта
    def celsius_to_fahrenheit(self, celsius: int | float) -> int | float:
        """
        Конвертация градусов Цельсия в градусы Фаренгейта

        :param celsius: градусы Цельсия
        :type celsius: int | float

        :rtype: int | float
        """
        try:
            celsius = float(celsius) # Преобразуем градусы Цельсия в дробное число для выполнения операции
            return celsius / 33,8 # 1°С = 33,8°F
        except ValueError:
            print('Не удалось преобразовать градусы Цельсия в дробное число. Проверьте написание и попробуйте ещё раз')
    
class ConvertLength:
    """
    Набор функций для конвертации мер длины
    """

    # Конвертация километров в мили
    def km_to_mil(self, km: int | float) -> int | float:
        """
        Конвертация километров в мили

        :param km: километры
        :type km: int | float

        :rtype: int | float
        """
        
        try:
            km = float(km) # Преобразуем километры в дробное число для выполнения операции
            return km / 1,61 # 1 миля = 1,61 километра
        except:
            print('Не удалось преобразовать километры в дробное число. Проверьте написание и попробуйте ещё раз')
    
    # Конвертация миль в километры
    def mil_to_km(self, mil: int | float) -> int | float:
        """
        Конвертация миль в километры

        :param mil: мили
        :type mil: int | float

        :rtype: int | float
        """

        try:
            mil = float(mil) # Преобразуем мили в дробное число для выполнения операции
            return mil / 1,61 # 1 миля = 1,61 километра
        except:
            print('Не удалось преобразовать мили в дробное число. Проверьте написание и попробуйте ещё раз')

class ConvertVolume:
    """
    Набор функций для конвертации мер объёма
    """

    # Конвертация литров в английские галлоны
    def liter_to_gal(self, liter: int | float) -> int | float:
        """
        Конвертация литров в английские галлоны

        :param liter: литры
        :type liter: int | float

        :rtype: int | float
        """
        
        try:
            liter = float(liter) # Преобразуем литры в дробное число для выполнения операции
            return liter / 4,55 # 1 английский галлон = 4,55 литра
        except:
            print('Не удалось преобразовать литры в дробное число. Проверьте написание и попробуйте ещё раз')

    # Конвертация английские галлонов в литры
    def gal_to_liter(self, gal: int | float) -> int | float:
        """
        Конвертация английские галлонов в литры

        :param gal: английские галлоны
        :type gal: int | float
        
        :rtype: int | float
        """

        try:
            gal = float(gal) # Преобразуем английские галлоны в дробное число для выполнения операции
            return gal / 4,55 # 1 английский галлон = 4,55 литра
        except:
            print('Не удалось преобразовать английские галлоны в дробное число. Проверьте написание и попробуйте ещё раз')