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

@app.route('/api/helloworld')
    return '<html><body>hello world</body></html>'
    
# run server file here
if __name__ == "__main__":

    app.run(debug=True, port=5001)