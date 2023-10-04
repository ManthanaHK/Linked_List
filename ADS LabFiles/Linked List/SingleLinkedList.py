class SingleLinkedList:
    
    class _Node:
        def __init__(self, ele):
            self.data = ele
            self.next = None
    
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.count == 0
    
    def getCount(self):
        return self.count
    
    def addAtHead(self,ele):
        new_node = self._Node(ele)
        if not self.isEmpty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count  += 1
        return self.count
    
    def addAtTail(self,ele):
        new_node = self._Node(ele)
        if not self.isEmpty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
        return self.count
    
    def deleteAtHead(self):
        if not self.isEmpty():
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.count -= 1
            return self.count
        else:
            return None
    
    def deleteAtTail(self):
        if not self.isEmpty():
            cur_node = self.head
            if cur_node == self.tail:
                self.head = self.tail = None
                self.count -= 1
                return self.count
            while cur_node.next != self.tail:
                cur_node = cur_node.next
            self.tail = cur_node
            self.tail.next = None
            self.count -= 1
            return self.count
        else:
            return None
    
    def isMember(self, key):
        if not self.isEmpty():
            cur_node = self.head
            while cur_node != None:
                if cur_node.data == key:
                    break
                else:
                    cur_node = cur_node.next
            return cur_node != None
        else:
            return False

    
    def addAfterKey(self,ele,key):
        if not self.isEmpty():
            new_node = self._Node(ele)
            cur_node = self.head
            while cur_node.next != None:
                if cur_node.data == key:
                    break
                cur_node = cur_node.next
            if cur_node == self.tail:
                return self.addAtTail(ele)
            if cur_node.next == None:
                return False
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.count += 1
            return self.count
        else:
            return False
    
    def addAferNode(self,ele,node):
        if not self.isEmpty():
            new_node = self._Node(ele)
            node_pos = 1
            cur_node = self.head
            if cur_node == self.tail:
                self.head.next = new_node
                self.tail = new_node
                self.count += 1
                return self.count
            while node_pos < node:
                cur_node = cur_node.next
                node_pos += 1
            if cur_node == self.tail:
                return self.addAtTail(ele)
            else:
                new_node.next = cur_node.next
                cur_node.next = new_node
                self.count += 1
                return self.count
        else:
            return False
    
    def deleteNode(self,node):
        if not self.isEmpty():
            node_pos = 1
            if node == 1:
                return self.deleteAtHead()
            cur_node = self.head
            if node <= self.count:
                while node_pos < node:
                    cur_node = cur_node.next
                    node_pos += 1
                if cur_node == self.tail:
                    return self.deleteAtTail()
                else:
                    prevTo_cur_node = self.head
                    while prevTo_cur_node.next != cur_node:
                        prevTo_cur_node = prevTo_cur_node.next
                    prevTo_cur_node.next = cur_node.next
                    self.count -= 1
                    return self.count
            return False
        else:
            return False

    def printSList(self):
        if not self.isEmpty():
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.data)
                cur_node = cur_node.next
        else:
            return False