# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect
from model.studente import Studente

class studente_DAO:
    def get_studenti(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "select * from studente"
        cursor.execute(query)
        listaStudenti =[]
        for row in cursor:
            s = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            listaStudenti.append(s)

        cursor.close()
        cnx.close()
        return listaStudenti
