class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []
        for i in S:
            if(i=='#'):
                if(len(s1)>=1):
                    s1.pop()
            else:
                s1.append(i)
                
        for i in T:
            if(i=='#'):
                if(len(s2)>=1):
                    s2.pop()
            else:
                s2.append(i)
        return s1==s2                
                    
