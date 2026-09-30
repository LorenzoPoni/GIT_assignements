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