from flask import Flask, make_response, jsonify
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

@app.route('/file_list/<int:course_id>')
def file_list(course_id):
	url ="%scourses/%s/files?access_token=%s" % (API_URL, course_id, API_KEY)
	
	r = requests.get(url)
	data = r.json()
	
	files = {'files': []}
	
	for f in data:
		files['files'].append({'filename': f['filename'], 'id': f['id'], 'content-type':f['content-type']})
	
	return jsonify(**files)

if __name__ == '__main__':
	app.run()
