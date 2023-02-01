tickets = int(input('Сколько билетов Вы хотите приобрести?\n'))
numbers_ages = []
for i in range(0, tickets):
    input_age = int(input(f'Введите возраст покупателя {i + 1} билета:\n'))
    numbers_ages.append(input_age)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    full_price = sum(map(price, numbers_ages))
discount_price = int(full_price * 0.9)
if tickets > 3:
    print('Стоимость Ваших билетов с учётом скидки: ', discount_price, "руб.")
else:
    print('Стоимость Ваших билетов: ', full_price, "руб.")
