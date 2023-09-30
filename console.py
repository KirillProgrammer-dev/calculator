import typing
import os

class Console:
    """
    The Console class provides utility methods for handling user input and validation.

    Methods:
        - validateIntRange(number: int, rangeMin: int, rangeMax: int) -> bool:
            Validates if the input number is within the specified range.

        - validateChar(char: str, allowed: Union[str, list]) -> bool:
            Validates if the input character is allowed, either a specific character or a list of allowed characters.

        - input_number(rangeMin: int = -2 ** 32, rangeMax: int = 2 ** 32, inputText: str = "Введите число: ") -> int:
            Takes user input within a specified numeric range and returns the input as an integer.

    """
    
    def validateIntRange(self, number:int, rangeMin:int, rangeMax:int) -> int:
        """
        Validates if a number falls within the specified range.

        :param number: Number to be validated
        :type number: int
        :param rangeMin: Minimum allowed value (inclusive)
        :type rangeMin: int
        :param rangeMax: Maximum allowed value (inclusive)
        :type rangeMax: int
        :return: True if the number is within the range, False otherwise
        :rtype: bool
        """
        return rangeMin <= number <= rangeMax
    
    def validateChar(self, char:str, allowed: typing.Union[str, list]) -> bool:
        """
        Validates if a character is allowed based on specified criteria.

        :param char: Character to be validated
        :type char: str
        :param allowed: Allowed character(s) (either a string or a list of characters)
        :type allowed: str or list
        :return: True if the character is allowed, False otherwise
        :rtype: bool
        """
        if isinstance(allowed, str):
            return char == allowed
        else:
            return char in allowed
    
    def input_number(self, rangeMin:int = -2 ** 32, rangeMax:int = 2 ** 32, inputText:str ="Введите число: ") -> int:
        """
        Takes user input and validates it within the specified range.

        :param rangeMin: Minimum allowed value (inclusive), default is -2**32
        :type rangeMin: int
        :param rangeMax: Maximum allowed value (inclusive), default is 2**32
        :type rangeMax: int
        :param inputText: Text to display when prompting for input, default is "Введите число: "
        :type inputText: str
        :return: Validated user input as an integer
        :rtype: int
        """
        def validation(number: int) -> bool:
            """
            Validates if the input can be converted to an integer and falls within the specified range.

            :param number: User input as a string
            :type number: str
            :return: True if the input is valid, False otherwise
            :rtype: bool
            """
            if number.isdigit() or number[1:].isdigit():
                if self.validateIntRange(int(number), rangeMin, rangeMax):
                    return True
            
            return False
        
        number = input(inputText)
        while not validation(number):
            number = input("Введите валидные данные: ")

        return int(number)

    def clear(self):
        """
        Clears the terminal screen.

        Note: This function works for both Windows and Unix-based systems.

        """
        os.system('cls' if os.name=='nt' else 'clear')