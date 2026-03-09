from compressors.compressor import Compressor
from compressors.compressor_type import CompressorType
from compressors.packbits import Packbits
from compressors.simple_rle import SimpleRLE
from factories.abstract_factory import AbstractFactory


class CompressorFactory(AbstractFactory[CompressorType, Compressor]):
    @staticmethod
    def get(type : CompressorType) -> Compressor:
        match type:
            case CompressorType.Packbits: return Packbits()
            case CompressorType.RLE: return SimpleRLE()
            case _: raise Exception("Unimplemented compressor!")