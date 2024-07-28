import time

# Registra el tiempo de inicio
start_time = time.perf_counter()

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

linked_list = LinkedList()
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
print(linked_list.contains(10))  # True
print(linked_list.contains(20))  # True
print(linked_list.contains(30))  # True
print(linked_list.contains(40))  # False
linked_list.remove(20)
print(linked_list.contains(20))  # False

# Registra el tiempo de finalización
end_time = time.perf_counter()

# Calcula y muestra el tiempo de ejecución en microsegundos
execution_time = (end_time - start_time) * 1_000_000
print(f"Tiempo de ejecución: {execution_time:.2f} microsegundos")