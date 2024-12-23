import pytest
from medication_management.medicamento import Medicamento

def test_medicamento_inizializzazione():
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    assert medicamento.nombre == "Aspirina"
    assert medicamento.cantidad == 100
    assert medicamento.precio == 4.50
    assert medicamento.unitad == "mg"
