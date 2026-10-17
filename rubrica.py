import sqlite3
from contatto import Contatto


class AddressBook:
    def __init__(self):
        # Lista dei contatti presenti in memoria
        self.contacts = []

        # Apertura del database
        self.connessione = sqlite3.connect("rubrica.db")
        self.cursore = self.connessione.cursor()

        # Creazione della tabella, se non esiste
        self.cursore.execute("""
            CREATE TABLE IF NOT EXISTS contatti (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                numero TEXT NOT NULL
            )
        """)
        self.connessione.commit()

        # Caricamento dei contatti già salvati
        self.load_contacts()

    def load_contacts(self):
        self.cursore.execute(
            "SELECT nome, numero, id FROM contatti"
        )
        righe = self.cursore.fetchall()

        for riga in righe:
            contact = Contatto(riga[0], riga[1],riga[2])
            self.contacts.append(contact)

    def add_contact(self, contact):
        # Salvataggio nel database
        self.cursore.execute(
            "INSERT INTO contatti (nome, numero) VALUES (?, ?)",
            (contact.nome, contact.numero)
        )
        self.connessione.commit()

        # Aggiornamento della lista in memoria
        self.contacts.append(contact)

    def visualize_Address_Book(self):
        for contact in self.contacts:
            print(contact.putting_together())

    def delete_contact(self,contact):
        self.cursore.execute(
            "DELETE FROM contatti WHERE id = ?",
            (contact.id_db,)
        )
        self.connessione.commit()

    def close(self):
        self.connessione.close()





