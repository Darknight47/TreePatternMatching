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
    
    def addRightChild(self, tempNode):
        self.rightChildElement = tempNode
    
    def connectEdges(self, toNode):
        self.childElement = toNode
        toNode.parentElement = toNode
    
    @property
    def getName(self):
        return self.name

    def __str__(self):
        if len(self.name) > 1:
            if self.leftChildElement is not None and self.rightChildElement is None:
                return f"{self.leftChildElement.name} is a {self.name}."
            elif self.leftChildElement is not None and self.rightChildElement is not None:
                if self.leftChildElement.parentElement.name == '\=':
                    return f"{self.leftChildElement.name} is not the same ({self.name}) as {self.rightChildElement.name}."
                return f"{self.leftChildElement.name} is the {self.name} of the {self.rightChildElement.name}."
            elif self.leftChildElement is None and self.rightChildElement is not None:
                return f"{self.rightChildElement.name} is {self.name}."