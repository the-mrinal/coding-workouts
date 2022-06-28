class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        min_citation = 0
        max_h_index = 0
        for i in range(len(citations)):
            min_citation = citations[i]
            if i + 1 <= min_citation:
                max_h_index = i + 1
        return max_h_index
