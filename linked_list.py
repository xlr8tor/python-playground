
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

keys = [1,2,3,4,5]
linked_list = construct(keys)
print_list(linked_list)