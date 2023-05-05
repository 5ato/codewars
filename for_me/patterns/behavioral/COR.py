from abc import abstractmethod, ABCMeta, ABC
from typing import Any, Optional


# Основная мысль паттерна Chain of Responsibility заключается в фильтрации передаваемых параметров
# То есть, передаваемый параметр должен пройти через создаемую цепочку
# и в зависимости от требований в случае ошибки в параметрах остановить цепучку и выдать ошибку,
# либо продолжить последовательность и найти нужную цепь

# Ниже релизована версия без выхода цепи в случае неверных параметров

class IWorker(metaclass=ABCMeta):
    @abstractmethod
    def set_next(self, iworker: 'IWorker') -> 'IWorker':
        raise NotImplementedError()

    @abstractmethod
    def execute(self, command: str) -> str:
        raise NotImplementedError()
    

class ABCWorker(IWorker):
    def __init__(self) -> None:
        self.__next_worker: IWorker = None

    def set_next(self, iworker: IWorker) -> IWorker:
        self.__next_worker: 'IWorker' = iworker
        return iworker
    
    def execute(self, command: str) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        else:
            return None
        

class Desiner(ABCWorker):
    def execute(self, command: str) -> str:
        if command == 'спроектировать дом':
            return 'Дом спроектирован'
        else:
            return super().execute(command)
        
    
class Carpenters(ABCWorker):
    def execute(self, command: str) -> str:
        if command == 'класть кирпич':
            return 'Кирпичи поставлены'
        else:
            return super().execute(command)
        
    
class FinishingWorker(ABCWorker):
    def execute(self, command: str) -> str:
        if command == 'клеить обои':
            return 'Обои наклеины'
        else:
            return super().execute(command)
        

# Ниже реализована версия с выходом из цепочки в случае неверных параметров


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        raise NotImplementedError()
    
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        raise NotImplementedError()
    

class AbstractHandler(Handler):
    def __init__(self) -> None:
        self.__next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self.__next_handler = handler
        return handler
    
    def handle(self, request: Any) -> Optional[str]:
        if self.__next_handler is not None:
            return self.__next_handler.handle(request)
        return 'Everyone has everything they need'
    

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if 'banana' in request:
            return super().handle(request)
        return 'Error in Monkey'
    

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if "nut" in request:
            return super().handle(request)
        return 'Error in Squirrel'
    

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if "meat_ball" in request:
            return super().handle(request)
        return 'Error in Dog'


def client_code(handler: Handler) -> None:
    foods = ["nut", "banana", "meat_ball"]
    print(f"\nClient: Who wants a {foods}?")
    result = handler.handle(foods)
    if result:
        print(f"  {result}", end="")
    else:
        print(f"  {foods} was left untouched.", end="")


if __name__ == '__main__':
    m = MonkeyHandler()
    s = SquirrelHandler()
    d = DogHandler()

    s.set_next(m).set_next(d)
    client_code(s)
