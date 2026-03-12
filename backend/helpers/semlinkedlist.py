class SemLinkedList:
    def __init__(self):
        self.head = None 
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"
    
    def add(self, data):
        new_node = SemNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

class SemNode:
    def __init__(self, data):
        self.data = data
        self.next = None 