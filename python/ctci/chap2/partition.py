from node import Node, insert_before, print_list


def partition(head: Node, pivot: int) -> None:
    boundary = head
    cur = head

    while cur:
        if cur.data < pivot:
            boundary.data, cur.data = cur.data, boundary.data
            boundary = boundary.next
        cur = cur.next


if __name__ == '__main__':
    head = Node(1)
    head = insert_before(head, 2)
    head = insert_before(head, 10)
    head = insert_before(head, 5)
    head = insert_before(head, 8)
    head = insert_before(head, 5)
    head = insert_before(head, 3)
    head = insert_before(head, 7)

    print("Input list")
    print_list(head)
    partition(head, 5)
    print("Output list")
    print_list(head)
