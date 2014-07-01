from flask import Flask, make_response
from config import *

import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	return "Emulator LTI"

@app.route('/file/<int:file_id>')
def get_file(file_id):

	url ="%sfiles/%s?access_token=%s" % (API_URL, file_id, API_KEY)
	
	r = requests.get(url)
	data = r.json()
	
	imageRequest = requests.get(data["url"])

	resp = make_response(imageRequest.content)
	resp.headers['Content-Type'] = data["content-type"]

	return resp


if __name__ == '__main__':
	app.run()
