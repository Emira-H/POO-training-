#creation of class city
class City:

    def __init__(self, nom, departement):

        self.nom = str(nom)
        self.departement = int(departement)

    def show_location(self):
        print("la ville {} est dans le département {}".format(self.nom,self.departement))

    def change_location(self,nom,departement):
        self.nom = nom
        self.departement = departement
        print("la nouvelle ville {} est dans le département {}".format(self.nom, self.departement))
