from flask import Flask, make_response
#from config import *

import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	return "Emulator LTI"

@app.route('/file/<int:file_id>')
def get_file(file_id):
	url = "https://webcourses2c.test.instructure.com/api/v1/files/%s?access_token=blah" % file_id
	r = requests.get(url)
	data = r.json()
	print data
	imageRequest = requests.get(data["url"])

	resp = make_response(imageRequest.content)
	resp.headers['Content-Type'] = data["content-type"]

	return resp


if __name__ == '__main__':
	app.run()
