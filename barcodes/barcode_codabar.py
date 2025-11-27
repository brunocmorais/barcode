from barcodes.barcode import Barcode

table = {
    '0': 3, '1': 6, '2': 9, '3': 96, '4': 18, '5': 66, '6': 33, '7': 36, '8': 48, '9': 72,
    '-': 12, '$': 24, ':': 69, '/': 81, '.': 84, '+': 21, 'A': 26, 'B': 41, 'C': 11, 'D': 14
}

start_end = ['A', 'B', 'C', 'D']

class BarcodeCodabar(Barcode):

    def generate(self, string : str, with_verification_digit : bool):

        self.validate(string)

        barcode : list[bool] = []

        char_values = [c for c in string]

        if with_verification_digit:
            digit = self.generate_verification_digit(string)
            char_values.insert(-1, digit)

        narrow_wide = [table[item] for item in char_values]

        for char_value in narrow_wide:
            bar = True
            
            for i in reversed(range(7)):
                item = self.bit_to_bool(char_value, i)
                count = 2 if item else 1
                barcode.extend([bar] * count)
                bar = not bar

            barcode.append(False)

        return barcode
    
    def validate(self, string : str):

        if string[0] not in start_end or string[-1] not in start_end:
            raise Exception("Barcode must start and end with either A, B, C or D")

        for char in string:
            if char == "*" or char not in table.keys():
                raise Exception(f"Character {char} is not valid for barcode generation!")
            
    def generate_verification_digit(self, string : str):
        keys = list(table.keys())

        values = [keys.index(key) if key in string else 0 for key in keys]
        mod = 16 - sum(values) % 16
        return keys[mod]