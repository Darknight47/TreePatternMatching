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
    leftChild = Node(tempArr[1], parent=treeRoot)
    rightChild = Node(tempArr[2], parent=treeRoot)
    treeRoot.addLeftChild(leftChild)
    treeRoot.addRightChild(rightChild)
    nodes.append(treeRoot)
    nodes.append(leftChild)
    nodes.append(rightChild)
    
    tempArr = readingFromFile(lineTemp=lineTemp)    
    tempRoot = Node(tempArr[0], parent=leftChild)
    leftChild.addLeftChild(tempRoot)
    leftChild = Node(tempArr[1], parent=tempRoot)
    rightChild = Node(tempArr[2], parent=tempRoot)
    tempRoot.addLeftChild(leftChild)
    tempRoot.addRightChild(rightChild)    
    nodes.append(tempRoot)
    nodes.append(leftChild)
    nodes.append(rightChild)
    
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
        tempRoot = Node(tempArr[0], parent=leftChild)
        leftChild.addLeftChild(tempRoot)
        leftChild = Node(tempArr[1], parent=tempRoot)
        tempRoot.addLeftChild(leftChild)
        nodes.append(tempRoot)
        nodes.append(leftChild)
        
        if(bs):
            tempArr = readingFromFile(lineTemp=lineTemp, bs=True)
            tempRoot = Node(tempArr[1], parent=leftChild)
            leftChild.addLeftChild(tempRoot)
            leftChild = Node(tempArr[0], parent=tempRoot)
            rightChild = Node(tempArr[2], parent=tempRoot)
            tempRoot.addLeftChild(leftChild)
            tempRoot.addRightChild(rightChild)    
            nodes.append(tempRoot)
            nodes.append(leftChild)
            nodes.append(rightChild)
    
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

"""
for tree in diction.values(): 
    print_tree(tree)
    print("-------------------")
for i in facts:
    print(i)
    print("----------")
"""
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

for temp in sourceDiction:
    tmpKey = temp
    tmpSourceValue = sourceDiction[temp]
    if(tmpKey in studentDiction):
        tmpStudentValue = studentDiction[tmpKey]
        
        print(tmpKey)
    else:
        totalScore -= 4

print("e")