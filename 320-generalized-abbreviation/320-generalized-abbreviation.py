class Substring:
    def __init__(self,s=[],start=0,count=0):
        self.s = s
        self.start = start
        self.count = count

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        n = len(word)
        result = []
        que = deque()
        que.append(Substring())
        
        while que:
            curr_ab = que.popleft()
            
            if curr_ab.start == n:
                if curr_ab.count != 0:
                    curr_ab.s.append(str(curr_ab.count))
                result.append(''.join(curr_ab.s))
            
            else:
    
                que.append(Substring(list(curr_ab.s),curr_ab.start + 1,curr_ab.count + 1)) # abb form
                
                if curr_ab.count != 0:
                    curr_ab.s.append(str(curr_ab.count))
                
                new_word = list(curr_ab.s)
                new_word.append(word[curr_ab.start])
                que.append(Substring(new_word,curr_ab.start + 1,0))
        
        return result