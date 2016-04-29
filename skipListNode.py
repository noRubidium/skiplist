class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.down = None
    def addNext(self,next):
        self.next = next
    def addDown(self,down):
        self.down = down
    def addPrev(self,prev):
        self.prev = prev
