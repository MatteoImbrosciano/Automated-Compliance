class Medicamento:
    
    def __init__(self, nombre, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un valor numérico positivo")
        self.nombre = nombre
        self.cantidad = cantidad
