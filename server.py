# python libs

# third party libs
from flask import Flask, render_template

# my libs
from model import Negro

# create app instance
app = Flask(__name__)

# all routes go here
@app.route('/')
def index():
	""" Homepage for Mayberry Tree """

	return render_template("index.html")

# run server file here
if __name__ == "__main__":

	app.run(debug=True)