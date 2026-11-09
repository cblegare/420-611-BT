###############
 Apprentissage
###############

L’apprentissage supervisé est une tâche dans laquelle un ordinateur apprend une
fonction qui associe des entrées à des sorties sur la base d’un ensemble de
données composé de paires entrée-sortie.

Il existe de multiples tâches relevant de l’apprentissage supervisé, et l’une
d’entre elles est la **Classification**. Il s’agit d’une tâche où la fonction
associe une entrée à une sortie discrète. Par exemple, à partir de certaines
informations sur l’humidité et la pression atmosphérique pour un jour donné
(entrée), l’ordinateur décide s’il va pleuvoir ce jour-là ou non (sortie).
L’ordinateur fait cela après s’être entraîné sur un ensemble de données
contenant de multiples jours où l’humidité et la pression atmosphérique sont
déjà associées au fait qu’il ait plu ou non.

Cette tâche peut être formalisée de la manière suivante. Nous observons la
nature, où une fonction :math:`f(\text{humidité}, \text{pression})` associe
l’entrée à une valeur discrète, soit Pluie, soit Pas de Pluie. Cette fonction
nous est cachée, et elle est probablement affectée par de nombreuses autres
variables auxquelles nous n’avons pas accès. Notre objectif est de créer une
fonction :math:`h(\text{humidité}, \text{pression}` qui peut approximer le
comportement de la fonction *f*. Une telle tâche peut être visualisée en traçant
les jours sur les dimensions de l’humidité et de la pluie (l’entrée), en
colorant chaque point de données en bleu s’il a plu ce jour-là et en rouge s’il
n’a pas plu (la sortie). Le point de données blanc ne possède que l’entrée, et
l’ordinateur doit deviner la sortie.

.. figure:: /assets/figures/classification.png

*****************************************
 Classification des plus proches voisins
*****************************************

Une façon de résoudre une tâche comme celle décrite ci-dessus consiste à
attribuer à la variable en question la valeur de l’observation la plus proche.
Ainsi, par exemple, le point blanc sur le graphique ci-dessus serait coloré en
bleu, car le point observé le plus proche est également bleu. Cela peut parfois
bien fonctionner, mais considérez le graphique ci-dessous.

.. figure:: /assets/figures/nearestneighbor.png

En suivant la même stratégie, le point blanc devrait être coloré en rouge, car
l’observation la plus proche de lui est également rouge. Cependant, en regardant
la situation dans son ensemble, il semble que la plupart des autres observations
autour de lui soient bleues, ce qui pourrait nous donner l’intuition que le bleu
est une meilleure prédiction dans ce cas, même si l’observation la plus proche
est rouge.

Une façon de contourner les limites de la classification du plus proche voisin
est d’utiliser la **classification des k plus proches voisins**
(k-nearest-neighbors classification), où le point est coloré en fonction de la
couleur la plus fréquente des *k* voisins les plus proches. C’est au programmeur
de décider ce qu’est *k*. En utilisant une classification à 3 plus proches
voisins, par exemple, le point blanc ci-dessus sera coloré en bleu, ce qui
semble intuitivement être une meilleure décision.

Un inconvénient de la classification des k plus proches voisins est que, si l’on
utilise une approche naïve, l’algorithme devra mesurer la distance de chaque
point au point en question, ce qui est coûteux en termes de calcul. Cela peut
être accéléré en utilisant des structures de données qui permettent de trouver
les voisins plus rapidement ou en élaguant les observations non pertinentes.

*****************************
 Apprentissage du Perceptron
*****************************

Une autre façon d’aborder un problème de classification, contrairement à la
stratégie des plus proches voisins, consiste à examiner les données dans leur
ensemble et à essayer de créer une frontière de décision. Dans des données
bidimensionnelles, nous pouvons tracer une ligne entre les deux types
d’observations. Chaque point de données supplémentaire sera classé en fonction
du côté de la ligne sur lequel il est tracé.

.. figure:: /assets/figures/decisionboundary.png

L’inconvénient de cette approche est que les données sont désordonnées, et il
est rare que l’on puisse tracer une ligne et diviser proprement les classes en
deux groupes d’observations sans aucune erreur. Souvent, nous ferons des
compromis en traçant une frontière qui sépare les observations correctement la
plupart du temps, mais qui continue de les classer de manière incorrecte à
l’occasion.

Dans ce cas, l’entrée composée de :

* :math:`x_1 = \text{Humidité}`
* :math:`x_2 = \text{Pression}`

sera donnée à une fonction d’hypothèse :math:`h(x_1, x_2)`, qui produira sa
prédiction quant à savoir s’il va pleuvoir ce jour-là ou non. Elle le fera en
vérifiant de quel côté de la frontière de décision tombe l’observation.
Formellement, la fonction pondérera chacune des entrées en y ajoutant une
constante, aboutissant à une équation linéaire de la forme suivante :

* Pluie si :math:`w_0 + w_1 x_1 + w_2 x_2 ≥ 0`
* Pas de pluie sinon

Souvent, la variable de sortie sera codée sous forme de 1 et de 0, de sorte que
si l’équation donne un résultat supérieur à 0, la sortie est 1 (Pluie), et 0
sinon (Pas de pluie).

Les poids et les valeurs sont représentés par des vecteurs, qui sont des
séquences de nombres (qui peuvent être stockées dans des listes ou des tuples en
Python). Nous produisons un vecteur de poids **w** : :math:`(w_0, w_1, w_2)`, et
obtenir le meilleur vecteur de poids est le but de l’algorithme d’apprentissage
automatique. Nous produisons également un vecteur d’entrée **x** : (1, x_1,
x_2).

Nous effectuons le produit scalaire des deux vecteurs. C’est-à-dire que nous
multiplions chaque valeur d’un vecteur par la valeur correspondante dans le
second vecteur, ce qui donne l’expression ci-dessus : :math:`w_0 + w_1 x_1 + w_2
x_2`. La première valeur dans le vecteur d’entrée est 1 car, lorsqu’elle est
multipliée par le poids :math:`w_0`, nous voulons la conserver comme une
constante.

