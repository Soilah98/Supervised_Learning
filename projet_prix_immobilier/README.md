Projet 1
# Prédiction des Prix de l'Immobilier 
 
## Description
Ce projet vise à prédire les prix des maisons en fonction de plusieurs caractéristiques (surface, emplacement, etc.) en utilisant un modèle de machine learning. L’objectif est d’identifier les facteurs clés influençant le prix et d’optimiser la précision des prédictions.

## Explications des variables: 

• OverallQual : Qualité globale des matériaux et de la finition. Souvent très corrélé au prix de vente. (note sur 10, entier)  
• GarageCars : Capacité du garage en nombre de voitures. Un élément clé pour de nombreux acheteurs.   
• FullBath : Nombre de salles de bains complètes. Un facteur important pour le confort de la maison.    
• TotRmsAbvGrd : Nombre total de pièces au-dessus du sol (hors salles de bains). Plus il y a de pièces, plus le bien est généralement cher.  
• Fireplaces : Nombre de cheminées. Une caractéristique qui peut augmenter l'attrait et la valeur d'une propriété. 

• GrLivArea : Surface habitable hors sous-sol. Directement liée à la taille de la maison.  
• TotalBsmtSF : Superficie totale du sous-sol. Ajoute une grande valeur à la propriété.  
• 1stFlrSF : Superficie du rez-de-chaussée. Indique la taille de la maison.  
• GarageArea : Taille du garage en pieds carrés. 
• LotArea : Surface totale du terrain. La taille du lot est un facteur important, notamment dans les zones urbaines.  
• SalePrice : Prix de vente de la maison. C'est la variable cible que nous devons prédire. 

• YearBuilt : Année de construction. Les maisons plus récentes ont tendance à se vendre à un prix plus élevé.  
• YearRemodAdd : Année de rénovation. Les rénovations récentes peuvent augmenter le prix.  

• KitchenQual : Qualité de la cuisine. Une cuisine de haute qualité ajoute une grande valeur.  
• Neighborhood : Emplacement physique au sein des limites de la ville. L'emplacement a un impact majeur sur les prix de l'immobilier.  
• ExterQual : Qualité du matériau extérieur. Un indicateur de la qualité globale de la maison. 

**Type de variables**   
- variable discretes : OverallQual, GarageCars, FullBath, TotRmsAbvGrd, Fireplaces   
- variable categorielles : KitchenQual, Neighborhood, ExterQual 
- variables Années :  YearBuilt, YearRemodAdd  
- variable continue : GrLivArea	TotalBsmtSF	1stFlrSF, GarageArea, LotArea, 	SalePrice
  
## Méthodologie
- **Analyse des données**
  - Nettoyage des données pour traiter les valeurs manquantes et les anomalies.
  - Analyse exploratoire avec statistiques univariées et bivariées.
  - Réalisation de tests statistiques pour valider les hypothèses.
  
- **Prétraitement**
  - Encoding des variables catégorielles.
  - Sélection des caractéristiques pertinentes.
  - Normalisation des données pour assurer la convergence des algorithmes.
  - Construction des Pipeline

- **Modélisation**
  - Choix de la métrique d'évaluation adaptée.
  - Analyse du problème d'overfitting vs underfitting.
  - Amélioration et optimisation du modèle à travers des itérations.
 
- **Resultats**
  Le meilleur modele est la regression ridge avec un R2 de 0.88 et un MAE de 18600k

## Technologies utilisées
- Python (Pandas, Scikit-Learn, Matplotlib)
- Jupyter Notebook
- Visualisation avec Seaborn

## Installation et Exécution
1. Clone le dépôt :
   ```bash
   git clone https://github.com/Soilah98/projet_data_scientist.git
