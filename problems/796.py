class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
        if goal == s:
            return True
        
        new_s = self.helper(list(s))

        while(goal != "".join(new_s)):
            if "".join(new_s) == s:
                return False
            new_s = self.helper(new_s)
    
        return True

    def helper(self, lst):
        temp = lst[0]
        lst.pop(0)
        lst.append(temp)
        return lst

