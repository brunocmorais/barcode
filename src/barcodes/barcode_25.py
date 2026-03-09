from barcodes.barcode import Barcode

table = [6, 17, 9, 24, 5, 20, 12, 3, 18, 10]

class Barcode25(Barcode):

    def generate(self, string : str, with_verification_digit : bool):

        self.validate(string)

        barcode : list[bool] = []
        barcode.extend([True, False, True, False])

        if (len(string) + (1 if with_verification_digit else 0)) % 2 != 0:
            char_values = [0]
        else:
            char_values = []

        char_values.extend([int(c) for c in string])

        if with_verification_digit:
            char_values.append(int(self.generate_verification_digit(string)))

        narrow_wide = [table[item] for item in char_values]

        for char_1, char_2 in zip(narrow_wide[::2], narrow_wide[1::2]):
            for i in reversed(range(5)):
                item1 = self.bit_to_bool(char_1, i)
                item2 = self.bit_to_bool(char_2, i)
                count1 = 3 if item1 else 1
                count2 = 3 if item2 else 1
                barcode.extend([True] * count1)
                barcode.extend([False] * count2)

        barcode.extend([True, True, True, False, True])

        return barcode
    
    def validate(self, string : str):
        for char in string:
            if not char.isdigit():
                raise Exception("Only numbers are allowed!");

    def generate_verification_digit(self, string : str):
        even, odd = [], []
        digits = [int(c) for c in string]

        for (index, digit) in enumerate(reversed(digits)):
            if index % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)

        sum_digits = sum(even) * 3 + sum(odd)
        verification_digit = 0
        
        while (sum_digits + verification_digit) % 10 > 0:
            verification_digit += 1

        return str(verification_digit)