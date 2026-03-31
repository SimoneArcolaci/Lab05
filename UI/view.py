import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        #Row 1:
        self.titolo = ft.Text(value="APP Gestione Studenti", color="Lightblue", text_align="center")
        #Row 2:
        self.txtCorso = ft.Dropdown(label="Seleziona corso",
                                    width = 500,
                                    )
        self.btnCI = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.CercaIscritti)
        #Row 3:
        self.txtMatricola = ft.TextField(label="Matricola")
        self.txtName = ft.TextField(label="Nome", read_only=True)
        self.txtCognome = ft.TextField(label="Cognome", read_only=True)
        #Row 4:
        self.btnCS = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.CercaStudente)
        self.btnCC = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.CercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.Iscrivi)


        self.lvOut = ft.ListView(expand=True)

        self.row1 = ft.Row(controls=[self.titolo], alignment="CENTER")
        self.row2 = ft.Row(controls=[self.txtCorso, self.btnCI], alignment="CENTER")
        self.row3 = ft.Row(controls=[self.txtMatricola, self.txtName, self.txtCognome], alignment="CENTER")
        self.row4 = ft.Row(controls=[self.btnCS, self.btnCC, self.btnIscrivi], alignment="CENTER")
        self._controller.aggiungiCorsiAView()

        self._page.add(self.row1, self.row2, self.row3, self.row4, self.lvOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
