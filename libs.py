'''All the library things'''
from model import Listing, Video, db
from flask_sqlalchemy import SQLAlchemy

# Set up
def add_listings():
    """Hard coded two of Nija's listings to add to db"""

    listing_0 = Listing(listing_url="https://www.airbnb.com/rooms/3060662", airbnb_id="nija.mashruwala@gmail.com")
    db.session.add(listing_0)

    listing_1 = Listing(listing_url="https://www.airbnb.com/rooms/2386522", airbnb_id="nija.mashruwala@gmail.com")
    db.session.add(listing_1)

    db.session.commit()

    print "Listings successfully added."
	
# Used by DirecTV
def get_video_for_listing(listing_url):
    """Queries db for video object by listing_url"""

    video = Video.query.filter_by(listing_url=listing_url).one()

    return video

# Used by Swift app
