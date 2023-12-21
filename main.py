class Fraction:
    """
    Набор функций для работы с дробями
    """

    # Инициализация начальных значений дроби
    def __init__(self, numerator: int | float, denominator: int | float) -> None:
        self.numerator: int | float = numerator # Числитель
        self.denominator: int | float = denominator # Знаменатель
    
    # Сложение
    def addition(self, choosen_num: int, number: int | float) -> None:
        """
        Добавление number к числителю/знаменателю (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое добавляется к числителю/знаменателю
        :type number: int | float
        """

        if choosen_num == '1': 
            self.numerator += number
            print(f'Успешно добавлено {number} к числителю. Текущее значение числителя: {self.numerator}')
        elif choosen_num == '2': 
            self.denominator += number
            print(f'Успешно добавлено {number} к знаменателю. Текущее значение знаменателя: {self.denominator}')
        else:
            print(f'Не распознана часть дроби, с которой требуется провести сложение (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')

    # Вычитание
    def substruct(self, choosen_num: int, number: int | float) -> None:
        """
        Вычитание number из числителя/знаменателя (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое вычитается у числителя/знаменателя
        :type number: int | float
        """

        if choosen_num == '1': 
            self.numerator -= number
            print(f'Успешно вычтено {number} у числителя. Текущее значение числителя: {self.numerator}')
        elif choosen_num == '2': 
            self.denominator -= number
            print(f'Успешно вычтено {number} у знаменателя. Текущее значение знаменателя: {self.denominator}')
        else:
            print(f'Не распознана часть дроби, с которой требуется провести вычитание (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
    
    def multi(self, choosen_num: int, number: int | float) -> None:
        """
        Умножение number на числитель/знаменатель (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: число, которое нужно умножить на числитель/знаменатель
        :type number: int | float
        """

        if choosen_num == '1': 
            self.numerator = self.numerator * number
            print(f'Успешно умножено {number} на числитель. Текущее значение числителя: {self.numerator}')
        elif choosen_num == '2': 
            self.denominator = self.denominator * number
            print(f'Успешно умножено {number} на знаменатель. Текущее значение знаменателя: {self.denominator}')
        else:
            print(f'Не распознана часть дроби, с которой требуется провести умножение (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
    
    def division(self, choosen_num: int, number: int | float) -> None:
        """
        Деление числителя/знаменателя на number (сhoosen_num - 1/2)

        :param choosen_num: выбор числителя / знаменателя (ожидается 1/2 соответственно)
        :type choosen_num: int

        :param number: делитель
        :type number: int | float
        """

        if choosen_num == '1': 
            self.numerator = self.numerator / number
            print(f'Успешно разделён числитель на {number}. Текущее значение числителя: {self.numerator}')
        elif choosen_num == '2': 
            self.denominator = self.denominator / number
            print(f'Успешно разделён знаменатель на {number}. Текущее значение знаменателя: {self.denominator}')
        else:
            print(f'Не распознана часть дроби, которая должна стать делимым (choosen_num={choosen_num}). Попробуйте снова. \n| 1 - Числитель \n| 2 - Знаменатель')
    
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
        """

        return fahrenheit / 33,8 # 1°С = 33,8°F
    
    # Конвертация градусов Цельсия в градусы Фаренгейта
    def celsius_to_fahrenheit(self, celsius: int | float) -> int | float:
        """
        Конвертация градусов Цельсия в градусы Фаренгейта

        :param celsius: градусы Цельсия
        :type celsius: int | float
        """

        return celsius / 33,8 # 1°С = 33,8°F
    
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
        """

        return km / 1,61 # 1 миля = 1,61 километра
    
    # Конвертация миль в километры
    def mil_to_km(self, mil: int | float) -> int | float:
        """
        Конвертация миль в километры

        :param mil: мили
        :type mil: int | float
        """

        return mil / 1,61 # 1 миля = 1,61 километра
    
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
        """

        return liter / 4,55 # 1 английский галлон = 4,55 литра
    
    # Конвертация английские галлонов в литры
    def gal_to_liter(self, gal: int | float):
        """
        Конвертация английские галлонов в литры

        :param gal: английские галлоны
        :type gal: int | float
        """

        return gal / 4,55 # 1 английский галлон = 4,55 литра