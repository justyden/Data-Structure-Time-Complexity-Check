# A linked list that performs all necessary functions.

from LLNode import *


class LinkedList:
    # Creates the linked list.
    def __init__(self):
        self.head = None
        self.last = None

    # Inserts at the end of the linked list. Checks to make
    # sure the head node is not none.
    # Check head node to see if it is none. Make that the
    # head and tail if it is. If not make last reference
    # the new node and make the new node the tail node.
    def endInsert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    # Inserts at the start of the linked list. Checks to make
    # sure that the head node is not none.
    # Check to make sure head node is not none and if it is
    # then make the new node the head and tail. If not then
    # make the new node reference the head node and make the
    # head node be the new node.
    def startInsert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            tempNode = Node(data)
            tempNode.next = self.head
            self.head = tempNode

    # Checks the size of the linked list and inserts a node
    # in the correct position.
    # Checks the size of the list and if the head node is
    # none then make the new node be the head and tail node.
    # If it is not none then iterate over the list to calculate the
    # size. Take that size and get the middle point. Insert the node in
    # in front of the middle spot and make it reference the node that the
    # middle node is pointing to. Then make that same previous node now
    # point to the new inserted node.
    def middleInsert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            tempNode = self.head
            listSize = 1
            # This checks the size of the linked list.
            while tempNode.next is not None:
                tempNode = tempNode.next
                listSize += 1
            insertSpot = int(listSize / 2)
            tempNode = self.head
            insertNode = Node(data)
            # This means the list is to small and the
            # node will be inserted as the head.
            if insertSpot == 0:
                insertNode.next = self.head
                self.head = insertNode
            # This node will be inserted into the middle
            # of the linked list.
            else:
                for i in range(insertSpot - 1):
                    tempNode = tempNode.next
                insertNode.next = tempNode.next
                tempNode.next = insertNode

    # Delete a given node. Has to check that it exists in the
    # linked list. Depending on where the node is depends
    # on how it will be deleted if it is found.
    # Check through the list to see if the value exists.
    # If it does exist the spot it is at needs to be determined.
    # If it is the head then it can be deleted and the list will be
    # empty. If it is the tail then simply have the previous node
    # reference none. If it is somewhere in the middle of the
    # linked list then have the previous node reference the
    # next node and delete the temporary node.
    def deleteNode(self, data):
        # This means the linked list was empty.
        if self.head == None:
            return False
        else:
            nodeFound = False
            tempNode = self.head
            # This means the node was the head node.
            if (tempNode.data == data):
                nodeFound = True
                self.head = tempNode.next
                # This checks to see if the new node
                # is none.
                if self.head == None:
                    self.tail = None
            # This means it is going to check the other nodes
            # to see if it exists in it.
            else:
                # Keeps track of the previous node.
                prevNode = None
                # This checks to see if it was found or if it as
                # the end of linked list.
                while (not nodeFound and tempNode is not None):
                    # This means it was found.
                    if tempNode.data == data:
                        nodeFound = True
                        # This means the node has no reference
                        # to a next node.
                        if tempNode.next is None:
                            prevNode.next = None
                            self.tail = prevNode
                            del tempNode
                        # This means it has a reference to the
                        # next node.
                        else:
                            prevNode.next = tempNode.next
                            del tempNode
                    # Keeps on searching the linked list.
                    else:
                        prevNode = tempNode
                        tempNode = tempNode.next
            # Returns if it found the and deleted the value.
            return nodeFound

    # This reverses the list. It checks to see if there is any
    # elements in the list.
    # It starts by keeping track of the previous node and the current
    # node. It starts at the head node and continues until current node is
    # set to none. Each time there is a new node created that takes the place
    # of the current nodes next node. This then allows the current.next node to become
    # the previous node which is what allows the the linked list to change order.
    # From this the current node is then set as the next node which keeps the
    # loop going until the end is reached. When the end is reached the new
    # tail and head nodes are set.
    def reverseLinkedList(self):
        # This means there were no elements in the list.
        if self.head == None:
            return None
        else:
            # Saves the valus of the all nodes around the current node.
            previousNode = None
            tempNode = self.head
            # Keeps going until it reaches the end of the linked list.
            while(tempNode is not None):
                # This keeps track of the next node.
                swapNode = tempNode.next
                # This changes the order of the nodes.
                tempNode.next = previousNode
                previousNode = tempNode
                tempNode = swapNode
            # This correctly sets the tail and head node.
            self.last = self.head
            self.head = previousNode

    # Prints the head of the linked list.
    def printHead(self):
        print(self.head.data)

    # Prints the tail of the linked list.
    def printTail(self):
        print(self.last.data)

    def findValue(self, inputData):
        currentNode = self.head
        while (currentNode is not None):
            if currentNode.data == inputData:
                return currentNode.data
            currentNode = currentNode.next
        return "Value not found."

    # Display all the data.
    # Iterate through the list until next node is
    # none and print all data values.
    def display(self):
        tempList = []
        currentNode = self.head
        while (currentNode is not None):
            tempList.append(currentNode.data)
            currentNode = currentNode.next
        return tempList
