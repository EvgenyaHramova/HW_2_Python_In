# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def binary_func(number: int, n: int):
    symbols = '0123456789abcdefghijklmnopqrsuvwxyz'
    binar_number = ''
    while number != 0:
        result = str(symbols[number % n])
        binar_number = result + binar_number
        number //= n
    return binar_number


number = int(input('Введите число: '))
calculus_system = int(input('Введите число, соответствующее системе исчисления: '))
print(binary_func(number, calculus_system))

# print(bin(number))  # двоичная
# print(oct(number))   # восмиричная
print(hex(number))   # 16-ричная
print(hex(number)[2:])


# задание из 2 семинара
# def binary_func(number: int, n: int = 2):
#     binar_number = ''
#     while number != 0:
#         result = str(number % n)
#         binar_number = result + binar_number
#         number //= n
#     return binar_number


# number = int(input('Введите число: ')) 
# calculus_system = int(input('Введите число, соответствующее системе исчисления: '))
# print(binary_func(number, calculus_system))


# # print(bin(number)[2:])  # двоичная
# print(oct(number)[2:])   # восмиричная