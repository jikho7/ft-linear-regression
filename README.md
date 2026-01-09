1. Predict program :
- But -> Predire le prix d'une voiture en fonction des km donnés en argument
- Au lancement -> demande un argument (km) -> retourne le prix estimé pour ce km
- Utilise la formule :
    estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
- theta 0 et theta 1 initialisé a 0 au début du programme
- Standardisé les données du Csv

2. Train program :
- Lis la dataset (csv file)
- Performe la linear_regression sur ces datas
- theta 0 et theta 1 sont sauvegardées pour être utilisées dans Predict Program
- Utilise les formules :
tmpθ0 = learningRate ∗ 1/m somme mX−1 i=0(estimateP rice(mileage[i]) − price[i])

tmpθ1 = learningRate ∗ 1/m somme mX−1 i=0 (estimateP rice(mileage[i]) − price[i]) ∗ mileage[i]
- Ne pas oublier de mettre á jour theta 0 et theta 1

3. Linear regression
- Formule :
    price of the car = theta0 + theta1 * km
    ex : price = -0.5 * km

4. Fonction de perte (Loss function)
- Permet de connaitre la précision du model -> Mesure la différence entre le prix prédis et le prix actuel
- Formule :
    ![alt text](image-1.png)
- Exemple avec dataset:
    Donnée 1 : actual value = 1000 et predict value = 900
    Donnée 2 : actual value = 2000 et predict value = 1900
    Donnée 3 : actual value = 3000 et predict value = 3100

    MAE = (|1000 - 900| + |2000 - 1900| + |3000 - 3100|) / 3 = 100

    On soustrait le prix prédit du prix actuel (qui est sur le CSV), on fait ca pour toutes les données (3 pour cette exemple) et on divise le tout par le nombre de données (3).

5. Gradient Descent Algorithm
- Maintenant qu'on connait la précision du model, nous devons trouver le meilleur theta0 et theta1 pour gagner en précison afin de passer de 100 á un nombre plus proche de 0.
- Le gradient Descent Algo permet de minimiser la loss function.
- Fonctionnement de l'algo:
    1. Initialise theta0 et theta1 á 0
    2. Permet de trouver le theta0 et le theta1 otpimal pour otpi la fonction loss
    3. Mets á jour theta0 et theta1 dans la direction opposée du gradient (soustraction)
    4. Répeter l'étape 2 et 3 jusqu'a la convergence (proche de 0)

- Forumule pour optimiser theta0 :
    tmpTheta0 = theta0 - learningRate * 1/m somme(estimatePrice(km[i] - price[i]))

- Forumule pour optimiser theta1 :
    tmpTheta1 = theta0 - learningRate * 1/m somme(estimatePrice(km[i] - price[i])* km[i])

6. Mise á l'échelle des données
- theta0 (price en millier) et theta1 (km en dizaine de millier)
- Utilise la formule de standardisation pour la mise á l'échelle :
    x scaled = (x - mu) / sigma

    x is the feature (km)
    mu est la moyenne de la feature (km)
    sigma is the standard deviation of the feature

    ex :    mileage = [1000, 2000, 3000]
            mu = 2000
            sigma = 816.5
            ![alt text](scaled.png)

7. Implementation
-> Predict program :
- Charger les données CSV
- Les mettre á l'échelle (les km)
- Initialiser theta0 et theta1 a 0
- Faire une premiére prédiction : prix = theta0 + theta1 * km et cela pour chaque data point

-> Train program :
- Calculer l'erreur moyenne (loss function ?)
- Mettre á jour theta0 et theta1
- Repeter etape 4 a 6 jusqu'á la convergence
- Sauvegarder theta0 et theta1 dans un fichier afin de pouvoir les reutiliser dans le predict program


8. Sources
https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5

gradient descent + dérivé : https://www.charlesbordet.com/fr/gradient-descent/#

