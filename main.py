from io import BytesIO
from flask import Flask, request, Response
from generator import BarcodeGenerator
from options import BarcodeOptions
import base64

app = Flask(__name__)

@app.post("/")
def post():
    try:
        options = BarcodeOptions(**request.get_json())
        image = BarcodeGenerator.generate(options)

        if options.base64:
            return { "result" : f"{base64.b64encode(image).decode("utf-8")}" }
        else:
            return Response(BytesIO(image), mimetype="image/bmp")
    except Exception as e:
        return { "error" : f"{e}" }, 400
    
@app.get("/<mode>/<type>/<string>")
def get(mode : str, type : str, string : str):
    try:
        b64 : bool

        match mode:
            case "image" : b64 = False
            case "base64" : b64 = True
            case _ : raise Exception("Unknown mode, valid modes are 'image' and 'base64'.")

        options = BarcodeOptions(string, type)
        image = BarcodeGenerator.generate(options)

        if b64:
            return { "result" : f"{base64.b64encode(image).decode("utf-8")}" }
        else:
            return Response(BytesIO(image), mimetype="image/bmp")
    except Exception as e:
        return { "error" : f"{e}" }, 400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)