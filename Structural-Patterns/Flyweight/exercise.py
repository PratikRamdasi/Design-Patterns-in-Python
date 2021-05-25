class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(' ')
        self.tokens = {}
        # self.caps = [False] * len(self.words)

    class WordCapitalizer:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    # def capitalize(self, idx): # capitalize word at index idx
    #    self.caps[idx] = True
    # __getitem__ used to access list items
    def __getitem__(self, item):
        wc = self.WordCapitalizer()
        self.tokens[item] = wc
        return self.tokens[item]
    
    def __str__(self):
        result = []
        
        for i in range(len(self.words)):
            w = self.words[i]
            if i in self.tokens and self.tokens[i].capitalize:
                # word needs to be capitalized
                w = w.upper()
            result.append(w)
    
        return ' '.join(result)


if __name__ == "__main__":
    ft = Sentence('hello world')
    ft[0].capitalize = True
    print(ft) # hello WORLD