from typing import Any



# ----------------------------- Singleton implementation ----------------------------- #

# Основная идея сохранить и не создавать новый экземпляр класса


class Singleton:
    def __new__(cls, *args: Any, **kwargs: Any) -> None:
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


# ----------------------------- Meta implementation ----------------------------- #

# Основная идея сохранить и не создавать новый класс


class MetaSingleton(type):
    instance = {}

    def __call__(cls, *args, **kwargs) -> None:
        if cls not in cls.instance:
            cls.instance[cls] = super().__call__(*args, **kwargs)
        return cls.instance[cls]
    

class Singleton(metaclass=MetaSingleton):
    pass


# ----------------------------- Monostate implementation ----------------------------- #

# Отличие Monostate от Singleton является сохранение состояния


class Monostate:
    _shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state
        if not self._shared_state:
            self.data = 'test-data'
