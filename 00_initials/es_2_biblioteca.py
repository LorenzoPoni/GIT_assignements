class Libro:
    def __init__(self, titolo, autore, anno, editore , numero_pagine):
        self.titolo = titolo
        self.autore = autore    
        self.anno_di_pubblicazione = anno
        self.editore = editore
        self.numero_pagine = numero_pagine

    def __str__(self):
        return f"{self.titolo} by {self.autore} ({self.anno} - {self.editore}, {self.numero_pagine} pages)"
    
    def redingTime(self, reading_speed):
        """Calcola il tempo di lettura stimato in minuti.

        reading_speed: velocità di lettura in pagine al minuto
        """
        if not isinstance(reading_speed, (int, float)):
            raise TypeError("reading_speed deve essere un numero")
        if reading_speed <= 0:
            raise ValueError("reading_speed deve essere maggiore di zero")
        
        return self.numero_pagine / reading_speed