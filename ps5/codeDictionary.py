class dictionaryNode:
    def __init__(self, index, freq, children=[]):
        self.index = index
        self.freq = freq
        self.children = children
        self.encoding = ''

    # Appends x to beginning of encoding and the beginning of all children's encoding
    def addToCode(self,x):
        self.encoding = x + self.encoding
        for i in range(0, len(self.children)):
            self.children[i].addToCode(x)
