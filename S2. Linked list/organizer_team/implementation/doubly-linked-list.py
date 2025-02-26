class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# TRAVERSAL
def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def backward_traversal(tail):
    curr = tail
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()

# LENGTH
def length(head):
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count

# INSERTION
def insertBegin(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def insert_end(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head

def insert_at_position(head, pos, new_data):
    new_node = Node(new_data)
    if pos == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    curr = head
    for i in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next
    if curr is None:
        print("Position is out of bounds.")
        return head
    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    return head

# DELETION
def del_head(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head

def del_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next
    if curr.prev is not None:
        curr.prev.next = None
    return head

def del_pos(head, pos):
    if head is None:
        return head
    curr = head
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next
    if curr is None:
        return head
    if curr.prev is not None:
        curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev
    if head == curr:
        head = curr.next
    return head