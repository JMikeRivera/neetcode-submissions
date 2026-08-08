class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in range(len(s)):
            print(res)
            if s[i] in ["(", "{", "["]:
                res.append(s[i])
            elif res != []:
                if s[i] == ")":
                    if res[-1] != "(":
                        return False
                    res.pop()
                if s[i] == "}":
                    if res[-1] != "{":
                        return False
                    res.pop()
                if s[i] == "]":
                    if res[-1] != "[":
                        return False
                    res.pop()
            else: return False

        if res == []:
            return True
        else: return False