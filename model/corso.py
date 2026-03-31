class Corso:
    def __init__(self,codins, nomeCorso, crediti, pd):
        self.codins = codins
        self.nomeCorso = nomeCorso
        self.crediti = crediti
        self.pd = pd
    def __str__(self):
        return f'{self.nomeCorso} ({self.codins})'