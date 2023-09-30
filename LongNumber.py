class LongNumber:
    def __init__(self, value:str = "") -> None:
        """
        Initializes a LongNumber object. Accepts a string representation of a number and sets its sign and digits.

        :param value: String representation of the number (default is an empty string)
        :type value: str
        """
        self.sign = 1
        if len(value) >= 1:
            if value[0] == '-':
                self.sign = -1
                value = value[1:]
        self.digits = [int(digit) for digit in reversed(value)]
            
    def __neg__(self) -> 'LongNumber':
        """
        Returns a LongNumber object with the opposite sign.

        :rtype: LongNumber
        :return: LongNumber object with opposite sign
        """
        negative_num = LongNumber(str(self))
        negative_num.sign = -self.sign
        return negative_num

    def __str__(self) -> str:
        """
        Returns the string representation of the number.

        :rtype: str
        :return: String representation of the number
        """
        if len(self.digits) == 1 and self.digits[0] == 0:
            return "0"
        sign_str = "-" if self.sign == -1 else ""
        return sign_str + ''.join(str(digit) for digit in reversed(self.digits))

    def __normalize(self) -> None:
        """
        Removes leading zeros from the number.
        """
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __add__(self, other: 'LongNumber') -> 'LongNumber':
        """
        Performs addition of two numbers and returns a new LongNumber object.

        :param other: Another LongNumber object to be added
        :type other: LongNumber

        :rtype: LongNumber
        :return: Result of addition as a LongNumber object
        """
        result = LongNumber()
        
        if self.sign == -1 and other.sign == 1:
            result = (other - self)
            if abs(self) > abs(other):
                result.sign = -1
            return result
            
        elif self.sign == -1 and other.sign == -1:
            return -(abs(other) + abs(self))
            
        carry = 0
        max_len = max(len(self.digits), len(other.digits))

        for i in range(max_len):
            x = self.digits[i] if i < len(self.digits) else 0
            y = other.digits[i] if i < len(other.digits) else 0
            temp_sum = x + y + carry
            result.digits.append(temp_sum % 10)
            carry = temp_sum // 10

        if carry > 0:
            result.digits.append(carry)

        result.__normalize()
        return result

    def __sub__(self, other: 'LongNumber') -> 'LongNumber':
        """
        Performs subtraction of two numbers and returns a new LongNumber object.

        :param other: Another LongNumber object to be subtracted
        :type other: LongNumber

        :rtype: LongNumber
        :return: Result of subtraction as a LongNumber object
        """
        if self.sign == -1 and other.sign == 1:
            return -(abs(other) + abs(self))
        
        elif self < other:
            return -(other - self)
        
        result = LongNumber()
        result.sign = self.sign

        borrow = 0
        for i in range(len(self.digits)):
            x = self.digits[i]
            y = other.digits[i] if i < len(other.digits) else 0
            temp_diff = x - y - borrow

            if temp_diff < 0:
                temp_diff += 10
                borrow = 1
            else:
                borrow = 0

            result.digits.append(temp_diff)

        result.__normalize()
        return result


    def __mul__(self, other: 'LongNumber') -> 'LongNumber':
        """
        Performs multiplication of two numbers and returns a new LongNumber object.

        :param other: Another LongNumber object to be multiplied
        :type other: LongNumber

        :rtype: LongNumber
        :return: Result of multiplication as a LongNumber object
        """
        result = LongNumber()

        for i in range(len(self.digits)):
            carry = 0
            temp_result = []

            for _ in range(i):
                temp_result.append(0)

            for j in range(len(other.digits)):
                product = self.digits[i] * other.digits[j] + carry
                temp_result.append(product % 10)
                carry = product // 10

            if carry > 0:
                temp_result.append(carry)

            partial_result = LongNumber("".join(map(str, reversed(temp_result))))
            result += partial_result

        result.sign = self.sign * other.sign
        result.__normalize()
        return result
        
    def __lt__(self, other: 'LongNumber') -> bool:
        """
        Compares the numbers and returns True if the current number is less than the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if current number is less than the other number, False otherwise
        """
        self_digits_reversed = list(reversed(self.digits))
        other_digits_reversed = list(reversed(other.digits))

        if len(self_digits_reversed) != len(other_digits_reversed):
            return len(self_digits_reversed) < len(other_digits_reversed)

        for i in range(len(self_digits_reversed) - 1, -1, -1):
            if self_digits_reversed[i] != other_digits_reversed[i]:
                return self_digits_reversed[i] < other_digits_reversed[i]

        return False

    def __gt__(self, other: 'LongNumber') -> bool:
        """
        Compares the numbers and returns True if the current number is greater than the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if current number is greater than the other number, False otherwise
        """
        return not self.__lt__(other) and self.__ne__(other)

    def __le__(self, other: 'LongNumber') -> bool:
        """
        Compares the numbers and returns True if the current number is less than or equal to the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if current number is less than or equal to the other number, False otherwise
        """
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: 'LongNumber') -> bool:
        """
        Compares the numbers and returns True if the current number is greater than or equal to the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if current number is greater than or equal to the other number, False otherwise
        """
        return not self.__lt__(other)

    def __eq__(self, other: 'LongNumber') -> bool:
        """
        Checks if the current number is equal to the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if the current number is equal to the other number, False otherwise
        """
        return self.sign == other.sign and self.digits == other.digits

    def __ne__(self, other: 'LongNumber') -> bool:
        """
        Checks if the current number is not equal to the other number.

        :param other: Another LongNumber object to be compared
        :type other: LongNumber

        :rtype: bool
        :return: True if the current number is not equal to the other number, False otherwise
        """
        return not self.__eq__(other)
    
    def copy(self) -> 'LongNumber':
        """
        Creates and returns a copy of the LongNumber object.

        :rtype: LongNumber
        :return: Copy of the LongNumber object
        """
        return LongNumber(self.__str__)
    
    def __abs__(self) -> 'LongNumber':
        """
        Returns a LongNumber object with a positive sign.

        :rtype: LongNumber
        :return: LongNumber object with a positive sign
        """
        abs_num = LongNumber(str(self))
        abs_num.sign = 1
        return abs_num