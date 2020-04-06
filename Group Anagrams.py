class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for w in strs:
            sw="".join(sorted(w))
            
            if sw not in dict:
                dict[sw] = [w]
            else:
                dict[sw].append(w)
                
        res = []
        for i in dict.values():
            res.append(i)
        return res    
            
        
