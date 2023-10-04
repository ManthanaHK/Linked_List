from SingleLinkedList import *

instance = SingleLinkedList()

assert instance.isEmpty() == True
assert instance.getCount() == 0
assert instance.addAtHead(10) == 1
assert instance.addAtHead(20) == 2
assert instance.addAtHead(500) == 3
assert instance.addAfterKey(30,20) == 4
assert instance.addAfterKey(40,30) == 5
assert instance.addAtTail(50) == 6
assert instance.addAferNode(1000,6) == 7
assert instance.deleteNode(1) == 6
assert instance.deleteAtTail() == 5
# assert instance.deleteAtHead() == 4
# assert instance.deleteAtTail() == 3
# assert instance.addAtHead(10) == 4
# assert instance.isMember(20) == True
instance.printSList()