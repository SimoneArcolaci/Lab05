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
        pass


