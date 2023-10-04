from SingleLinkedList import *

list = SingleLinkedList()

def addElements():
    list.addAtHead(20)
    list.addAtHead(30)
    list.addAtHead(40)
    list.addAtHead(50)
    list.addAtHead(60)
    list.addAtHead(70)

def ElementalSum(n):
    ele = []
    cur = list.head
    while cur != None:
        ele.append(cur.data)
        cur = cur.next
    i = -1
    sum = 0
    while i >= -n:
        sum = sum + ele[i]
        i = i - 1
    return (sum)

addElements()

number = int(input("Enter the number of elements have to be added:"))
print(ElementalSum(number))
