'''
- find the len of total sum
- apply subarray of size k logic and 
- if subArray is == k and checkValidaity()
    - store winddow_start
-   - window_start += 1

'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        
        k = len(words)
        
        w = len(words[0])
        
        window_start = 0
        
        res = []
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        words.sort()
        def checkValidity(si,ei):
            if ei - si + 1 == w*k:
                    words_coll = s[si:ei+1]
                    words_coll = [words_coll[i:i+w] for i in range(0,len(words_coll),w)]
                    visited = freq.copy()
                    words_coll.sort()
                    for i in range(k):
                        if words_coll[i] != words[i]:
                            return False
                            
                    return True
                
        for window_end in range(n):
            if window_end - window_start + 1 == w * k:
                if checkValidity(window_start,window_end):
                    res.append(window_start)
                window_start += 1
        
        return res