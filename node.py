class Node:
    name = ""
    relationship = ""
    def __init__(self, n, parent = None, leftChild = None, rightChild = None):
        self.name = n
        self.parentElement = parent
        self.leftChildElement = leftChild
        self.rightChildElement = rightChild 
    
    def addLeftChild(self, tempNode):
        self.leftChildElement = tempNode
        #tempNode.parentElement = self
    
    def addRightChild(self, tempNode):
        self.rightChildElement = tempNode
        #tempNode.parentElement = self
    
    def connectEdges(self, toNode):
        self.childElement = toNode
        toNode.parentElement = toNode
    
    @property
    def getName(self):
        return self.name