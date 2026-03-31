from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO
from UI.controller import Controller
class Model:
    def __init__(self):
        self._listaCorsi = []
        self._listaStudenti = []
        self._DAOC = corso_DAO()
        self._DAOS = studente_DAO()

    @property
    def popolaCorsi(self):
        return self._listaCorsi
    @property
    def popolaStudenti(self):
        return self._listaStudenti

    def caricaCorsi(self):
        self._listaCorsi = self._DAOC.get_corsi()
    def caricaStudenti(self):
        self._listaStudenti = self._DAOS.get_studenti()

    def cercaStudentiPerCorso(self, corso):
        matricole = self._DAOC.get_iscritti_a_corso(corso)
        listaRisultati = []
        for m in matricole:
            for studente in self._listaStudenti:
                if m == studente.matricola:
                    listaRisultati.append(studente)

        return listaRisultati

    def cercaStudentiPerMatricola(self, matricola):
        for i in self._listaStudenti:
            # Usiamo str() per assicurarci che siano dello stesso tipo!
            if str(matricola) == str(i.matricola):
                return i
        return None  # Aggiungiamo un return esplicito per chiarezza


