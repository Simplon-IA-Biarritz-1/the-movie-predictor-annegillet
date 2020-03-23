from tsv import TSV
from db import DB
from clean import Cleaning
import pprint
from pymongo.errors import BulkWriteError
from pymongo import bulk

tsv = TSV('./Datas/crew.tsv')
db = DB('The_Movie_Predictor', 'crew_clean_2') #(database, collection)
clean = Cleaning()

liste = []
while True:
    lines = tsv.read_seq(100000)

    if lines == '':
        break

    for row in lines:
        row = clean.replace_id_tconst(row)
        row = clean.replace_nan(row, key = 'writers')
        liste.append(row)

        if len(liste) >= 10:
            db.bulk_insert(liste)
            liste = []


filter = {"category": "director"}
request = db.filt(filter)

for x in request:
    pprint.pprint(x)

"""une fois le format bien mis en place,
il faut récupérer tous les tconst, les intégrer dans un tableau puis dire "je veux tous mes films qui correspondent à ces tconst"

un moment : besoin de faire des requêtes avec des conditions
exemple je vais ressortir les titre dont la liste est la région Fr ("je veux tous les titres français")
dans la barre de recherche MongoDb {"region": "FR"} pus FIND

récupérer les api de films pour pouvoir récupérer l'intégralité des données 
par exemple les dates de sorties ne sont pas renseignées"""