from SingleLinkedList import *

list1 = SingleLinkedList()
list2 = SingleLinkedList()
orgList = SingleLinkedList()

def addElements():
    orgList.addAtHead(30)
    orgList.addAtHead(40)
    orgList.addAtHead(50)
    orgList.addAtHead(60)

addElements()

print("Org List:")
orgList.printSList()

cur = orgList.head
temp = cur.next
print(f"Bla: {temp.data}")

def split():
    flag = 0
    cur = orgList.head
    while cur != None:
        if flag == 0:
            list1.addAtTail(cur.data)
            flag = 1
            cur = cur.next
            continue
        else:
            list2.addAtTail(cur.data)
            flag = 0
            cur = cur.next
            continue

split()

print("1st List:")
list1.printSList()

print("2nd List")
list2.printSList()