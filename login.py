import urllib
import urllib2
import json

# get access tokens with airbnb login and password
url = 'https://api.airbnb.com/v1/authorize'
values = { 'client_id': '3092nxybyb0otqw18e8nh5nty','locale': 'en-US',
           'currency': 'USD', 'grant_type': 'password', 'password': XXXXXXX,
           'username': 'email@gmail.com' }
header = { 'User-Agent': 'Mozilla/4.0' }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, header)
response = urllib2.urlopen(req)
print response
result = json.load(response)
print result


# use access_token to query for user information
access_token = result['access_token']
print access_token

response.close()

url = 'https://api.airbnb.com/v1/account/active\?client_id\=3092nxybyb0otqw18e8nh5nty\&locale\=en-US\&currency\=USD\&alert_types%5B%5D\=reservation_request'
values = { 'X-Airbnb-Oauth-Token': access_token }
header = { 'User-Agent': 'Mozilla/4.0' }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, header)
response = urllib2.urlopen(req)
print response
result = response.read()
print result

