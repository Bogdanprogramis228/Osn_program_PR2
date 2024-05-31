# Знайти суму цифр заданого натурального числа n.

def sum_of_numbers(n):
    sum_num = 0
    
    while n > 0:
        # Додаємо останню цифру до суми
        sum_num += n % 10
        # Видаляємо останню цифру з числа
        n = n // 10
    
    return sum_num

number = int(input("Введіть натуральне число: "))

print("Сума цифр числа:", sum_of_numbers(number))
