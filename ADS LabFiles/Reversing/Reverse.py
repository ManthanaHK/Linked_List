from SingleLinkedList import *

list = SingleLinkedList()

def addElements():
    list.addAtHead(30)
    list.addAtHead(40)
    list.addAtHead(50)
    list.addAtHead(60)

addElements()

def reverseList():
    prev = None
    cur = list.head
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    list.head = prev

reverseList() 

list.printSList()