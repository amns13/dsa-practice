from node import Node

def delete_duplicates(head: Node):
    if not head:
        return
    seen = set()
    seen.add(head.data)
    cur = head
    while cur.next:
        nxt = cur.next
        if nxt.data in seen:
            cur.next = nxt.next
        else:
            seen.add(nxt.data)
            cur = cur.next


def print_list(head: Node):
    while head:
        print(head, end='->')
        head = head.next
    print()


if __name__ == '__main__':
    n4 = Node(3)
    n3 = Node(3, n4)
    # n2 = Node(2, n3)
    # n1 = Node(1, n2)
    # n0 = Node(0, n1)
    # n3dup = Node(3, n0)
    # n2dup = Node(2, n3dup)
    # h = Node(10, n2dup)
    print_list(n3)
    delete_duplicates(n3)
    print_list(n3)


