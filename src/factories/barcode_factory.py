from barcodes.barcode import Barcode
from barcodes.barcode_128c import Barcode128C
from barcodes.barcode_25 import Barcode25
from barcodes.barcode_39 import Barcode39
from barcodes.barcode_93 import Barcode93
from barcodes.barcode_codabar import BarcodeCodabar
from barcodes.barcode_ean13 import BarcodeEAN13
from barcodes.barcode_ean8 import BarcodeEAN8
from barcodes.barcode_type import BarcodeType
from barcodes.barcode_upca import BarcodeUPCA
from factories.abstract_factory import AbstractFactory

class BarcodeFactory(AbstractFactory[BarcodeType, Barcode]):
    @staticmethod
    def get(type : BarcodeType) -> Barcode:
        match type:
            case BarcodeType.Barcode25: return Barcode25()
            case BarcodeType.Barcode39: return Barcode39()
            case BarcodeType.BarcodeEAN13: return BarcodeEAN13()
            case BarcodeType.BarcodeEAN8: return BarcodeEAN8()
            case BarcodeType.BarcodeUPCA: return BarcodeUPCA()
            case BarcodeType.Barcode128C: return Barcode128C()
            case BarcodeType.Barcode93: return Barcode93()
            case BarcodeType.BarcodeCodabar: return BarcodeCodabar()

