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

from Tandapy.auth.token import Token

from Tandapy.user.userlist import UserList
from Tandapy.department.departmentlist import DepartmentList
from Tandapy.schedule.schedulelist import ScheduleList
from Tandapy.role.rolelist import RoleList
from Tandapy.leave.leavelist import LeaveList
from Tandapy.shift.shiftlist import ShiftList
from Tandapy.award.awardlist import AwardList
from Tandapy.unavailability.unavailabilitylist import UnavailabilityList

from Tandapy.roster.roster import Roster


class Tanda:
    def __init__(self):
        pass

    def authenticate(self, token):
        """
        This function is a quick fix for the hackathon. Provide a token gained by following these instructions:
        https://docs.google.com/document/d/1-P9DbnG7iCupIToRaaOwUQ01IBUf_qltVrYmoan9Gh8/edit#
        :param token: Auth token
        """
        self.token = Token(token=token)


    def getCurrentRoster(self):
        return Roster(self.token, current=True)

    def getRosterOn(self, date):
        return Roster(self.token, on=date)

    def getRoster(self, id):
        return Roster(self.toke, id=id)


    def getUsers(self):
        """
        :return: List of User objects
        """
        return UserList(self.token)

    def getDepartments(self):
        return DepartmentList(self.token)


    def getSchedule(self):
        return ScheduleList(self.token)

    def getRole(self):
        return RoleList(self.token)

    def getShift(self):
        return ShiftList(self.token)

    def getLeave(self):
        return LeaveList(self.token)

    def getAward(self):
        return AwardList(self.token)

    def getUnavailability(self):
        return UnavailabilityList(self.token, fromDate='2016-03-15', toDate='2016-04-05')