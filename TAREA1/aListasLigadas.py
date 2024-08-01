import time

# Registra el tiempo de inicio
start_time = time.perf_counter()

class LinkedListNode:
    def __init__(self, value):
        # Inicializa un nodo con un valor y un puntero al siguiente nodo
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        print(f"Añadiendo {value} a la lista...")
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
            print(f"Lista estaba vacía. {value} es ahora la cabeza de la lista.")
        else:
            current = self.head
            print(f"Recorriendo la lista para encontrar el final...")
            while current.next:
                print(f"Nodo actual: {current.value}")
                current = current.next
            current.next = new_node
            print(f"Se añadió {value} al final de la lista.")
        self.print_list()

    def remove(self, value):
        print(f"Eliminando {value} de la lista...")
        if not self.head:
            print("La lista está vacía. No se puede eliminar.")
            return
        if self.head.value == value:
            self.head = self.head.next
            print(f"{value} era la cabeza de la lista y se ha eliminado.")
            self.print_list()
            return
        current = self.head
        print(f"Recorriendo la lista para encontrar {value}...")
        while current.next and current.next.value != value:
            print(f"Nodo actual: {current.value}")
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"Se eliminó {value} de la lista.")
        else:
            print(f"{value} no se encontró en la lista.")
        self.print_list()

    def contains(self, value):
        print(f"Buscando {value} en la lista...")
        current = self.head
        while current:
            print(f"Nodo actual: {current.value}")
            if current.value == value:
                print(f"{value} se encontró en la lista.")
                return True
            current = current.next
        print(f"{value} no se encontró en la lista.")
        return False

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print("Estado actual de la lista: " + (" -> ".join(elements) if elements else "Lista vacía"))

# Ejemplo de uso de la lista ligada
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