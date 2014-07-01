from flask import Flask
app = Flask(__retroti__)

@app.route('/')
def index():
	return "Emulator LTI"

if __retroti__ = '__main__':
	app.run()
