from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
client = pymongo.MongoClient('mongodb+srv://200527804mini:Minibus123@cluster0.pcvneej.mongodb.net/?retryWrites=true&w=majority')
mongo_db = client.Cluster0
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		results = mongo_db.Cluster0.find_one({}, {'_id': 0})
		return jsonify(results)


# driver function
if __name__ == '__main__':
	app.run(debug = True)
