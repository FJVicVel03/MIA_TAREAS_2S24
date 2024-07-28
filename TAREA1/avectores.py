import time

# Registra el tiempo de inicio
start_time = time.perf_counter()

class BitVector:
    def __init__(self, size):
        self.size = size
        self.vector = [0] * ((size // 32) + 1)

    def add(self, element):
        if element >= self.size:
            raise ValueError("Element out of range")
        index = element // 32
        bit = element % 32
        self.vector[index] |= (1 << bit)

    def remove(self, element):
        if element >= self.size:
            raise ValueError("Element out of range")
        index = element // 32
        bit = element % 32
        self.vector[index] &= ~(1 << bit)

    def contains(self, element):
        if element >= self.size:
            raise ValueError("Element out of range")
        index = element // 32
        bit = element % 32
        return (self.vector[index] & (1 << bit)) != 0

# Ejemplo de uso
bit_vector = BitVector(100)

# Agregar elementos
bit_vector.add(10)
bit_vector.add(20)
bit_vector.add(30)

# Verificar elementos
print(bit_vector.contains(10))  # True
print(bit_vector.contains(20))  # True
print(bit_vector.contains(30))  # True
print(bit_vector.contains(40))  # False

# Eliminar elementos
bit_vector.remove(20)
print(bit_vector.contains(20))  # False

# Registra el tiempo de finalización
end_time = time.perf_counter()

# Calcula y muestra el tiempo de ejecución en microsegundos
execution_time = (end_time - start_time) * 1_000_000
print(f"Tiempo de ejecución: {execution_time:.2f} microsegundos")