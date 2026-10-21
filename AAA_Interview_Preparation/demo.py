class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node


    def printLL(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

lis = LinkedList()
lis.insertAtStart('a')
lis.insertAtStart('b')
lis.printLL()