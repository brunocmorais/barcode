from barcodes.barcode import Barcode

table_l = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
table_r = [114, 102, 108, 66, 92, 78, 80, 68, 72, 116]

class BarcodeUPCA(Barcode):
    def generate(self, string : str, with_verification_digit : bool) -> list[bool]:
        
        self.validate(string)

        digits = [int(d) for d in string]
        barcode : list[bool] = [True, False, True]

        for (index, digit) in enumerate(digits):

            if index == 6:
                barcode.extend([False, True, False, True, False])

            if (index < 6):
                barcode.extend(self.number_to_bitarray(table_l[digit], 7))
            else:
                barcode.extend(self.number_to_bitarray(table_r[digit], 7))

        barcode.extend([True, False, True])

        return barcode
    
    def validate(self, string : str):
        for char in string:
            if not char.isdigit():
                raise Exception("Only numbers are allowed!");

        if len(string) != 12:
            raise Exception("UPC-A must have 12 digits!")

    def generate_verification_digit(self, string : str):
        raise NotImplementedError("UPC-A doesn't generate verification digit!")