from abc import ABC, abstractmethod
from typing import Any, Generator


class Compressor(ABC):
    @abstractmethod
    def compress(self, bytes : bytes) -> Generator[int, Any, None]:
        pass