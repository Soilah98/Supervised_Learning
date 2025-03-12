# <span style="color:orange;"> Objectif du Projet  
Développer un modèle de **machine learning** pour identifier les **clients à risque de désabonnement** en fonction de leurs caractéristiques **démographiques, financières et comportementales**.  

## Source des Données  
Les données proviennent de Kaggle : [[Lien vers le dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)]  

---

## Explication des Variables  

### Informations Générales  
- **Gender** : Genre du client (*Male* / *Female*)  
- **SeniorCitizen** : Indique si le client est une personne âgée (*Oui* / *Non*)  
- **Partner** : Si le client a un(e) partenaire (*Oui* / *Non*)  
- **Dependents** : Si le client a des personnes à charge (*Oui* / *Non*)  

### Détails sur le Service  
- **Tenure** : Nombre de mois pendant lesquels le client est resté avec l'entreprise  
- **PhoneService** : Dispose-t-il d'un service téléphonique ? (*Oui* / *Non*)  
- **MultipleLines** : A-t-il plusieurs lignes ? (*Oui* / *Non* / *Pas de service téléphonique*)  
- **InternetService** : Type de connexion Internet (*DSL* / *Fibre optique* / *Non*)  

### Sécurité et Assistance  
- **OnlineSecurity** : Sécurité en ligne activée ? (*Oui* / *Non* / *Pas de service Internet*)  
- **OnlineBackup** : Sauvegarde en ligne activée ? (*Oui* / *Non* / *Pas de service Internet*)  
- **DeviceProtection** : Protection des appareils ? (*Oui* / *Non* / *Pas de service Internet*)  
- **TechSupport** : Support technique disponible ? (*Oui* / *Non* / *Pas de service Internet*)  

### Services de Streaming  
- **StreamingTV** : Dispose-t-il d'un service de télévision en streaming ? (*Oui* / *Non* / *Pas de service Internet*)  
- **StreamingMovies** : Dispose-t-il d'un service de streaming de films ? (*Oui* / *Non* / *Pas de service Internet*)  

### Informations Contractuelles et Facturation  
- **Contract** : Type de contrat (*Mensuel* / *1 an* / *2 ans*)  
- **PaperlessBilling** : Facturation électronique activée ? (*Oui* / *Non*)  
- **PaymentMethod** : Mode de paiement (*Chèque électronique* / *Chèque postal* / *Virement bancaire (automatique)* / *Carte de crédit*)  
- **MonthlyCharges** : Montant facturé mensuellement  
- **TotalCharges** : Montant total facturé  

### Résiliation du Service  
- **Churn** : Le client a-t-il quitté l’entreprise ? (*Oui* / *Non*)  

---

## Méthodologie  

### 1 Analyse Exploratoire  

####  **Analyse de la Structure des Données**  
- **Variable cible** : `Churn` (*Yes* / *No*)  
    - **Classe No** : `73%`  
    - **Classe Yes** : `26%`  
    - **Déséquilibre de classes** identifié  
- **Dimensions du dataset** : `7 032 lignes × 21 colonnes`  
- **Types des variables** :  
  - **Variables qualitatives** : `15`  
  - **Variables quantitatives** : `5`  
- **Valeurs manquantes** : Aucune valeur manquante détectée  

####  ** Visualisation ** 
- Statistiques Univarié  
   - Barplot des variables qualitative 
   - Histogramme des variablea continues
- Statistiques bivariées 
   - Relation entre target et les variables continues 
   - Relation entre target et les varibales qualitatives 


#### **Test d'hypothèse**  
-  **Hypothèse 1** : Le montant des charges mensuelles pourrait influencer la résiliation du contrant ?
-  **Hypothèse 2** : La durée d'abonnement pourrait jouer un rôle dans le churn  ?

---

### 2️ Préprocessing des Données  
- **Encodage** des variables catégoriques  
- **Normalisation** des variables numériques  
- **Sélection des features pertinentes**  

---

### 3️ Modélisation et Évaluation  

#### **Modèles Testés**  
-  **Random Forest**  
-  **SVM**  
-  **Régression Logistique**  
-  **KNN**  

#### **Choix de la Métrologie d’Évaluation**  
**Recall (Sensibilité)** :  
   - Objectif : **Minimiser les faux négatifs** → Détecter **autant de churns que possible**  
   - **Pourquoi ?** Si un client à risque est mal classé comme "non churn", l’entreprise **perd une opportunité d’intervention**  

**Courbe Précision / Recall** :  
   - Ajuster le seuil de décision pour trouver le **meilleur compromis** entre **précision** et **sensibilité**  

---

## Conclusion 
Notre objectif était de maximiser la détection des clients susceptibles de résilier leur contrat. Pour cela, notre modèle atteint un **recall de 81 %**, ce qui signifie qu'il identifie correctement 81 % des clients churners présents dans notre jeu de données. De plus, il affiche une **précision de 77%**, indiquant que parmi les clients prédits comme churners, 77 % le sont réellement.
