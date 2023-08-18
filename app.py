from flask import Flask, request
#from flask_cors import CORS, cross_origin
from face_service import validate_faces

app = Flask(__name__)
#cors = CORS(app)

#@cross_origin()
@app.route("/")
def index():
    return "Hi! Please visit the Github Repo (https://github.com/markvarga21/faceApi) for usage!"

#@cross_origin()
@app.route("/validate", methods=['GET'])
def validateImages():
    idPhoto = request.files['idPhoto']
    selfiePhoto = request.files['selfiePhoto']
    output = validate_faces(idPhoto, selfiePhoto)

    return output

if __name__ == '__main__':
    app.run(debug=True)