Ainsi, nous pouvons représenter notre fonction d’hypothèse de la manière
suivante :

.. figure:: /assets/figures/dotproduct.png

Étant donné que le but de l’algorithme est de trouver le meilleur vecteur de
poids, lorsque l’algorithme rencontre de nouvelles données, il met à jour les
poids actuels. Il le fait en utilisant la **règle d’apprentissage du
perceptron** :

.. figure:: /assets/figures/perceptronlearning.png

Ce qu’il faut retenir d’important de cette règle, c’est que pour chaque point de
données, nous ajustons les poids pour rendre notre fonction plus précise. Les
détails, qui sont moins cruciaux pour notre propos, sont que chaque poids est
défini comme étant égal à lui-même plus une certaine valeur entre parenthèses.
Ici, y représente la valeur observée tandis que la fonction d’hypothèse
représente l’estimation. S’ils sont identiques, tout ce terme est égal à zéro,
et par conséquent le poids n’est pas modifié. Si nous avons sous-estimé (en
prédisant Pas de pluie alors que Pluie a été observée), alors la valeur entre
les parenthèses sera de 1 et le poids augmentera de la valeur de xᵢ mise à
l’échelle par :math:`\alpha`, le coefficient d’apprentissage. Si nous avons
surestimé (en prédisant Pluie alors que Pas de pluie a été observée), alors la
valeur entre les parenthèses sera de -1 et le poids diminuera de la valeur de x
mise à l’échelle par :math:`\alpha`. Plus :math:`\alpha` est élevé, plus
l’influence de chaque nouvel événement sur le poids est forte.

Le résultat de ce processus est une fonction à seuil qui passe de 0 à 1 une fois
que la valeur estimée franchit un certain seuil.

.. figure:: /assets/figures/hardthreshold.png

Le problème avec ce type de fonction est qu’elle est incapable d’exprimer
l’incertitude, puisqu’elle ne peut être égale qu’à 0 ou à 1. Elle emploie un
**seuil strict** (hard threshold). Une façon de contourner cela consiste à
utiliser une fonction logistique, qui emploie un **seuil souple** (soft
threshold). Une fonction logistique peut produire un nombre réel compris entre 0
et 1, qui exprimera la confiance dans l’estimation. Plus la valeur est proche de
1, plus il est probable qu’il pleuve.

.. figure:: /assets/figures/softthreshold.png

********************************
 Machines à vecteurs de support
********************************

En plus des plus proches voisins et de la régression linéaire, une autre
approche de la classification est la Machine à Vecteurs de Support (SVM). Cette
approche utilise un vecteur supplémentaire (vecteur de support) près de la
frontière de décision pour prendre la meilleure décision lors de la séparation
des données. Considérez l’exemple ci-dessous.

.. figure:: /assets/figures/supportvector.png

Toutes les frontières de décision fonctionnent dans la mesure où elles séparent
les données sans aucune erreur. Cependant, sont-elles toutes aussi bonnes ? Les
deux frontières de décision les plus à gauche sont très proches de certaines
observations. Cela signifie qu’un nouveau point de données qui ne diffère que
légèrement d’un groupe peut être classé à tort dans l’autre. À l’opposé, la
frontière de décision la plus à droite maintient la plus grande distance par
rapport à chacun des groupes, offrant ainsi la plus grande marge de manœuvre
pour la variation en son sein. Ce type de frontière, qui est aussi éloignée que
possible des deux groupes qu’elle sépare, est appelée le **Séparateur à vaste
marge**.

Un autre avantage des machines à vecteurs de support est qu’elles peuvent
représenter des frontières de décision avec plus de deux dimensions, ainsi que
des frontières de décision non linéaires, comme ci-dessous.

.. figure:: /assets/figures/circleboundary.png

En résumé, il existe de multiples façons d’aborder les problèmes de
classification, sans qu’aucune ne soit toujours meilleure que l’autre. Chacune a
ses inconvénients et pourrait s’avérer plus utile que les autres dans des
situations spécifiques.

************
 Régression
************

La régression est une tâche d’apprentissage supervisé d’une fonction qui associe
un point d’entrée à une valeur continue, un nombre réel. Cela diffère de la
classification dans la mesure où les problèmes de classification associent une
entrée à des valeurs discrètes (Pluie ou Pas de pluie).

Par exemple, une entreprise pourrait utiliser la régression pour répondre à la
question de savoir comment l’argent dépensé en publicité prédit l’argent gagné
en ventes. Dans ce cas, une fonction observée *f(publicité)* représente les
revenus observés à la suite de l’argent dépensé en publicité (notez que la
fonction peut prendre plus d’une variable d’entrée). Ce sont les données avec
lesquelles nous commençons. Avec ces données, nous voulons trouver une fonction
d’hypothèse *h(publicité)* qui essaiera d’approximer le comportement de la
fonction *f*. *h* générera une ligne dont le but n’est pas de séparer les types
d’observations, mais de prédire, sur la base de l’entrée, quelle sera la valeur
de la sortie.

.. figure:: /assets/figures/regression.png

********************
 Fonctions de perte
********************

Les fonctions de perte sont un moyen de quantifier l’utilité perdue par l’une
des règles de décision ci-dessus. Moins la prédiction est précise, plus la perte
est importante.

Pour les problèmes de classification, nous pouvons utiliser une **Fonction de
perte 0-1** (0-1 Loss Function).

