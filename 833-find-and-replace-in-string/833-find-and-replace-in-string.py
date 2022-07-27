class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        '''
        abcd 
        0 1
        a cd
        eee ffff
        
        for index,substr,replacestr in zip(indices,sources,targets):
                if  substr == s[index:index + len(substr)]:
                        s = s[:index] + replacestr + s[index + len(substr):]
        
        
        
        '''
        offset  = 0
        for index,substr,replacestr in sorted(zip(indices,sources,targets)):
            # print(substr)
            # print(s[index+offset:index+offset + len(substr)])
            # print(index + offset)
            updated_index = index + offset
            if  substr == s[updated_index:updated_index + len(substr)]:
                s = s[:updated_index] + replacestr + s[updated_index + len(substr):]
                offset +=  len(replacestr) - len(substr)

        return s