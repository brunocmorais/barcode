import sys
from barcodes.barcode_type import BarcodeType
from factories.barcode_factory import BarcodeFactory


if len(sys.argv) < 3:
    print("Usage: python console.py <barcode_type> <barcode_string>")
    print("Available types: " + ", ".join([t.name for t in BarcodeType]))
    sys.exit(1)

barcode_type_value = sys.argv[1]
barcode_string = sys.argv[2]

try:
    barcode_type = BarcodeType(barcode_type_value)
except ValueError:
    print(f"Invalid barcode type: {barcode_type_value}")
    print("Available types: " + ", ".join([t.value for t in BarcodeType]))
    sys.exit(1)

barcode = BarcodeFactory.get(barcode_type)
bitstring = barcode.generate(barcode_string, False)
quiet_zone = ("\u2588" * 5)
result = quiet_zone + "".join(["\u2588" if b == 0 else " " for b in bitstring]) + quiet_zone

print()

for _ in range(7):
    print(result)

print()
