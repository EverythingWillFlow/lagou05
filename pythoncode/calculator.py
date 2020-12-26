class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            return e.__doc__

    def sub(self, a, b):
        try:
            return a - b
        except Exception as e:
            return e.__doc__

    def mul(self, a, b):
        try:
            return a * b
        except Exception as e:
            return e.__doc__

    def div(self, a, b):
        try:
            return a / b
        except Exception as e:
            return e.__doc__