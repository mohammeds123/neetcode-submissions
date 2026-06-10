class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare_str = s.replace(" ", "").lower()
        final = "".join(char for char in compare_str if char.isalnum())
        x = 0
        y = len(final) - 1
        while x < y:
            if final[x] == final[y]:
                x+=1
                y-=1
            else:
                return False
        return True