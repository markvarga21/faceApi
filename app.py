from flask import Flask, request
from face_service import validate_faces

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi! Please visit the Github Repo (https://github.com/markvarga21/faceApi) for usage!"

@app.route("/validate", methods=['GET'])
def validateImages():
    idPhoto = request.files['idPhoto']
    selfiePhoto = request.files['selfiePhoto']
    output = validate_faces(idPhoto, selfiePhoto)

    return output