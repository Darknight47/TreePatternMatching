import re
from node import Node
from fact import Fact

sourceDiction = {}
sourceFacts = []

studentDiction = {}
studentFacts = []

totalScore = 20
studentTotalScore = 0
ok_f_m_tree = True
ok_b_s_tree = True
ok_sib_tree = True

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

def readingFromFile(lineTemp):
    lineTemp = file.readline()
    lineTemp = lineTemp.strip()
    lineTemp = lineTemp.replace(" ", "")
    if(lineTemp.count('\=') > 0):
        tempArr = re.split(r'(\\=)', lineTemp)
    else:
        tempArr = re.split(r'[(), ]+', lineTemp)
    return tempArr

def male_female_subTree(tempArr):
    tempRoot = Node(tempArr[0])
    leftChild = Node(tempArr[1], parent=tempRoot)
    tempRoot.addLeftChild(leftChild)
    return tempRoot
def sibling_subTree(tempArr):
    tempRoot = Node(tempArr[0])
    leftChild = Node(tempArr[1], parent=tempRoot)
    rightChild = Node(tempArr[2], parent=tempRoot)
    tempRoot.addLeftChild(leftChild)
    tempRoot.addRightChild(rightChild)
    return tempRoot
def notEqual_subTree(tempArr):
    tempRoot = Node(tempArr[1])
    leftChild = Node(tempArr[0], parent=tempRoot)
    rightChild = Node(tempArr[2], parent=tempRoot)
    tempRoot.addLeftChild(leftChild)
    tempRoot.addRightChild(rightChild)
    return tempRoot

def father_mother_tree_builder(lineTemp, tempArr):
    treeRoot = Node(tempArr[0])
    leftChildFirst = Node(tempArr[1], parent=treeRoot)
    rightChildFirst = Node(tempArr[2], parent=treeRoot)
    treeRoot.addLeftChild(leftChildFirst)
    treeRoot.addRightChild(rightChildFirst)
    nodes.append(treeRoot)
    nodes.append(leftChildFirst)
    nodes.append(rightChildFirst)
    
    for i in range(2):
        tempArr = readingFromFile(lineTemp=lineTemp)
        treeRootTemp = None
        if(len(tempArr) != 1):
            if(tempArr[0] == 'male' or tempArr[0] == 'female'):
                treeRootTemp = male_female_subTree(tempArr)
            elif(tempArr[0] == 'parent'):
                treeRootTemp = sibling_subTree(tempArr)
            if(treeRootTemp != None):
                if(treeRootTemp.leftChildElement.name == leftChildFirst.name):
                    leftChildFirst.addLeftChild(treeRootTemp)          
                else:
                    rightChildFirst.addLeftChild(treeRootTemp)
                leftChildFirst = treeRootTemp.leftChildElement
                rightChildFirst = treeRootTemp.rightChildElement
        else:
            print("Couldn't build the ", treeRoot.name, "tree!")
            ok_f_m_tree = False
            break
    return treeRoot    

def brother_sister_tree_builder(lineTemp, tempArr):
    treeRoot = Node(tempArr[0])
    leftChildFirst = Node(tempArr[1], parent=treeRoot)
    rightChildFirst = Node(tempArr[2], parent=treeRoot)
    treeRoot.addLeftChild(leftChildFirst)
    treeRoot.addRightChild(rightChildFirst)
    nodes.append(treeRoot)
    nodes.append(leftChildFirst)
    nodes.append(rightChildFirst)
    
    for i in range(3):
        tempArr = readingFromFile(lineTemp=lineTemp)
        treeRootTemp = None
        if(len(tempArr) != 1):
            if(tempArr[0] == 'male' or tempArr[0] == 'female'):
                treeRootTemp = male_female_subTree(tempArr)
            elif(tempArr[0] == 'sibling'):
                treeRootTemp = sibling_subTree(tempArr)
            elif(tempArr[1] == '\='):
                treeRootTemp = notEqual_subTree(tempArr)
                
            if(treeRootTemp.leftChildElement.name == leftChildFirst.name):
                leftChildFirst.addLeftChild(treeRootTemp)          
            else:
                if(rightChildFirst is not None):
                    rightChildFirst.addLeftChild(treeRootTemp)
            leftChildFirst = treeRootTemp.leftChildElement
            rightChildFirst = treeRootTemp.rightChildElement
        else:
            print("Couldn't build the tree!")
            ok_b_s_tree = False
            break
    return treeRoot

