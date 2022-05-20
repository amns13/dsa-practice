from node import Node, insert_before, print_list, list_len


def is_palindrome_recur(head: Node, n: int, length: int) -> bool:
    if n == 0:
        if length % 2 == 0:
            return True, head
        else:
            return True, head.next

    res, comapre_node = is_palindrome_recur(head.next, n-1, length)
    if not res:
        return False, None
    return head.data == comapre_node.data, comapre_node.next


def is_palindrome(head: Node) -> bool:
    n = list_len(head)
    res, _ = is_palindrome_recur(head, n//2, n)
    return res


if __name__ == '__main__':
    head = Node(1)
    head = insert_before(head, 2)
    head = insert_before(head, 3)
    head = insert_before(head, 3)
    head = insert_before(head, 3)
    head = insert_before(head, 2)
    head = insert_before(head, 1)
    print_list(head)
    print(f"Palindrome: {is_palindrome(head)}")
