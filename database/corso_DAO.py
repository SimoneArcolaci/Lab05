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
