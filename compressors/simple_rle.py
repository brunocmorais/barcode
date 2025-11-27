from typing import Any, Generator
from compressors.compressor import Compressor

class SimpleRLE(Compressor):

    def compress(self, bytes: bytes) -> Generator[int, Any, None]:
        counter = 0
        last_byte = bytes[0]

        for b in bytes:
            if b == last_byte:
                counter += 1
            else:
                yield counter
                yield last_byte
                counter = 1

            if counter == 9:
                yield counter
                yield last_byte
                counter = 0

            last_byte = b

        yield counter
        yield last_byte