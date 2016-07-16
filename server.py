# python libs



# third party libs
from flask import Flask, render_template

# custom libs
from model import Listing, Video, connect_to_db
from libs import *

# create app instance
app = Flask(__name__)

# all routes go here
@app.route('/')
def index():
    """ Homepage for Mayberry Tree """

    return render_template("index.html")

@app.route('/api/helloworld')
def helloworld():
    return '<html><body>hello world</body></html>'
    
@app.route('/api/add')
def route_add_listings():
    add_listings()
    return '<html><body>listings added</body></html>'

    
# run server file here
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=5001)