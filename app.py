from flask import Flask, render_template
from config import *

app = Flask(__retroti__)

@app.route('/')
def index():
	return "Emulator LTI"

if __retroti__ = '__main__':
	app.run()
