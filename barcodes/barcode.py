from abc import ABC, abstractmethod


class Barcode(ABC):

    @abstractmethod
    def generate(self, string : str, with_verification_digit : bool) -> list[bool]:
        pass

    @abstractmethod
    def validate(self, string : str):
        pass

    @abstractmethod
    def generate_verification_digit(self, string : str) -> str:
        pass

    def number_to_bitarray(self, number : int, bit_count : int):
        for i in reversed(range(bit_count)):
            yield self.bit_to_bool(number, i)

    def bit_to_bool(self, number : int, bit_number : int):
        return (number & (0x1 << bit_number)) == (0x1 << bit_number)