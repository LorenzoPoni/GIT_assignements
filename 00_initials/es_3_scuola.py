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

    def cerca_per_cognome(self, cognome):
        return [studente for studente in self.studenti if studente.cognome == cognome]

    def cerca_per_eta(self, eta):
        return [studente for studente in self.studenti if studente.eta == eta]

    def conta_studenti(self):
        return len(self.studenti)


def leggi_testo(messaggio):
    """Chiede un testo non vuoto finché l'utente non lo inserisce."""
    while True:
        valore = input(messaggio).strip()
        if valore:
            return valore
        print("Il campo non può essere vuoto.")
 
 
def leggi_eta(messaggio):
    """Chiede un'età intera positiva finché l'utente non la inserisce."""
    while True:
        try:
            eta = int(input(messaggio))
        except ValueError:
            print("Inserisci un numero intero.")
            continue
        if eta <= 0:
            print("L'età deve essere maggiore di zero.")
            continue
        return eta
 
 
def stampa_studenti(studenti):
    """Stampa l'elenco degli studenti trovati, con la categoria."""
    if not studenti:
        print("Nessuno studente trovato.")
        return
    print(f"Trovati {len(studenti)} studenti:")
    for studente in studenti:
        print(f"  - {studente.informazioni()} ({studente.categoria_eta()})")
 
 
def mostra_menu():
    print()
    print("=== GESTIONE STUDENTI ===")
    print("1) Aggiungi studente")
    print("2) Cerca per cognome")
    print("3) Cerca per età")
    print("4) Conta studenti")
    print("0) Esci")
 
 
def aggiungi(scuola):
    nome = leggi_testo("Nome: ")
    cognome = leggi_testo("Cognome: ")
    eta = leggi_eta("Età: ")
    città = leggi_testo("Città di residenza: ")
    studente = Studente(nome, cognome, eta, città)
    scuola.aggiungi_studente(studente)
    print(f"Aggiunto: {studente.informazioni()} ({studente.categoria_eta()})")
 
 
def cerca_cognome(scuola):
    cognome = leggi_testo("Cognome da cercare: ")
    stampa_studenti(scuola.cerca_per_cognome(cognome))
 
 
def cerca_eta(scuola):
    eta = leggi_eta("Età da cercare: ")
    stampa_studenti(scuola.cerca_per_eta(eta))
 
 
def conta(scuola):
    print(f"Studenti presenti: {scuola.conta_studenti()}")
 
 
def main():
    scuola = Scuola("Istituto Superiore", "Via Roma 1")
    azioni = {
        "1": aggiungi,
        "2": cerca_cognome,
        "3": cerca_eta,
        "4": conta,
    }
 
    while True:
        mostra_menu()
        scelta = input("Scelta: ").strip()
        if scelta == "0":
            print("Arrivederci!")
            break
        azione = azioni.get(scelta)
        if azione is None:
            print("Scelta non valida, riprova.")
        else:
            azione(scuola)
 
 
if __name__ == "__main__":
    main()