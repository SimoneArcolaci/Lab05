# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import DBConnect
class corso_DAO:

    def get_corsi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM corso"""
        listaCorsi = []
        cursor.execute(query)
        for row in cursor:
            c = Corso(row["codins"], row["nome"], row["crediti"], row["pd"])
            listaCorsi.append(c)
        cursor.close()
        cnx.close()

        return listaCorsi

    def get_iscritti_a_corso(self, c):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT matricola FROM iscrizione where codins = %s"""
        listaIscriti = []
        cursor.execute(query, (c,))
        for row in cursor:
            s = row["matricola"]
            listaIscriti.append(s)
        cnx.close()
        cursor.close()
        return listaIscriti
    def get_Iscrizioni(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione """
        cursor.execute(query)
        listaIscritti = []
        for row in cursor:
            listaIscritti.append(row)
        cnx.close()
        cursor.close()
        return listaIscritti

    def addIscrizione(self, matricola, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        valori = (codins, matricola)
        query = """Insert into iscrizione (codins, matricola) values (%s, %s)"""
        cursor.execute(query, valori)
        cnx.commit()
        cursor.close()
        cnx.close()