def sibling_tree_builder(lineTemp, tempArr) :
    treeRoot = Node(tempArr[0])
    leftChildFirst = Node(tempArr[1], parent=treeRoot)
    rightChildFirst = Node(tempArr[2], parent=treeRoot)
    treeRoot.addLeftChild(leftChildFirst)
    treeRoot.addRightChild(rightChildFirst)
    nodes.append(treeRoot)
    nodes.append(leftChildFirst)
    nodes.append(rightChildFirst)
    
    for i in range(3):
        tempArr = readingFromFile(lineTemp=lineTemp)
        if(len(tempArr) != 1):
            treeRootTemp = None
            if(tempArr[0] == 'parent'):
                treeRootTemp = sibling_subTree(tempArr)
            elif(tempArr[1] == '\='):
                treeRootTemp = notEqual_subTree(tempArr)
            if(treeRootTemp.leftChildElement.name == leftChildFirst.name):
                leftChildFirst.addLeftChild(treeRootTemp)          
            else:
                rightChildFirst.addLeftChild(treeRootTemp)
            leftChildFirst = treeRootTemp.leftChildElement
            rightChildFirst = treeRootTemp.rightChildElement
        else:
            print("Could Not build the SIBLING TREE")
            break
    return treeRoot

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
                treeRoot = father_mother_tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'brother' or tempKey == 'sister'):
                treeRoot = brother_sister_tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'sibling'):
                treeRoot = sibling_tree_builder(lineTemp=lineTemp, tempArr=tempArr)


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
                treeRoot = father_mother_tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'brother' or tempKey == 'sister'):
                treeRoot = brother_sister_tree_builder(lineTemp=lineTemp, tempArr=tempArr)
            elif(tempKey == 'sibling'):
                treeRoot = sibling_tree_builder(lineTemp=lineTemp, tempArr=tempArr)  

for tempKey in sourceDiction:
    sourceRoot = sourceDiction[tempKey]
    studentRoot =  studentDiction.get(tempKey)
    if(studentRoot == None):
        print(tempKey, "rule is not defined!")
    else:
        sourceRootMeaning = getTheMeaning(sourceRoot)
        studentRootMeaning = getTheMeaning(studentRoot)
        sourceRootMeaning = [elem for elem in sourceRootMeaning if elem is not None]
        studentRootMeaning = [elem for elem in studentRootMeaning if elem is not None]
        theRuleSent = studentRootMeaning[len(studentRootMeaning) - 1]
        varOne = theRuleSent[0]
        varTwo = theRuleSent[len(theRuleSent) - 1]
        varThird = None
        tempAnswers = []
        acc = True
        if(tempKey == 'sibling'):
            for senTemp1 in sourceRootMeaning:
                senTemp1 = senTemp1.replace(".", "")
                tempSen1 = senTemp1[2:len(senTemp1) - 2]
                tempOk = True
                varOneTemp = None
                varTwoTemp = None                
                for senTemp2 in studentRootMeaning:
                    senTemp2 = senTemp2.replace(".", "")
                    varTwoTemp = senTemp2[len(senTemp2) - 1]
                    if(senTemp2.count(tempSen1) > 0):
                        if(senTemp2.count("parent") > 0 and varTwoTemp == varTwo):
                            varThird = senTemp2[0]
                            varTwoTemp = senTemp2[len(senTemp2) - 1]
                        elif(senTemp2.count("parent") > 0 and varTwoTemp == varOne):
                            varThird = senTemp2[0]
                        elif(senTemp2.count('\=')):
                            varOneTemp = senTemp2[0]
                            varTwoTemp = None
                            if(not senTemp2[len(senTemp2) - 1].islower() or senTemp2[len(senTemp2) - 1] == ''):
                                varTwoTemp = senTemp2[len(senTemp2) - 1]
                            if(varOneTemp != varOne):
                                print("Wrong First Variable,", varOne, f", ERROR IN ({tempKey}/2)")
                                tempOk = False
                                acc = False
                            if(varTwoTemp is not None and varTwoTemp != varTwo):
                                print("Wrong Second Variable,", varTwo, f", ERROR IN ({tempKey}/2)")
                                tempOk = False
                                acc = False
                            if(tempOk):
                                tempAnswers.append(senTemp2)
                                tempOk = False
        else:
            for sen1 in sourceRootMeaning:
                sen1 = sen1.replace(".", "")
                tempSen1 = sen1[2:len(sen1) - 2]
                tempOk = True
                for sen2 in studentRootMeaning:
                    sen2 = sen2.replace(".", "")
                    if(sen2.count(tempSen1) > 0):
                        varOneTemp = sen2[0]
                        varTwoTemp = None
                        if(not sen2[len(sen2) - 1].islower() or sen2[len(sen2) - 1] == ''):
                            varTwoTemp = sen2[len(sen2) - 1]
                        if(varOneTemp != varOne):
                            print("Wrong First Variable,", varOne, f", ERROR IN ({tempKey}/2)")
                            tempOk = False
                            acc = False
                        if(varTwoTemp is not None and varTwoTemp != varTwo):
                            print("Wrong Second Variable,", varTwo, f", ERROR IN ({tempKey}/2)")
                            tempOk = False
                            acc = False
                        if(tempOk):
                            tempAnswers.append(sen2)
                            tempOk = False
                if(tempOk):
                    print(sen1, "IS MISSING!", f"({tempKey}/2)")
                    acc = False
        if(acc):
            studentTotalScore += 4
        else:
            print("One Subpart of the ", tempKey, "is missing!")
                
src = getTheMeaning(sourceDiction['brother'])
