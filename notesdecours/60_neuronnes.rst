#####################
 Réseaux de neurones
#####################

Les réseaux de neurones artificiels s’inspirent des neurosciences. Dans le
cerveau, les neurones sont des cellules connectées entre elles qui forment des
réseaux. Chaque neurone est capable de recevoir et d’envoyer des signaux
électriques. Dès que le signal électrique reçu par un neurone dépasse un certain
seuil, il s’active et transmet son signal électrique à son tour.

Un **réseau de neurones artificiel** est un modèle mathématique d’apprentissage
inspiré des réseaux de neurones biologiques. Les réseaux de neurones artificiels
modélisent des fonctions mathématiques qui associent des entrées à des sorties
en fonction de la structure et des paramètres du réseau. Dans les réseaux de
neurones artificiels, la structure du réseau se façonne grâce à l’entraînement
sur des données.

En intelligence artificielle, l’équivalent de chaque neurone est une **unité**
connectée à d’autres unités. Par exemple, tout comme dans le cours précédent,
l’IA peut associer deux entrées, :math:`x_1` et :math:`x_2`, pour déterminer
s’il va pleuvoir aujourd’hui ou non. Au cours précédent, nous avons suggéré la
forme suivante pour cette fonction d’hypothèse : :math:`h(x_1, x_2) = w_0 +
w_1x_1 + w_2x_2`, où :math:`w_1` et :math:`w_2` sont des poids qui modifient les
entrées, et :math:`w_0` est une constante, également appelée **biais**, qui
modifie la valeur de l’expression entière.

************************
 Fonctions d’activation
************************

Pour utiliser la fonction d’hypothèse afin de décider s’il pleut ou non, nous
devons créer une sorte de seuil basé sur la valeur qu’elle produit.

Une façon d’y parvenir est d’utiliser une fonction échelon, qui renvoie 0 avant
qu’un certain seuil ne soit atteint et 1 après.

.. figure:: /assets/figures/step.png

Une autre approche consiste à utiliser une fonction logique (sigmoïde), qui
produit en sortie un nombre réel quelconque de 0 à 1, ce qui permet d’exprimer
une confiance nuancée dans son jugement.

.. figure:: /assets/figures/logistic.png

Une autre fonction possible est l’unité linéaire rectifiée (ReLU), qui permet à
la sortie d’être n’importe quelle valeur positive. Si la valeur est négative, la
fonction ReLU la définit à 0.

.. figure:: /assets/figures/relu.png

Quelle que soit la fonction choisie, nous avons appris au cours précédent que
les entrées sont modifiées par des poids en plus du biais, et que leur somme est
transmise à une fonction d’activation. Cela reste vrai pour les réseaux de
neurones simples.

***********************************
 Structure d’un réseau de neurones
***********************************

Un réseau de neurones peut être perçu comme la représentation de l’idée
ci-dessus, où une fonction additionne les entrées pour produire une sortie.

.. figure:: /assets/figures/nnstructure.png

Les deux unités blanches à gauche représentent l’entrée et l’unité à droite
représente la sortie. Les entrées sont connectées à la sortie par une arête
pondérée. Pour prendre une décision, l’unité de sortie multiplie les entrées par
leurs poids en plus du biais (:math:`w_0`), puis utilise la fonction :math:`g`
pour déterminer la sortie.

Par exemple, un connecteur logique OU (Or) peut être représenté comme une
fonction :math:`f` ayant la table de vérité suivante :

========= ========= ===============
:math:`x` :math:`y` :math:`f(x, y)`
========= ========= ===============
0         0         0
0         1         1
1         0         1
1         1         1
========= ========= ===============

Nous pouvons visualiser cette fonction sous la forme d’un réseau de neurones.
:math:`x_1` est une unité d’entrée et :math:`x_2` en est une autre. Elles sont
connectées à l’unité de sortie par une arête de poids 1. L’unité de sortie
utilise ensuite la fonction :math:`g(-1 + 1x_1 + 1x_2)` avec un seuil de 0 pour
renvoyer soit 0, soit 1 (faux ou vrai).

.. figure:: /assets/figures/nnor.png

