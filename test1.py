zavd_5 = """
Завдання 5
Напишіть програму, яка вводить з клавіатури послідовність чисел, перетворює послідовність на кортеж і 
виводить його відсортованим у порядку зростання. 
"""
print(zavd_5)
enter_str = input("Введіть цілі числа через пробіл: ")
str_sp = list(enter_str.split(" "))
posl = []
for i in str_sp:
    if i.isdigit():
        posl.append(int(i))
    else:
        print("Не коректно введені дані")
        break
    print(tuple(sorted(posl)))














