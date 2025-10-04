def safe_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Помилка: ділення на нуль ❌"
        except SyntaxError:
            return "Помилка: неправильний вираз 🧩"
        except Exception as e:
            return f"Сталася невідома помилка: {e}"
    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("2 + 2"))         
print(calculate("10 / 0")) 
print(calculate("5 +"))            
print(calculate("abc"))
