import csv # pour utiliser DictReader(), permet un rendu plus propre
import math
# - But -> Predire le prix d'une voiture en fonction des km donnés en argument
# - Au lancement -> demande un argument (km) -> retourne le prix estimé pour ce km
# - Utilise la formule :
#     estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
# - theta 0 et theta 1 initialisé a 0 au début du programme
# - Standardisé les données du Csv


# 1. demande d'un argument, km
# 2. charger et standardiser donnees du CSV (scaled)
# 3. standardiser entree user
# 4. Initialiser theta0 et theta1 a 0
# 5. Faire une premiére prédiction : prix = theta0 + theta1 * km et cela pour chaque data point (estimatePrice(mileage) = θ0 + (θ1 ∗ mileage))
# 6. Retourne le prix estimé pour le km donné en entrée

# def nom_fonction(liste de paramètres):
#       bloc d'instructions

def load_and_scale_data():
    with open("data.csv") as fichier:
        liste_km = []
        for km in fichier:
            liste_km.append(km)
            print(km)
# Étape 1 : calculer la moyenne (mu)

    return
    
open("scaled.csv", 'w')
# 1. Demande d'un argument
input_user  = input("Entrez km : ")
# Recuperer donnees du CSV, km et price afin de pouvoir les standardiser
# - Charger les données CSV
with open("data.csv") as fichier: #mode lecture par desfois a l ouverture
        scale_data(fichier)
        print(fichier)

with open('data.csv') as fichier:
    reader = csv.DictReader(fichier, delimiter=',')
    for ligne in reader:
        scale_data(int(ligne['km']), int(ligne['price']))


# with open('data.csv') as fichier:
#     reader = csv.DictReader(fichier, delimiter=',')
#     for ligne in reader:
#         km = int(ligne['km'])
#         price = int(ligne['price'])
#        # print(ligne['km'] + " kilometres pour " + ligne['price'] + " francs")
#     print(km)
#     print(price) 
        
        #with ferme automatiquement le fichier a la fin du bloc, sinon mettre fichier.close()



