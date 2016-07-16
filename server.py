# python libs
import os

# third party libs
from flask import Flask, render_template
from werkzeug import SharedDataMiddleware
# custom libs
from model import Listing, Video, connect_to_db
from libs import *

# Set up storage for uploaded photos
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])


# Create app
app = Flask(__name__, static_url_path="/static")

# Handles users uploaded files and builds path to uploads folder
# so that uploaded files can be served as '/uploads/<name-of-file>'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

# all routes go here
@app.route('/')
def index():
    """ Homepage for Mayberry Tree """

    # return render_template("frontend.html", video_loc='/uploads/sample.mp4')

    return render_template("index.html")

@app.route('/helloworld')
def helloworld():
    return '<html><body><h1 style="color:white">hello world</h1><video id="videoSample" src="https://s3-us-west-2.amazonaws.com/hellobnb/m09yFoF+copy.mp4" height="720" width="1280" autoplay="autoplay"></video></body></html>'
    
@app.route('/api/add-listing')
def route_add_listings():
    """Hard coded two listings in libs.py to add to server"""

    add_listings()
    return '<html><body>listings added</body></html>'

@app.route('/api/get')
def get_video_to_display():
    """Get request from DirecTV including the listing_url to query the db to find the relevant video and text to display to renter"""

    video_obj = get_video_for_listing()

    return render_template("frontend.html", video=video_obj)

    
# run server file here
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=5001, host="0.0.0.0")


# Load web page on
# STB URL parameters must be escaped      http://10.10.31.132:8080/itv/startURL?url=http://10.10.31.78:5001
# Stop currently running app              http://10.10.31.132:8080/itv/stopITV
# Retrieve WebKit logs from STB           http://10.10.31.132:8080/itv/getLogs

