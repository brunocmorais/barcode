from pydantic import BaseModel, Field, validator
from barcodes.barcode_type import BarcodeType
from compressors.compressor_type import CompressorType
from contracts.output_type import OutputType

class BarcodeOptions(BaseModel):
    type : BarcodeType
    output_type : OutputType
    compressor : CompressorType = CompressorType.Uncompressed
    string : str = Field(min_length=2)
    verification_digit : bool = False
    scale_factor : int = Field(gt=0, default=3)
    height : int = Field(gt=0, default=75)
    quiet_zone_x : int = Field(ge=0, default=5)
    quiet_zone_y : int = Field(ge=0, default=5)

    @validator("compressor", pre=False)
    def validate_compressor(cls, value : CompressorType, values : dict):
        if value != CompressorType.Uncompressed and values.get("output_type") != OutputType.Base64:
            raise Exception("Compression only supported with base64!")
        
        return value