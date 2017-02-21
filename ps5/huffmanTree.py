class huffmanNode:
    def __init__(self, keyVal, leftNode=None, rightNode=None):
        self.parentNode = None
        self.keyVal = keyVal
        if (leftNode):
            self.leftNode = leftNode
        if (rightNode):
            self.rightNode = rightNode
    def parent(self, x=None):
        if (x == None):
            return self.parentNode
        self.parentNode = x
    def left(self, x=None):
        if (x == None):
            return self.leftNode
        self.leftNode = x
    def right(self, x=None):
        if (x == None):
            return self.rightNode
        self.rightNode = x
    def key(self, x=None):
        if (x == None):
            return self.keyVal
        self.key = x
