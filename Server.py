from flask import Flask,request
import base64
import io
from PIL import Image
from main import ExecuteProcess
from ExtractInfoFromDiploma import ExecuteDiplomaProcess

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route('/getimage', methods=['POST'])
def handle_form():
    payload = request.form.to_dict(flat=False)
    im_b64 = payload['image'][0]
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    img = Image.open(buf)
    img.save("Uploads/permis.PNG")

    return ExecuteProcess()

@app.route('/getdiploma', methods=['POST'])
def handle_form_diploma():
    payload = request.form.to_dict(flat=False)
    im_b64 = payload['image'][0]
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    img = Image.open(buf)
    img.save("Uploads/diplome1.jpg")

    return ExecuteDiplomaProcess()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

