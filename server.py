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
    
@app.route('/api/add-listing')
def route_add_listings():
    """Hard coded two listings in libs.py to add to server"""

    add_listings()
    return '<html><body>listings added</body></html>'

@app.route('/api/get', methods=["GET"])
def get_video_to_display():
    """Get request from DirecTV including the listing_url to query the db to find the relevant video and text to display to renter"""

    video_obj = get_video_for_listing(request)

    return '<html><body>FIX ME: DirectTV</body></html>'

    
# run server file here
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=5001)