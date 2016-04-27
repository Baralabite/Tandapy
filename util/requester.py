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
import requests
from Tandapy.auth.token import Token

token = ""

class Requester:
    def __init__(self):
        self.url = None             #Overwritten by subclasses

        self.base_url = "https://my.tanda.co/api/v2/"
        self.auth = 'Bearer ' + self.getToken().getToken()
        self.headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json', 'Authorization': self.auth}

    @staticmethod
    def getToken():
        return token

    @staticmethod
    def setToken(newToken):
        global token
        token = Token(token=newToken)

    def get(self, extension):
        try:
            print(self.base_url + extension)
            request = requests.get(self.base_url + extension, headers=self.headers)
            print(request.content.decode('utf-8'))
            data = json.loads(request.content.decode('utf-8'))
            return data
        except json.JSONDecodeError:
            raise Exception("Bad Tanda stuff happened.")

    def getRequestURL(self, extension):
        return (self.base_url + extension, self.headers)

    def post(self, extension, params):
        requests.post(self.base_url + self.url, params=params, headers=self.headers)

    def put(self, params):
        requests.put(self.base_url + self.url, params=params, headers=self.headers)

    def delete(self):
        requests.delete(self.base_url + self.url, headers=self.headers)


