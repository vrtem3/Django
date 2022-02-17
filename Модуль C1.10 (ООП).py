class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}."

    def get_area(self):
        return self.width * self.heigth


figure1 = Rectangle(5, 10, 50, 10)
print(figure1)
print(figure1.get_area())

print("""
        *********
        Next task
        *********
        """)

# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»


class Customers:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."

    def get_guest(self):
        return f"{self.name} {self.surname}, {self.city}"


Client1 = Customers("Иван", "Петров", "Москва", 50)
Client2 = Customers("Артем", "Горбунов", "Пермь", 50)
Client3 = Customers("Данил", "Гонцов", "Питер", 50)
Client4 = Customers("Дмитрий", "Жилин", "Питер", 50)


List = [Client1, Client2, Client3, Client4]

for guest in List:
    print(guest.get_guest())


