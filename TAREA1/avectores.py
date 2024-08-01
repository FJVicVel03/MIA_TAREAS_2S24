import time

# Registra el tiempo de inicio
start_time = time.perf_counter()

class BitVector:
    def __init__(self, size):
        # Inicializa un vector de bits con el tamaño especificado
        self.size = size
        self.vector = [0] * ((size // 32) + 1)

    def add(self, element):
        print(f"Añadiendo {element} al vector de bits...")
        if element >= self.size:
            raise ValueError("Elemento fuera de rango")
        index = element // 32
        bit = element % 32
        self.vector[index] |= (1 << bit)
        print(f"Se añadió {element} al vector de bits.")
        self.print_vector()

    def remove(self, element):
        print(f"Eliminando {element} del vector de bits...")
        if element >= self.size:
            raise ValueError("Elemento fuera de rango")
        index = element // 32
        bit = element % 32
        self.vector[index] &= ~(1 << bit)
        print(f"Se eliminó {element} del vector de bits.")
        self.print_vector()

    def contains(self, element):
        print(f"Buscando {element} en el vector de bits...")
        if element >= self.size:
            raise ValueError("Elemento fuera de rango")
        index = element // 32
        bit = element % 32
        found = (self.vector[index] & (1 << bit)) != 0
        print(f"{element} {'se encontró' if found else 'no se encontró'} en el vector de bits.")
        return found

    def print_vector(self):
        print("Estado actual del vector de bits:")
        for i, bits in enumerate(self.vector):
            print(f"Bloque {i}: {bin(bits)[2:].zfill(32)}")

# Ejemplo de uso del vector de bits
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