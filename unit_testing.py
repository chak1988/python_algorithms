def calculator(expression: str):
    allowed = '+-/*'
    if not any(sign for sign in allowed if sign in expression):
        raise ValueError(f"Expression must contain atleast one of those {allowed}")
    for sign in expression:
        if sign in allowed:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    "+": lambda a, b: a + b,
                    "-": lambda a, b: a - b,
                    "/": lambda a, b: a / b,
                    "*": lambda a, b: a * b
                }[sign](left,right)
                # if sign == '+':
                #     return left + right
                # elif sign == '-':
                #     return left - right
                # elif sign == '/':
                #     return left / right
                # elif sign == '*':
                #     return left * right

            except(ValueError, TypeError):
                raise ValueError("Expression must contain two integers and one operator")


if __name__ == '__main__':
    print(calculator('2  +   2'))
    a = [2, 3, 4]
    b = [3, 5, 6]

    print([x in a for x in b])
    print([x for x in a if x in b])

# discover -s tests -p '*_test.py' выбираем в настройках edit configurations --> custom и вписываем
# discover найти  tests это папка где тесты  "*_test.py" это выражение в конце окончание на _test.py
