class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None    

# TRAVERSAL
def traverse(head):
    current = head
    while current is not None:
        print(current.data),
        current = current.next
    print()

# SEARCH
def search(head, target):
    while head is not None:
        if head.data == target:
            return True
        head = head.next
    return False

# LENGTH
def length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

# INSERTION
def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def insert_at_pos(head, pos, data):
    if pos < 1:
        print("Invalid position!")
        return head
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node
    prev = head
    count = 1
    while count < pos - 1 and prev is not None:
        prev = prev.next
        count += 1
    if prev is None:
        print("Invalid position!")
        return head
    new_node = Node(data)
    new_node.next = prev.next
    prev.next = new_node
    return head

# DELETION
def removeFirstNode(head):
    if not head:
        return None
    temp = head
    head = head.next
    temp = None
    return head

def removeLastNode(head):
    if head is None:
        return None
    if head.next is None:
        head = None
        return None
    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next
    second_last.next = None
    return head

def delete_at_position(head, position):
    if head is None or position < 1:
        return head
    if position == 1:
        temp = head
        head = head.next
        temp = None
        return head
    current = head
    for i in range(1, position - 1):
        if current is not None:
            current = current.next
    if current is None or current.next is None:
        return head
    temp = current.next
    current.next = current.next.next
    temp = None
    return head

