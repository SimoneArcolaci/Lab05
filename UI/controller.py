import flet as ft
from model.corso import *

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
    def CercaIscritti(self,e):
        pass
    def CercaStudente(self,e):
        pass
    def CercaCorsi(self,e):
        pass
    def Iscrivi(self,e):
        pass
    def aggiungiCorsiAView(self):
        self._model.caricaCorsi()
        self._view.txtCorso.options.clear()
        listaCorsi = self._model.popolaCorsi
        for i in listaCorsi:
            opzione =ft.dropdown.Option(key=i.codins, text=i.__str__())
            self._view.txtCorso.options.append(opzione)

        self._view.update_page()


