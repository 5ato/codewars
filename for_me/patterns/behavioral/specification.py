from abc import abstractmethod
from typing import Any
from dataclasses import dataclass


# ----------------------------- Specification implementation ----------------------------- #

# Основная идея в том, что паттерн Specification осуществляет реализацию отпределение параметров для бизнес-логики


class Specification:
    @abstractmethod
    def is_satisfied(self, candidate: Any) -> bool:
        raise NotImplementedError()
    
    def __call__(self, candidate: Any) -> bool:
        return self.is_satisfied(candidate)

    def __and__(self, other: 'Specification') -> 'AndSpecification':
        return AndSpecification(self, other)
    
    def __or__(self, other: 'Specification') -> 'OrSpecification':
        return OrSpecification(self, other)
    
    def __invert__(self) -> 'NotSpecification':
        return NotSpecification(self)
    

@dataclass(frozen=True)
class AndSpecification(Specification):
    first: Specification
    second: Specification

    def is_satisfied(self, candidate: Any) -> bool:
        return self.first.is_satisfied(self) and self.second.is_satisfied(candidate)
    

@dataclass(frozen=True)
class OrSpecification(Specification):
    first: Specification
    second: Specification

    def is_satisfied(self, candidate: Any) -> bool:
        return self.first.is_satisfied(self) or self.second.is_satisfied(candidate)
    

@dataclass(frozen=True)
class NotSpecification(Specification):
    subject: Specification

    def is_satisfied(self, candidate: Any) -> bool:
        return self.subject.is_satisfied(candidate)


# ----------------------------- Meta implementation ----------------------------- #

# Реализация Specification через Метаклассы


class MetaSpecification(type):
    def __and__(self, other):
        return MetaSpecification('AndSpecification', (), {'__new__': lambda _, arg: self(arg) and other(arg)})
    
    def __or__(self, other):
        return MetaSpecification('OrSpecification', (), {'__new__': lambda _, arg: self(arg) or other(arg)})

    def __invest__(self):
        return MetaSpecification('NotSpecification', (), {'__new__': lambda _, arg: not self(arg)})
    

class Specification(metaclass=MetaSpecification):
    pass
