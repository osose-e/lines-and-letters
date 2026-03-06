import os
import firebase_admin
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS

# Initialize Firebase (databaseURL from env for flexibility when recreating project)
_default_db_url = "https://lines-and-letters-game-default-rtdb.firebaseio.com/"
_credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
cred = firebase_admin.credentials.Certificate(_credentials_path)
firebase_admin.initialize_app(cred, {
    "databaseURL": os.environ.get("FIREBASE_DATABASE_URL", _default_db_url),
})

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
api = Api(app)

# Register API blueprints
from api.APIHandler import APIHandler
from api.lobbyAPI import lobby_api
from api.dotsandboxesAPI import dotsandboxes_api
from api.anagramsAPI import anagrams_api
from api.usersAPI import users_api

api.add_resource(APIHandler, '/flask/hello')
app.register_blueprint(lobby_api)
app.register_blueprint(dotsandboxes_api)
app.register_blueprint(anagrams_api)
app.register_blueprint(users_api)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Cache-Control', 'public, max-age=60, s-maxage=60')
  return response


# Ensure CORS preflight (OPTIONS) is handled so browser requests from Firebase Hosting succeed
@app.route('/<path:path>', methods=['OPTIONS'])
def options_catch_all(path):
  return '', 204

# Serve frontend files
@app.route("/", defaults={'path':''})
def getApp(path):
    return send_from_directory(app.static_folder,'index.html')

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = int(os.environ.get("PORT", 8080)))