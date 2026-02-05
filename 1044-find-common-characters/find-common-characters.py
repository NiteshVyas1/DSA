class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word) # &= means words[0] & min_freq i.e further words (dono ka common milta hai & operator se)
        return list(min_freq.elements())  # counter stores {'e':1, 'l':2} but elements expands frequncies output ["e", "l", "l"]