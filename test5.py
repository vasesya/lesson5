zavd_3 = """
Завдання 3
Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) 
у форматі RGB і виводить на екран кортеж, у якому зберігається колір.
"""
print(zavd_3)
r, g, b = "300", "300", "300"
while not r.isdigit() or not 0 <= int(r) <= 255:
        r = input("Введіть значення R: ")
while not g.isdigit() or not 0 <= int(g) <= 255:
        g = input("Введіть значення G: ")
while not b.isdigit() or not 0 <= int(b) <= 255:
        b = input("Введіть значення B: ")
color = (r, g, b)
print("RGB color is: ", color)




