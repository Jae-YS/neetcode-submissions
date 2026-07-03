class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node: Node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value
            node = self.cache[key]
            node.value = value
            # Move to most recent
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove least recently used (head.next)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

