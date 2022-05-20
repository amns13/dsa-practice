from functools import cache


class LRUCache:
    class Node:
        def __init__(self, key, value, nxt=None, prev=None):
            self.key = key
            self.value = value
            self.nxt = nxt
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = self.tail = None
        self.keys = {}
        
    def _node_push_front(self, key, value):
        new_node = LRUCache.Node(key, value, nxt=self.head)
        if self.head:
            self.head.prev = new_node
            
        self.head = new_node

        if not self.tail:
            self.tail = new_node
        self.keys[key] = new_node
        self.size += 1
            
    def _node_pop_back(self):
        key = self.tail.key
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            prev = self.tail.prev
            prev.nxt = None
            self.tail.prev = None
            self.tail = prev
        self.size -= 1
        del self.keys[key]
            
    def _node_make_head(self, node):
        if node != self.head:
            if node == self.tail:
                self.tail = node.prev
            else:
                node.nxt.prev = node.prev
            node.prev.nxt = node.nxt
            node.prev = None
            node.nxt = self.head
            self.head.prev = node
            self.head = node

    def get(self, key: int) -> int:
        node = self.keys.get(key)
        if not node:
            return -1
        value = node.value
        self._node_make_head(node)
        return value

    def put(self, key: int, value: int) -> None:
        node = self.keys.get(key)
        if node:
            node.value = value
            self._node_make_head(node)
        else:
            if self.size == self.capacity:
                self._node_pop_back()
            self._node_push_front(key, value)
            
    def print_cache(self):
        cur = self.head
        while cur:
            print(f"[{cur.key}->{cur.value}]", end=" => ")
            cur = cur.nxt
        print()

        cur = self.tail
        while cur:
            print(f"[{cur.key}->{cur.value}]", end=" => ")
            cur = cur.prev
        print()
        

cache = LRUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)
cache.print_cache()
print(cache.get(4))
cache.print_cache()
print(cache.get(3))
cache.print_cache()
print(cache.get(2))
print(cache.get(1))
cache.put(5,5)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)