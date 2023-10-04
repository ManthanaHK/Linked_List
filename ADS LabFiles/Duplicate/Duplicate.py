from SingleLinkedList import *

l1 = SingleLinkedList()
l2  = SingleLinkedList()

new_list = set()

def addElements():
    l1.addAtHead(10)
    l1.addAtHead(20)
    l1.addAtHead(30)
    l1.addAtHead(20)

def renovingDuplicates():
    count = 0
    node = 1
    cur = l1.head
    temp = l1.head
    while cur != None:
        if count != node - 1:
            
        new_list.add(cur.data)
        count += 1
        temp = cur
        cur = cur.next
