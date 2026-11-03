class WordDictionary:

    def __init__(self):
        self.map = {}

    def addWord(self, word: str) -> None:
        curr = self.map
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
                
        curr["*"] = {}

    def search(self, word: str) -> bool:
        
        
        def to_search(idx, curr):
            if not curr:
                return False
            if idx == len(word) and "*" in curr:
                return True
            elif idx == len(word):
                return False
        

            if word[idx] in curr:
                retVal = to_search(idx + 1, curr[word[idx]])
            elif word[idx] == ".":
                for key in curr:
                    retVal = to_search(idx + 1, curr[key])
                    if retVal:
                        return True
            elif word[idx] not in curr:
                return False


            return retVal
        
        return to_search(0, self.map)


            
            

