
from compressors.compressor import Compressor

class Packbits(Compressor):
    def compress(self, bytes : bytes):
        index = 0

        while index < len(bytes):
            char = bytes[index]
            run_length = 1

            while (index + run_length) < len(bytes) and bytes[index + run_length] == char and run_length < 128:
                run_length += 1

            if run_length > 1:
                yield run_length - 1
                yield char
                index += run_length
            else:
                literal_start = index

                while index < len(bytes) and (index + 1 >= len(bytes) or bytes[index] != bytes[index + 1]) and (index - literal_start) < 128:
                    index += 1

                yield 256 - (index - literal_start)

                for i in bytes[literal_start:index]:
                    yield i
