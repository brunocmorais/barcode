from enum import Enum

class CompressorType(Enum):
    Uncompressed = "none"
    Packbits = "packbits"
    RLE = "rle"