Par exemple, dans le cas où :math:`x_1 = x_2 = 0`, la somme est de :math:`(-1)`.
C’est en dessous du seuil, donc la fonction :math:`g` renverra 0. Cependant, si
l’une ou les deux entrées :math:`x_1` et :math:`x_2` sont égales à 1, la somme
de toutes les entrées sera soit 0, soit 1. Les deux atteignent ou dépassent le
seuil, de sorte que la fonction renverra 1.

Un processus similaire peut être répété avec la fonction ET (où le biais sera de
:math:`(-2)`). De plus, les entrées et les sorties ne doivent pas nécessairement
être distinctes. Un processus similaire peut être utilisé pour prendre
l’humidité et la pression atmosphérique comme entrées, et produire la
probabilité de pluie comme sortie. Ou, dans un autre exemple, les entrées
peuvent être l’argent dépensé en publicité et le mois de la dépense pour obtenir
le revenu attendu des ventes. Cela peut être étendu à un nombre quelconque
d’entrées en multipliant chaque entrée :math:`x_1 \dots x_n` par un poids
:math:`w_1 \dots w_n`, en additionnant les valeurs obtenues et en ajoutant un
biais :math:`w_0`.

**********************
 Descente de gradient
**********************

La descente de gradient est un algorithme permettant de minimiser la perte lors
de l’entraînement des réseaux de neurones. Comme mentionné précédemment, un
réseau de neurones est capable de déduire des connaissances sur sa propre
structure à partir des données. Alors que nous avons défini manuellement les
différents poids jusqu’à présent, les réseaux de neurones nous permettent de
calculer ces poids à partir des données d’entraînement. Pour ce faire, nous
utilisons l’algorithme de descente de gradient, qui fonctionne de la manière
suivante :

* Commencer par un choix aléatoire de poids. C’est notre point de départ naïf,
      où nous ignorons quel poids accorder à chaque entrée.
* Répéter :

      * Calculer le gradient basé sur tous les points de données qui permettront de
            diminuer la perte. En fin de compte, le gradient est un vecteur (une
            séquence de nombres).
      * Mettre à jour les poids en fonction du gradient.

Le problème de ce type d’algorithme est qu’il nécessite de calculer le gradient
sur la base de *tous les points de données*, ce qui s’avère très coûteux en
calculs. Il existe plusieurs façons de minimiser ce coût. Par exemple, dans la
**descente de gradient stochastique**, le gradient est calculé à partir d’un
seul point choisi au hasard. Ce type de gradient peut s’avérer assez imprécis,
ce qui mène à l’algorithme de **descente de gradient par mini-lots**, qui
calcule le gradient à partir de quelques points sélectionnés au hasard, trouvant
ainsi un compromis entre le coût de calcul et la précision. Comme c’est souvent
le cas, aucune de ces solutions n’est parfaite et différentes solutions peuvent
être employées selon les situations.

En utilisant la descente de gradient, il est possible de résoudre de nombreux
problèmes. Par exemple, nous pourrions vouloir en savoir plus que « va-t-il
pleuvoir aujourd’hui ? ». Nous pouvons utiliser certaines entrées pour générer
des probabilités pour différents types de conditions météorologiques, puis
simplement choisir le temps le plus probable.

.. figure:: /assets/figures/weather.png

Cette démarche peut être appliquée à un nombre quelconque d’entrées et de
sorties, où chaque entrée est connectée à chaque sortie, et où les sorties
représentent des décisions que nous pouvons prendre. Notez que dans ce type de
réseaux de neurones, les sorties ne sont pas connectées entre elles. Cela
signifie que chaque sortie et ses poids associés provenant de toutes les entrées
peuvent être considérés comme un réseau de neurones individuel et donc être
entraînés séparément du reste des sorties.

Jusqu’à présent, nos réseaux de neurones reposaient sur des unités de sortie de
type **perceptron**. Ce sont des unités capables d’apprendre uniquement une
frontière de décision linéaire, utilisant une ligne droite pour séparer les
données. Autrement dit, à partir d’une équation linéaire, le perceptron peut
classer une entrée dans un type ou un autre (par exemple, l’image de gauche).
Cependant, les données ne sont souvent pas linéairement séparables (par exemple,
l’image de droite). Dans ce cas, nous nous tournons vers les réseaux de neurones
multicouches pour modéliser des données de manière non linéaire.

