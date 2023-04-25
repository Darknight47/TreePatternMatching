import re
from node import Node
from fact import Fact
diction = {}
facts = []
indx = 0

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


with open("text.txt") as file:
    while True:
        lineTemp = file.readline()
        if(lineTemp == '\n'):
            print_tree(treeRoot)
        if not lineTemp: #End of the File.
            print_tree(treeRoot)
            break
        lineTemp = lineTemp.strip()
        lineTemp = lineTemp.replace(" ", "")
        tempArr = re.split(r'[(), ]+', lineTemp)
        if(tempArr[len(tempArr) - 1] == '.'):
            tempFact = Fact(tempArr[0], tempArr[1], tempArr[2])
            facts.append(tempFact)
        elif(tempArr[len(tempArr) - 1] == ':-'):
            nodes = []
            treeRoot = Node(tempArr[0])
            leftChild = Node(tempArr[1], parent=treeRoot)
            rightChild = Node(tempArr[2], parent=treeRoot)
            treeRoot.addLeftChild(leftChild)
            treeRoot.addRightChild(rightChild)
            nodes.append(treeRoot)
            nodes.append(leftChild)
            nodes.append(rightChild)
            while True:
                lineTemp = file.readline()
                lineTemp = lineTemp.strip()
                lineTemp = lineTemp.replace(" ", "")
                tempArr = re.split(r'[(), ]+', lineTemp)
                if(tempArr[len(tempArr) - 1] == '.'):
                    tempRoot = Node(tempArr[0], parent=leftChild)
                    leftChild.addLeftChild(tempRoot)
                    leftChild = Node(tempArr[1], parent=tempRoot)
                    tempRoot.addLeftChild(leftChild)
                    nodes.append(tempRoot)
                    nodes.append(leftChild)               
                    break
                else:
                    tempRoot = Node(tempArr[0], parent=leftChild)
                    leftChild.addLeftChild(tempRoot)
                    leftChild = Node(tempArr[1], parent=tempRoot)
                    rightChild = Node(tempArr[2], parent=tempRoot)
                    tempRoot.addLeftChild(leftChild)
                    tempRoot.addRightChild(rightChild)    
                    nodes.append(tempRoot)
                    nodes.append(leftChild)
                    nodes.append(rightChild)