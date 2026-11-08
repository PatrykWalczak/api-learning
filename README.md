# Praca z Postman - nauka pisania / obslugi API

JSONPlaceholder to kolekcja dla trzech testow:
- pobranie post gdzie userId to 1 
- pobranie listy wszystkich postow
- pobranie listy postow tam gdzie userId jest 1

Kolekcja testuje status 200, pola id i userId, lista niepusta

# Import do Postman:
Postman → Import → wskaż pliki JSON z folderu postman, w tym środowisko
Potrzebne jest środowisko JSONPlaceholder - prod i trzeba je wybrać jako aktywne, bo bez tego {{base_url}} nie zadziała