name = input("Введіть своє ім'я: ")
print("Привіт, " + name + "!")
my_age = 25
user_age = int(input("Введіть свій вік: "))
if user_age > 18:
    print("Ти дорослий.")
else:
    print("Ви ще дитина.")
#3
number = float(input("Введіть число: "))
if number >= 0:
    print("Число без змін:", number)
else:
    opposite_number = -number
    print("Число з протилежним знаком:", opposite_number)
#4
password = input("Пароль - ")
passcode = input("Ваш пароль -")
if passcode == password:
    print("Пароль вірний")
else:
    print("Пароль невірний")