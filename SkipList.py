from skipListNode import Node
import random
class SkipList:
    def __init__(self):
        self.layer = 1
        self.headList = Node(None)
        self.tailList = Node(None)
        self.tailList.prev = self.headList
        self.headList.next = self.tailList
    def addNode(self,value):
        if value == None:
            return
        i = 0
        while random.random() > 0.5:
            i += 1
        while self.layer <= i:
            self.addLayer()
        head = self.getNthLayer()


    def getNthLayer(self,n):
        head = self.list
        while head != None:
            if n == self.layer:
                break
            n += 1
            head = head.down

    def addLayer(self):
        n = Node(None)
        t = Node(None)
        n.addDown(self.headList)
        t.addDown(self.tailList)
        n.addNext(t)
        t.addPrev(n)
        self.headList = n
        self.tailList = t
        self.layer += 1

s = SkipList()
