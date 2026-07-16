class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        
        list1 = startTime.split(":")

        hours_sec = int(list1[0])*60*60
        minutes_sec = int(list1[1])*60
        sec = int(list1[2])

        start_sec = hours_sec+minutes_sec+sec

        list2 = endTime.split(":")

        hours_sec2 = int(list2[0])*60*60
        minutes_sec2 = int(list2[1])*60
        sec2 = int(list2[2])

        end_sec = hours_sec2+minutes_sec2+sec2


        return end_sec-start_sec