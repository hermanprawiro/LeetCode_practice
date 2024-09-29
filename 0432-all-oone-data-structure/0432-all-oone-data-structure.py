class FreqNode:
    def __init__(self, val: int = 0):
        self.freq = val
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.keys = {} # {"key_string": FreqNode(key_count: int)}
        self.head = FreqNode()
        self.tail = FreqNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.keys:
            # get current freq
            node = self.keys[key]
            freq = node.freq
            node.keys.remove(key)
            # find node with freq = freq + 1
            next_node = node.next
            if next_node == self.tail or next_node.freq > freq + 1: # create new
                new_node = self._insertNode(freq + 1, node, next_node)
                new_node.keys.add(key)
                self.keys[key] = new_node
            else:
                next_node.keys.add(key)
                self.keys[key] = next_node
            
            if not node.keys:
                self._removeNode(node)
        else: # find node with freq = 1, create if not exists
            node = self.head.next
            if node == self.tail or node.freq > 1: # create new
                new_node = self._insertNode(1, self.head, node)
                new_node.keys.add(key)
                self.keys[key] = new_node
            else: # node is FreqNode(1)
                node.keys.add(key)
                self.keys[key] = node

    def dec(self, key: str) -> None:
        if key not in self.keys:
            return
        node = self.keys[key]
        freq = node.freq
        node.keys.remove(key)
        if freq == 1:
            del self.keys[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq < freq - 1:
                new_node = self._insertNode(freq - 1, prev_node, node)
                new_node.keys.add(key)
                self.keys[key] = new_node
            else:
                prev_node.keys.add(key)
                self.keys[key] = prev_node
        if not node.keys:
            self._removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: # is empty
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: # is empty
            return ""
        return next(iter(self.head.next.keys))

    def _insertNode(self, val, prev_node, next_node):
        new_node = FreqNode(val)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        return new_node

    def _removeNode(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()