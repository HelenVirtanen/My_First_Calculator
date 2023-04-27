import time
from random import choice

print("Добро пожаловать! Это калькулятор. Давайте что-нибудь посчитаем!:)")

def try_again():
    again = input(choice(["Хотите попробовать еще раз?:) ", "Посчитаем еще?:) ", "Давайте еще посчитаем?:) ", "Еще? "]))
    if again.lower() in "давайхорошокугу":
        calc()
    else:
        print("Пока-пока! До новых расчетов!")

def calc():
    num_1 = input("Введите первое число: ")
    while not num_1.isdigit():
        print(f"Ой! '{num_1}' это какой-то другой знак.")
        num_1 = input("Введите первое число: ")

    oper = input("Введите любую из следующих операций: +-*/ ")
    while oper not in "+-*//да":
        if oper == " " or oper == "**":
            print("Может Вы хотите возвести число в степень?", end=" ")
            oper = input("Напишите 'Да/Нет': ")
        elif oper.lower() == "нет":
            oper = input("Введите любую из следующих операций: + - * / ")
        else:
            print("Такую операцию калькулятор еще не знает.")
            oper = input("Введите, пожалуйста, другую операцию: ")

    num_2 = input("Введите второе число: ")
    while not num_2.isdigit():
        print("Это не похоже на число")
        num_2 = input("Введите второе число: ")

    if int(num_2) == 0 and oper == "/":
        print("На ноль делить нельзя!")
        try_again()

    print("Отлично! Сейчас посчитаем!:)")
    time.sleep(1)

    num_1, num_2 = int(num_1), int(num_2)
    if oper == "+":
        print("Сумма равна:", num_1 + num_2)
    elif oper == "-":
        print("Разность равна:", num_1 - num_2)
    elif oper == "*":
        print("Умножение равно:", num_1 * num_2)
    elif oper == "/" or oper == "//":
        print("Деление равно:", num_1 / num_2)
        print("Деление нацело равно:", num_1 // num_2)
        print("Деление с остатком равно:", num_1 % num_2)

        if num_1 % num_2 == 0:
            print(f"Получается {num_1} кратно {num_2}. Здорово!")

    elif oper.lower() == "да":
        print(f"Число {num_1} в степени {num_2} равно: {num_1 ** num_2}")

    try_again()

calc()
