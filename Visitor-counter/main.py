import os
from flask import Flask, request
from google.cloud import firestore
from flask import jsonify
from flask_cors import CORS, cross_origin

db = firestore.Client(project="api-dev-417502",
                      database="(default)",
                      credentials=os.environ.get("/home/hazzemammar/visitorcounter/api-dev-417502-5480183e4ee0.json"))
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

ref = db.collection(u'viewer-count').document('ZpQWEMVcYPFWq45q4hQ2')

@app.route("/", methods=['POST', 'OPTIONS'])
@cross_origin()
def view_count():
    ref.update({"count": firestore.Increment(1)});
    viewcount = ref.get().to_dict()['count']
    response = jsonify({'ViewCount': viewcount})
    print("Returning: ", response)
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
