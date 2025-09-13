import random

def greeting():
    name = input("Введіть своє ім'я: ")
    age = input("Введіть свій вік: ")
    print(f"Привіт {name}, тобі {age}!")

def age_check():
    age = int(input("Введіть свій вік: "))
    if age > 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("Я загадав число від 1 до 10. У вас 3 спроби!")
    for i in range(attempts):
        guess = int(input("Ваш варіант: "))
        if guess == secret_number:
            print("Вітаю, ви вгадали!")
            break
        elif guess > secret_number:
            print("Менше!")
        else:
            print("Більше!")
    else:
        print(f"Ви програли. Було загадано число {secret_number}.")

def range_numbers():
    start = int(input("Введіть число 'з': "))
    end = int(input("Введіть число 'по': "))
    for i in range(start, end + 1):
        print(i, end=" ")
    print()

def even_reverse():
    n = int(input("Введіть число n: "))
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def factorial():
    n = int(input("Введіть число для обчислення факторіалу: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Факторіал числа {n} = {fact}")

def exam_grade():
    score = int(input("Введіть кількість балів (0-100): "))
    if 0 <= score <= 49:
        print("Незадовільно")
    elif 50 <= score <= 69:
        print("Задовільно")
    elif 70 <= score <= 89:
        print("Добре")
    elif 90 <= score <= 100:
        print("Відмінно")
    else:
        print("Некоректні бали!")

def calculator():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    op = input("Вкажіть дію (+, -, *, /): ")
    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
            print("Ділення на нуль!")
        else:
            print("Результат:", a / b)
    else:
        print("Невідома операція!")

# === Головне меню ===
while True:
    print("\n--- МЕНЮ ---")
    print("1. Привітання з ім'ям та віком")
    print("2. Перевірка віку (вхід дозволено/заборонено)")
    print("3. Гра «Вгадай число»")
    print("4. Вивід чисел у діапазоні")
    print("5. Парні числа у зворотному порядку")
    print("6. Факторіал числа")
    print("7. Оцінка за балами")
    print("8. Калькулятор")
    print("0. Вихід")

    choice = input("Оберіть пункт меню: ")

    if choice == "1":
        greeting()
    elif choice == "2":
        age_check()
    elif choice == "3":
        guess_number()
    elif choice == "4":
        range_numbers()
    elif choice == "5":
        even_reverse()
    elif choice == "6":
        factorial()
    elif choice == "7":
        exam_grade()
    elif choice == "8":
        calculator()
    elif choice == "0":
        print("Програму завершено.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз!")
