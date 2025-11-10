

from barcodes.barcode import Barcode
from barcodes.barcode_128c import Barcode128C
from barcodes.barcode_25 import Barcode25
from barcodes.barcode_39 import Barcode39
from barcodes.barcode_ean13 import BarcodeEAN13
from barcodes.barcode_ean8 import BarcodeEAN8
from barcodes.barcode_type import BarcodeType
from barcodes.barcode_upca import BarcodeUPCA

class BarcodeFactory:

    @staticmethod
    def get(type : str) -> Barcode:
        try:
            barcode_type = BarcodeType(type)
        except:
            valid_types = [type.value for type in BarcodeType]
            raise Exception(f"Type '{type}' is not valid, available types are: {", ".join(valid_types)}")

        match barcode_type:
            case BarcodeType.Barcode25: return Barcode25()
            case BarcodeType.Barcode39: return Barcode39()
            case BarcodeType.BarcodeEAN13: return BarcodeEAN13()
            case BarcodeType.BarcodeEAN8: return BarcodeEAN8()
            case BarcodeType.BarcodeUPCA: return BarcodeUPCA()
            case BarcodeType.Barcode128C: return Barcode128C()
