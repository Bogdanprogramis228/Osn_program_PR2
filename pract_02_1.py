# Напишіть програму, яка в залежності від характеру вітру видає повідомлення про
# його швидкість: від 1 до 4 м / с - слабкий; від 5-10 м/c - помірний; від 9-18 м/c -
# сильний; більше 19 м / c - ураганний

def wind_speed_description(speed):
    if 1 <= speed <= 4:
        return "Слабкий вітер"
    elif 5 <= speed <= 10:
        return "Помірний вітер"
    elif 11 <= speed <= 18:
        return "Сильний вітер"
    elif speed >= 19:
        return "Ураганний вітер"
    else:
        return "Некоректна швидкість вітру"

try:
    speed = float(input("Введіть швидкість вітру: "))
    print(wind_speed_description(speed))
except ValueError:
    print("Будь ласка, введіть числове значення.")
