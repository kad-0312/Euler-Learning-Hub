class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None    

# TRAVERSAL
def traverse(head):
    if head is None:
        print("The list is empty.")
        return
    current = head
    while True:
        print(current.data, end=" ")
        current = current.next
        if current == head:
            break
    print()  

# LENGTH
def length(head):
    if head is None:
        return 0
    length = 1
    current = head.next
    while current != head:
        length += 1
        current = current.next
    return length

# SEARCH
def search(last, key):
    if last is None:
        return False    
    head = last.next
    curr = head
    while curr != last:
        if curr.data == key:
            return True
        curr = curr.next
    if last.data == key:
        return True
    return False


# INSERTION
def insertInEmptyList(last, data):
    if last is not None:
        return last
    new_node = Node(data)
    last = new_node
    return last

def insert_at_beginning(last, value):
    new_node = Node(value)
    if last is None:
        new_node.next = new_node
        return new_node
    new_node.next = last.next
    last.next = new_node
    return last

def insert_end(tail, value):
    new_node = Node(value)
    if tail is None:
        tail = new_node
        new_node.next = new_node
    else:
        new_node.next = tail.next
        tail.next = new_node
        tail = new_node
    return tail

def insertAtPosition(last, data, pos):
    if last is None:
        if pos != 1:
            print("Invalid position!")
            return last
        new_node = Node(data)
        last = new_node
        last.next = last
        return last
    new_node = Node(data)
    curr = last.next
    if pos == 1:
        new_node.next = curr
        last.next = new_node
        return last
    for i in range(1, pos - 1):
        curr = curr.next
        if curr == last.next:
            print("Invalid position!")
            return last
    new_node.next = curr.next
    curr.next = new_node
    if curr == last:
        last = new_node
    return last

# DELETION
def deleteFirstNode(last):
    if last is None:
        print("List is empty")
        return None
    head = last.next
    if head == last:
        last = None
    else:
        last.next = head.next
    return last

def deleteLastNode(last):
    if last is None:
        print("List is empty, nothing to delete.")
        return None
    head = last.next
    if head == last:
        last = None
        return last
    curr = head
    while curr.next != last:
        curr = curr.next
    curr.next = head
    last = curr
    return last

def deleteSpecificNode(last, key):
    if last is None:
        print("List is empty, nothing to delete.")
        return None
    curr = last.next
    prev = last
    if curr == last and curr.data == key:
        last = None
        return last
    if curr.data == key:
        last.next = curr.next
        return last
    while curr != last and curr.data != key:
        prev = curr
        curr = curr.next
    if curr.data == key:
        prev.next = curr.next
        if curr == last:
            last = prev
    else:
        print(f"Node with data {key} not found.")
    return last
