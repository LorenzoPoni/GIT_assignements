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

def leggi_testo(messaggio):
    """Chiede un testo non vuoto finché l'utente non lo inserisce."""
    while True:
        valore = input(messaggio).strip()
        if valore:
            return valore
        print("Il campo non può essere vuoto.")
 
 
def leggi_intero(messaggio, minimo):
    """Chiede un intero >= minimo finché l'utente non lo inserisce."""
    while True:
        try:
            valore = int(input(messaggio))
        except ValueError:
            print("Inserisci un numero intero.")
            continue
        if valore < minimo:
            print(f"Il valore deve essere almeno {minimo}.")
            continue
        return valore
 
 
def mostra_menu():
    print()
    print("=== GESTIONE CD ===")
    print("1) Aggiungi brano")
    print("2) Mostra brani")
    print("3) Durata totale")
    print("4) Taglia la durata di un brano")
    print("5) Mostra CD")
    print("0) Esci")
 
 
def aggiungi_brano(cd):
    titolo = leggi_testo("Titolo del brano: ")
    autore = leggi_testo("Autore del brano: ")
    durata = leggi_intero("Durata in secondi: ", 1)
    brano = Brano(autore, titolo, durata)
    cd.aggiungi_brano(brano)
    print(f"Aggiunto: {brano}")
 
 
def mostra_brani(cd):
    if not cd.brani:
        print("Il CD non contiene ancora brani.")
        return
    for numero, brano in enumerate(cd.brani, start=1):
        print(f"  {numero}) {brano}")
 
 
def durata_totale(cd):
    totale = cd.durata_totale()
    minuti, secondi = divmod(totale, 60)
    print(f"Durata totale: {totale}s ({minuti}:{secondi:02d})")
 
 
def taglia_brano(cd):
    if not cd.brani:
        print("Il CD non contiene ancora brani.")
        return
    mostra_brani(cd)
    numero = leggi_intero("Numero del brano da tagliare: ", 1)
    if numero > len(cd.brani):
        print("Numero di brano non valido.")
        return
    secondi = leggi_intero("Secondi da tagliare: ", 0)
    brano = cd.brani[numero - 1]
    brano.taglia_durata(secondi)
    print(f"Aggiornato: {brano}")
 
 
def mostra_cd(cd):
    print(cd)
 
 
def main():
    print("=== CREAZIONE CD ===")
    titolo = leggi_testo("Titolo del CD: ")
    autore = leggi_testo("Autore del CD: ")
    cd = CD(titolo, autore)
 
    azioni = {
        "1": aggiungi_brano,
        "2": mostra_brani,
        "3": durata_totale,
        "4": taglia_brano,
        "5": mostra_cd,
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
            azione(cd)
 
 
if __name__ == "__main__":
    main()