import re
from node import Node
from fact import Fact

diction = {}
facts = []
indx = -1

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

def tree_builder(lineTemp, tempArr, bs = False, nephew = False):
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
        #rightChild = treeRoot.rightChildElement
        tempArr = readingFromFile(lineTemp=lineTemp)    
        tempRoot = Node(tempArr[0], parent=treeRoot.rightChildElement)
        #leftChild.addLeftChild(tempRoot)
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


with open("text.txt") as file:
    while True:
        lineTemp = file.readline()
        nodes = []
        if(lineTemp == '\n'):
            if(indx == 0):
                diction["MotherTree"] = treeRoot
            elif(indx == 1):
                diction["FatherTree"] = treeRoot
            elif(indx == 2):
                diction["BrotherTree"] = treeRoot
        if not lineTemp: #End of the File.
            if(indx == 3):
                diction["SisterTree"] = treeRoot
            break
        lineTemp = lineTemp.strip()
        lineTemp = lineTemp.replace(" ", "")
        tempArr = re.split(r'[(), ]+', lineTemp)
        if(tempArr[len(tempArr) - 1] == '.'):
            tempFact = Fact(tempArr[0], tempArr[1], tempArr[2])
            facts.append(tempFact)
        elif(tempArr[len(tempArr) - 1] == ':-'):
            indx += 1
            if(indx == 0):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr)
                print_tree(treeRoot)
            elif(indx == 1):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr)
                print_tree(treeRoot)
            elif(indx == 2):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, bs=True)
                print_tree(treeRoot)
            elif(indx == 3):
                treeRoot = tree_builder(lineTemp=lineTemp, tempArr=tempArr, bs=True)
                print_tree(treeRoot)
print(2)