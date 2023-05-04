import re
from node import Node
from fact import Fact

sourceDiction = {}
sourceFacts = []

studentDiction = {}
studentFacts = []

totalScore = 20

def print_tree(node, level=0):
    if level == 0:
        print(node.name)
    else:
        pref = "├── "
        if node.leftChildElement is None and node.rightChildElement is None:
            pref = "└── " 
        print("|   " * (level-1) + pref + node.name)

    if node.leftChildElement is not None:
        print_tree(node.leftChildElement, level + 1)

    if node.rightChildElement is not None:
        print_tree(node.rightChildElement, level + 1)

def readingFromFile(lineTemp, bs= False):
    lineTemp = file.readline()
    lineTemp = lineTemp.strip()
    lineTemp = lineTemp.replace(" ", "")
    if(bs):
        tempArr = tempArr = re.findall(r'\w+|\\=|\S', lineTemp)
    else:
        tempArr = re.split(r'[(), ]+', lineTemp)
    return tempArr
    
def tree_builder(lineTemp, tempArr, sib = False, bs = False, nephew = False):
    treeRoot = Node(tempArr[0])
    leftChildFirst = Node(tempArr[1], parent=treeRoot)
    rightChildFirst = Node(tempArr[2], parent=treeRoot)
    treeRoot.addLeftChild(leftChildFirst)
    treeRoot.addRightChild(rightChildFirst)
    nodes.append(treeRoot)
    nodes.append(leftChildFirst)
    nodes.append(rightChildFirst)
    
    tempArr = readingFromFile(lineTemp=lineTemp)
    if(tempArr[1] == leftChildFirst.name):    
        tempRootSecond = Node(tempArr[0], parent=leftChildFirst)
    else:
        tempRootSecond = Node(tempArr[0], parent=rightChildFirst)
    leftChildSecond = Node(tempArr[1], parent=tempRootSecond)
    if(tempArr[2] != ''):
        rightChildSecond = Node(tempArr[2], parent=tempRootSecond)
        tempRootSecond.addRightChild(rightChildSecond)   
        nodes.append(rightChildSecond)
    tempRootSecond.addLeftChild(leftChildSecond)
    nodes.append(tempRootSecond)
    nodes.append(leftChildSecond)
    
    tempRootSecond.parentElement.addLeftChild(tempRootSecond)
    
    if(sib):
        tempArr = readingFromFile(lineTemp=lineTemp)    
        tempRoot = Node(tempArr[0], parent=leftChild)
        treeRoot.rightChildElement.addLeftChild(tempRoot)
        leftChild = Node(tempArr[1], parent=tempRoot)
        rightChild = Node(tempArr[2], parent=tempRoot)
        tempRoot.addLeftChild(leftChild)
        tempRoot.addRightChild(rightChild)    
        nodes.append(tempRoot)
        nodes.append(leftChild)
        nodes.append(rightChild)
        
        tempArr = readingFromFile(lineTemp=lineTemp, bs=True)
        tempRoot = Node(tempArr[1], parent=leftChild)
        treeRoot.leftChildElement.leftChildElement.addLeftChild(tempRoot)
        #leftChild.addLeftChild(tempRoot)
        leftChild = Node(tempArr[0], parent=tempRoot)
        rightChild = Node(tempArr[2], parent=tempRoot)
        tempRoot.addLeftChild(leftChild)
        tempRoot.addRightChild(rightChild)    
        nodes.append(tempRoot)
        nodes.append(leftChild)
        nodes.append(rightChild)
    else:
        tempArr = readingFromFile(lineTemp=lineTemp)
        if(tempArr[1] == leftChildSecond.name or rightChildSecond is None):
            tempRootThird = Node(tempArr[0], parent=leftChildSecond)
        else:
            tempRootThird = Node(tempArr[0], parent=rightChildSecond)
        leftChildThird = Node(tempArr[1], parent=tempRootThird)
        tempRootThird.addLeftChild(leftChildThird)
        rightChildThird = None
        if(tempArr[2] != '' and tempArr[2] != '.' and tempArr[2] != None):
            rightChildThird = Node(tempArr[2], parent=tempRootThird)
            tempRootThird.addRightChild(rightChildThird)
            nodes.append(rightChildThird)
        nodes.append(tempRootThird)
        nodes.append(leftChildThird)
        
        tempRootThird.parentElement.addLeftChild(tempRootThird)
        if(bs):
            tempArr = readingFromFile(lineTemp=lineTemp, bs=True)
            if(tempArr[0] == leftChildThird.name or rightChildThird is None):
                tempRootFourth = Node(tempArr[1], parent=leftChildThird)
            else:
                tempRootFourth = Node(tempArr[1], parent=rightChildThird)
            leftChildFourth = Node(tempArr[0], parent=tempRootFourth)
            tempRootFourth.addLeftChild(leftChildFourth)    
            nodes.append(tempRootFourth)
            nodes.append(leftChildFourth)
            if(tempArr[2] != '' and tempArr[2] != '.' and tempArr[2] != None):
                rightChildFourth = Node(tempArr[2], parent=tempRootFourth)
                tempRootFourth.addRightChild(rightChildFourth)
                nodes.append(rightChildFourth)
            tempRootFourth.parentElement.addLeftChild(tempRootFourth)

    
        if(nephew):
            tempArr = readingFromFile(lineTemp=lineTemp)    
            tempRoot = Node(tempArr[0], parent=treeRoot.rightChildElement)
            treeRoot.rightChildElement.addRightChild(tempRoot)
            leftChild = Node(tempArr[1], parent=tempRoot)
            rightChild = Node(tempArr[2], parent=tempRoot)
            tempRoot.addLeftChild(leftChild)
            tempRoot.addRightChild(rightChild)    
            nodes.append(tempRoot)
            nodes.append(leftChild)
            nodes.append(rightChild)
        
            tempArr = readingFromFile(lineTemp=lineTemp)
            tempRoot = Node(tempArr[0], parent=leftChild)
            leftChild.addLeftChild(tempRoot)
            leftChild = Node(tempArr[1], parent=tempRoot)
            tempRoot.addLeftChild(leftChild)
            nodes.append(tempRoot)
            nodes.append(leftChild)
        
    return treeRoot 


