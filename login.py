import urllib
import urllib2
import json
import os


def get_access_tokens(email, password):
    """get access tokens with airbnb login and password"""

    url = 'https://api.airbnb.com/v1/authorize'
    values = { 'client_id': '3092nxybyb0otqw18e8nh5nty','locale': 'en-US',
               'currency': 'USD', 'grant_type': 'password', 'password': os.environ['PASSWORD'],
               'username': os.environ['EMAIL'] }
    header = { 'User-Agent': 'Mozilla/4.0' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, header)
    response = urllib2.urlopen(req)
    print response
    result = json.load(response)
    print result

    access_token = result['access_token']
    print access_token
    response.close()

    return access_token

    
def get_user_info(access_token): 
    """use access token to get info about user"""

    url = 'https://api.airbnb.com/v1/account/active\?client_id\=3092nxybyb0otqw18e8nh5nty\&locale\=en-US\&currency\=USD\&alert_types%5B%5D\=reservation_request'
    values = { 'X-Airbnb-Oauth-Token': access_token }
    header = { 'User-Agent': 'Mozilla/4.0' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, header)
    response = urllib2.urlopen(req)
    result = json.load(response)
    print result

    response.close()

    return result

