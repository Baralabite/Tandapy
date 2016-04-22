'''
Python methods for Tanda API.  You will need to install Requests: HTTP for Humans
pip install requests
http://docs.python-requests.org/en/master/
'''
import json

from util import requests


# Creates new token based on Tanda username, password and scope
# You can view your tokens here https://my.tanda.co/api/oauth/access_tokens
# View available scopes https://my.tanda.co/api/v2/documentation#header-scopes
def authenticate(username, password, scope = 'me'):
  url = 'https://my.tanda.co/api/oauth/token'
  body = {'username': username, 'password': password, 'scope': scope, 'grant_type': 'password'}
  headers = {'Cache-Control': 'no-cache'}
  data  = requests.post(url, params=body, headers=headers)
  token = str(json.loads(data.content.decode('utf-8')).get('access_token'))
  return token

#Get a token which you will use to authenticate yourself
#Seperate scopes with spaces or leave blank for default scope
#token = authenticate("john@johnrobboard.com", "tandahack2016", "user")

token = '7b644150f008d07360869b9b3e3ab3a67fabb6c6f7ac6ecc0a8c7967d210ccb2'

#Use token to get information about your user.
user = get("users", token)

#Print the content of the request i.e. user details
print(user.content)