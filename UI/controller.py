import flet as ft

from model import studente
from model.corso import *







class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def CercaStudente(self,e):
         matricola = self._view.txtMatricola.value
         if matricola is None or matricola == "":
             self.erroreMatricola()
             return
         studente = self._model.cercaStudentiPerMatricola(matricola)
         if studente is None:
             self.erroreMatricola()
             return
         nome = studente.nome
         cognome = studente.cognome
         self._view.txtName.value = str(nome)
         self._view.txtCognome.value = str(cognome)
         self._view.update_page()




    def CercaCorsi(self,e):
        matricola = self._view.txtMatricola.value
        listaCorsi = self._model.cercaCorsiPerMatricola(matricola)
        self._view.lvOut.controls.clear()
        print(listaCorsi)
        if matricola is None or matricola == "":
            self.erroreMatricola()
            return
        if len(listaCorsi) == 0:
            self.erroreMatricola()
            return
        for i in listaCorsi:
            self._view.lvOut.controls.append(ft.Text(value=f"{i.nomeCorso} - {i.codins}"))
        self._view.update_page()
        return






    def Iscrivi(self,e):
        codins = self._view.txtCorso.value
        matricola = self._view.txtMatricola.value
        codins = self._model.esistenzaCorso(codins)
        matricola = self._model.esistenzaStudenti(matricola)
        if codins is False or matricola is False:
            self.erroreDatiNonTrovati()
            return
        self._model.caricaIscrizioni()
        listaIscrizioni = self._model.getIscrizioni
        for i in listaIscrizioni:
            if str(i["matricola"]) == str(matricola) and str(i["codins"]) == str(codins):
                print("La relazione è già presente")
                return
        self._model.aggiungiIscrizione(matricola, codins)










    def aggiungiCorsiAView(self):
        self._model.caricaCorsi()
        self._model.caricaStudenti()
        self._view.txtCorso.options.clear()
        listaCorsi = self._model.popolaCorsi
        for i in listaCorsi:
            opzione =ft.dropdown.Option(key=i.codins, text=i.__str__())
            self._view.txtCorso.options.append(opzione)

        self._view.update_page()


    def CercaIscritti(self,e):
            codins = self._view.txtCorso.value
            self._view.lvOut.controls.clear()
            if codins is None or codins == "":
                self.funzioneErroreCorso()
                return
            listaIscritti = []
            listaIscritti = self._model.cercaStudentiPerCorso(codins)
            numIscritti = len(listaIscritti)
            self._view.lvOut.controls.append(ft.Text(value=f"ci sono {numIscritti} iscritti al corso"))
            for i in listaIscritti:
                self._view.lvOut.controls.append(ft.Text(value=f"{i.nome} - {i.cognome} - {i.matricola}"))
            self._view.update_page()

    def funzioneErroreCorso(self):
        def chiudi_errore(e):
            errCorsoNonSelezionato.open = False
            self._view._page.update()

        errCorsoNonSelezionato = ft.AlertDialog(
            title=ft.Text(value="Errore di ricerca"),
            content=ft.Text(value="Selezionare un corso"),
            actions=[ft.TextButton("Chiudi", on_click=chiudi_errore)],
            open=True,
        )
        self._view._page.dialog = errCorsoNonSelezionato
        self._view._page.update()


    def erroreMatricola(self):
        def chiudi_errore(e):
            errMatricolaInesistente.open = False
            self._view._page.update()
        errMatricolaInesistente = ft.AlertDialog(
            title=ft.Text(value="Errore di ricerca"),
            content=ft.Text(value="La matricola non è presente"),
            actions=[ft.TextButton("Chiudi", on_click=chiudi_errore)],
            open=True,
        )
        self._view._page.dialog = errMatricolaInesistente
        self._view._page.update()

    def erroreDatiNonTrovati(self):
        def chiudi_errore(e):
            errDatoNonTrovato.open = False
            self._view._page.update()
        errDatoNonTrovato = ft.AlertDialog(
            title=ft.Text(value="Errore di Ricerca"),
            content=ft.Text(value="I Dati richiesti non sono presenti nel database"),
            actions=[ft.TextButton("Chiudi", on_click=chiudi_errore)],
            open=True,
        )
        self._view._page.dialog = errDatoNonTrovato
        self._view._page.update()

    def provaAlert(self,e):
        self._view.create_alert("Svegliati l'acido")
        self._view.update_page()
        return