.. figure:: /assets/figures/linearnonlinear.png

**********************************
 Réseaux de neurones multicouches
**********************************

Un réseau de neurones multicouche est un réseau de neurones artificiel doté
d’une couche d’entrée, d’une couche de sortie et d’au moins une couche
**cachée**. Bien que nous fournissions les entrées et les sorties pour entraîner
le modèle, nous, les humains, ne fournissons aucune valeur aux unités situées à
l’intérieur des couches cachées. Chaque unité de la première couche cachée
reçoit une valeur pondérée de chacune des unités de la couche d’entrée, effectue
une opération sur celle-ci et produit une valeur en sortie. Chacune de ces
valeurs est pondérée puis propagée à la couche suivante, répétant le processus
jusqu’à ce que la couche de sortie soit atteinte. Grâce aux couches cachées, il
est possible de modéliser des données non linéaires.

.. figure:: /assets/figures/multilayer.png

******************
 Rétropropagation
******************

La rétropropagation est l’algorithme principal utilisé pour entraîner les
réseaux de neurones dotés de couches cachées. Elle procède en partant des
erreurs commises par les unités de sortie, en calculant la descente de gradient
pour les poids de la couche précédente, et en répétant le processus jusqu’à ce
que la couche d’entrée soit atteinte. En pseudo-code, nous pouvons décrire
l’algorithme comme suit :

* Calculer l’erreur pour la couche de sortie.
* Pour chaque couche, en commençant par la couche de sortie et en progressant
  vers l’intérieur en direction de la première couche cachée :

  * Propager l’erreur d’une couche en arrière. En d’autres termes, la couche
    actuelle envoie ses erreurs à la couche précédente.
  * Mettre à jour les poids.

Cela peut être étendu à un nombre quelconque de couches cachées, créant ainsi
des **réseaux de neurones profonds**, qui sont des réseaux de neurones possédant
plus d’une couche cachée.

.. figure:: /assets/figures/deepnn.png

******************
 Surapprentissage
******************

Le surapprentissage est le risque de modéliser les données d’entraînement avec
trop de précision, ce qui empêche la généralisation à de nouvelles données. Une
façon de lutter contre le surapprentissage est l’utilisation du **dépot
(dropout)**. Cette technique consiste à supprimer temporairement des unités
sélectionnées au hasard pendant la phase d’apprentissage. De cette façon, nous
cherchons à éviter une dépendance excessive envers une unité particulière du
réseau. Tout au long de l’entraînement, le réseau de neurones prendra
différentes formes, désactivant à chaque fois certaines unités avant de les
réutiliser :

.. figure:: /assets/figures/dropout.png

Notez qu’une fois l’entraînement terminé, l’intégralité du réseau de neurones
est à nouveau utilisée.

************
 TensorFlow
************

Comme c’est souvent le cas en Python, de nombreuses bibliothèques intègrent déjà
une implémentation des réseaux de neurones utilisant l’algorithme de
rétropropagation, et TensorFlow en fait partie. Vous êtes invités à expérimenter
avec les réseaux de neurones TensorFlow dans cette `application Web
<https://playground.tensorflow.org/>`__, qui vous permet de définir différentes
propriétés du réseau et de l’exécuter tout en visualisant le résultat. Nous
allons maintenant aborder un exemple d’utilisation de TensorFlow pour accomplir
la tâche discutée lors du cours précédent : distinguer les faux billets des
vrais billets.

..
    code: python

    import csv
    import tensorflow as tf
    from sklearn.model_selection import train_test_split

Nous importons TensorFlow et le nommons ``tf`` (afin de raccourcir le code).

.. code-block:: python

    # Lecture des donnees a partir du fichier
    with open("banknotes.csv") as f:
        reader = csv.reader(f)
        next(reader)

        data = []
        for row in reader:
            data.append(
                {
                    "evidence": [float(cell) for cell in row[:4]],
                    "label": 1 if row[4] == "0" else 0,
                }
            )

    # Separation des donnees en groupes d'entrainement et de test
    evidence = [row["evidence"] for row in data]
    labels = [row["label"] for row in data]
    X_training, X_testing, y_training, y_testing = train_test_split(
        evidence, labels, test_size=0.4
    )

