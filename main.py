from io import BytesIO
from typing import cast
from flask import Flask, request, Response
from barcodes.barcode_type import BarcodeType
from contracts.output_type import OutputType
from services.generator import BarcodeGenerator
from contracts.barcode_options import BarcodeOptions

app = Flask(__name__)

@app.post("/generate")
def post():
    try:
        return response(BarcodeOptions(**request.get_json()))
    except Exception as e:
        return { "error" : f"{e}" }, 400
    
@app.get("/<mode>/<type>/<string>")
def get(mode : str, type : str, string : str):
    try:
        return response(BarcodeOptions(string=string, type=BarcodeType(type), output_type=OutputType(mode)))
    except Exception as e:
        return { "error" : f"{e}" }, 400
    
def response(options : BarcodeOptions):
    result = BarcodeGenerator.generate(options)

    if options.output_type == OutputType.Image:
        return Response(BytesIO(cast(bytes, result)), mimetype="image/bmp")
    else:
        return { "result" : f"{result}" }
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)