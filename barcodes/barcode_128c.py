from barcodes.barcode import Barcode

table = [
    1740, 1644, 1638, 1176, 1164, 1100, 1224, 1220, 1124, 1608, 
    1604, 1572, 1436, 1244, 1230, 1484, 1260, 1254, 1650, 1628, 
    1614, 1764, 1652, 1902, 1868, 1836, 1830, 1892, 1844, 1842, 
    1752, 1734, 1590, 1304, 1112, 1094, 1416, 1128, 1122, 1672, 
    1576, 1570, 1464, 1422, 1134, 1496, 1478, 1142, 1910, 1678, 
    1582, 1768, 1762, 1774, 1880, 1862, 1814, 1896, 1890, 1818, 
    1914, 1602, 1930, 1328, 1292, 1200, 1158, 1068, 1062, 1424, 
    1412, 1232, 1218, 1076, 1074, 1554, 1616, 1978, 1556, 1146, 
    1340, 1212, 1182, 1508, 1268, 1266, 1956, 1940, 1938, 1758, 
    1782, 1974, 1400, 1310, 1118, 1512, 1506, 1960, 1954, 1502,
    1518, 1886, 1966
]

start_c = 1692
stop = 6379

# https://en.wikipedia.org/wiki/Code_128

class Barcode128C(Barcode):
    def generate(self, string : str, with_verification_digit : bool):

        barcode : list[bool] = []

        barcode.extend(self.number_to_bitarray(start_c, 11))

        if len(string) % 2 != 0:
            char_values = ['0']
        else:
            char_values = []

        char_values.extend([c for c in string])

        for char_1, char_2 in zip(char_values[::2], char_values[1::2]):
            bits = self.number_to_bitarray(table[int(char_1 + char_2)], 11)
            barcode.extend(bits)
        
        verification_digit = int(self.generate_verification_digit("".join(char_values)))

        barcode.extend(self.number_to_bitarray(table[verification_digit], 11))
        barcode.extend(self.number_to_bitarray(stop, 13))
        
        return barcode
    
    def validate(self, string : str):
        for char in string:
            if not char.isdigit():
                raise Exception("Only numbers are allowed!");

    def generate_verification_digit(self, string : str):
        sum = 105
        char_values = [c for c in string]

        for index, (char_1, char_2) in enumerate(zip(char_values[::2], char_values[1::2])):
            sum += int(char_1 + char_2) * (index + 1)

        return str(sum % 103)
