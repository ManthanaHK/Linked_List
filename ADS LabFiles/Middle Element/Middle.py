from SingleLinkedList import *

l1 = SingleLinkedList()

def addElements():
    l1.addAtHead(10)
    l1.addAtHead(20)
    l1.addAtHead(90)
    l1.addAtHead(40)
    l1.addAtHead(50)
    l1.addAtHead(100)

addElements()

def middleElement():
    slowPtr = l1.head
    fastPtr = l1.head

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
    return slowPtr.data

assert middleElement() == 90