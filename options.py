from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class BarcodeOptions:
    string : str
    type : str
    base64 : bool = False
    compress : bool = False
    verification_digit : bool = False
    scale_factor : int = 3
    height : int = 80
    quiet_zone_size : int = 10