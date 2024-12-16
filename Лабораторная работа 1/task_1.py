from abc import ABC, abstractmethod
from typing import Union


class Book(ABC):
    """
    Класс, представляющий книгу.

    Атрибуты:
    - title (str): Название книги.
    - author (str): Автор книги.
    - pages (int): Количество страниц в книге.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги с проверкой правильности значений.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")
        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> str:
        """
        Метод для чтения книги.

        Возвращает строку с информацией о книге.

        :return: Информация о текущем прогрессе чтения.
        :rtype: str
        """
        pass

    @abstractmethod
    def get_summary(self) -> str:
        """
        Метод для получения краткого содержания книги.

        :return: Краткое содержание книги.
        :rtype: str
        """
        pass


class ConcreteBook(Book):
    """
    Конкретная реализация книги.
    """

    def read(self) -> str:
        """
        Возвращает информацию о том, что книга читается.

        :return: Строка с описанием чтения книги.
        :rtype: str
        """
        return f'Чтение книги "{self.title}" от {self.author}.'

    def get_summary(self) -> str:
        """
        Возвращает краткое содержание книги.

        :return: Строка с кратким содержанием.
        :rtype: str
        """
        return f'Книга "{self.title}" написана {self.author}, рассказывает о важной теме.'


class Tree(ABC):
    """
    Класс, представляющий дерево.

    Атрибуты:
    - species (str): Вид дерева.
    - age (int): Возраст дерева в годах.
    """

    def __init__(self, species: str, age: int):
        """
        Инициализация дерева с проверкой возраста.

        :param species: Вид дерева.
        :param age: Возраст дерева в годах.
        :raises ValueError: Если возраст дерева меньше или равен 0.
        """
        if age <= 0:
            raise ValueError("Возраст дерева должен быть больше 0.")
        self.species = species
        self.age = age

    @abstractmethod
    def grow(self) -> str:
        """
        Метод для роста дерева.

        Возвращает строку, описывающую текущий рост дерева.

        :return: Описание роста дерева.
        :rtype: str
        """
        pass

    @abstractmethod
    def produce_fruit(self) -> str:
        """
        Метод для получения плодов дерева.

        :return: Описание плодов дерева.
        :rtype: str
        """
        pass


class ConcreteTree(Tree):
    """
    Конкретная реализация дерева.
    """

    def grow(self) -> str:
        """
        Метод, описывающий рост дерева.

        :return: Строка о продолжении роста дерева.
        :rtype: str
        """
        return f'Дерево {self.species} продолжает расти!'

    def produce_fruit(self) -> str:
        """
        Метод, описывающий плоды дерева.

        :return: Строка о плодах дерева.
        :rtype: str
        """
        return f'Дерево {self.species} приносит плоды.'


class SocialMediaProfile(ABC):
    """
    Класс, представляющий профиль в социальной сети.

    Атрибуты:
    - username (str): Имя пользователя.
    - followers (int): Количество подписчиков.
    """

    def __init__(self, username: str, followers: int):
        """
        Инициализация профиля с проверкой количества подписчиков.

        :param username: Имя пользователя.
        :param followers: Количество подписчиков.
        :raises ValueError: Если количество подписчиков меньше 0.
        """
        if followers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным.")
        self.username = username
        self.followers = followers

    @abstractmethod
    def post_update(self, message: str) -> str:
        """
        Метод для публикации обновления на профиле.

        :param message: Сообщение, которое публикуется.
        :return: Строка с результатом публикации.
        :rtype: str
        """
        pass

    @abstractmethod
    def interact(self, action: str) -> str:
        """
        Метод для взаимодействия с другими пользователями.

        :param action: Действие, которое выполняет пользователь (например, лайк, комментарий).
        :return: Описание действия.
        :rtype: str
        """
        pass


class ConcreteSocialMediaProfile(SocialMediaProfile):
    """
    Конкретная реализация профиля в социальной сети.
    """

    def post_update(self, message: str) -> str:
        """
        Публикация сообщения на профиле.

        :param message: Сообщение, которое публикуется.
        :return: Строка с результатом публикации.
        :rtype: str
        """
        return f'Публикация от {self.username}: {message}'

    def interact(self, action: str) -> str:
        """
        Взаимодействие с другими пользователями (например, лайк).

        :param action: Действие пользователя.
        :return: Описание действия.
        :rtype: str
        """
        return f'{self.username} {action}.'


# Пример работы с классами через doctest:
if __name__ == "__main__":
    import doctest

    doctest.testmod()
