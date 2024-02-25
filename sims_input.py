class Human:
    def __init__(self, name: str = "Sim", age: int = 0, energy: int = 100, happiness: int = 100, hunger: int = 0):
        """Конструктор класу Human."""
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger

    def eat(self, food: int):
        """Метод для зміни рівня голоду."""
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} ate. Hunger: {self.hunger}")

    def sleep(self, hours: int):
        """Метод для зміни рівня енергії."""
        self.energy += hours
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept. Energy: {self.energy}")

    def play(self, activity: int):
        """Метод для зміни рівня щастя."""
        self.happiness += activity
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} played. Happiness: {self.happiness}")

    def age_up(self, years: int = 1):
        """Метод для зміни віку."""
        self.age += years
        print(f"{self.name} aged up. Age: {self.age}")

    def status(self):
        """Метод для відображення статусу персонажа."""
        print(
            f"{self.name}'s Status - Age: {self.age}, Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")


# Введення даних користувачем
name = input("Enter the name of your character: ")
age = int(input("Enter the age of your character: "))
energy = int(input("Enter the energy level of your character: "))
happiness = int(input("Enter the happiness level of your character: "))
hunger = int(input("Enter the hunger level of your character: "))

# Створення об'єкту Human з введеними даними
sim1 = Human(name, age, energy, happiness, hunger)

# Виклик методів для симуляції дій персонажа
sim1.eat(int(input("Enter the amount of food your character ate: ")))
sim1.sleep(int(input("Enter the number of hours your character slept: ")))
sim1.play(int(input("Enter the level of activity your character engaged in: ")))
sim1.age_up(int(input("Enter the number of years your character aged up: ")))

# Виведення статусу персонажа
sim1.status()
