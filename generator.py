from barcodes.barcode_39 import Barcode39
from bitmap import Bitmap
from factory import BarcodeFactory
from options import BarcodeOptions
from packbits import Packbits

class BarcodeGenerator:
    @staticmethod
    def generate(options : BarcodeOptions):
        if options.compress and not options.base64:
            raise Exception("Compress only supported with base64!")
        
        barcode = BarcodeFactory.get(options.type)
        bitmap = Bitmap()
        result = barcode.generate(options.string, options.verification_digit)
        pixels = bitmap.to_pixels(result, options)
        image = bytes(bitmap.to_bitmap(pixels))

        if options.compress:
            packbits = Packbits()
            compressed = bytearray([*packbits.compress(image)])
            return bytes(compressed)
        
        return image