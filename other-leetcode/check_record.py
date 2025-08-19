# Author aw.ahmed.werghi@gmail.com
# problem statement : https://leetcode.com/problems/student-attendance-record-i/description/

class Solution:
    def checkRecord(self, s: str) -> bool:
        count_consecutive_not_late = 0
        count_absences = 0
        ok = True
        for i in range(len(s)):
            if s[i] == 'A' :
                count_absences += 1
                count_consecutive_not_late = 0
            elif s[i] == 'L' :
                count_consecutive_not_late += 1
                if count_consecutive_not_late == 3:
                    ok = False
            else :
                count_consecutive_not_late = 0

        if count_absences < 2 and ok :
            return True
        else :
            return False

s = Solution()
print(s.checkRecord("PPALLP")) # output : True
print(s.checkRecord("PPALLL")) # output : False
