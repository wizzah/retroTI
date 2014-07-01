from flask import Flask, render_template
from config import *

app = Flask(__name__)

@app.route('/')
def index():
	return "Emulator LTI"

if __name__ == '__main__':
	app.run()
