class Studente:
    def __init__(self, nome, cognome, eta ,città_residenza):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta
        self._città_residenza = città_residenza

    def registro(self):
        return f"nome studente:{self.nome} cognome studente: {self.cognome} età studente: {self.eta} anni. città di residenza studente: {self.città_residenza}"

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def cognome(self) -> str:
        return self._cognome

    @property
    def eta(self) -> int:
        return self._eta

    @property
    def città_residenza(self) -> str:
        return self._città_residenza

    def classifica_anno(self):
        if self.eta < 16:
            return "Biennio"
        else 
            return "Triennio"
