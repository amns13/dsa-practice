class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def insert_before(node: Node, data: int):
    return Node(data, node)

def print_list(head: Node):
    while head:
        print(head, end='->')
        head = head.next
    print()

def list_len(head: Node) -> int:
    cnt = 0
    while head:
        cnt += 1
        head = head.next
    return cnt
