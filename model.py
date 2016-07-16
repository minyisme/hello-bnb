""" Models and database function for Hello AirBnB application"""

# python std libs

# third-part libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# connect to database here.
# replace "my_database" with the name of your database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///my_database'
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


if __name__ == "__main__":
    print "Successful Connected to database"