Nous fournissons les données CSV au modèle. Notre travail consiste souvent à
formater les données pour qu’elles correspondent aux exigences de la
bibliothèque. La partie difficile du codage du modèle est déjà implémentée pour
nous.

.. code-block:: python

    # Creation d'un reseau de neurones
    model = tf.keras.models.Sequential()

Keras est une interface de programmation (API) utilisée par différents
algorithmes d’apprentissage automatique. Un modèle séquentiel est un modèle dont
les couches se succèdent les unes après les autres (comme ceux que nous avons
vus jusqu’à présent).

.. code-block:: python

    # Ajout d'une couche cachee de 8 unites avec activation ReLU
    model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

Une couche dense (fully connected) est une couche où chaque nœud de la couche
actuelle est connecté à tous les nœuds de la couche précédente. Ici, nous créons
une couche dense de 8 unités, chacune possédant 4 neurones d’entrée, en
utilisant la fonction d’activation ReLU mentionnée ci-dessus.

.. code-block:: python

    # Ajout de la couche de sortie avec 1 unite et activation sigmoide
    model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

Dans notre couche de sortie, nous voulons créer une couche dense qui utilise une
fonction d’activation sigmoïde, c’est-à-dire une fonction d’activation dont la
sortie est une valeur comprise entre 0 et 1.

.. code-block:: python

    # Entrainement du reseau de neurones
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X_training, y_training, epochs=20)

    # Evaluation de la performance du modele
    model.evaluate(X_testing, y_testing, verbose=2)

Enfin, nous compilons le modèle en précisant l’algorithme d’optimisation, le
type de fonction de perte utilisé et la manière dont nous souhaitons mesurer sa
réussite (dans notre cas, nous nous intéressons à la précision de la sortie).
Enfin, nous ajustons le modèle sur les données d’entraînement avec 20
répétitions (époques), puis nous l’évaluons sur les données de test.

***********************
 Vision par ordinateur
***********************

La vision par ordinateur englobe les différentes méthodes computationnelles
permettant d’analyser et de comprendre des images numériques, et elle est
souvent mise en œuvre à l’aide de réseaux de neurones. Par exemple, la vision
par ordinateur est à l’œuvre lorsque les réseaux sociaux emploient la
reconnaissance faciale pour identifier automatiquement des personnes sur des
photos. D’autres exemples incluent la reconnaissance de l’écriture manuscrite et
les voitures autonomes.

Les images se composent de pixels, et les pixels sont représentés par trois
valeurs allant de 0 à 255 : une pour le rouge, une pour le vert et une pour le
bleu. Ces valeurs sont souvent désignées par l’acronyme RVB (ou RGB). Nous
pouvons exploiter cela pour créer un réseau de neurones où chaque valeur de
couleur de chaque pixel constitue une entrée, où nous disposons de quelques
couches cachées, et où la sortie correspond à un certain nombre d’unités nous
indiquant ce qui est représenté sur l’image. Cependant, cette approche présente
quelques inconvénients. Tout d’abord, en décomposant l’image en pixels et en
valeurs de couleur, nous ne pouvons pas utiliser la structure globale de l’image
comme aide. Autrement dit, en tant qu’humains, si nous voyons une partie d’un
visage, nous savons à quoi nous attendre pour le reste, ce qui accélère le
calcul. Nous voulons pouvoir bénéficier d’un avantage similaire dans nos réseaux
de neurones. Deuxièmement, le nombre total d’entrées est très élevé, ce qui
signifie que nous devrons calculer un volume considérable de poids.

**********************
 Convolution d’images
**********************

La convolution d’images consiste à appliquer un filtre qui ajoute la valeur de
chaque pixel d’une image à ses voisins, pondérés selon une matrice appelée noyau
(kernel). Cette opération modifie l’image et peut aider le réseau de neurones à
la traiter.

Considérons l’exemple suivant :

.. figure:: /assets/figures/convolution.png

