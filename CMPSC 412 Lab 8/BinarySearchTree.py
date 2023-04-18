# Create a binary search tree that has operations
# that allow it to function correctly.

from BinaryNode import *
import copy
import sys


class BinarySearchTree:
    # This creates the tree. If the list is empty is that is passed then
    # the tree will be empty.
    def __init__(self, inputList=[]):
        # This means the tree is empty.
        if inputList == []:
            self.rootNode = None
        else:
            # This creates the tree in order.
            self.rootNode = Node(inputList[0])
            for i in range(len(inputList) - 1):
                self.insertNode(inputList[i + 1])

    # This inserts a node in the tree in the tree at the correct spot.
    def insertNode(self, inputNumber):
        # This means the tree is empty.
        if self.rootNode == None:
            self.rootNode = Node(inputNumber)
        else:
            tempNode = self.rootNode
            nodeFound = False
            # This keeps traveling through the tree and finds the
            # place in the tree in number should be inserted at.
            while(not nodeFound):
                # Check the left side of the tree.
                if tempNode.number > inputNumber:
                    if tempNode.child1 == None:
                        # Create a new node at the spot.
                        tempNode.child1 = Node(inputNumber)
                        nodeFound = True
                    else:
                        tempNode = tempNode.child1
                # Check the right side of the tree.
                else:
                    if tempNode.child2 == None:
                        # Create a new node at the spot.
                        tempNode.child2 = Node(inputNumber)
                        nodeFound = True
                    else:
                        tempNode = tempNode.child2

    # Checks the tree to see if it contains a value. It returns
    # a boolean value depending on if it containes it.
    def findValue(self, inputNumber):
        # This means the tree was empty.
        if self.rootNode == None:
            return False
        else:
            tempNode = self.rootNode
            nodeFound = False
            # This keeps checking the given node in the tree.
            while (not nodeFound):
                if tempNode.number == inputNumber:
                    # The number was found.
                    nodeFound = True
                elif tempNode.number > inputNumber:
                    if tempNode.child1 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        tempNode = tempNode.child1
                else:
                    if tempNode.child2 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        tempNode = tempNode.child2
            return nodeFound

    # Performs and in order traversal on the tree.
    def inOrderTraversal(self, tempList=[], inputNode=None, isStart=True):
        # Checks to see if it is the first time it is called.
        if isStart:
            tempList = []
            if self.rootNode == None:
                return tempList
            else:
                inputNode = self.rootNode
        # This means there was no node found.
        if inputNode == None:
            return tempList
        # Adds the value to the list.
        tempList.append(inputNode.number)
        # Searchs another part of the tree.
        if (inputNode.child1 != None):
            self.inOrderTraversal(tempList, inputNode.child1, False)
        # Searchs another part of the tree.
        if (inputNode.child2 != None):
            self.inOrderTraversal(tempList, inputNode.child2, False)
        return tempList

    # Performs a pre order traversal on the tree.
    def preOrderTraversal(self, tempList=[], inputNode=None, isStart=True):
        # Checks to see if it is the first time it is called.
        if isStart:
            tempList = []
            if self.rootNode == None:
                return tempList
            else:
                inputNode = self.rootNode
        # This means there was no node found.
        if inputNode == None:
            return tempList
        # Checks another part of the tree.
        if (inputNode.child1 != None):
            self.preOrderTraversal(tempList, inputNode.child1, False)

        # Adds the value to the list.
        tempList.append(inputNode.number)

        # Checks another part of the tree.
        if (inputNode.child2 != None):
            self.preOrderTraversal(tempList, inputNode.child2, False)

        return tempList

    # Performs a post order traversal on the tree.
    def postOrderTraversal(self, tempList=[], inputNode=None, isStart=True):
        # Checks to see if it is the first time being called.
        if isStart:
            tempList = []
            if self.rootNode == None:
                return tempList
            else:
                inputNode = self.rootNode
        # This means a node was not found.
        if inputNode == None:
            return tempList
        # Checks another part of the tree.
        if (inputNode.child1 != None):
            self.postOrderTraversal(tempList, inputNode.child1, False)

        # Checks another part of the tree.
        if (inputNode.child2 != None):
            self.postOrderTraversal(tempList, inputNode.child2, False)

        # Adds the value to the list.
        tempList.append(inputNode.number)

        return tempList

    # Finds the lowest value in the tree.
    def minValue(self):
        if self.rootNode == None:
            return 0
        else:
            tempNode = self.rootNode
            # Keeps checking the next node.
            while (tempNode.child1 != None):
                tempNode = tempNode.child1
            return tempNode.number

    # Finds the highest value in the tree.
    def maxValue(self):
        if self.rootNode == None:
            return 0
        else:
            tempNode = self.rootNode
            # Keeps checking the next node.
            while (tempNode.child2 != None):
                tempNode = tempNode.child2
            return tempNode.number

    # Removes a node from the tree if it exists.
    def removeValue(self, inputNumber):
        # This means the tree was empty.
        if self.rootNode == None:
            return False
        else:
            parentNode = None
            tempNode = self.rootNode
            flag = 0
            nodeFound = False
            # This keeps checking the given node in the tree.
            while (not nodeFound):
                if tempNode.number == inputNumber:
                    # The number was found.
                    nodeFound = True
                elif tempNode.number > inputNumber:
                    if tempNode.child1 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        parentNode = tempNode
                        flag = 0
                        tempNode = tempNode.child1
                else:
                    if tempNode.child2 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        parentNode = tempNode
                        flag = 1
                        tempNode = tempNode.child2
            # This means the node was found in the tree.
            if nodeFound:
                # This checks to see if the node was the root node.
                if (parentNode == None):
                    # This means it had a child on no sides.
                    if (tempNode.child1 == None and tempNode.child2 == None):
                        self.rootNode = None
                    # This means it had a child on the right side.
                    elif (tempNode.child1 == None):
                        self.rootNode = self.rootNode.child2
                    # This means it had a child on the left side.
                    elif (tempNode.child2 == None):
                        self.rootNode = self.rootNode.child1
                    # This means it had a child on both sides.
                    else:
                        # This means the right child takes the place.
                        if (tempNode.child2.child1 == None):
                            tempStorageNode = tempNode
                            self.rootNode = tempNode.child2
                            self.rootNode.child1 = tempStorageNode.child1
                        else:
                            # Checks the tree to find the correct node.
                            tempStorageNode = tempNode.child2
                            tempParent = tempNode
                            while (tempStorageNode.child1 != None):
                                tempParent = tempStorageNode
                                tempStorageNode = tempStorageNode.child1
                            if (tempStorageNode.child2 != None):
                                tempParent.child1 = tempStorageNode.child2
                            self.rootNode = tempStorageNode
                            self.rootNode.child1 = tempNode.child1
                            self.rootNode.child2 = tempNode.child2

                # This means there was no childs on either side.
                elif (tempNode.child1 == None and tempNode.child2 == None):
                    if (flag == 0):
                        parentNode.child1 = None
                        tempNode = None
                    else:
                        parentNode.child2 = None
                        tempNode = None
                # This means there was a child on the right side.
                elif (tempNode.child1 == None):
                    if (flag == 0):
                        parentNode.child1 = tempNode.child2
                        tempNode = tempNode.child2
                    else:
                        parentNode.child2 = tempNode.child2
                        tempNode = tempNode.child2
                # This means there was a child the left side.
                elif (tempNode.child2 == None):
                    if (flag == 0):
                        parentNode.child1 = tempNode.child1
                        tempNode = tempNode.child1
                    else:
                        parentNode.child2 = tempNode.child1
                        tempNode = tempNode.child1
                # This means there was a child on both sides.
                else:
                    # This means the right child takes over.
                    if (tempNode.child2.child1 == None):
                        tempStorageNode = tempNode
                        tempNode = tempNode.child2
                        tempNode.child1 = tempStorageNode.child1
                        if (flag == 0):
                            parentNode.child1 = tempNode
                        else:
                            parentNode.child2 = tempNode
                    else:
                        # Searches the tree to find the correct node.
                        tempStorageNode = tempNode.child2
                        tempParent = tempNode
                        while (tempStorageNode.child1 != None):
                            tempParent = tempStorageNode
                            tempStorageNode = tempStorageNode.child1
                        if (tempStorageNode.child2 != None):
                            tempParent.child1 = tempStorageNode.child2
                        tempStorageNode.child1 = tempNode.child1
                        tempStorageNode.child2 = tempNode.child2
                        if (flag == 0):
                            parentNode.child1 = tempStorageNode
                        else:
                            parentNode.child2 = tempStorageNode
                return True
            else:
                return False

    # Checks to see if it is a valid binary tree.
    def checkValid(self, inputNode=None, isStart=True):
        # This means it is the first time it is called.
        if isStart:
            if self.rootNode == None:
                return True
            else:
                inputNode = self.rootNode
        # This means there is a child on both sides.
        if (inputNode.child1 != None and inputNode.child2 != None):
            if (inputNode.number > inputNode.child1.number):
                self.checkValid(inputNode.child1, False)
            else:
                return False
            if (inputNode.number < inputNode.child2.number):
                self.checkValid(inputNode.child2, False)
            else:
                return False
        # This means there was a child on the left side.
        elif (inputNode.child1 != None):
            if (inputNode.number > inputNode.child1.number):
                self.checkValid(inputNode.child1, False)
            else:
                return False
        # This means there was a child on the right side.
        elif (inputNode.child2 != None):
            if (inputNode.number < inputNode.child2.number):
                self.checkValid(inputNode.child2, False)
            else:
                return False
        # This means it was a complete tree.
        return True


# This combines trees.
def combineTree(inputTree1, inputTree2):
    # Creates a list that will hold the nodes of both trees.
    tempList = []
    tempList.extend(inputTree1.inOrderTraversal())
    tempList.extend(inputTree2.inOrderTraversal())
    # Creates a new tree with the new list.
    outputTree = BinarySearchTree(tempList)
    return outputTree
