
#creation of class city
class City:
    """Classe définissant une ville caractérisée par:
    - son nom
    - son département"""

#Constructeur avec hydratation
    def __init__(self, dict):
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        self.hydratation(dict)

#fonction d'hydratation: on parcourt un dictionnaire et si les attributs du constructeur existent
#et
    def hydratation(self, dict):
        for key, value in dict.items():
            if hasattr(self, key):
                setattr(self,key, value)

    def show_information(self):
        txt = "----------------\n\
        name: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n "
        print(txt.format(self.name, self.department, self.country, self.mayor, self.capital))