Le noyau est la matrice bleue et l’image est la grande matrice située à gauche.
L’image filtrée obtenue est la petite matrice en bas à droite. Pour filtrer
l’image à l’aide du noyau, nous commençons par le pixel de valeur 20 situé dans
le coin supérieur gauche de l’image (coordonnées 1,1). Ensuite, nous multiplions
toutes les valeurs qui l’entourent par la valeur correspondante dans le noyau et
nous les additionnons (:math:`10\times0 + 20\times(-1) + 30\times0 +
10\times(-1) + 20\times5 + 30\times(-1) + 20\times0 + 30\times(-1) +
40\times0`), ce qui donne la valeur 10. Nous faisons ensuite de même pour le
pixel situé à droite (30), le pixel situé sous le premier (30), et le pixel
situé à droite de celui-ci (40). Cela génère une image filtrée avec les valeurs
visibles en bas à droite.

Différents noyaux permettent d’accomplir différentes tâches. Pour la détection
de contours, le noyau suivant est fréquemment utilisé :

.. figure:: /assets/figures/kernel.png

L’idée ici est que lorsqu’un pixel est similaire à tous ses voisins, ils
s’annulent mutuellement, donnant une valeur de 0. Par conséquent, plus les
pixels se ressemblent, plus la zone de l’image est sombre, et plus ils
diffèrent, plus elle est claire. L’application de ce noyau à une image (à
gauche) produit une image aux contours prononcés (à droite) :

.. figure:: /assets/figures/edgedetection.png

Considérons une implémentation de la convolution d’images. Nous utilisons la
bibliothèque PIL (qui signifie *Python Imaging Library*), capable d’effectuer la
majeure partie du travail difficile à notre place.

.. code-block:: python

    import math
    import sys

    from PIL import Image, ImageFilter

    # S'assurer d'une utilisation correcte
    if len(sys.argv) != 2:
        sys.exit("Utilisation : python filter.py nom_de_fichier")

    # Ouvrir l'image
    image = Image.open(sys.argv[1]).convert("RGB")

    # Filtrer l'image selon le noyau de detection de contours
    filtered = image.filter(
        ImageFilter.Kernel(size=(3, 3), kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=1)
    )

    # Afficher l'image resultante
    filtered.show()

Cependant, le traitement de l’image dans un réseau de neurones reste coûteux en
calculs en raison du nombre de pixels servant d’entrées. Une autre approche
consiste à utiliser le **sous-échantillonnage par max (pooling)**, où la taille
de l’entrée est réduite en échantillonnant des régions de l’entrée. Les pixels
adjacents appartiennent à la même zone de l’image, ce qui signifie qu’ils sont
probablement similaires. Par conséquent, nous pouvons utiliser un seul pixel
pour représenter toute une zone. Une façon d’y parvenir est le **max-pooling**,
où le pixel sélectionné est celui qui possède la valeur la plus élevée parmi
tous les autres de la même région. Par exemple, si nous divisons le carré de
gauche (ci-dessous) en quatre carrés de :math:`2\times2`, l’application du
max-pooling à cette entrée nous donne le petit carré de droite.

.. figure:: /assets/figures/maxpooling.png

*******************************************
 Réseaux de neurones convolutionnels (CNN)
*******************************************

Un réseau de neurones convolutionnel est un réseau de neurones qui utilise la
convolution, généralement pour analyser des images. Il commence par appliquer
des filtres capables d’extraire certaines caractéristiques de l’image à l’aide
de différents noyaux. Ces filtres peuvent être améliorés de la même manière que
les autres poids du réseau de neurones, en ajustant leurs noyaux en fonction de
l’erreur de sortie. Ensuite, les images obtenues sont sous-échantillonnées
(pooling), après quoi les pixels sont fournis en tant qu’entrées à un réseau de
neurones traditionnel (processus appelé **aplatissement** ou *flattening*).

.. figure:: /assets/figures/convolutionalnn.png

