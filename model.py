""" Models and database function for Hello AirBnB application"""

# python std libs

# third-part libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# connect to database here.
# replace "my_database" with the name of your database 
db = SQLAlchemy()

# All models go here

class Listing(db.Model):
    """Airbnb listings"""

    __tablename__ = "listings"

    listing_url = db.Column(db.String(1024), nullable=False, primary_key=True)
    airbnb_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):

        return ("<Listing listing_url=%s airbnb_id=%s>" %(self.listing_url, self.airbnb_id))



class Video(db.Model):
    """Listing videos"""

    __tablename__ = "videos"

    video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    video_url = db.Column(db.String(1024), nullable=False)
    listing_url = db.Column(db.String(1024), db.ForeignKey('listings.listing_url'), nullable=False)

    listing = db.relationship('Listing', backref='video')

    def __repr__(self):

        return ("<Video video_id=%s video_url=%s listing_url=%s>" %(self.video_id, self.video_url, self.listing_url))


def connect_to_db(app):    
    '''Create tables if none exist'''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///hello_bnb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # Test to see if our Video table exists
    query1 = """
    SELECT count(relname)
    FROM pg_class
    WHERE relname = 'videos'
    """
    db_cursor = db.session.execute(query1)
    row = db_cursor.fetchone()
    # Check to see if the table exists; 0 means to recreate everything
    if row[0] == 0:
        db.create_all()



if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Successful Connected to database"