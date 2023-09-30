from math import *


class NumbersCalculator:
    def calc_simple(self, sign: str, firstNumber: int, secondNumber: int):
        """
        Performs basic arithmetic operations on two input numbers.

        :param sign: Operator indicating the operation (+, -, *, /)
        :type sign: str
        :param firstNumber: First input number
        :type firstNumber: int
        :param secondNumber: Second input number
        :type secondNumber: int
        :return: Result of the arithmetic operation
        :rtype: int
        """
        if sign == '+':
            return firstNumber + secondNumber
        elif sign == '-':
            return firstNumber - secondNumber
        elif sign == '*':
            return firstNumber * secondNumber
        elif sign == '/':
            if secondNumber != 0:
                    return firstNumber / secondNumber
            else:
                return -1
            
    def sin_or_cos(self, option: int, angle: int) -> float: 
        """
        Calculates sin or cos of a given value.

        :param option: Option indicating the trigonometric function to calculate (1 for sin, 2 for cos)
        :type option: int
        :param angle: Angle in degrees
        :type angle: int
        :return: Sin or cos of the given angle
        :rtype: float
        """
        if option == 1:
            return sin(radians(angle))
        elif option == 2:
            return cos(radians(angle))
    
    def sin_or_cos_rad(self, option: int, angle: int) -> float: 
        """
        Calculates sin or cos of a given value.

        :param option: Option indicating the trigonometric function to calculate (1 for sin, 2 for cos)
        :type option: int
        :param angle: Angle in degrees
        :type angle: int
        :return: Sin or cos of the given angle
        :rtype: float
        """
        if option == 1:
            return sin(angle)
        elif option == 2:
            return cos(angle)

    def check_brackets(self, string: str) -> bool:
        """
        Checks if the parentheses in a given string are balanced.

        :param string: Input string with parentheses (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: True if parentheses are balanced, False otherwise
        :rtype: bool
        """

        flag = True 
        open_cnt = 0
        close_cnt = 0
        for i in range(0, len(string)):
            if (string[i] == "("):
                open_cnt += 1
            if (string[i] == ")"):
                close_cnt += 1
                if (open_cnt < close_cnt): 
                    flag = False

        if (open_cnt != close_cnt):
            flag = False
        
        return flag

