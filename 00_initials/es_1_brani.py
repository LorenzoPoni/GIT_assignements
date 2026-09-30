# prova per commit nel main branch
a = 5

class Brano:
    # Creazione di un metodo/funzione
    # Self: sta per indicare che verrà creata un'istanza nuova (oggetto)
    def __init__(self, autore: str, titolo: str, durata: int):
        # attributi interni
        self._autore = None
        self._titolo = None
        self._durata = None

        # usa i setter per validare i valori iniziali
        self.autore = autore
        self.titolo = titolo
        self.durata = durata

    def __str__(self):
        return f"{self.titolo} - {self.autore} ({self.durata}s)"

    # property autore
    @property
    def autore(self) -> str:
        return self._autore

    @autore.setter
    def autore(self, value: str):
        if not isinstance(value, str):
            raise TypeError("autore deve essere una stringa")
        self._autore = value

    # property titolo
    @property
    def titolo(self) -> str:
        return self._titolo

    @titolo.setter
    def titolo(self, value: str):
        if not isinstance(value, str):
            raise TypeError("titolo deve essere una stringa")
        self._titolo = value

    # property durata (in secondi)
    @property
    def durata(self) -> int:
        return self._durata

    @durata.setter
    def durata(self, value: int):
        if not isinstance(value, int):
            raise TypeError("durata deve essere un intero (secondi)")
        if value < 0:
            raise ValueError("durata non può essere negativa")
        self._durata = value

    def taglia_durata(self, secondi: int) -> int:
        """Taglia la durata del brano di `secondi` secondi.

        Se il valore porto la durata sotto zero, la imposta a 0.
        Restituisce la nuova durata.
        """
        if not isinstance(secondi, int):
            raise TypeError("secondi deve essere un intero")
        if secondi < 0:
            raise ValueError("secondi non può essere negativo")

        nuova = max(0, self._durata - secondi)
        self._durata = nuova
        return self._durata


if __name__ == "__main__":
    newBrano = Brano("Gue", "Scooteroni", 180)
    print(newBrano)
    # esempio di taglio
    newBrano.taglia_durata(30)
    print("Dopo taglio:", newBrano)


class CD:
    def __init__(self, titolo: str, autore: str ):
        self.titolo = titolo
        self.autore = autore
        self.brani = []

    @property
    def titolo(self) -> str:
        return self._titolo
    @property
    def autore(self) -> str:
        return self._autore
        
    def aggiungi_brano(self, brano: Brano):
        if not isinstance(brano, Brano):
            raise TypeError("brano deve essere un'istanza di Brano")
        self.brani.append(brano)

    def durata_totale(self) -> int:
        return sum(brano.durata for brano in self.brani)

    def __str__(self):
        return f"CD: {self.titolo} - {self.autore}, Durata totale: {self.durata_totale()}s"