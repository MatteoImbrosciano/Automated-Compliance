from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from .medicamento import Medicamento
import locale

@dataclass
class Ticket:
    cliente: str = None
    fecha: datetime = None
    medicamentos: List[Medicamento] = field(default_factory=list)
    totale: float = None

    def cargar_ticket_desde_txt(self, file_path: str):
        """Carica i dati di un ticket leggendo un file di testo."""
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')  # Configura la locale italiana
        lines = self._leggi_file(file_path)
        self._parsa_dati(lines)

    def _leggi_file(self, file_path: str) -> List[str]:
        """Legge un file di testo e restituisce una lista di righe."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def _parsa_dati(self, lines: List[str]):
        """Analizza le righe del file e aggiorna gli attributi del ticket."""
        self.medicamentos.clear()  # Reset dei farmaci

        for line in lines:
            line = line.strip()

            if line.startswith("Cliente:"):
                self.cliente = self._parsa_cliente(line)

            elif line.startswith("Data:"):
                self.fecha = self._parsa_data(line)

            elif line.startswith("Totale:"):
                self.totale = self._parsa_totale(line)

            elif "|" in line and not line.startswith("Articolo"):
                medicamento = self._parsa_medicamento(line)
                if medicamento:
                    self.medicamentos.append(medicamento)

    def _parsa_cliente(self, line: str) -> str:
        """Estrae il cliente dalla riga."""
        return line.split(":", 1)[1].strip()

    def _parsa_data(self, line: str) -> datetime:
        """Estrae e converte la data dalla riga."""
        data_testo = line.split(":", 1)[1].strip()  # Estrae il contenuto dopo "Data:"
        
        # Converte la stringa della data in oggetto datetime usando il formato italiano
        return datetime.strptime(data_testo, "%d %B %Y")

    def _parsa_totale(self, line: str) -> float:
        """Estrae e converte il totale dalla riga."""
        return float(line.split(":", 1)[1].strip().replace("€", "").replace(",", "."))

    def _parsa_medicamento(self, line: str) -> Medicamento:
        """Estrae i dati di un farmaco dalla riga e li converte in un oggetto Medicamento."""
        parts = line.split("|")
        if len(parts) == 4:
            nombre = parts[0].strip()
            cantidad_info = parts[1].strip().split()
            cantidad = float(cantidad_info[0])
            unitad = cantidad_info[1] if len(cantidad_info) > 1 else ''
            prezzo = float(parts[3].strip().replace("€", "").replace(",", "."))
            return Medicamento(nombre, cantidad, prezzo, unitad)
        return None
