from barcodes.barcode import Barcode


table = {
    '*': 148, '0':  52, '1': 289, '2':  97, '3': 352, '4':  49, '5': 304, '6': 112, '7':  37, 
    '8': 292, '9': 100, 'A': 265, 'B':  73, 'C': 328, 'D':  25, 'E': 280, 'F':  88, 'G':  13, 
    'H': 268, 'I':  76, 'J':  28, 'K': 259, 'L':  67, 'M': 322, 'N':  19, 'O': 274, 'P':  82, 
    'Q':   7, 'R': 262, 'S':  70, 'T':  22, 'U': 385, 'V': 193, 'W': 448, 'X': 145, 'Y': 400, 
    'Z': 208, '–': 133, '.': 388, ' ': 196, '$': 168, '/': 162, '+': 138, '%': 42
}

class Barcode39(Barcode):

    def generate(self, string : str, with_verification_digit : bool):

        self.validate(string)

        barcode : list[bool] = []

        char_values = ["*", *[c for c in string + (self.generate_verification_digit(string) if with_verification_digit else "")], "*"]

        narrow_wide = [table[item] for item in char_values]

        for char_value in narrow_wide:
            bar = True
            
            for i in reversed(range(9)):
                item = self.bit_to_bool(char_value, i)
                count = 2 if item else 1
                barcode.extend([bar] * count)
                bar = not bar

            barcode.append(False)

        return barcode
    
    def validate(self, string : str):
        for char in string:
            if char == "*" or char not in table.keys():
                raise Exception(f"Character {char} is not valid for barcode generation!")
            
    def generate_verification_digit(self, string : str):
        keys = list(table.keys())

        values = [keys.index(key) - 1 if key in string else 0 for key in keys]
        mod = sum(values) % 43
        return keys[mod + 1]