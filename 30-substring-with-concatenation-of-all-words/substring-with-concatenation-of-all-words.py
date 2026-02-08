from collections import Counter , defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]: 

        if not s or not words:
            return []

        totalWords = len(words) 
        wordLen = len(words[0])
        wordCount = Counter(words)
        totalLen = totalWords * wordLen # input s me kaha tak dhund na he 
        result = []

        for i in range(wordLen):
            left = i
            curr = defaultdict(int)
            matched = 0 

            for right in range(i , len(s) - wordLen + 1 , wordLen):
                word = s[right : right + wordLen]
                if word in wordCount:
                    curr[word] += 1
                    matched += 1
                    while curr[word] > wordCount[word]:
                        leftWord = s[left : left + wordLen]  
                        curr[leftWord] -= 1
                        matched -= 1
                        left += wordLen

                    if matched == totalWords:
                        result.append(left)
                else:
                    curr.clear()
                    matched = 0
                    left = right + wordLen

        return result
# Note dry run remaining