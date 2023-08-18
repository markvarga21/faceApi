from flask import Flask, request
from flask_cors import CORS, cross_origin
from face_service import validate_faces
import json

app = Flask(__name__)
cors = CORS(app)

@cross_origin()
@app.route("/validate", methods=['GET'])
def hello_world():
    idPhoto = request.files['idPhoto']
    selfiePhoto = request.files['selfiePhoto']
    output = validate_faces(idPhoto, selfiePhoto)

    return output