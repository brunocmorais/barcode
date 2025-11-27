from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TEnum = TypeVar("TEnum")
TReturn = TypeVar("TReturn")

class AbstractFactory(ABC, Generic[TEnum, TReturn]):
    @staticmethod
    @abstractmethod
    def get(type : TEnum) -> TReturn:
        pass