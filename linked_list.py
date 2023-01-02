
class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

def construct(keys):
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)
    
    return head

def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end='->')
        ptr = ptr.next

    print('None')

def append_list(head,key):
    current = head
    node = Node(key)

    if current is None:
        head = node
    else:
        while current.next:
            current = current.next
        current.next = node

    return head


linked_list = construct( [1,2,3,4,5])
print_list(linked_list)

append_list(linked_list, 6)
print_list(linked_list)