class Contatto:
    def __init__(self, nome, numero, id_db=None):
        self.nome = nome
        self.numero = numero
        self.id_db = id_db

    def check_all(self):
        if self.nome and (len(self.numero)==10 and self.numero.isdigit()):
            return True
        else:
            return False

    def putting_together(self):
        visualizzazione_finale= "👤"+ " "+self.nome + "    " + "|"+ "    "+ "📞"+" "+self.numero
        return visualizzazione_finale