.. math::

    L(\text{réel}, \text{prédit})` = \begin{cases}
        0 & si \text{réel} = \text{prédit} \\
        1 & sinon
    \end{cases}

En d’autres termes, cette fonction prend de la valeur lorsque la prédiction est
incorrecte et n’en prend pas lorsqu’elle est correcte (c’est-à-dire lorsque les
valeurs observées et prédites correspondent).

.. figure:: /assets/figures/01loss.png

Dans l’exemple ci-dessus, les jours qui sont évalués à 0 sont ceux où nous avons
correctement prédit la météo (les jours de pluie sont en dessous de la ligne et
les jours sans pluie sont au-dessus de la ligne). Cependant, les jours où il n’a
pas plu en dessous de la ligne et les jours où il a plu au-dessus de celle-ci
sont ceux que nous n’avons pas réussi à prédire. Nous donnons à chacun la valeur
de 1 et les additionnons pour obtenir une estimation empirique des pertes de
notre frontière de décision.

Les fonctions de perte :math:`L_1` et :math:`L_2` peuvent être utilisées lors de
la prédiction d’une valeur continue. Dans ce cas, nous sommes intéressés à
quantifier pour chaque prédiction de *combien* elle différait de la valeur
observée. Nous le faisons en prenant soit la valeur absolue, soit la valeur au
carré de la valeur observée moins la valeur prédite (c’est-à-dire à quelle
distance la prédiction se trouvait de la valeur observée).

* :math:`L_1` : :math:`L(\text{réel}, \text{prédit}) = |\text{réel} -
  \text{prédit}|`
* :math:`L_2` : :math:`L(\text{réel}, \text{prédit}) = (\text{réel} -
  \text{prédit})^2`

On peut choisir la fonction de perte qui sert le mieux ses objectifs.
:math:`L_2` pénalise les valeurs aberrantes plus durement que :math:`L_1` car
elle élève la différence au carré. :math:`L_1` peut être visualisée en sommant
les distances de chaque point observé au point prédit sur la ligne de régression
:

.. figure:: /assets/figures/l1.png

******************
 Surapprentissage
******************

Le surapprentissage se produit lorsqu’un modèle s’ajuste si bien aux données
d’entraînement qu’il ne parvient pas à se généraliser à d’autres ensembles de
données. En ce sens, les fonctions de perte sont une arme à double tranchant.
Dans les deux exemples ci-dessous, la fonction de perte est minimisée de telle
sorte que la perte est égale à 0. Cependant, il est peu probable qu’elle
s’ajuste bien à de nouvelles données.

.. figure:: /assets/figures/overfitting.png

Par exemple, dans le graphique de gauche, un point à côté du point rouge au bas
de l’écran a de fortes chances d’être Pluie (bleu). Cependant, avec le modèle en
surapprentissage, il sera classé comme Pas de Pluie (rouge).

****************
 Régularisation
****************

La régularisation est le processus consistant à pénaliser les hypothèses qui
sont plus complexes pour favoriser des hypothèses plus simples et plus
générales. Nous utilisons la régularisation pour éviter le surapprentissage.

Dans la régularisation, nous estimons le coût de la fonction d’hypothèse h en
additionnant sa perte et une mesure de sa complexité.

.. math::

    \text{coût}(h) = perte(h) + \lambda \cdot \text{complexité}(h)

Lambda (:math:`\lambda`) est une constante que nous pouvons utiliser pour
moduler la force avec laquelle nous pénalisons la complexité dans notre fonction
de coût. Plus :math:`\lambda` est élevé, plus la complexité est coûteuse.

Une façon de tester si nous avons surajusté le modèle est la **Validation
croisée par maintien d’un échantillon de test** (Holdout Cross Validation). Dans
cette technique, nous divisons toutes les données en deux : un **ensemble
d’entraînement** (training set) et un **ensemble de test** (test set). Nous
exécutons l’algorithme d’apprentissage sur l’ensemble d’entraînement, puis nous
observons à quel point il prédit bien les données de l’ensemble de test. L’idée
ici est qu’en testant sur des données qui n’ont pas été utilisées lors de
l’entraînement, nous pouvons mesurer à quel point l’apprentissage se généralise
bien.

L’inconvénient de la validation croisée par maintien est que nous ne pouvons pas
entraîner le modèle sur une partie des données, puisqu’elle est utilisée à des
fins d’évaluation. Une façon de contourner ce problème consiste à utiliser la
**Validation croisée à k blocs** (k-Fold Cross-Validation). Dans ce processus,
nous divisons les données en k ensembles. Nous exécutons l’entraînement k fois,
en laissant chaque fois de côté un ensemble de données pour l’utiliser comme
ensemble de test. Nous nous retrouvons avec k évaluations différentes de notre
modèle, dont nous pouvons faire la moyenne et obtenir une estimation de la
manière dont notre modèle se généralise sans perdre de données d’entraînement.

**************
 scikit-learn
**************

Comme c’est souvent le cas avec Python, il existe de multiples bibliothèques qui
nous permettent d’utiliser commodément des algorithmes d’apprentissage
automatique. L’une de ces bibliothèques est scikit-learn.

.. figure:: /assets/figures/banknotes.png

À titre d’exemple, nous allons utiliser un jeu de données au format `CSV
<https://en.wikipedia.org/wiki/Comma-separated_values>`__ de billets de banque
contrefaits.

Les quatre colonnes de gauche sont des données que nous pouvons utiliser pour
prédire si un billet est authentique ou contrefait, ce qui correspond à des
données externes fournies par un humain, codées sous forme de 0 et 1. Nous
pouvons maintenant entraîner notre modèle sur cet ensemble de données et voir si
nous pouvons prédire si de nouveaux billets sont authentiques ou non.

.. code-block:: python

    import csv
    import random

    from sklearn import svm
    from sklearn.linear_model import Perceptron
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier

    # model = KNeighborsClassifier(n_neighbors=1)
    # model = svm.SVC()
    model = Perceptron()

Notez qu’après avoir importé les bibliothèques, nous pouvons choisir quel modèle
utiliser. Le reste du code restera le même. SVC signifie *Support Vector
Classifier* (que nous connaissons sous le nom de machine à vecteurs de support).
Le ``KNeighborsClassifier`` utilise la stratégie des k-voisins, et requiert en
entrée le nombre de voisins qu’il doit considérer.

