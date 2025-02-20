class Car:
    """
    Базовый класс для автомобилей.

    Атрибуты:
    - brand (str): марка автомобиля.
    - model (str): модель автомобиля.
    - year (int): год выпуска.
    - color (str): цвет автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, color: str):
        """
        Инициализация данных об автомобиле.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param color: Цвет автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта (информация о марке и модели).

        :return: строковое представление автомобиля.
        """
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает подробное представление объекта для отладки.

        :return: строковое представление объекта для отладки.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"

    def drive(self) -> str:
        """
        Метод, который реализует движение автомобиля.

        :return: сообщение о движении автомобиля.
        """
        return f"{self.brand} {self.model} is driving."


class Sedan(Car):
    """
    Класс для легковых автомобилей.

    Атрибуты:
    - seats (int): количество сидений в автомобиле.
    """

    def __init__(self, brand: str, model: str, year: int, color: str, seats: int):
        """
        Инициализация легкового автомобиля с дополнительным параметром количества сидений.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param color: Цвет автомобиля.
        :param seats: Количество сидений.
        """
        super().__init__(brand, model, year, color)
        self.seats = seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля, включая количество сидений.

        :return: строковое представление легкового автомобиля.
        """
        return f"{self.brand} {self.model}, {self.seats} seats"

    def __repr__(self) -> str:
        """
        Возвращает подробное представление для отладки, включая количество сидений.

        :return: строковое представление для отладки.
        """
        return f"Sedan(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}', seats={self.seats})"

    def drive(self) -> str:
        """
        Перегружаем метод drive для легкового автомобиля, уточнив сообщение.

        :return: сообщение о движении легкового автомобиля.
        """
        return f"The sedan {self.brand} {self.model} is cruising on the road."


class Truck(Car):
    """
    Класс для грузовых автомобилей.

    Атрибуты:
    - capacity (float): грузоподъемность автомобиля в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, color: str, capacity: float):
        """
        Инициализация грузового автомобиля с дополнительным параметром грузоподъемности.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param color: Цвет автомобиля.
        :param capacity: Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(brand, model, year, color)
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля, включая его грузоподъемность.

        :return: строковое представление грузового автомобиля.
        """
        return f"{self.brand} {self.model}, {self.capacity} tons capacity"

    def __repr__(self) -> str:
        """
        Возвращает подробное представление для отладки, включая грузоподъемность.

        :return: строковое представление для отладки.
        """
        return f"Truck(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}', capacity={self.capacity})"

    def drive(self) -> str:
        """
        Перегружаем метод drive для грузового автомобиля, уточнив сообщение.

        :return: сообщение о движении грузового автомобиля.
        """
        return f"The truck {self.brand} {self.model} is transporting goods."


if __name__ == "__main__":
    # Создание объектов и тестирование
    sedan = Sedan("Toyota", "Camry", 2022, "red", 5)
    print(sedan)  # Toyota Camry, 5 seats
    print(sedan.drive())  # The sedan Toyota Camry is cruising on the road.

    truck = Truck("Volvo", "FH16", 2023, "blue", 25.0)
    print(truck)  # Volvo FH16, 25.0 tons capacity
    print(truck.drive())  # The truck Volvo FH16 is transporting goods.

    # Вывод для отладки
    print(repr(sedan))  # Sedan(brand='Toyota', model='Camry', year=2022, color='red', seats=5)
    print(repr(truck))  # Truck(brand='Volvo', model='FH16', year=2023, color='blue', capacity=25.0)
