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
from Tandapy.util.requester import Requester
from Tandapy.user.user import User

class UserList(Requester):
    def __init__(self, token):
        Requester.__init__(self, token)

        self.users = {}
        self.fetchUsers()

    def fetchUsers(self, wages=False):
        request = "users?show_wages=true" if wages else "users"
        data = self.get(request)
        print(data)

        for userData in data:
            self.users[userData['id']] = User(userData)

    def deleteUser(self, id):
        self.delete("users/{}".format(id))
        del self.users[id]

    def getUser(self, id):
        return self.users[id]

    def getUserName(self, id):
        return self.users[id].name

    def getUserID(self, name):
        for user in self.users.values():
            if user.name == name:
                return user.id

    def getMe(self):
        data = self.get("users/me")
        return self.users[data['id']]