.. code-block:: python

    # Read data in from file
    with open("banknotes.csv") as f:
        reader = csv.reader(f)
        next(reader)

        data = []
        for row in reader:
            data.append(
                {
                    "evidence": [float(cell) for cell in row[:4]],
                    "label": "Authentic" if row[4] == "0" else "Counterfeit",
                }
            )

    # Separate data into training and testing groups
    holdout = int(0.40 * len(data))
    random.shuffle(data)
    testing = data[:holdout]
    training = data[holdout:]

    # Train model on training set
    X_training = [row["evidence"] for row in training]
    y_training = [row["label"] for row in training]
    model.fit(X_training, y_training)

    # Make predictions on the testing set
    X_testing = [row["evidence"] for row in testing]
    y_testing = [row["label"] for row in testing]
    predictions = model.predict(X_testing)

    # Compute how well we performed
    correct = 0
    incorrect = 0
    total = 0
    for actual, predicted in zip(y_testing, predictions):
        total += 1
        if actual == predicted:
            correct += 1
        else:
            incorrect += 1

    # Print results
    print(f"Results for model {type(model).__name__}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    print(f"Accuracy: {100 * correct / total:.2f}%")

Cette version manuelle de l’exécution de l’algorithme peut être trouvée dans le
code source de cette leçon sous le nom ``banknotes0.py``. Étant donné que
l’algorithme est souvent utilisé d’une manière similaire, scikit-learn contient
des fonctions supplémentaires qui rendent le code encore plus succinct et facile
à utiliser, et cette version peut être trouvée sous ``banknotes1.py``.

********************************
 Apprentissage par renforcement
********************************

L’apprentissage par renforcement est une autre approche de l’apprentissage
automatique, où après chaque action, l’agent reçoit un retour sous forme de
récompense ou de punition (une valeur numérique positive ou négative).

.. figure:: /assets/figures/reinforcement.png

Le processus d’apprentissage commence par la fourniture d’un état à l’agent par
l’environnement. Ensuite, l’agent effectue une action sur cet état. En se basant
sur cette action, l’environnement retournera un état et une récompense à
l’agent, où la récompense peut être positive, rendant le comportement plus
probable à l’avenir, ou négative (c.-à-d. une punition), rendant le comportement
moins probable à l’avenir.

Ce type d’algorithme peut être utilisé pour entraîner des robots marcheurs, par
exemple, où chaque pas réussi renvoie un nombre positif (récompense) et chaque
chute un nombre négatif (punition).

Processus de décision markoviens
================================

L’apprentissage par renforcement peut être considéré comme un processus de
décision markovien, possédant les propriétés suivantes :

* Un ensemble d’états :math:`S`
* Un ensemble d’actions :math:`Actions(S)`
* Un modèle de transition :math:`P(s’ | s, a)`
* Une fonction de récompense :math:`R(s, a, s’)`

Par exemple, considérez la tâche suivante :

.. figure:: /assets/figures/markov.png

L’agent est le cercle jaune, et il doit se rendre au carré vert tout en évitant
les carrés rouges. Chaque carré de la tâche est un état. Se déplacer vers le
haut, le bas ou les côtés est une action. Le modèle de transition nous donne le
nouvel état après l’exécution d’une action, et la fonction de récompense
correspond au type de rétroaction que reçoit l’agent. Par exemple, si l’agent
choisit d’aller à droite, il marchera sur un carré rouge et recevra une
rétroaction négative. Cela signifie que l’agent apprendra que, lorsqu’il se
trouve dans l’état correspondant au carré en bas à gauche, il doit éviter
d’aller à droite. De cette façon, l’agent commencera à explorer l’espace, en
apprenant quelles paires état-action il doit éviter. L’algorithme peut être
probabiliste, choisissant d’entreprendre différentes actions dans différents
états en fonction d’une certaine probabilité qui est augmentée ou diminuée en
fonction de la récompense. Lorsque l’agent atteint le carré vert, il obtiendra
une récompense positive, apprenant ainsi qu’il est favorable d’entreprendre
l’action qu’il a prise dans l’état précédent.

************
 Q-Learning
************

Le Q-Learning est un modèle d’apprentissage par renforcement, où une fonction
:math:`Q(s, a)` produit une estimation de la valeur qu’il y a à entreprendre
l’action *a* dans l’état *s*.

Le modèle commence avec toutes les valeurs estimées égales à 0 ( :math:`Q(s, a)
= 0` pour tous les *s, a*). Lorsqu’une action est entreprise et qu’une
récompense est reçue, la fonction fait deux choses : 1) elle estime la valeur de
:math:`Q(s, a)` en se basant sur la récompense actuelle et les récompenses
futures attendues, et 2) elle met à jour :math:`Q(s, a)` pour prendre en compte
à la fois l’ancienne estimation et la nouvelle estimation. Cela nous donne un
algorithme qui est capable d’améliorer ses connaissances passées sans repartir
de zéro.

.. math::

    Q(s, a) ⟵ Q(s, a) + \alpha \cdot (\text{nouvelle estimation de valeur} - Q(s, a))

La valeur mise à jour de :math:`Q(s, a)` est égale à la valeur précédente de
:math:`Q(s, a)` à laquelle s’ajoute une valeur de mise à jour. Cette valeur est
déterminée comme la différence entre la nouvelle valeur et l’ancienne valeur,
multipliée par :math:`\alpha`, un coefficient d’apprentissage. Lorsque
:math:`\alpha = 1`, la nouvelle estimation écrase simplement l’ancienne. Lorsque
:math:`\alpha = 0`, la valeur estimée n’est jamais mise à jour. En augmentant et
en diminuant :math:`\alpha`, nous pouvons déterminer à quelle vitesse les
connaissances précédentes sont mises à jour par de nouvelles estimations.

