# Assume that we have two linked lists. 
# Elements in individual list are unique. 
# There may be identical elements across linkedlists. 
# Create a third list which contains
# only common elements across first two lists.


from SingleLinkedList import *

l1 = SingleLinkedList()
l2 = SingleLinkedList()
inter = SingleLinkedList()

def adding_To_List1():
    l1.addAtHead(30)
    l1.addAtHead(40)
    l1.addAtHead(50)
    l1.addAtHead(60)

adding_To_List1()

def adding_To_List2():
    l2.addAtHead(60)
    l2.addAtHead(70)
    l2.addAtHead(80)
    l2.addAtHead(90)

adding_To_List2()

def creating_Intersection_List():
    cur1 = l1.head
    while cur1 != None:
        cur2 = l2.head
        while cur2 != None:
            if cur1.data == cur2.data:
                inter.addAtHead(cur1.data)
            cur2 = cur2.next
        cur1 = cur1.next
    inter.printSList()

creating_Intersection_List()
       