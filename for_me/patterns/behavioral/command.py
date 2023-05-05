from abc import abstractmethod, ABC


# Основная мысль в том, что создаётся для каждой бизнес-логики отдельный класс Command-а
# И в конечном итоге нужные нам команды, использовать в специальном классе Invoker


class ChiefAssistant:
    def help_chief(self):
        print('Помогаю Шефу')


class Stove:
    def prepare_stove(self):
        print('Разогреваю печь')

    def cooking_pizza(self):
        print('Готовлю пиццу')


class ChiefCooker:
    def make_pizza(self):
        print('Делаю основную работу по готовке пиццы')


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class HelpChiefCommand(Command):
    def __init__(self, executor: ChiefAssistant) -> None:
        self.__executor = executor

    def execute(self):
        self.__executor.help_chief()


class PrepareStoveCommand(Command):
    def __init__(self, executor: Stove) -> None:
        self.__executor = executor

    def execute(self):
        self.__executor.prepare_stove()


class CookingPizzaCommand(Command):
    def __init__(self, executor: Stove) -> None:
        self.__executor = executor

    def execute(self):
        self.__executor.cooking_pizza()


class MakePizzaCommand(Command):
    def __init__(self, executor: ChiefCooker) -> None:
        self.__executor = executor

    def execute(self):
        self.__executor.make_pizza()


class Invoker:
    def __init__(self) -> None:
        self.history: list[Command] = []

    def addCommand(self, command: Command) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print('Нету задач')
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()
