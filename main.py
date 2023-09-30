import console
import typing
from LongNumber import LongNumber
from StringUtils import StringUtils
from NumbersCalculator import NumbersCalculator


class Calculator(console.Console):
    """
    Class representing a calculator with various mathematical operations and functions.

    Attributes:
        None

    Methods:
        calc_radians: Calculates sine or cosine of an angle in radians.
        calc_extended: Performs advanced mathematical operations (exponentiation, modulo, square root).
        menu_logic: Converts numbers to different numeral systems (binary, octal, hexadecimal).
        check_brackets: Validates the correct placement of brackets in a mathematical expression.
        calc_degrees: Calculates sine or cosine of an angle in degrees.
        calc_simple: Performs basic mathematical operations (+, -, *, /).
        calc_logic: Performs logical operations (and, or, not).
    """

    def calc_10_2(self, number: int = 0, interactive: bool = False) -> str:
        """
        Converts a decimal number to binary.

        :param number: Decimal number to be converted (default is 0)
        :type number: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Binary representation of the input number
        :rtype: str
        """
        if interactive:
            number = self.input_number()

        binaryNumber = bin(int(number))
        result = "-" + \
            binaryNumber[3:] if binaryNumber[0] == "-" else binaryNumber[2:]
        if interactive:
            print(
                f"Ваш результат перевода {number} в двоичную систему счисления: {result}")

        return result

    def calc_10_16(self, number: int = 0, interactive: bool = False) -> str:
        """
        Converts a decimal number to hexadecimal.

        :param number: Decimal number to be converted (default is 0)
        :type number: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Hexadecimal representation of the input number
        :rtype: str
        """
        if interactive:
            number = self.input_number()

        hexNumber = hex(int(number))
        result = "-" + hexNumber[3:] if hexNumber[0] == "-" else hexNumber[2:]
        if interactive:
            print(
                f"Ваш результат перевода {number} в шестнадцатеричную систему счисления: {result}")

        return result

    def calc_10_8(self, number: int = 0, interactive: bool = False) -> str:
        """
        Converts a decimal number to octal.

        :param number: Decimal number to be converted (default is 0)
        :type number: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Octal representation of the input number
        :rtype: str
        """
        if interactive:
            number = self.input_number()

        octNumber = oct(int(number))
        result = "-" + octNumber[3:] if octNumber[0] == "-" else octNumber[2:]
        if interactive:
            print(
                f"Ваш результат перевода {number} в восьмеричную систему счисления: {result}")

        return result

    def menu_logic(self, option: int = 0, interactive: bool = False) -> None:
        """
        Handles logic for conversion menu.

        :param option: User-selected option (default is 0)
        :type option: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        """
        if interactive:
            print("1. Перевод 10СИ -> 2СИ;")
            print("2. Перевод 10СИ -> 16СИ;")
            print("3. Перевод 10СИ -> 8СИ;")

            option = self.input_number(
                1, 3, inputText="Введите номер выбранной опции: ")

        if option == 1:
            self.calc_10_2(interactive=interactive)  # Перевод из 10 в 2 СС
        elif option == 2:
            self.calc_10_16(interactive=interactive)  # Перевод из 10 в 16 СС
        elif option == 3:
            self.calc_10_8(interactive=interactive)  # Перевод из 10 в 8 СС

    def str_words(self, string: str = "", interactive: bool = False) -> dict:
        """
        Counts the number of words and unique words in a string.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Dictionary containing word count and unique word count
        :rtype: dict
        """
        if interactive:
            string = input("Введите строку для подсчета: ")

        result = StringUtils.count_words(string)

        if interactive:
            print(
                f"Количество слов в строке: {result['words_amount']}, количество уникальных слов в строке: {result['unique_words_amount']}")

        return result

    def str_showcenter(self, string: str = "", interactive: bool = False) -> str:
        """
        Centers the input string within the console width.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Centered string
        :rtype: str
        """
        if interactive:
            string = input("Введите строку для форматирования: ")

        result = StringUtils.center_text(string)

        if interactive:
            print(result)

        return result

    def str_stat(self, string: str = "", interactive: bool = False) -> dict:
        """
        Computes various statistics for the input string.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Dictionary containing string statistics
        :rtype: dict
        """

        if interactive:
            string = input("Введите строку для подсчета: ")

        result = StringUtils.analyze_characters(string)

        if interactive:
            print(f"Длина строки: {result['length']}")
            print(f"Количество цифр в строке: {result['digits']}")
            print(
                f"Количество букв в верхнем регистре в строке: {result['uppers']}")
            print(f"Количество букв в нижнем регистре: {result['lowers']}")
            print(f"Количество пробелов в строке: {result['spaces']}")

        return result

    def str_simple(self, sign: str = "", interactive: bool = False) -> str:
        """
        Performs simple string operations based on the input sign.

        :param sign: Input sign for the operation (+ for concatenation, * for repetition)
        :type sign: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of the string operation
        :rtype: str
        """
        result = "undefiend"

        if interactive:
            sign = input('Введите строку с операцией (+ или *): ')
            while not self.validateChar(sign, ["+", "*"]):
                sign = input('Введите валидную операцию (+ или *): ')

        if sign == '+':
            firstString = input('Введите первую строку: ')
            secondString = input('Введите вторую строку: ')

            result = StringUtils.perform_string_operation(
                "+", firstString, second_string=secondString)

        if sign == '*':
            string = input('Введите строку: ')
            multiplyNumber = self.input_number(
                rangeMin=1, inputText="Введите множитель: ")

            result = StringUtils.perform_string_operation(
                "*", string, multiply_number=multiplyNumber)

        if interactive:
            print(f"Ваш результат: {result}")

        return result

    def menu_strings(self, option: int = 0, sign: str = "", interactive: bool = False) -> None:
        """
        Handles logic for string operations menu.

        :param option: User-selected option (default is 0)
        :type option: int
        :param sign: Input sign for string operation (default is an empty string)
        :type sign: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        """
        if interactive:
            print("Выберите действие в калькуляторе строк:")
            print("1. Простые операции со строками")
            print("2. Вывод строки по центру экрана")
            print("3. Количество слов и количество уникальных слов")
            print("4. Статистика по символам строк")
            option = self.input_number(
                rangeMin=1, rangeMax=4, inputText="Введите номер выбранной опции: ")

        if option == 1:
            self.str_simple(interactive=interactive)

        elif option == 2:
            self.str_showcenter(interactive=interactive)

        elif option == 3:
            self.str_words(interactive=interactive)

        elif option == 4:
            self.str_stat(interactive=interactive)

    def long_add(self, number1: typing.Union[int, str] = 0, number2: typing.Union[int, str] = 0, interactive: bool = False) -> LongNumber:
        """
        Adds two long numbers.

        :param number1: First long number (default is 0)
        :type number1: int or str
        :param number2: Second long number (default is 0)
        :type number2: int or str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of addition as a LongNumber object
        :rtype: LongNumber
        """
        if interactive:
            number1 = input("Введите первое число для сложения: ")
            number2 = input("Введите второе число для сложения: ")

        result = LongNumber(number1) + LongNumber(number2)

        if interactive:
            print(f"Результат сложения - {result}")

        return result

    def long_sub(self, number1: typing.Union[int, str] = 0, number2: typing.Union[int, str] = 0, interactive: bool = False) -> LongNumber:
        """
        Subtracts two long numbers.

        :param number1: First long number (default is 0)
        :type number1: int or str
        :param number2: Second long number (default is 0)
        :type number2: int or str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of subtraction as a LongNumber object
        :rtype: LongNumber
        """

        if interactive:
            number1 = input("Введите первое число для вычитания: ")
            number2 = input("Введите второе число для вычитания: ")

        result = LongNumber(number1) - LongNumber(number2)

        if interactive:
            print(f"Результат вычитания - {result}")

        return result

    def long_multiply(self, number1: typing.Union[int, str] = 0, number2: typing.Union[int, str] = 0, interactive: bool = False) -> LongNumber:
        """
        Multiplies two long numbers.

        :param number1: First long number (default is 0)
        :type number1: int or str
        :param number2: Second long number (default is 0)
        :type number2: int or str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of multiplication as a LongNumber object
        :rtype: LongNumber
        """

        if interactive:
            number1 = input("Введите первое число для умножения: ")
            number2 = input("Введите второе число для умножения: ")

        result = LongNumber(number1) * LongNumber(number2)

        if interactive:
            print(f"Результат умножения - {result}")

        return result

    def menu_long(self, option: int = 0, interactive: bool = False) -> LongNumber:
        """
        Handles logic for long number option menu.

        :param option: Option value to select from the menu (default is 0)
        :type option: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result from the option menu as a LongNumber object
        :rtype: LongNumber
        """
        if interactive:
            print("Меню длинной арифметики:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")

        option = self.input_number(
            rangeMin=1, rangeMax=3, inputText="Введите номер операции: ")

        self.clear()

        if option == 1:
            return self.long_add(interactive=interactive)
        elif option == 2:
            return self.long_sub(interactive=interactive)
        elif option == 3:
            return self.long_multiply(interactive=interactive)

    def calc_simple(self, sign: str = "", firstNumber: int = 0, secondNumber: int = 0, interactive: bool = False) -> int:
        """
        Performs simple arithmetic operations (+, *, - or /) on two numbers.

        :param sign: Arithmetic operation sign (default is an empty string)
        :type sign: str
        :param firstNumber: First number for the operation (default is 0)
        :type firstNumber: int
        :param secondNumber: Second number for the operation (default is 0)
        :type secondNumber: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of the arithmetic operation
        :rtype: int
        """
        if interactive:
            sign = input('Введите строку с операцией (+ или *): ')
            while not self.validateChar(sign, ["+", "*", "-", "/"]):
                sign = input('Введите валидную операцию (+, *, - или /): ')

            firstNumber = self.input_number(inputText="Введите первое число: ")
            secondNumber = self.input_number(
                inputText="Введите второе число: ")

        result = NumbersCalculator().calc_simple(
            sign=sign, firstNumber=firstNumber, secondNumber=secondNumber)

        if interactive:
            print(f"Ваш результат - {result}")

        return result

    def calc_degrees(self, option: int = 0, angle: int = 0, interactive: bool = False) -> float:
        """Calculates sin or cos of a given value

        :param act: int
        :param angle: float

        :return: Sin or cos of a given value
        :rtype: float

        """
        if interactive:
            print("Меню расчета тригонометрических функций:")
            print("1. Синус")
            print("2. Косинус")

            option = self.input_number(
                rangeMin=1, rangeMax=2, inputText="Введите номер операции: ")

            self.clear()

        angle = self.input_number(inputText="Введите угол: ")

        result = NumbersCalculator().sin_or_cos(option=option, angle=angle)

        if interactive:
            print(f"Ваш результат - {result}")

        return result

    def calc_extended(self, option: int = 0, interactive: bool = False) -> float:
        """
        Performs extended mathematical operations based on user input.

        :param interactive: Flag indicating interactive mode (default is True)
        :type interactive: bool
        """
        if interactive:
            print("Меню расширенного калькулятора")
            print("1. Возведение в степень")
            print("2. Остаток от деления")
            print("3. Нахождение корня")

            option = self.input_number(1, 3, "Введите номер операции: ")

            self.clear()

        if option == 1:
            base = self.input_number(inputText="Введите основание: ")
            exponent = self.input_number(inputText="Введите степень: ")
            result = base ** exponent
        elif option == 2:
            dividend = self.input_number(inputText="Введите делимое: ")
            divisor = self.input_number(inputText="Введите делитель: ")
            result = dividend % divisor
        elif option == 3:
            number = self.input_number()
            result = number ** 0.5

        if interactive:
            print(f"Ваш результат - {result}")

        return result

    def check_brackets(self, string: str = "", interactive: bool = False) -> bool:
        """
        Checks if the parentheses in a given string are balanced.

        :param string: Input string with parentheses (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: True if parentheses are balanced, False otherwise
        :rtype: bool
        """
        if interactive:
            string = input("Введите строку с формулой:")

        result = NumbersCalculator().check_brackets(string)

        if interactive:
            if (result == True):
                print("Все скобки указаны корректно")
            else:
                print("Все скобки указаны некорректно")

        return result

    def calc_radians(self, option: int = 0, angle: int = 0, interactive: bool = False):
        """Calculates sin or cos of a given value

        :param act: int
        :param angle: float

        :return: Sin or cos of a given value
        :rtype: float

        """
        if interactive:
            print("Меню расчета тригонометрических функций (для радиан):")
            print("1. Синус")
            print("2. Косинус")

            option = self.input_number(
                rangeMin=1, rangeMax=2, inputText="Введите номер операции: ")

            self.clear()

        angle = self.input_number(inputText="Введите угол: ")

        result = NumbersCalculator().sin_or_cos_rad(option=option, angle=angle)

        if interactive:
            print(f"Ваш результат - {result}")

        return result

    def calc_logic(self, option: int = 0, A: bool = False, B: bool = False, interactive: bool = False) -> bool:
        """
        Performs logical operations (AND, OR, NOT) on given input values.

        :param option: Integer representing the logical operation (1 for AND, 2 for OR, 3 for NOT) (default is 0)
        :type option: int
        :param A: First boolean input value (default is False)
        :type A: bool
        :param B: Second boolean input value (default is False)
        :type B: bool
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Result of the logical operation
        :rtype: bool
        """
        if interactive:
            print("Меню логических операций")
            print("1. And")
            print("2. Or")
            print("3. Not")
            option = self.input_number(1, 3, "Введите номер выбранной опции: ")

            self.clear()

        if option in [1, 2]:
            if interactive:
                A = bool(self.input_number(
                    0, 1, "Введите первое число (0 или 1): "))
                B = bool(self.input_number(
                    0, 1, "Введите второе число (0 или 1): "))
            if option == 1:
                result = A and B
            elif option == 2:
                result = A or B

        elif option == 3:
            if interactive:
                A = bool(self.input_number(
                    0, 1, "Введите первое число (0 или 1): "))
            result = not A

        if interactive:
            print(f"Ваш результат - {result}")

        return result

    def menu_numbers(self, option: int = 0, interactive: bool = False):
        """
        Displays a menu of operations for numbers and performs the selected operation.

        :param option: Selected menu option (default is 0)
        :type option: int
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        """

        if interactive:
            print("Меню операций с числами")
            print('1. Простые операции')
            print("2. Расширенные операции")
            print("3. Тригонометрические действия с градусами")
            print("4. Тригонометрические действия с радианами")
            print("5. Логические операции")
            print("6. Перевод чисел в различные СС")
            print("7. Проверка скобок")

            option = self.input_number(1, 7, "Введите выбранное действие: ")

            self.clear()

        if option == 1:
            self.calc_simple(interactive=interactive)
        elif option == 2:
            self.calc_extended(interactive=interactive)
        elif option == 3:
            self.calc_degrees(interactive=interactive)
        elif option == 4:
            self.calc_radians(interactive=interactive)
        elif option == 5:
            self.calc_logic(interactive=interactive)
        elif option == 6:
            self.menu_logic(interactive=interactive)
        elif option == 7:
            self.check_brackets(interactive=interactive)

    def menu(self):
        print("Это интерактивное меню Калькулятора 2.0")
        print("1. Калькулятор чисел")
        print("2. Калькулятор строк")
        print("3. Длинная арифметика")

        option = self.input_number(1, 3, inputText="Выбранная опция: ")

        self.clear()

        if option == 1:
            self.menu_numbers(interactive=True)

        elif option == 2:
            self.menu_strings(interactive=True)

        elif option == 3:
            self.menu_long(interactive=True)


cal = Calculator()
cal.menu()
