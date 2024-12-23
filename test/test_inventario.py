import pytest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

def test_aggiunta_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    inventario.agregar_medicamento(medicamento)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0] == medicamento
