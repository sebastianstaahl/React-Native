from flask import Flask, request, abort, jsonify
from sqlitedict import SqliteDict


userCredentials = SqliteDict("userCredentialsDB.sqlite", journal_mode="OFF")
trashData = SqliteDict("trashDataDB.sqlite", journal_mode="OFF")

app = Flask(__name__)

@app.route("/")
def mainPage():
	return "Hello"

@app.route("/login", methods=["POST"])
def login():
	username = request.json.get("username", None)
	password = request.json.get("password", None)

	if str(username) in userCredentials.keys() and str(userCredentials[username])== str(password):
		return jsonify(plastic=trashData[username]['plastic'], paper=trashData[username]['paper'], rest=trashData[username]['rest'])
	else:
		abort(403)


@app.route("/trash", methods=["POST"])
def trash():
	username = request.json.get("username", None)
	userdata = request.json.get("userdata", None)
	trashData[username] = userdata

	return 'Successfully added data'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
