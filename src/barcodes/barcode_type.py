from enum import Enum

class BarcodeType(Enum):
    Barcode25 = "2-of-5"
    Barcode39 = "3-of-9"
    Barcode93 = "CODE-93"
    BarcodeEAN13 = "EAN-13"
    BarcodeEAN8 = "EAN-8"
    BarcodeUPCA = "UPC-A"
    Barcode128C = "128C"
    BarcodeCodabar = "Codabar"