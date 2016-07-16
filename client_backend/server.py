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

@app.route('/login', methods=["POST"])
def user_login():
    """Post request from Swift app containing email and password that will be passed along to the airbnb authorization to be validated"""

    user_email = request.form.get('email')
    user_password = request.form.get('password')

    return """FIX ME: send email and password to airbnb login"""

@app.route('/logout')
def user_logout():
    """Logs out from airbnb"""

    """FIX ME"""
    pass

@app.route('/api/add-video', methods=["POST"])
def route_add_video():

    # Test 
    listing_url = request.form.get('listing_url')
    video_url = request.form.get('video_url')
    info_text = request.form.get('info_text')

    # video_obj = add_video(request)

    return """FIX ME: confirmation that video has been added"""

# run server file here
if __name__ == "__main__":

	app.run(debug=True)