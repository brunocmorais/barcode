from barcodes.barcode import Barcode

table_l = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
table_g = [39, 51, 27, 33, 29, 57, 5, 17, 9, 23]
table_r = [114, 102, 108, 66, 92, 78, 80, 68, 72, 116]
table_ean = [0, 11, 13, 14, 19, 25, 28, 21, 22, 26]

class BarcodeEAN13(Barcode):
    def generate(self, string : str, with_verification_digit : bool) -> list[bool]:
        
        self.validate(string)

        digits = [int(d) for d in string]
        first_digit = int(digits[0])
        ean_rule = table_ean[first_digit]
        barcode : list[bool] = [True, False, True]

        for (index, digit) in enumerate(digits[1:7]): # first group
            table = table_g if self.bit_to_bool(ean_rule, 5 - index) else table_l
            barcode.extend(self.number_to_bitarray(table[digit], 7))

        barcode.extend([False, True, False, True, False])

        for digit in digits[7:13]: # second group
            barcode.extend(self.number_to_bitarray(table_r[digit], 7))

        barcode.extend([True, False, True])

        return barcode
    
    def validate(self, string : str):
        for char in string:
            if not char.isdigit():
                raise Exception("Only numbers are allowed!");

        if len(string) != 13:
            raise Exception("EAN-13 must have 13 digits!")

    def generate_verification_digit(self, string : str):
        raise NotImplementedError("EAN-13 doesn't generate verification digit!")