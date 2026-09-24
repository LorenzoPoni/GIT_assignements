# prova per commit nel main branch
a = 5

class Brano:
    # Creazione di un metodo/funzione
    # Self: sta per indicare che verrà creata un'istanza nuova (oggetto)
    def __init__(self, autore: str, titolo: str, durata: int): #questi qui sono i parametri di una funzione
        self.autore = autore
        self.titolo = titolo
        self.durata = durata

    def __str__(self):
        return f"{self.titotlo}"

if __name__ == "__main__":
    newBrano = Brano("Gue", "Scooteroni", 180)
    print(newBrano)