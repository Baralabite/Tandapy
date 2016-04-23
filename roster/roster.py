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

from Tandapy.util.requester import Requester
from Tandapy.schedule.schedule import Schedule
from Tandapy.schedule.schedulelist import ScheduleList
import pprint

class Roster(Requester):
    def __init__(self, token, id=None, on=None, current=False, show_costs=False):
        Requester.__init__(self, token)
        self.roster = {}

        if current:
            request = "rosters/current"
        elif on:
            request = "rosters/on/{}".format(on)
        elif id:
            request = "roster/{}".format(id)

        if show_costs:
            request += "&show_costs=true"

        data = self.get(request)

        for day in data["schedules"]:
            date = day["date"]
            schedules = day["schedules"]
            self.roster[date] = ScheduleList(token, scheduleListData=schedules)

    def getScheduleOnDate(self, date):
        return self.roster[date]

    def getWeekDates(self):
        return list(self.roster.keys())

