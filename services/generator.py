import base64
from compressors.compressor_type import CompressorType
from contracts.output_type import OutputType
from factories.compressor_factory import CompressorFactory
from imaging.bitmap import Bitmap
from factories.barcode_factory import BarcodeFactory
from contracts.barcode_options import BarcodeOptions
from compressors.packbits import Packbits

class BarcodeGenerator:
    @staticmethod
    def generate(options : BarcodeOptions) -> bytes | str:
        barcode = BarcodeFactory.get(options.type)
        bitmap = Bitmap()
        result = barcode.generate(options.string, options.verification_digit)

        match options.output_type:
            case OutputType.Image:
                pixels = bitmap.to_pixels(result, options)
                return bytes(bitmap.to_bitmap(pixels))
            case OutputType.Base64:
                pixels = bitmap.to_pixels(result, options)
                image = bytes(bitmap.to_bitmap(pixels))

                if options.compressor != CompressorType.Uncompressed:
                    compressor = CompressorFactory.get(options.compressor)
                    compressed = bytearray([*compressor.compress(image)])
                    return base64.b64encode(bytes(compressed)).decode("utf-8")
                else:
                    return base64.b64encode(image).decode("utf-8")
            case OutputType.BitString:
                return "".join(["1" if bit else "0" for bit in result])