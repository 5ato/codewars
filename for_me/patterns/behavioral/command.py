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


class ABCCommand(ABC):
    @abstractmethod
    def positive(self):
        raise NotImplementedError()

    @abstractmethod
    def negative(self):
        raise NotImplementedError()
    

class Conveyor:
    def on(self):
        print('start conveyor')

    def off(self):
        print('finish conveyor')

    def speed_increase(self):
        print('speed increase')

    def speed_decrease(self):
        print('speed decrease')


class ConveyorWorkCommand(ABCCommand):
    def __init__(self, conveyor: Conveyor) -> None:
        self.conveyor: Conveyor = conveyor

    def positive(self):
        return self.conveyor.on()
    
    def negative(self):
        return self.conveyor.off()
    

class ConveyorAdjustCommand(ABCCommand):
    def __init__(self, conveyor: Conveyor) -> None:
        self.conveyor: Conveyor = conveyor

    def positive(self):
        return self.conveyor.speed_increase()
    
    def negative(self):
        return self.conveyor.speed_decrease()
    

class Invorker:
    def __init__(self) -> None:
        self.commands: list[ABCCommand] = [None, None]
        self.history: list[ABCCommand] = []

    def set_command(self, button: int, command: ABCCommand):
        self.commands[button] = command
    
    def press_on(self, button: int):
        self.commands[button].positive()
        self.history.append(self.commands[button])

    def press_off(self):
        self.commands.pop().negative()


if __name__ == '__main__':
    c = Conveyor()
    wc = ConveyorWorkCommand(c)
    ac = ConveyorAdjustCommand(c)

    i = Invorker()
    i.set_command(0, wc)
    i.set_command(1, ac)
    i.press_on(0)
    i.press_on(1)

    i.press_off()
    i.press_off()
