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
def get_video_for_listing():
    """Queries db for video object by listing_url"""

    listing_url = 'https://www.airbnb.com/rooms/2386522'

    video = Video.query.filter_by(listing_url=listing_url).one()

    return video

# Used by Swift app
def add_video(request):
    """Adds video object info to db"""

    listing_url = request.form.get('listing_url')
    video_url = request.form.get('video_url')
    info_text = request.form.get('info_text')

    video = Video(video_url=video_url, listing_url=listing_url, info_text=info_text)

    db.session.add(video)

    db.session.commit()

    return video
