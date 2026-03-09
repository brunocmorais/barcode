from barcodes.barcode import Barcode

table = {
    '0': 276, '1': 328, '2': 324, '3': 322, '4': 296, '5': 292, '6': 290, '7': 336, '8': 274, '9': 266, 'A': 424, 
    'B': 420, 'C': 418, 'D': 404, 'E': 402, 'F': 394, 'G': 360, 'H': 356, 'I': 354, 'J': 308, 'K': 282, 'L': 344, 
    'M': 332, 'N': 326, 'O': 300, 'P': 278, 'Q': 436, 'R': 434, 'S': 428, 'T': 422, 'U': 406, 'V': 410, 'W': 364, 
    'X': 358, 'Y': 310, 'Z': 314, '-': 302, '.': 468, ' ': 466, '$': 458, '/': 366, '+': 374, '%': 430, '!': 294, 
    '#': 474, '¬': 470, '&': 306, '*': 350, 
}

unallowed = ["!", "#", "-", "&", "*"]

# https://web.archive.org/web/20090225114452/http://www.barcodeisland.com/code93.phtml

class Barcode93(Barcode):

    def generate(self, string : str, with_verification_digit : bool):

        self.validate(string)

        barcode : list[bool] = []

        char_values = ["*", *[c for c in string + self.generate_verification_digit(string)], "*"]

        narrow_wide = [table[item] for item in char_values]

        for char_value in narrow_wide:
            for i in reversed(range(9)):
                item = self.bit_to_bool(char_value, i)
                barcode.append(item)

        barcode.append(True)

        return barcode
    
    def validate(self, string : str):
        for char in string:
            if char == "*" or char not in table.keys() or char in unallowed:
                raise Exception(f"Character {char} is not valid for barcode generation!")
            
    def generate_verification_digit(self, string : str):
        digit_c = self.generate_digit(string)
        digit_k = self.generate_digit(string + digit_c)
        return digit_c + digit_k

    def generate_digit(self, string : str):
        keys = list(table.keys())

        counter = len(string)
        result = 0

        for char in string:
            result += counter * keys.index(char)
            counter -= 1

        mod = result % 47
        return keys[mod]