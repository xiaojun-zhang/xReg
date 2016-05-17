class Postfix:
    precedence = {'*': 3,
                  '?': 3,
                  '+': 3,
                  '#': 2}

    def __init__(self):
        pass

    def in_2_post(self, reg):
        """
        convert infix regular expression to postfix
        :rtype: String
        :param reg: String
        """
        result, operators = [], []
        concatenated_reg = self._add_concatenation(reg)
        for char in concatenated_reg:
            if self._is_open_parentheses(char):
                operators.append(char)
            elif self._is_close_parentheses(char):
                while len(operators) != 0 \
                        and not self._is_open_parentheses(operators[-1]):
                    result.append(operators.pop())

                if len(operators) != 0 \
                        and self._is_open_parentheses(operators[-1]):
                    operators.pop()
            elif self._is_operator(char):
                if len(operators) != 0 and self._is_operator(operators[-1]):
                    if not self._heigher_priority(char, operators[-1]):
                        result.append(operators.pop())
                operators.append(char)
            else:
                result.append(char)

        while len(operators) != 0:
            result.append(operators.pop())

        return result

    def _add_concatenation(self, str):
        result = []
        for char in str:
            if self._possible_concatenation(result) \
                    and not self._is_operator(char) \
                    and not self._is_close_parentheses(char):
                result.append('#')

            result.append(char)

        return result

    def _possible_concatenation(self, str):
        if str is None or len(str) == 0:
            return False

        return not self._is_open_parentheses(str[-1]) \
            and not self._is_concatenation(str[-1])

    def _is_open_parentheses(self, char):
        return char == '('

    def _is_close_parentheses(self, char):
        return char == ')'

    def _is_concatenation(self, char):
        return char == '#'

    def _is_operator(self, char):
        return char in ['*', '+', '?', '#']

    def _heigher_priority(self, op1, op2):
        return self.precedence[op1] > self.precedence[op2]