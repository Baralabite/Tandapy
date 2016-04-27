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

from Tandapy.util.Node import Node
from Tandapy.department.department import Department

class User(Node):
    def __init__(self, id, **kwargs):
        Node.__init__(self, id, **kwargs)

    def getResourceURL(self, id, **kwargs):
        url = "users/{}".format(id)

        if "show_wages" in kwargs and kwargs["show_wages"]:
            url += "&show_wages=true"

        return url

    def getDepartments(self):
        for departmentID in self.department_ids:
            print(departmentID)
        return [Department(departmentID) for departmentID in self.department_ids]