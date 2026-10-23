"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        maxRooms = 0

        starts = [] #meeting start times
        ends = [] # meeting end times

        for meeting in intervals: #runs O(n) times
            starts.append(meeting.start)
            ends.append(meeting.end)

        starts.sort()
        ends.sort() #this only works if we sort the lists

        l = 0#starts at start
        r = 0 #starts at ends #two pointers

        while l < len(intervals):
            if starts[l] < ends[r]: #this means: does this meeting start while another meeting hasnt ended? is the start time for this meeting less than this other metings end time? if so that meeting is still running and we need an extra room
                rooms += 1
                l += 1

            else: #this means: has this meating started after another meeting has ended? aka is the start time more than or equal to the end time? if so then we dont need a new room for this meeting! a room freed up so we can reduce our number of rooms
                rooms -= 1
                r += 1

            maxRooms = max(maxRooms, rooms)

        return maxRooms



        

        