Les étapes de convolution et de sous-échantillonnage peuvent être répétées
plusieurs fois pour extraire des caractéristiques supplémentaires et réduire la
taille de l’entrée du réseau de neurones. L’un des avantages de ces processus
est que, grâce à la convolution et au sous-échantillonnage, le réseau de
neurones devient moins sensible aux variations. Autrement dit, si la même photo
est prise sous des angles légèrement différents, l’entrée pour le réseau de
neurones convolutionnel restera similaire, alors que sans convolution ni
sous-échantillonnage, l’entrée de chaque image serait radicalement différente.

En code, un réseau de neurones convolutionnel ne diffère pas beaucoup d’un
réseau de neurones traditionnel. TensorFlow propose des jeux de données pour
tester nos modèles. Nous utiliserons MNIST, qui contient des images de chiffres
manuscrits en noir et blanc. Nous entraînerons notre réseau de neurones
convolutionnel à reconnaître ces chiffres.

.. code-block:: python

    import sys
    import tensorflow as tf

    # Utiliser le jeu de donnees d'ecriture manuscrite MNIST
    mnist = tf.keras.datasets.mnist

    # Preparer les donnees pour l'entrainement
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    y_train = tf.keras.utils.to_categorical(y_train)
    y_test = tf.keras.utils.to_categorical(y_test)
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

    # Creer un reseau de neurones convolutionnel
    model = tf.keras.models.Sequential(
        [
            * Couche de convolution. Apprendre 32 filtres en utilisant un noyau 3x3
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
            * Couche de max-pooling, utilisant une taille de regroupement 2x2
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            * Aplatir les unites
            tf.keras.layers.Flatten(),
            * Ajouter une couche cachee avec depot (dropout)
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            * Ajouter une couche de sortie avec des unites pour les 10 chiffres
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )

    # Entrainer le reseau de neurones
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=10)

    # Evaluer la performance du reseau de neurones
    model.evaluate(x_test, y_test, verbose=2)

Comme l’entraînement du modèle prend du temps, nous pouvons sauvegarder le
modèle déjà entraîné pour l’utiliser ultérieurement.

.. code-block:: python

    # Sauvegarder le modele dans un fichier
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        model.save(filename)
        print(f"Modele sauvegarde dans {filename}.")

Désormais, si nous exécutons un programme qui reçoit des chiffres dessinés à la
main comme entrée, il sera capable de classifier et de restituer le chiffre à
l’aide du modèle. Pour une implémentation d’un tel programme, consultez le
fichier ``recognition.py`` dans le code source de ce cours.

********************************
 Réseaux de neurones récurrents
********************************

Les **réseaux de neurones à propagation avant (feed-forward)** sont le type de
réseaux de neurones que nous avons abordés jusqu’à présent, dans lesquels les
données d’entrée sont fournies au réseau, qui produit finalement une sortie. Un
schéma du fonctionnement des réseaux de neurones à propagation avant est
présenté ci-dessous.

.. figure:: /assets/figures/ffnndiagram.png

À l’opposé, les **réseaux de neurones récurrents** possèdent une structure non
linéaire où le réseau utilise sa propre sortie comme entrée. Par exemple,
l’outil `captionbot <https://www.captionbot.ai>`__ de Microsoft est capable de
décrire le contenu d’une image à l’aide des mots d’une phrase. Cela diffère de
la classification dans la mesure où la sortie peut être de longueur variable
selon les propriétés de l’image. Alors que les réseaux de neurones à propagation
avant sont incapables de faire varier le nombre de sorties, les réseaux de
neurones récurrents le peuvent grâce à leur structure. Dans le cadre de la
génération de légendes, un réseau traite l’entrée pour produire une sortie, puis
poursuit le traitement à partir de ce point pour produire une autre sortie, et
répète l’opération autant de fois que nécessaire.

.. figure:: /assets/figures/recurrent.png

Les réseaux de neurones récurrents s’avèrent utiles lorsque le réseau traite des
séquences et non un simple objet individuel. Dans l’exemple précédent, le réseau
de neurones devait produire une séquence de mots. Toutefois, le même principe
peut s’appliquer à l’analyse de fichiers vidéo, qui consistent en une séquence
d’images, ou à des tâches de traduction, où une séquence d’entrées (des mots
dans la langue source) est traitée pour générer une séquence de sorties (des
mots dans la langue cible).
