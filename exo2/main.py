from cities import *
from classe import *

for city in cities:
    ma_ville = City(city)
    City.show_information(city)
    #ou bien on peut faire ma_ville.show_information()