La nouvelle estimation de valeur peut être exprimée comme la somme de la
récompense (r) et de l’estimation de la récompense future. Pour obtenir
l’estimation de la récompense future, nous considérons le nouvel état que nous
avons obtenu après avoir pris la dernière action, et ajoutons l’estimation de
l’action dans ce nouvel état qui mènera à la récompense la plus élevée. De cette
façon, nous estimons l’utilité d’effectuer l’action *a* dans l’état *s* non
seulement par la récompense reçue, mais aussi par l’utilité attendue de la
prochaine étape. La valeur de l’estimation de la récompense future peut parfois
apparaître avec un coefficient gamma qui contrôle la valeur accordée aux
récompenses futures. Nous nous retrouvons avec l’équation suivante :

.. math::

    Q(s, a) \leftarrow Q(s, a) + \alpha ((r + \gamma \cdot max_{a'} Q(s', a') - Q(s, a))

Un algorithme de **Prise de décision gloutonne** (Greedy Decision-Making) ignore
complètement les récompenses futures estimées, et choisit toujours l’action
**a** dans l’état actuel **s** qui a le :math:`Q(s, a)` le plus élevé.

Cela nous amène à discuter du compromis **Exploration vs Exploitation**. Un
algorithme glouton exploite toujours, en entreprenant les actions qui sont déjà
établies pour mener à de bons résultats. Cependant, il suivra toujours le même
chemin vers la solution, sans jamais trouver un meilleur chemin. L’exploration,
en revanche, signifie que l’algorithme peut utiliser un itinéraire précédemment
inexploré sur son chemin vers la cible, ce qui lui permet de découvrir des
solutions plus efficaces en cours de route. Par exemple, si vous écoutez les
mêmes chansons à chaque fois, vous savez que vous les apprécierez, mais vous ne
découvrirez jamais de nouvelles chansons que vous pourriez aimer encore plus !

Pour implémenter le concept d’exploration et d’exploitation, nous pouvons
utiliser l’algorithme **:math:`\epsilon`-glouton**. Dans ce type d’algorithme,
nous fixons :math:`\epsilon` en fonction de la fréquence à laquelle nous voulons
nous déplacer de manière aléatoire. Avec une probabilité :math:`1 - \epsilon`,
l’algorithme choisit le meilleur mouvement (exploitation). Avec une probabilité
:math:`\epsilon`, l’algorithme choisit un mouvement aléatoire (exploration).

Une autre façon d’entraîner un modèle d’apprentissage par renforcement est de
donner une rétroaction non pas à chaque mouvement, mais à la fin de l’ensemble
du processus. Par exemple, considérez une partie du jeu de Nim. Dans ce jeu,
différents nombres d’objets sont répartis entre des piles. Chaque joueur prend
n’importe quel nombre d’objets dans une seule pile, et le joueur qui prend le
dernier objet perd. Dans un tel jeu, une IA non entraînée jouera de manière
aléatoire, et il sera facile de gagner contre elle. Pour entraîner l’IA, elle
commencera par jouer une partie au hasard, et obtiendra à la fin une récompense
de 1 en cas de victoire et de -1 en cas de défaite. Lorsqu’elle est entraînée
sur 10 000 parties, par exemple, elle est déjà suffisamment intelligente pour
qu’il soit difficile de gagner contre elle.

Cette approche devient plus exigeante en termes de calcul lorsqu’un jeu comporte
de multiples états et actions possibles, comme les échecs. Il est impossible de
générer une valeur estimée pour chaque mouvement possible dans chaque état
possible. Dans ce cas, nous pouvons utiliser une **approximation de fonction**
(function approximation), qui nous permet d’approximer :math:`Q(s, a)` à l’aide
de diverses autres caractéristiques, plutôt que de stocker une valeur pour
chaque paire état-action. Ainsi, l’algorithme devient capable de reconnaître
quels mouvements sont suffisamment similaires pour que leur valeur estimée doive
l’être également, et d’utiliser cette heuristique dans sa prise de décision.

*****************************
 Apprentissage non supervisé
*****************************

Dans tous les cas que nous avons vus précédemment, comme dans l’apprentissage
supervisé, nous disposions de données avec des étiquettes (labels) à partir
desquelles l’algorithme pouvait apprendre. Par exemple, lorsque nous avons
entraîné un algorithme à reconnaître les faux billets, chaque billet de banque
possédait quatre variables avec des valeurs différentes (les données d’entrée)
et s’il était contrefait ou non (l’étiquette). Dans l’apprentissage non
supervisé, seules les données d’entrée sont présentes et l’IA apprend des
modèles (patterns) dans ces données.

Regroupement (Clustering)
    Le regroupement (Clustering) est une tâche d’apprentissage non supervisé qui
    prend les données d’entrée et les organise en groupes de sorte que des
    objets similaires se retrouvent dans le même groupe. Cela peut être utilisé,
    par exemple, dans la recherche en génétique, lorsque l’on essaie de trouver
    des gènes similaires, ou dans la segmentation d’image, lors de la définition
    de différentes parties de l’image en fonction de la similitude entre les
    pixels.

Regroupement des k-moyennes
===========================

Le regroupement des k-moyennes est un algorithme permettant d’effectuer une
tâche de clustering. Il cartographie tous les points de données dans un espace,
puis place de manière aléatoire k centres de regroupement dans l’espace (c’est
au programmeur de décider combien ; c’est l’état de départ que nous voyons à
gauche). Chaque centre de regroupement est simplement un point dans l’espace.
Ensuite, chaque regroupement se voit attribuer tous les points qui sont plus
proches de son centre que de n’importe quel autre centre (c’est l’image du
milieu). Puis, dans un processus itératif, le centre du regroupement se déplace
vers le milieu de tous ces points (l’état sur la droite), et les points sont
ensuite réassignés aux regroupements dont les centres leur sont maintenant les
plus proches. Lorsque, après avoir répété le processus, chaque point reste dans
le même regroupement qu’auparavant, nous avons atteint un équilibre et
l’algorithme est terminé, nous laissant avec des points divisés entre les
différents regroupements.

.. figure:: /assets/figures/kclustering.png


***********
 Exercices
***********

.. ia2:exercice:: 50.1
    Classification avec les k plus proches voisins (k-NN)

    Un système d'intelligence artificielle tente de prédire la météo (Pluie ou Pas de pluie) en se basant sur deux variables : le taux d'humidité et la pression atmosphérique. Le système utilise l'algorithme des k plus proches voisins (k-NN).

    Voici les données existantes (les voisins observés) :

    * Jour 1 : (Humidité élevée, Pression basse) -> Pluie
    * Jour 2 : (Humidité faible, Pression haute) -> Pas de pluie
    * Jour 3 : (Humidité moyenne, Pression basse) -> Pluie
    * Jour 4 : (Humidité très faible, Pression très haute) -> Pas de pluie
    * Jour 5 : (Humidité très élevée, Pression moyenne) -> Pluie

    On évalue une nouvelle journée, le Jour 6, avec une humidité et une pression spécifiques.
    Les distances mathématiques entre le Jour 6 et les autres jours dans l'espace des caractéristiques sont calculées ainsi :

    * Distance avec Jour 1 : 2.23
    * Distance avec Jour 2 : 2.23
    * Distance avec Jour 3 : 1.00
    * Distance avec Jour 4 : 2.82
    * Distance avec Jour 5 : 3.16

    a. Si l'algorithme utilise **k=1** (le plus proche voisin), quelle sera la prédiction pour le Jour 6 ?
    b. Si l'algorithme utilise **k=3** (les 3 plus proches voisins), quelle sera la prédiction pour le Jour 6 ?
    c. Expliquez comment la valeur de *k* permet de contourner les limites d'une classification avec un seul voisin (k=1).

    Solution: :ia2:solution:`50.1`

.. ia2:exercice:: 50.2
    Apprentissage du Perceptron et règle de mise à jour

    Une intelligence artificielle utilise un perceptron pour déterminer si un email est un pourriel (1) ou non (0).
    La fonction d'hypothèse utilise un seuil strict : 1 si :math:`w_0 + w_1 x_1 + w_2 x_2 \ge 0`, sinon 0.

    * Les poids actuels sont : :math:`(w_0=0, w_1=0.5, w_2=-0.5)`.
    * Le taux d'apprentissage (:math:`\alpha`) est de 0.1.
    * Un nouvel email arrive avec les caractéristiques : :math:`x_1=2` (nombre de mots « gratuit ») et :math:`x_2=1` (longueur de l'email).
    * L'email est en réalité un pourriel, donc la valeur observée (:math:`y`) est 1.

    a. Calculez la prédiction actuelle de la fonction d'hypothèse (:math:`h(x)`) pour cet email.
    b. En utilisant la règle d'apprentissage du perceptron (:math:`w_i \leftarrow w_i + \alpha (y - h(x)) \times x_i`), calculez les nouveaux poids :math:`w_1` et :math:`w_2`. (Pour :math:`w_0`, considérez que :math:`x_0 = 1`).

    Solution: :ia2:solution:`50.2`

.. ia2:exercice:: 50.3
    Machines à vecteurs de support (SVM) et frontières de décision

    Un ingénieur de données entraîne un modèle SVM pour séparer des chats et des chiens selon leur poids et leur taille. L'ingénieur doit choisir entre deux frontières de décision possibles (Frontière A et Frontière B). Les deux frontières séparent correctement tous les points d'entraînement sans aucune erreur.

    * La Frontière A passe très près de plusieurs observations.
    * La Frontière B maintient la plus grande distance possible par rapport à chaque groupe d'observations.

    a. Selon les principes des machines à vecteurs de support (SVM), quelle frontière l'algorithme privilégiera-t-il et pourquoi ? Comment nomme-t-on ce type de frontière ?
    b. Identifiez un avantage supplémentaire des machines à vecteurs de support par rapport à une simple régression linéaire concernant la forme des frontières de décision.

    Solution: :ia2:solution:`50.3`

.. ia2:exercice:: 50.4
    Régression, Fonctions de perte et Régularisation

    Un modèle de régression linéaire tente de prédire le prix d'une maison (en milliers de dollars) en fonction de sa superficie.
    Voici les prix réels (observés) et les prix prédits par le modèle pour 3 maisons :

    * Maison 1 : Réel = 200, Prédit = 210
    * Maison 2 : Réel = 350, Prédit = 350
    * Maison 3 : Réel = 400, Prédit = 380

    a. Calculez la perte totale en utilisant la fonction de perte :math:`L_1`.
    b. Calculez la perte totale en utilisant la fonction de perte :math:`L_2`.
    c. Laquelle de ces deux fonctions pénalise le plus durement les valeurs aberrantes (les grandes erreurs) ?
    d. Pour éviter que le modèle ne colle trop parfaitement aux données (surapprentissage), l'ingénieur ajoute une mesure de complexité à la fonction de perte : :math:`\text{coût}(h) = \text{perte}(h) + \lambda \cdot \text{complexité}(h)`. Comment s'appelle ce processus et quel est le rôle de :math:`\lambda` ?

    Solution: :ia2:solution:`50.4`

.. ia2:exercice:: 50.5
    Apprentissage par renforcement : Q-Learning et l'équation de mise à jour

    Un robot-aspirateur utilise l'algorithme Q-Learning pour apprendre à naviguer dans une pièce.
    L'estimation actuelle de la valeur d'avancer tout droit dans l'état actuel est :math:`Q(s, a) = 5`.
    Le robot avance, reçoit une récompense immédiate :math:`r = 2`, et atteint un nouvel état :math:`s'`.
    Dans ce nouvel état :math:`s'`, l'action ayant la plus haute estimation donne :math:`\max_{a'} Q(s', a') = 10`.
    Le coefficient d'apprentissage est :math:`\alpha = 0.5` et le facteur d'escompte (gamma) est :math:`\gamma = 0.8`.

    Rappel de l'équation : :math:`Q(s, a) \leftarrow Q(s, a) + \alpha \cdot ((r + \gamma \cdot \max_{a'} Q(s', a')) - Q(s, a))`.

    a. Calculez la nouvelle estimation de valeur (c'est-à-dire :math:`r + \gamma \cdot \max_{a'} Q(s', a')`).
    b. Calculez la valeur finale mise à jour de :math:`Q(s, a)`.
    c. Si le robot utilise une approche :math:`\epsilon`-gloutonne pour choisir ses actions, expliquez la différence entre l'exploration et l'exploitation.

    Solution: :ia2:solution:`50.5`

.. ia2:exercice:: 50.6
    Utilisation de scikit-learn en Python

    Le cours montre comment utiliser la bibliothèque ``scikit-learn`` pour entraîner et évaluer des modèles d'apprentissage automatique de manière succincte[cite: 13].

    Complétez le script Python ci-dessous en utilisant les méthodes standard de ``scikit-learn`` (comme démontré dans l'exemple des billets de banque contrefaits) pour accomplir les trois étapes manquantes[cite: 13] :
    1. Initialiser le modèle des k plus proches voisins avec $k=3$[cite: 13].
    2. Ajuster (entraîner) le modèle sur les données d'entraînement[cite: 13].
    3. Générer les prédictions pour l'ensemble de test[cite: 13].

    .. code-block:: python

        from sklearn.neighbors import KNeighborsClassifier

        X_training = [[0.8, 0.2], [0.4, 0.5], [0.9, 0.8], [0.1, 0.9]]
        y_training = ["Pluie", "Pas de pluie", "Pluie", "Pas de pluie"]

        X_testing = [[0.7, 0.3], [0.2, 0.8]]

        # 1. Initialiser le modèle avec 3 voisins
        model = # À COMPLÉTER

        # 2. Entraîner le modèle sur les données d'entraînement (X_training, y_training)
        # À COMPLÉTER

        # 3. Faire une prédiction sur les données de test (X_testing)
        predictions = # À COMPLÉTER

        print(predictions)

    Solution: :ia2:solution:`50.6`

.. ia2:exercice:: 50.7
    Implémentation de l'équation de mise à jour Q-Learning en Python

    L'algorithme Q-Learning met à jour ses estimations de valeurs en se basant sur la formule suivante[cite: 13] :
    :math:`Q(s, a) \leftarrow Q(s, a) + \alpha \cdot ((r + \gamma \cdot \max_{a'} Q(s', a')) - Q(s, a))`

    Écrivez une fonction Python ``update_q_value`` qui prend en paramètres les valeurs nécessaires et retourne la nouvelle valeur calculée de :math:`Q(s, a)`[cite: 13].

    .. code-block:: python

        def update_q_value(current_q, reward, max_future_q, alpha, gamma):
            """
            Calcule et retourne la nouvelle valeur Q(s, a).
            """
            # À COMPLÉTER : Implémenter l'équation de mise à jour
            pass

        # Code de test avec les valeurs de l'exercice 50.5
        # Le résultat attendu affiché devrait être 7.5
        nouveau_q = update_q_value(current_q=5, reward=2, max_future_q=10, alpha=0.5, gamma=0.8)
        print(nouveau_q)

    Solution: :ia2:solution:`50.7`

**********
 Solutions
**********

.. ia2:solution:: 50.1
    Classification avec les k plus proches voisins (k-NN)

    Solution de :ia2:ex:`50.1`

    a. Avec **k=1**, l'algorithme cherche le voisin le plus proche. La plus petite distance est 1.00, correspondant au Jour 3. Le Jour 3 a pour résultat « Pluie ». La prédiction pour le Jour 6 sera donc **Pluie**.
    b. Avec **k=3**, l'algorithme identifie les 3 voisins les plus proches. Ce sont le Jour 3 (distance 1.00), le Jour 1 (distance 2.23) et le Jour 2 (distance 2.23). Leurs résultats respectifs sont : Pluie, Pluie, et Pas de pluie. La classe la plus fréquente (la majorité) parmi ces 3 voisins dictera la décision. Puisqu'il y a 2 « Pluie » et 1 « Pas de pluie », la prédiction sera **Pluie**.
    c. Utiliser une approche basée sur plusieurs voisins (k > 1) permet de contourner les limites de la classification du plus proche voisin unique en rendant le modèle moins sensible au bruit. Si le point le plus proche est une anomalie ou une exception (par exemple, un jour de pluie atypique entouré de jours secs), examiner les *k* voisins permet de capturer la tendance générale locale et de prendre une meilleure décision.

.. ia2:solution:: 50.2
    Apprentissage du Perceptron et règle de mise à jour

    Solution de :ia2:ex:`50.2`

    a. Calcul de la fonction d'hypothèse :math:`h(x)` :
       On calcule d'abord le produit scalaire : :math:`w_0 + w_1 x_1 + w_2 x_2 = 0 + (0.5 \times 2) + (-0.5 \times 1) = 0 + 1 - 0.5 = 0.5`.
       Puisque la somme (0.5) est supérieure ou égale à 0, la prédiction :math:`h(x)` est **1 (Pourriel)**.

    b. Mise à jour des poids :
       Puisque la prédiction (1) est identique à la valeur observée (1), le perceptron a fait une bonne prédiction.
       Le terme d'erreur :math:`(y - h(x))` est donc :math:`1 - 1 = 0`.
       La règle d'apprentissage indique que chaque poids est mis à jour en ajoutant le produit de l'erreur, du taux d'apprentissage et de l'entrée.
       Comme l'erreur est nulle, les poids **ne seront pas modifiés** :

       * Nouveau :math:`w_1 = 0.5 + 0.1 \times 0 \times 2 = 0.5`
       * Nouveau :math:`w_2 = -0.5 + 0.1 \times 0 \times 1 = -0.5`

.. ia2:solution:: 50.3
    Machines à vecteurs de support (SVM) et frontières de décision

    Solution de :ia2:ex:`50.3`

    a. L'algorithme privilégiera la **Frontière B**. Les Machines à Vecteurs de Support recherchent le **Séparateur à vaste marge**, c'est-à-dire une frontière de décision qui est aussi éloignée que possible des groupes qu'elle sépare. Cela offre la plus grande marge de manœuvre et réduit le risque qu'un nouveau point de données légèrement différent soit classé à tort.
    b. Un avantage des machines à vecteurs de support est qu'elles peuvent représenter des frontières de décision **non linéaires** (comme des cercles) ainsi que des frontières avec plus de deux dimensions.

.. ia2:solution:: 50.4
    Régression, Fonctions de perte et Régularisation

    Solution de :ia2:ex:`50.4`

    a. La fonction de perte :math:`L_1` prend la valeur absolue de la différence entre la valeur réelle et la valeur prédite (:math:`|\text{réel} - \text{prédit}|`) :

       * Maison 1 : :math:`|200 - 210| = 10`
       * Maison 2 : :math:`|350 - 350| = 0`
       * Maison 3 : :math:`|400 - 380| = 20`

       Perte totale :math:`L_1 = 10 + 0 + 20 = 30`.

    b. La fonction de perte :math:`L_2` prend la différence au carré (:math:`(\text{réel} - \text{prédit})^2`) :

       * Maison 1 : :math:`(-10)^2 = 100`
       * Maison 2 : :math:`(0)^2 = 0`
       * Maison 3 : :math:`(20)^2 = 400`

       Perte totale :math:`L_2 = 100 + 0 + 400 = 500`.

    c. La fonction de perte **:math:`L_2`** pénalise plus durement les valeurs aberrantes (outliers) que la fonction :math:`L_1`, car elle élève la différence au carré.

    d. Ce processus s'appelle la **régularisation**. Il pénalise les hypothèses complexes pour favoriser des modèles plus simples et plus généraux. La constante :math:`\lambda` (Lambda) permet de moduler la force de cette pénalité : plus :math:`\lambda` est élevé, plus la complexité du modèle est « coûteuse » dans le calcul global.

.. ia2:solution:: 50.5
    Apprentissage par renforcement : Q-Learning et l'équation de mise à jour

    Solution de :ia2:ex:`50.5`

    a. La nouvelle estimation de valeur est calculée en additionnant la récompense immédiate à l'estimation de la récompense future maximale, pondérée par gamma :

       .. math::

          \text{Nouvelle estimation} = r + \gamma \cdot \max_{a'} Q(s', a') = 2 + 0.8 \cdot 10 = 2 + 8 = 10

    b. On applique l'équation de mise à jour complète :

       .. math::

          Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (\text{nouvelle estimation} - Q(s, a))

       En remplaçant par les valeurs :

       .. math::

          Q(s, a) \leftarrow 5 + 0.5 \cdot (10 - 5) = 5 + 0.5 \cdot 5 = 5 + 2.5 = 7.5

    c. L'**exploitation** consiste à choisir l'action qui est déjà établie pour mener aux meilleurs résultats, maximisant ainsi les gains immédiats connus. L'**exploration** signifie que l'algorithme entreprend parfois des actions ou des itinéraires précédemment inexplorés (des mouvements aléatoires), ce qui lui permet de découvrir de nouvelles solutions qui pourraient être encore plus efficaces à long terme.


.. ia2:solution:: 50.6
    Utilisation de scikit-learn en Python

    Solution de :ia2:ex:`50.6`

    Pour utiliser ``scikit-learn``, on instancie la classe du modèle en passant les hyperparamètres requis, on utilise la méthode ``fit()`` pour l'entraînement et la méthode ``predict()`` pour évaluer de nouvelles données[cite: 13].

    .. code-block:: python

        from sklearn.neighbors import KNeighborsClassifier

        X_training = [[0.8, 0.2], [0.4, 0.5], [0.9, 0.8], [0.1, 0.9]]
        y_training = ["Pluie", "Pas de pluie", "Pluie", "Pas de pluie"]

        X_testing = [[0.7, 0.3], [0.2, 0.8]]

        # 1. Initialiser le modèle avec 3 voisins
        model = KNeighborsClassifier(n_neighbors=3)

        # 2. Entraîner le modèle sur les données d'entraînement
        model.fit(X_training, y_training)

        # 3. Faire une prédiction sur les données de test
        predictions = model.predict(X_testing)

        print(predictions)

.. ia2:solution:: 50.7
    Implémentation de l'équation de mise à jour Q-Learning en Python

    Solution de :ia2:ex:`50.7`

    La fonction traduit l'équation mathématique en code Python. Il est recommandé de calculer d'abord la nouvelle estimation pour rendre le code plus lisible, tel qu'expliqué dans la décomposition de la formule du cours[cite: 13].

    .. code-block:: python

        def update_q_value(current_q, reward, max_future_q, alpha, gamma):
            """
            Calcule et retourne la nouvelle valeur Q(s, a).
            """
            # 1. Calcul de la nouvelle estimation de valeur
            nouvelle_estimation = reward + (gamma * max_future_q)

            # 2. Application de la mise à jour pondérée par le taux d'apprentissage (alpha)
            new_q = current_q + alpha * (nouvelle_estimation - current_q)

            return new_q

        # Code de test
        nouveau_q = update_q_value(current_q=5, reward=2, max_future_q=10, alpha=0.5, gamma=0.8)
        print(nouveau_q) # Affiche: 7.5