class StringUtils:
    
    @staticmethod
    def count_words(input_string: str) -> dict:
        """
        Counts the number of words and unique words in a string.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Dictionary containing word count and unique word count
        :rtype: dict
        """
        words = input_string.split()
        unique_words = set(words)
        return {
            "words_amount": len(words),
            "unique_words_amount": len(unique_words)
        }

    @staticmethod
    def center_text(input_string: str, console_width: int = 80) -> str:
        """
        Centers the input string on the console screen.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Centered string
        :rtype: str
        """
        return input_string.center(console_width)

    @staticmethod
    def analyze_characters(input_string: str) -> dict:
        """
        Analyzes the input string and provides statistics.

        :param string: Input string (default is an empty string)
        :type string: str
        :param interactive: Flag indicating interactive mode (default is False)
        :type interactive: bool
        :return: Dictionary containing string statistics
        :rtype: dict
        """
        string_length = len(input_string)
        digits_amount = sum(map(str.isdigit, input_string))
        spaces_amount = sum(map(str.isspace, input_string))
        lower_amount = sum(map(str.islower, input_string))
        upper_amount = sum(map(str.isupper, input_string))

        return {
            "length": string_length,
            "digits": digits_amount,
            "uppers": upper_amount,
            "lowers": lower_amount,
            "spaces": spaces_amount,
        }

    @staticmethod
    def perform_string_operation(sign: str, first_string: str, second_string: str = "", multiply_number: int = 0) -> str:
        """
        Performs string operations based on the provided sign and input strings.

        :param sign: Operator indicating the operation (+ or *)
        :type sign: str
        :param first_string: First input string
        :type first_string: str
        :param second_string: Second input string (default is an empty string)
        :type second_string: str
        :param multiply_number: Multiplier for string multiplication (default is 0)
        :type multiply_number: int
        :return: Resultant string after performing the specified operation
        :rtype: str
        """
        if sign == '+':
            return first_string + second_string
        elif sign == '*':
            return second_string * multiply_number