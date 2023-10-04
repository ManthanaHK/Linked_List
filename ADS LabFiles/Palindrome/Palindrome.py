from SingleLinkedList import *

list = SingleLinkedList()

def addElements():
    list.addAtHead(140)
    list.addAtHead(500)
    list.addAtHead(500)
    list.addAtHead(140)

    org_list = []
    cur = list.head
    while cur != None:
        org_list.append(cur.data)
        cur = cur.next
    return org_list


def reverse():
    prev = None
    cur = list.head
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    list.head = prev

    new_cur = list.head
    rev_list = []
    while new_cur != None:
        rev_list.append(new_cur.data)
        new_cur = new_cur.next
    return rev_list


assert addElements() == reverse()