with open("student1.txt") as file:
    while True:
        lineTemp = file.readline().replace(" ", "")
        nodes = []
        if(lineTemp == '\n'):
            tk = treeRoot.name
            if(tk not in studentDiction):
                studentDiction[tk] = treeRoot
        if not lineTemp: #End of the File.
            tk = treeRoot.name
            if(tk not in studentDiction):
                studentDiction[tk] = treeRoot
            break
        lineTemp = lineTemp.strip()
        lineTemp = lineTemp.replace(" ", "")
        tempArr = re.split(r'[(), ]+', lineTemp)
        if(tempArr[len(tempArr) - 1] == '.'):
            tempFact = Fact(tempArr[0], tempArr[1], tempArr[2])
            studentFacts.append(tempFact)
        elif(tempArr[len(tempArr) - 1] == ':-'):
            tempKey = tempArr[0]
            if(tempKey == 'mother' or tempKey == 'father'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'brother' or tempKey == 'sister'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, bs=True)
            elif(tempKey == 'sibling'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, sib=True)  


def getTheMeaning(node):
    result = []
    if node is None:
        return result
    if node.leftChildElement is not None:
        result += getTheMeaning(node.leftChildElement)
    if node.rightChildElement is not None:
        result += getTheMeaning(node.rightChildElement)
    if len(node.name) > 1:
        result.append(node.__str__())
    return result

s = getTheMeaning(studentDiction['brother'])
s3 = getTheMeaning(studentDiction['father'])



with open("source.txt") as file:
    while True:
        lineTemp = file.readline().replace(" ", "")
        nodes = []
        if(lineTemp == '\n'):
            tk = treeRoot.name
            if(tk not in sourceDiction):
                sourceDiction[tk] = treeRoot
        if not lineTemp: #End of the File.
            tk = treeRoot.name
            if(tk not in sourceDiction):
                sourceDiction[tk] = treeRoot
            break
        lineTemp = lineTemp.strip()
        lineTemp = lineTemp.replace(" ", "")
        tempArr = re.split(r'[(), ]+', lineTemp)
        if(tempArr[len(tempArr) - 1] == '.'):
            tempFact = Fact(tempArr[0], tempArr[1], tempArr[2])
            sourceFacts.append(tempFact)
        elif(tempArr[len(tempArr) - 1] == ':-'):
            tempKey = tempArr[0]
            if(tempKey == 'mother' or tempKey == 'father'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'brother' or tempKey == 'sister'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, bs=True)
            elif(tempKey == 'sibling'):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, sib=True)
