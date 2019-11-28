#creation of class city
class City:
    """Classe définissant une ville caractérisée par:
    - son nom
    - son département"""

    def __init__(self, dict):
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None

    def hydratation(self, dict):
        for key, value in dict.items():
            if hasattr(self, key):
                setattr(self,key, value)

    def show_information(self):
        txt = "----------------\n\
        name: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n"

        print(text.format(self.name, self.department, self.country, self.mayor, self.capital))
