import UI
from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO
from UI.controller import Controller
class Model:
    def __init__(self):
        self._listaCorsi = []
        self._listaStudenti = []
        self._listaIscrizioni = []
        self._DAOC = corso_DAO()
        self._DAOS = studente_DAO()

    @property
    def popolaCorsi(self):
        return self._listaCorsi
    @property
    def popolaStudenti(self):
        return self._listaStudenti
    @property
    def getIscrizioni(self):
        return self._listaIscrizioni

    def caricaCorsi(self):
        self._listaCorsi = self._DAOC.get_corsi()
    def caricaStudenti(self):
        self._listaStudenti = self._DAOS.get_studenti()
    def caricaIscrizioni(self):
        self._listaIscrizioni = self._DAOC.get_Iscrizioni()

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

    def cercaCorsiPerMatricola(self, matricola):
        matricola1 = ""
        for s in self._listaStudenti:
            if matricola ==s.matricola:
                print(f"La matricola {matricola} è presente")
                matricola1 = matricola
        if matricola1 is None or matricola1 == "":
            print("La matricola no existe")
        lista = self._DAOS.getCorsiPerStudente(matricola1)
        print(f"La lista in model è :{lista}")
        listaCorsiMatricola = []
        for i in lista:
            for j in self._listaCorsi:
                if str(i["codins"]) == str(j.codins):
                    print(j)
                    listaCorsiMatricola.append(j)
        return listaCorsiMatricola

    def esistenzaCorso(self, c):
        flag = False
        for corso in self._listaCorsi:
            if str(c) == str(corso.codins):
                flag = True
                print("Corso trovato")
                return c
        if flag is False:
            return False

    def esistenzaStudenti(self, s):
        flag = False
        for studenti in self._listaStudenti:
            if str(s) == str(studenti.matricola):
                flag = True
                print("Studenti trovato")
                return s
        if flag is False:
            return False


    def aggiungiIscrizione(self, matricola, codins):
        self._DAOC.addIscrizione(matricola, codins)
