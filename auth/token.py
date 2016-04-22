"""
The MIT License (MIT)

Copyright (c) 2016 John Board

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json


#TODO Very messy - can use username/password auth, although for the hackathon a token should be used


class Token:
    def __init__(self, username='', password='', scope='me', token=''):
        """

        :param username: Tanda username
        :param password: Tanda password
        :param scope: https://my.tanda.co/api/v2/documentation#header-scopes
        :return:
        """
        if username != '' and password != '':
            self.username = username
            self.password = password
            self.scope = scope

            self.authenticateToken()
        elif token != '':
            self.tokenString = token

        self.getTokenType = ''
        self.createdAt = 0
        self.scope = ''
        self.username = ''
        self.password = ''

    def getToken(self):
        return self.tokenString

    def getTokenType(self):
        return self.tokenType

    def createdAt(self):
        """
        :return: Unix datestamp of creation time of the token
        """
        return self.createdAt

    def getScope(self):
        """
        https://my.tanda.co/api/v2/documentation#header-scopes
        :return: Scope
        """
        return self.scope

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def authenticateToken(self):
        """
        Creates new token based on Tanda username, password and scope
        You can view your tokens here https://my.tanda.co/api/oauth/access_tokens
        """
        url = 'https://my.tanda.co/api/oauth/token'
        body = {'username': self.username, 'password': self.password, 'scope': self.scope, 'grant_type': 'password'}
        headers = {'Cache-Control': 'no-cache'}
        data  = requests.post(url, params=body, headers=headers)
        unpackedData = json.loads(data.content.decode('utf-8'))

        self.tokenType = str(unpackedData.get('token_type'))
        self.tokenString = str(unpackedData.get('access_token'))
        self.createdAt = int(unpackedData.get('created_at'))

    def __str__(self):
        return "<" + self.getTokenType() + " token (" + self.getToken() + ") created at " + str(self.createdAt) + ">"