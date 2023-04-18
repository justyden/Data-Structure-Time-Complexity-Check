'''
A program designed to test the speed of certain
data structures through a series of operations
they perform.
'''

import random
import time
import BinarySearchTree
import LinkedList
import sys

# A decorator function that will time all functions
# of the data structures.
def calculateTime(function: object) -> None:

    # Printes the time it took to perform a function
    # on the data structures.
    def printTime(*args, **kwargs) -> None:
        startTime = time.perf_counter()
        function(*args, **kwargs)
        finalTime = time.perf_counter()
        print(f'The time was {finalTime - startTime} for {function.__name__}')
    
    return printTime

# Generates the the numbers that will be held
# within the data structures.
def generateNumbers(inputAmount: int) -> list[int]:
    tempList = []
    for i in range(inputAmount):
        tempList.append(random.randrange(1, 10000))
    return tempList


# Add the data to a list.
def addToList(inputList: list, dataList: list) -> None:
    for i in range(len(dataList)):
        inputList.append(dataList[i])


# Add the data to a dictionary.
def addToDictionary(inputDictionary: dict, dataList: list[int]) -> None:
    for i in range(len(dataList)):
        inputDictionary[i] = dataList[i]


# Add the data to a linked list.
def addToLinkedList(inputLinkedList: LinkedList, dataList: list[int]) -> None:
    for i in range(len(dataList)):
        inputLinkedList.startInsert(dataList[i])

# Checks the time to print a list.
@calculateTime
def printList(list: list[int]) -> None:
    print(list)

# Checks the time to print a dictionary.
@calculateTime
def printDictionary(dictionary: dict) -> None:
    print(dictionary)

# Checks the time to print a binary search tree.
@calculateTime
def printTree(tree: BinarySearchTree) -> None:
    print(tree.inOrderTraversal())

# Checks the time to print a linked list.
@calculateTime
def printLinkedList(linkedList: LinkedList) -> None:
    print(linkedList.display())

# Stops the program to record results.
def stopProgram():
    inputPrompt = input("Enter anything to continue.")
    inputPrompt = inputPrompt.lower()
    if inputPrompt == "stop":
        sys.exit(0)

# Check time to find a random value in a list.
@calculateTime
def getRandomList(list: list, inputNumber: int) -> None:
    print(list.index(inputNumber))

# Check time to find a random value in a dictionary.
@calculateTime
def getRandomDictionary(dictionary: dict, inputNumber: int) -> None:
    print(dictionary.get(inputNumber))

# Check time to find a random value in a binary search tree.
@calculateTime
def getRandomTree(tree: BinarySearchTree, inputNumber: int) -> None:
    print(tree.findValue(inputNumber))

# Check time to find a random value in a linked list.
@calculateTime
def getRandomLinkedList(linkedList: LinkedList, inputNumber: int) -> None:
    print(linkedList.findValue(inputNumber))

# Check time to insert a random value in a list.
@calculateTime
def insertRandomList(list: list, inputNumber) -> None:
    list.insert(0, inputNumber)

# Check time to insert a random value in a dictionary.
@calculateTime
def insertRandomDictionary(dictionary: dict, inputNumber: int) -> None:
    dictionary[len(dictionary) + 1] = inputNumber

# Check time to insert a random value in a binary search tree.
@calculateTime
def insertRandomTree(tree: BinarySearchTree, inputNumber: int) -> None:
    tree.insertNode(inputNumber)

# Check time to insert a random value in a linked list.
@calculateTime
def insertRandomLinkedList(linkedList: LinkedList, inputNumber: int) -> None:
    linkedList.startInsert(inputNumber)

# Check time to delete a random value in list.
@calculateTime
def deleteRandomList(list: list, inputNumber: int) -> None:
    list.remove(inputNumber)

# Check time to delete a random value in a dictionary.
@calculateTime
def deleteRandomDictionary(dictionary: dict, inputNumber: int) -> None:
    key = dictionary.get(inputNumber)
    del dictionary[key]

# Check time to delete a random value in a binary search tree.
@calculateTime
def deleteRandomTree(tree: BinarySearchTree, inputNumber: int) -> None:
    tree.removeValue(inputNumber)

# Check time to delete a random value in linked list.
@calculateTime
def deleteRandomLinkedList(linkedList: LinkedList, inputNumber: int) -> None:
    linkedList.deleteNode(inputNumber)

data = generateNumbers(25000)

list1 = []
addToList(list1, data)

dict1 = {}
addToDictionary(dict1, data)

tree1 = BinarySearchTree.BinarySearchTree(data)

linkedList1 = LinkedList.LinkedList()
addToLinkedList(linkedList1, data)


printList(list1)
stopProgram()
printDictionary(dict1)
stopProgram()
printTree(tree1)
stopProgram()
printLinkedList(linkedList1)
stopProgram()

for i in range(5):
    randomNumber = random.choice(data)
    getRandomList(list1, randomNumber)
    stopProgram()
    getRandomDictionary(dict1, randomNumber)
    stopProgram()
    getRandomTree(tree1, randomNumber)
    stopProgram()
    getRandomLinkedList(linkedList1, randomNumber)
    stopProgram()

for i in range(5):
    randomNumber = random.randint(1, 10000)
    insertRandomList(list1, randomNumber)
    stopProgram()
    insertRandomDictionary(dict1, randomNumber)
    stopProgram()
    insertRandomTree(tree1, randomNumber)
    stopProgram()
    insertRandomLinkedList(linkedList1, randomNumber)
    stopProgram()

for i in range(5):
    randomNumber = random.choice(data)
    deleteRandomList(list1, randomNumber)
    stopProgram()
    deleteRandomDictionary(dict1, randomNumber)
    stopProgram()
    deleteRandomTree(tree1, randomNumber)
    stopProgram()
    deleteRandomLinkedList(linkedList1, randomNumber)
    stopProgram()


