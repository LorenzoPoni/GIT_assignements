class RegistroVoti:
    def __init__(self):
        # {nome studente: [(materia, voto), ...]}
        self.voti = {}
 
    def aggiungi_voto(self, studente, materia, voto):
        if not 1 <= voto <= 10:
            raise ValueError("Il voto deve essere tra 1 e 10")
        self.voti.setdefault(studente, []).append((materia, voto))
 
    def voti_di(self, studente):
        return self.voti.get(studente, [])
 
    def media(self, studente):
        voti = self.voti_di(studente)
        if not voti:
            return None
        return sum(voto for _, voto in voti) / len(voti)

    def statistiche(self):
        stats = {}
        for studente, voti in self.voti.items():
            media = self.media(studente)
            stats[studente] = {
                "numero_voti": len(voti),
                "media": media
            }
        return stats