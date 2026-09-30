class Studente:
    def __init__(self, nome, cognome, eta, città):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.città = città

    def informazioni(self):
        return f"Studente: {self.nome} {self.cognome}, età: {self.eta}, città di residenza: {self.città}"

    def categoria_eta(self):
        if self.eta < 16:
            return "Biennio"
        elif self.eta >= 16:
            return "Triennio"

class Scuola:
    def __init__(self, nome, indirizzo):
        self.nome = nome
        self.indirizzo = indirizzo
        self.studenti = []

    def aggiungi_studente(self, studente):
        if isinstance(studente, Studente):
            self.studenti.append(studente)
        else:
            raise TypeError("Devi fornire un oggetto Studente")

    def elenco_studenti(self):
        return [studente.informazioni() for studente in self.studenti]

    def cerca_per_cognome(self, cognome):
        return [studente for studente in self.studenti if studente.cognome == cognome]

    def cerca_per_eta(self, eta):
        return [studente for studente in self.studenti if studente.eta == eta]

    def conta_studenti(self):
        return len(self.studenti)