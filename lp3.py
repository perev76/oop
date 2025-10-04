import time
import functools
import unittest

def time_function(return_elapsed=False):
    """
    Декоратор, який вимірює час виконання функції.
    Якщо return_elapsed=True — повертає (результат, час).
    Якщо False — додає атрибут last_elapsed до самої функції.
    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            try:
                result = fn(*args, **kwargs)
            except Exception:
                elapsed = time.perf_counter() - start
                setattr(wrapper, "last_elapsed", elapsed)
                raise
            elapsed = time.perf_counter() - start
            setattr(wrapper, "last_elapsed", elapsed)
            if return_elapsed:
                return result, elapsed
            return result
        return wrapper
    return decorator

# --- Приклади використання ---
@time_function(return_elapsed=True)
def add_and_wait(a, b, wait=0.0):
    """Проста функція, яка додає два числа і робить паузу."""
    if wait:
        time.sleep(wait)
    return a + b

@time_function(return_elapsed=False)
def multiply_and_wait(a, b, wait=0.0):
    """Множить числа з паузою."""
    if wait:
        time.sleep(wait)
    return a * b

# --- Демонстрація ---
print("Демонстрація роботи:")
res, elapsed = add_and_wait(2, 3, wait=0.05)
print(f"add_and_wait → результат: {res}, час: {elapsed:.4f} c")

prod = multiply_and_wait(4, 5, wait=0.02)
print(f"multiply_and_wait → результат: {prod}, час: {multiply_and_wait.last_elapsed:.4f} c")

# --- Тести ---
class TestTimeFunction(unittest.TestCase):
    def test_returns_result_and_elapsed(self):
        result, elapsed = add_and_wait(10, 20, wait=0.02)
        self.assertEqual(result, 30)
        self.assertGreaterEqual(elapsed, 0.015)

    def test_attaches_last_elapsed(self):
        result = multiply_and_wait(3, 7, wait=0.03)
        self.assertEqual(result, 21)
        self.assertTrue(hasattr(multiply_and_wait, "last_elapsed"))
        self.assertGreaterEqual(multiply_and_wait.last_elapsed, 0.025)

    def test_exception_handling(self):
        @time_function()
        def will_raise(wait):
            time.sleep(wait)
            raise ValueError("error")
        with self.assertRaises(ValueError):
            will_raise(0.02)
        self.assertTrue(hasattr(will_raise, "last_elapsed"))
        self.assertGreaterEqual(will_raise.last_elapsed, 0.015)

print("\nПеревірка тестів:")
unittest.main(argv=[''], exit=False)
