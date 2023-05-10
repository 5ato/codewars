from enum import Enum
from abc import ABC, abstractmethod


# Основная мысль в том, что фабричный метод создаёт экземпляры определённых классов,
# Используется для удобного добавлени новых классов в систему или чтобы расширять эту самую систему


class PizzaType(Enum):
    mazarello = 'mazarello'
    margarito = 'margarito'
    cheese = 'cheese'


class Pizza:
    def __init__(self, price: float) -> None:
        self.price: float = price

    def get_price(self) -> float:
        return self.price
    

class MazarelloPizza(Pizza):
    def __init__(self) -> None:
        super().__init__(17.5)


class MargaritoPizza(Pizza):
    def __init__(self) -> None:
        super().__init__(23.7)


class CheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__(15.1)


def create_Pizza(pizza_type: PizzaType) -> Pizza:
    factory_dict = {
        PizzaType.mazarello: MazarelloPizza,
        PizzaType.margarito: MargaritoPizza,
        PizzaType.cheese: CheesePizza,
    }
    return factory_dict[pizza_type]()


# Ниже реализация фабричного метода через класс Creator, в котором не только храниться метод для создания объектов,
# А так же ещё и выполнение некой нужной бизнес логики


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        raise NotImplementedError()
    
    @abstractmethod
    def do_somethings(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()
    

class Product(ABC):
    @abstractmethod
    def operation(self):
        raise NotImplementedError()
    

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


# Ниже банальный пример исполбзования паттерна фабричный метод


class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        pass

    @abstractmethod
    def do_export(self, folder: str):
        pass

class LosslessVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class VideoType:
    lossless = 'lossless'
    h264BP = 'h264BP'
    h264Hi422P = 'h264Hi422P'


def factory_method(type: VideoType) -> VideoExporter:
    factory_dict = {
        VideoType.lossless: LosslessVideoExporter,
        VideoType.h264BP: H264BPVideoExporter,
        VideoType.h264Hi422P: H264Hi422PVideoExporter,
    }
    return factory_dict[type]()
