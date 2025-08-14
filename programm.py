# Базовый класс Animal
class Animal:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def make_sound(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def eat(self):
        print(f"{self._name} ест свою пищу")

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def __str__(self):
        return f"Животное: {self._name}, Возраст: {self._age}"


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self._wing_span = wing_span

    def make_sound(self):
        print(f"{self._name} щебечет")

    def fly(self):
        print(f"{self._name} летает с размахом крыльев {self._wing_span} метров")

    def __str__(self):
        return f"Птица: {self._name}, Возраст: {self._age}, Размах крыльев: {self._wing_span} м"


# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self._fur_color = fur_color

    def make_sound(self):
        print(f"{self._name} издает характерный звук")

    def run(self):
        print(f"{self._name} бежит")

    def __str__(self):
        return f"Млекопитающее: {self._name}, Возраст: {self._age}, Цвет шерсти: {self._fur_color}"


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name: str, age: int, scale_color: str):
        super().__init__(name, age)
        self._scale_color = scale_color

    def make_sound(self):
        print(f"{self._name} шипит")

    def crawl(self):
        print(f"{self._name} ползает")

    def __str__(self):
        return f"Рептилия: {self._name}, Возраст: {self._age}, Цвет чешуи: {self._scale_color}"


# Демонстрация полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс сотрудника ZooKeeper
class ZooKeeper:
    def __init__(self, name: str):
        self._name = name

    def feed_animal(self, animal: Animal):
        print(f"{self._name} кормит {animal.get_name()}")

    def __str__(self):
        return f"Смотритель зоопарка: {self._name}"


# Класс сотрудника Veterinarian
class Veterinarian:
    def __init__(self, name: str):
        self._name = name

    def heal_animal(self, animal: Animal):
        print(f"{self._name} лечит {animal.get_name()}")

    def __str__(self):
        return f"Ветеринар: {self._name}"


# Класс Zoo с композицией
class Zoo:
    def __init__(self, name: str):
        self._name = name
        self._animals = []
        self._employees = []

    def add_animal(self, animal: Animal):
        self._animals.append(animal)
        print(f"Добавлено животное: {animal.get_name()}")

    def add_employee(self, employee):
        self._employees.append(employee)
        print(f"Добавлен сотрудник: {employee._name}")

    def get_animals(self):
        return self._animals

    def get_employees(self):
        return self._employees

    def save_to_file(self, filename):
        import json
        data = {
            "name": self._name,
            "animals": [
                {
                    "type": type(animal).__