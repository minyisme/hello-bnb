'''All the library things'''
from model import Listing, Video, db

def add_listings():
    listing_0 = Listing(listing_url="https://www.airbnb.com/rooms/3060662", airbnb_id="nija.mashruwala@gmail.com")
    db.session.add(listing_0)

    listing_1 = Listing(listing_url="https://www.airbnb.com/rooms/2386522", airbnb_id="nija.mashruwala@gmail.com")
    db.session.add(listing_1)

    db.session.commit()

    print "Listings successfully added."
	
