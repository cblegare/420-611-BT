#########
 Langage
#########

Jusqu’à présent dans le cours, nous devions façonner les tâches et les données de
manière à ce qu’une IA puisse les traiter. Aujourd’hui, nous allons examiner
comment une IA peut être construite pour traiter le langage humain.

Le Traitement du Langage Naturel (Natural Language Processing ou NLP) englobe
toutes les tâches dans lesquelles l’IA reçoit du langage humain en entrée. Voici
quelques exemples de ces tâches :

Résumé automatique
    l’IA reçoit un texte en entrée et produit un résumé de ce texte en sortie.

Extraction d’informations
    l’IA reçoit un corpus de texte et en extrait des données structurées.

Identification de la langue
    l’IA reçoit un texte et retourne la langue dans laquelle il est écrit.

Traduction automatique
    l’IA reçoit un texte dans une langue source et produit sa traduction dans une langue cible.

Reconnaissance d’entités nommées
    l’IA reçoit un texte et extrait les noms des entités présentes (par exemple, des noms
    d’entreprises, de personnes ou de lieux).

Reconnaissance de la parole
    l’IA reçoit un signal vocal et produit les mots correspondants sous forme de texte.

Classification de texte
    l’IA reçoit un texte et doit le catégoriser selon une classe ou un type particulier.

Désambiguïsation du sens des mots (word sense disambiguation) : l’IA doit
choisir la bonne signification d’un mot possédant plusieurs sens (par
exemple, le mot « banque » qui désigne aussi bien une institution financière
que le bord d’un cours d’eau).

***********************
 Syntaxe et sémantique
***********************

La syntaxe désigne la structure des phrases. En tant que locuteurs natifs d’une
langue humaine, nous n’avons aucun mal à produire des phrases grammaticales et à
identifier les phrases incorrectes. Par exemple, la phrase « Just before nine
o’clock Sherlock Holmes stepped briskly into the room » est grammaticale, tandis
que la phrase « Just before Sherlock Holmes nine o’clock stepped briskly the
room » ne l’est pas. La syntaxe peut être à la fois grammaticale et ambiguë,
comme dans « I saw the man with the telescope ». Ai-je vu (l’homme avec le
télescope), ou ai-je vu (l’homme) en observant à travers le télescope ? Pour
être capable d’analyser et de produire du langage humain, l’IA doit maîtriser la
syntaxe.

La sémantique désigne le sens des mots ou des phrases. Bien que la phrase «
Just before nine o’clock Sherlock Holmes stepped briskly into the room » soit
syntaxiquement différente de « Sherlock Holmes stepped briskly into the room
just before nine o’clock », leur contenu est pratiquement identique. De même,
bien que la phrase « A few minutes before nine, Sherlock Holmes walked quickly
into the room » utilise des mots différents des phrases précédentes, elle porte un
sens très similaire. De plus, une phrase peut être parfaitement grammaticale tout
en étant totalement dénuée de sens, comme dans l’exemple célèbre de Chomsky : «
Colorless green ideas sleep furiously » (Des idées vertes sans couleur dorment
furieusement). Pour être capable d’analyser et de produire du langage humain,
l’IA doit également maîtriser la sémantique.

Grammaire hors-contexte
=======================

Une grammaire formelle est un système de règles permettant de générer des phrases
dans une langue. Dans une grammaire hors-contexte (Context-Free Grammar ou
CFG), le texte est abstrait de sa signification afin de représenter la structure
de la phrase à l’aide d'une grammaire formelle. Considérons la phrase suivante :

    « She saw the city. »

Il s’agit d’une phrase grammaticale simple, et nous aimerions générer un arbre
syntaxique représentant sa structure.

Nous commençons par attribuer à chaque mot sa catégorie grammaticale (partie du
discours). She et city sont des noms (Noun), que nous noterons N. Saw est
un verbe (Verb), que nous noterons V. The est un déterminant (Determiner),
qui indique si le nom suivant est défini ou indéfini, et que nous noterons D.
Désormais, la phrase ci-dessus peut être réécrite sous forme de symboles.

Jusqu'à présent, nous avons abstrait chaque mot de sa signification sémantique
pour le réduire à sa catégorie grammaticale. Cependant, les mots d'une phrase
sont liés entre eux, et pour comprendre la phrase, nous devons comprendre comment
ils se connectent. Un groupe nominal (Noun Phrase ou NP) est un groupe de mots
qui se rattachent à un nom. Par exemple, le mot She constitue un groupe nominal
dans cette phrase. De plus, les mots the city forment également un groupe
nominal, composé d’un déterminant et d’un nom. Un groupe verbal (Verb Phrase
ou VP) est un groupe de mots qui se rattachent à un verbe. Le mot saw est un
groupe verbal en soi, mais les mots saw the city forment aussi un groupe verbal
composé d’un verbe et d'un groupe nominal. Enfin, l’ensemble de la phrase
(Sentence ou S) peut être représenté sous la forme d’un arbre :

.. figure:: /assets/figures/syntactictree.png

Grâce à la grammaire formelle, l’IA est capable de représenter la structure des
phrases. La grammaire que nous venons de décrire contient suffisamment de règles
pour représenter cette phrase simple. Pour représenter des phrases plus
complexes, nous devrions ajouter des règles supplémentaires à notre grammaire
formelle.

nltk
====

Comme c’est souvent le cas en Python, plusieurs bibliothèques existent pour mettre
en œuvre cette idée. nltk (Natural Language Toolkit) en fait partie. Pour
analyser la phrase précédente, nous fournissons à l’algorithme des règles de
grammaire :

.. code-block:: python

    import nltk

    grammar = nltk.CFG.fromstring("""
        S -> NP VP

        NP -> D N | N
        VP -> V | V NP

        D -> "the" | "a"
        N -> "she" | "city" | "car"
        V -> "saw" | "walked"
    """)

    parser = nltk.ChartParser(grammar)


De manière analogue à ce que nous avons fait plus haut, nous définissons quels
composants peuvent être inclus dans d’autres. Une phrase (S) peut inclure un
groupe nominal (NP) et un groupe verbal (VP), tandis que les groupes eux-mêmes
peuvent être constitués d’autres groupes, de noms, de verbes, etc., jusqu'à ce
que chaque catégorie grammaticale couvre certains mots de la langue.

.. code-block:: python

    sentence = input("Sentence: ").split()
    try:
        for tree in parser.parse(sentence):
            tree.pretty_print()
            tree.draw()
    except ValueError:
        print("No parse tree possible.")


Après avoir fourni à l’algorithme une phrase découpée en une liste de mots, la
fonction affiche l’arbre syntaxique résultant dans la console (pretty_print)
et génère également une représentation graphique (draw).

.. figure:: /assets/figures/trees.png

n-grammes
=========

Un n-gramme est une séquence de n éléments tirés d’un échantillon de texte.
Dans un n-gramme de caractères, les éléments sont des caractères, et dans un
n-gramme de mots, les éléments sont des mots. Un unigramme, un bigramme et
un trigramme sont respectivement des séquences de un, deux et trois éléments.
Dans la phrase suivante, les trois premiers n-grammes (trigrammes) sont « how
often have », « often have I » et « have I said » :

« How often have I said to you that when you have eliminated the impossible
whatever remains, however improbable, must be the truth? »

Les n-grammes sont très utiles pour le traitement de texte. Même si l’IA n’a pas
nécessairement déjà vu la phrase entière, elle a très certainement vu des
portions de celle-ci, comme « have I said ». Puisque certains mots apparaissent
ensemble plus fréquemment que d’autres, il est possible de prédire le mot suivant
avec une certaine probabilité. Par exemple, votre téléphone intelligent vous
suggère des mots basés sur une distribution de probabilité dérivée des derniers
mots que vous avez tapés. Ainsi, une étape essentielle du traitement du langage
naturel consiste à découper la phrase en n-grammes.

Tokenisation
============

La tokenisation (ou segmentation) est la tâche consistant à découper une
séquence de caractères en morceaux appelés jetons (tokens). Les jetons
peuvent être aussi bien des mots que des phrases, auquel cas la tâche est
appelée tokenisation de mots (word tokenization) ou tokenisation de phrases
(sentence tokenization).

La tokenisation est nécessaire pour pouvoir analyser les n-grammes, car ceux-ci
reposent sur des séquences de jetons. On peut commencer par séparer le texte
selon les espaces. Bien que ce soit un bon début, cette méthode est imparfaite
car elle conserve la ponctuation collée aux mots (par exemple remains,). On
pourrait supprimer toute la ponctuation, mais d’autres défis apparaissent alors :
les mots avec apostrophes (ex. o'clock) ou avec tirets (ex. pearl-grey). De
plus, certains signes de ponctuation sont essentiels à la structure de la phrase,
comme le point final. Il faut toutefois pouvoir faire la différence entre le
point abréviatif de « Mr. » et le point marquant la fin d’une phrase. Gérer
toutes ces subtilités constitue le cœur du processus de tokenisation.

Modèles de Markov
=================

Comme vu dans les chapitres précédents, les modèles de Markov sont composés de
nœuds dont chaque valeur suit une distribution de probabilité basée sur un nombre
fini de nœuds précédents.

Les modèles de Markov peuvent être utilisés pour générer du texte. Pour ce faire,
nous entraînons le modèle sur un corpus de texte, puis nous établissons les
probabilités pour chaque n-ième jeton d'un n-gramme en fonction des n-1 mots qui
le précèdent. Par exemple, avec des trigrammes, après avoir reçu deux mots, le
modèle de Markov peut choisir un troisième mot selon la distribution de
probabilité conditionnée par les deux premiers. Il peut ensuite choisir un
quatrième mot basé sur les deuxième et troisième mots, et ainsi de suite.

À l’aide des modèles de Markov, nous sommes capables de générer du texte souvent
grammatical et superficiellement similaire au langage humain. Cependant, ces
phrases manquent de véritable sens et d’intention.

Modèle du sac de mots
=====================

Le sac de mots (Bag-of-Words) est un modèle qui représente un texte comme une
collection non ordonnée de mots. Ce modèle ignore la syntaxe et ne prend en
compte que la présence et la fréquence des mots.

Cette approche est particulièrement utile dans les tâches de classification,
telles que l’analyse de sentiments (une autre tâche de classification étant par
exemple la distinction entre courriels légitimes et pourriels). L’analyse de
sentiments peut être utilisée sur des avis de produits pour les catégoriser en
avis positifs ou négatifs. Considérons les phrases suivantes :

    « My grandson loved it! So much fun! »

    « Product broke after a few days. »

    « One of the best games I’ve played in a long time. »

    « Kind of cheap and flimsy, not worth it. »

En nous basant uniquement sur les mots présents et en ignorant la grammaire, nous
voyons que les phrases 1 et 3 sont positives (loved, fun, best) et que les
phrases 2 et 4 sont négatives (broke, cheap, flimsy).

Bayes naïf
==========

Le Bayes naïf (Naive Bayes) est une technique fréquemment utilisée pour
l’analyse de sentiments avec le modèle du sac de mots. Il s’agit de répondre à la
question : « Quelle est la probabilité que la phrase soit positive (ou négative)
sachant les mots qu'elle contient ? »

Pour répondre à cette question, nous faisons appel à la probabilité conditionnelle
et à la règle de Bayes :

.. figure:: /assets/figures/bayesrule.png

Nous cherchons à calculer :math:P(\text{sentiment} \mid \text{texte}), par
exemple :math:P(\text{positif} \mid \text{« my grandson loved it »}). Après
tokenisation, cela équivaut à calculer :math:P(\text{positif} \mid \text{« my »}, \text{« grandson »}, \text{« loved »}, \text{« it »}). En appliquant
directement la règle de Bayes :

.. math::

    P(\text{positif} \mid \text{mots}) = \frac{P(\text{mots} \mid \text{positif}) \cdot P(\text{positif})}{P(\text{mots})}


Pour comparer les classes (positif vs négatif), le dénominateur :math:P(\text{mots})
est identique et peut être omis, car nous cherchons une valeur proportionnelle
que nous pourrons normaliser à la fin pour que la somme des probabilités soit
égale à 1. Nous simplifions donc le calcul au numérateur :

.. math::

    P(\text{positif}, \text{mots}) = P(\text{positif}) \cdot P(\text{mots} \mid \text{positif})


Cependant, calculer la probabilité conjointe exacte de tous les mots ensemble est
extrêmement complexe car la probabilité de chaque mot dépend des mots qui le
précèdent. C’est ici qu’intervient la simplification « naïve » : nous supposons
que la probabilité d’apparition de chaque mot est indépendante de celle des autres
mots.

Bien que cette hypothèse soit fausse en pratique, le Bayes naïf donne d’excellents
résultats en analyse de sentiments. Grâce à cette hypothèse d’indépendance, la
formule devient :

.. math::

    P(\text{positif}) \cdot P(\text{« my »} \mid \text{positif}) \cdot P(\text{« grandson »} \mid \text{positif}) \cdot P(\text{« loved »} \mid \text{positif}) \cdot P(\text{« it »} \mid \text{positif})


Chaque terme est facile à calculer à partir des données d’entraînement :
:math:P(\text{positif}) est la proportion de phrases positives, et
:math:P(\text{« loved »} \mid \text{positif}) est le nombre de fois où le mot
loved apparaît dans les phrases positives divisé par le nombre total de mots dans
les phrases positives.

.. figure:: /assets/figures/naivebayes.png

La force du Bayes naïf réside dans sa sensibilité aux mots qui apparaissent beaucoup
plus fréquemment dans une classe que dans l’autre. Dans notre exemple, le mot
loved apparaît beaucoup plus souvent dans les phrases positives, ce qui fait
pencher la probabilité globale en faveur de la classe positive.

Un problème survient lorsqu’un mot du texte n'a jamais été observé dans les données
d’entraînement pour une classe donnée (par exemple si grandson n’apparaissait
dans aucune phrase positive). La probabilité conditionnelle associée serait de 0,
annulant la probabilité totale de la classe. Pour résoudre ce problème, on utilise
le lissage additif (Additive Smoothing), qui consiste à ajouter une valeur
:math:\alpha à tous les comptages. Un cas particulier est le lissage de
Laplace, où :math:\alpha = 1, simulant le fait que chaque mot a été observé au
moins une fois dans chaque classe.

Représentation des mots

Pour que l’IA manipule le sens des mots, il faut représenter les mots sous forme
numérique.

Une première approche est la représentation One-Hot (One-Hot Representation),
où chaque mot est représenté par un vecteur de taille égale au nombre total de«fpapi
mots du vocabulaire. Toutes les valeurs du vecteur sont à 0, sauf une seule qui
vaut 1 à l’indice correspondant au mot. Par exemple, pour un vocabulaire de 4
mots (he, wrote, a, book) :

.. code-block:: none

    [1, 0, 0, 0] (he)

    [0, 1, 0, 0] (wrote)

    [0, 0, 1, 0] (a)

    [0, 0, 0, 1] (book)

Bien que simple, cette représentation pose deux problèmes majeurs :

Pour un dictionnaire de 50 000 mots, chaque mot nécessite un vecteur de
dimension 50 000 très creux (sparse), ce qui est inefficace.

Elle est incapable de capturer la proximité sémantique entre deux mots
similaires (par exemple entre wrote et authored).

Pour y remédier, on utilise une représentation distribuée (Distributed
Representation ou Word Embeddings), où le sens d’un mot est réparti sur les
différentes dimensions d’un vecteur continu de taille réduite (par exemple 50 ou
300 dimensions) :

.. code-block:: none

    [-0.34, -0.08,  0.02, -0.18, ...] (he)

    [-0.27,  0.40,  0.00, -0.65, ...] (wrote)

    [-0.12, -0.25,  0.29, -0.09, ...] (a)

    [-0.23, -0.16, -0.05, -0.57, ...] (book)

Cette méthode permet non seulement d'utiliser des vecteurs plus compacts, mais
aussi de mesurer la similarité entre deux mots en calculant la distance géométrique
entre leurs vecteurs.

Comme l’a écrit le linguiste J. R. Firth : « You shall know a word by the company
it keeps » (Vous connaîtrez un mot par les compagnies qu’il fréquente). On
définit ainsi le sens d’un mot par son contexte d’apparition.

word2vec
========

word2vec est un algorithme permettant de générer des représentations
distribuées de mots. Il repose notamment sur l’architecture Skip-Gram, un
réseau de neurones entraîné à prédire les mots de contexte à partir d’un mot
cible.

.. figure:: /assets/figures/sgarchitecture.png

Dans cette architecture, la couche cachée intermédiaire (par exemple de 50 ou 100
unités) produit les valeurs qui constitueront le vecteur du mot. Une fois le
réseau entraîné par rétropropagation sur un vaste corpus de texte, chaque mot est
associé à un vecteur dense.

En calculant la similarité cosinus entre les vecteurs, l’IA peut identifier les
mots les plus proches sémantiquement de book : books, essay, memoir,
essays, novella, anthology, autobiography, etc.

De plus, ces représentations vectorielles permettent des opérations algébriques sur
le sens des mots :

.. math::

    \text{vecteur}(\text{king}) - \text{vecteur}(\text{man}) + \text{vecteur}(\text{woman}) \approx \text{vecteur}(\text{queen})


.. math::

    \text{vecteur}(\text{ramen}) - \text{vecteur}(\text{japan}) + \text{vecteur}(\text{america}) \approx \text{vecteur}(\text{burritos})


Réseaux de neurones
===================

Dans les tâches de traduction automatique ou de dialogue (chatbots), l'IA doit
traiter et générer des séquences de longueur variable.

Les réseaux de neurones récurrents (RNN) permettent de traiter des séquences en
réexécutant le réseau de manière séquentielle tout en conservant un état caché
(hidden state) qui résume l'information accumulée.

Dans une architecture séquence-à-séquence (seq2seq) :

Un encodeur traite chaque mot de la séquence d’entrée un par un et met à
jour l’état caché.

Un décodeur prend le dernier état caché et génère la séquence de sortie mot
par mot jusqu’à produire un jeton de fin.

Cependant, cette approche se heurte à des limites : lorsque la séquence d'entrée
est très longue, il devient difficile de compresser toute l'information dans un
seul état caché final. De plus, tous les mots d'entrée n'ont pas la même
importance pour prédire un mot de sortie spécifique.

Attention
=========

Le mécanisme d’attention permet au réseau de neurones de déterminer
dynamiquement quelles parties de la séquence d’entrée sont les plus importantes à
chaque étape de la génération de la sortie.

Par exemple, lors de la traduction de la phrase « What is the capital of
Massachusetts? », au moment de générer le mot final de la réponse, le mécanisme
d'attention attribuera un poids plus élevé aux états associés aux mots « capital »
et « Massachusetts ».

En multipliant les états cachés de l’encodeur par ces poids d’attention, le
réseau construit un vecteur de contexte spécifique à l’étape courante de
décodage.

Un inconvénient majeur des RNN (même avec attention) reste leur nature
séquentielle : les mots doivent être traités l'un après l'autre, ce qui empêche
la parallélisation des calculs et ralentit considérablement l'entraînement sur de
très grands corpus.

Transformers
============

L’architecture des Transformers résout ce problème de parallélisation. Au lieu
de traiter les mots séquentiellement, le Transformer reçoit tous les mots de la
séquence d’entrée simultanément.

Puisque tous les mots sont fournis en même temps, l’ordre naturel de la phrase
serait perdu. Pour y remédier, on ajoute un encodage positionnel (positional
encoding) aux représentations des mots d’entrée.

Le cœur du Transformer repose sur le mécanisme d’auto-attention (self-attention),
qui permet à chaque mot de la séquence de mettre en relation sa signification avec
tous les autres mots de la même phrase au même moment. Ce processus est répété à
travers plusieurs couches d’auto-attention pour capturer des relations
contextuelles complexes.

Grâce à cette structure, le traitement de texte devient extrêmement rapide sur les
cartes graphiques (GPU) grâce à une parallélisation massive, permettant le
développement des grands modèles de langage (Large Language Models ou LLM).

Conclusion
==========

Au cours de ce cheminement à travers l’intelligence artificielle, nous avons
exploré une grande variété de paradigmes :

Les problèmes de recherche et les algorithmes d’exploration pour trouver des
solutions optimales.

La représentation des connaissances et la logique pour effectuer des
déductions formelles.

La gestion de l’incertitude grâce aux modèles probabilistes et aux réseaux
bayésiens.

L’optimisation pour maximiser ou minimiser des fonctions d'évaluation.

L’apprentissage automatique pour découvrir des motifs à partir de données
d'entraînement.

Les réseaux de neurones et le deep learning pour modéliser des fonctions
complexes.

Et enfin, le traitement du langage naturel, qui permet aux machines de
comprendre, d'analyser et de générer la langue humaine.


***********
 Exercices
***********

.. ia2:exercice:: 70.1
    Grammaire hors-contexte (CFG) et arbre syntaxique

    Un système d'analyse automatique du langage doit traiter des commandes simples transmises à un assistant virtuel.
    Considérez la phrase suivante : « *The drone detects the target.* »

    a. Identifiez la catégorie grammaticale (partie du discours : N, V, D) de chaque mot de cette phrase.
    b. En utilisant les règles de grammaire hors-contexte (CFG) suivantes :

       * :math:`S \rightarrow NP \quad VP`
       * :math:`NP \rightarrow D \quad N \mid N`
       * :math:`VP \rightarrow V \quad NP \mid V`

       Rédigez la décomposition pas à pas montrant comment la phrase est structurée sous forme de groupes (NP, VP, S).

    Solution: :ia2:solution:`70.1`

.. ia2:exercice:: 70.2
    Tokenisation et extraction de n-grammes

    Un système d'analyse de presse scrute des dépêches d'actualité. On extrait l'extrait de texte suivant :
    « *The robot moves fast.* »

    a. Expliquez pourquoi le simple découpage par espace (*split*) est insuffisant pour un système de tokenisation robuste lors du traitement de textes réels comportant de la ponctuation ou des contractions.
    b. Listez tous les **unigrammes**, **bigrammes** et **trigrammes** de mots obtenus à partir de cette phrase de 4 mots.

    Solution: :ia2:solution:`70.2`

.. ia2:exercice:: 70.3
    Classificateur de Bayes naïf avec Lissage de Laplace

    Un modèle du sac de mots (*Bag-of-Words*) est entraîné pour classifier des avis sur des produits en deux catégories : **Positif** et **Négatif**.

    Voici les données d'entraînement :

    * **Avis Positifs (2 phrases) :**

      1. « *excellent produit fiable* »
      2. « *excellent service* »
    * **Avis Négatifs (2 phrases) :**

      1. « *produit défectueux* »
      2. « *service médiocre défectueux* »

    Le vocabulaire total du corpus contient :math:`|V| = 6` mots uniques : {*excellent*, *produit*, *fiable*, *service*, *défectueux*, *médiocre*}.
    On suppose que les probabilités a priori sont égales : :math:`P(\text{Positif}) = 0{,}5` et :math:`P(\text{Négatif}) = 0{,}5`.

    On évalue un nouvel avis : « *excellent produit* ».

    a. À quoi sert le **lissage de Laplace** (:math:`\alpha = 1`) lors du calcul des probabilités conditionnelles ?
    b. Calculez les probabilités conditionnelles avec lissage de Laplace : :math:`P(\text{« excellent »} \mid \text{Positif})`, :math:`P(\text{« produit »} \mid \text{Positif})`, :math:`P(\text{« excellent »} \mid \text{Négatif})` et :math:`P(\text{« produit »} \mid \text{Négatif})`.
    c. Calculez la probabilité a posteriori normalisée :math:`P(\text{Positif} \mid \text{« excellent produit »})` et concluez quant à la classe attribuée.

    Solution: :ia2:solution:`70.3`

.. ia2:exercice:: 70.4
    Représentation vectorielle des mots : One-Hot vs Embeddings et Algèbre vectorielle

    Pour traiter le sens des mots, les modèles de NLP convertissent le texte en représentations numériques.

    a. Présentez deux limites majeures de la représentation **One-Hot** par rapport aux représentations distribuées (**Word Embeddings** / *word2vec*).
    b. Dans un espace vectoriel dense à 3 dimensions, supposons les vecteurs *word2vec* suivants :

       * :math:`\text{vec}(\text{Paris}) = [0{,}8\,;\; 0{,}2\,;\; 0{,}9]`
       * :math:`\text{vec}(\text{France}) = [0{,}7\,;\; 0{,}1\,;\; 0{,}2]`
       * :math:`\text{vec}(\text{Japon}) = [0{,}1\,;\; 0{,}9\,;\; 0{,}3]`

       Calculez le vecteur cible résultant de l'opération d'analogie :
       :math:`\vec{v}_{\text{cible}} = \text{vec}(\text{Paris}) - \text{vec}(\text{France}) + \text{vec}(\text{Japon})`.
    c. Entre deux candidats possédant les vecteurs :math:`\text{vec}(\text{Tokyo}) = [0{,}2\,;\; 1{,}0\,;\; 1{,}0]` et :math:`\text{vec}(\text{Kyoto}) = [0{,}5\,;\; 0{,}4\,;\; 0{,}1]`, déterminez quel mot est le plus proche de :math:`\vec{v}_{\text{cible}}` en calculant la distance euclidienne.

    Solution: :ia2:solution:`70.4`

.. ia2:exercice:: 70.5
    Architectures de séquences : RNN, Attention et Transformers

    Le traitement de séquences de texte a évolué à travers plusieurs architectures clés.

    a. Quel est le goulot d'étranglement principal des réseaux de neurones récurrents (**RNN**) traditionnels lorsqu'ils traitent de très longues phrases ?
    b. Quel est le rôle du mécanisme d'**attention** dans une architecture de traduction de séquence à séquence ?
    c. Pourquoi les **Transformers** permettent-ils un entraînement nettement plus rapide que les RNN sur de grands corpus, et quel mécanisme permet aux Transformers de préserver l'ordre des mots sans traitement séquentiel ?

    Solution: :ia2:solution:`70.5`

.. ia2:exercice:: 70.6
    Code Python : Parsing de grammaire CFG avec NLTK

    La bibliothèque ``nltk`` permet de définir des grammaires hors-contexte et d'analyser des phrases.

    Complétez le script Python ci-dessous pour :
    1. Définir une grammaire CFG acceptant les phrases formées d'un groupe nominal (NP) et d'un groupe verbal (VP).
    2. Instancier le parseur ``ChartParser``.
    3. Parcourir et afficher les arbres syntaxiques générés pour la phrase « *she walked a car* ».

    .. code-block:: python

        import nltk

        # 1. Définition des règles de grammaire
        grammar = nltk.CFG.fromstring("""
            S -> NP VP
            NP -> D N | N
            VP -> V NP | V

            D -> "a" | "the"
            N -> "she" | "car" | "city"
            V -> "walked" | "saw"
        """)

        # 2. Instancier le parseur
        parser = # À COMPLÉTER

        sentence = "she walked a car".split()

        # 3. Analyser la phrase et afficher l'arbre
        # À COMPLÉTER

    Solution: :ia2:solution:`70.6`

.. ia2:exercice:: 70.7
    Code Python : Extraction de n-grammes de mots

    Écrivez une fonction Python ``generate_ngrams(tokens, n)`` qui prend en entrée une liste de mots (jetons) et un entier :math:`n`, puis retourne la liste de tous les :math:`n`-grammes (sous forme de tuples de longueur :math:`n`).

    .. code-block:: python

        def generate_ngrams(tokens, n):
            """
            Génère la liste des n-grammes à partir d'une liste de mots.
            """
            # À COMPLÉTER
            pass

        # Données de test
        texte = ["Sherlock", "Holmes", "stepped", "into", "the", "room"]

        # Test bigrammes (n=2)
        print(generate_ngrams(texte, 2))
        # Résultat attendu :
        # [('Sherlock', 'Holmes'), ('Holmes', 'stepped'), ('stepped', 'into'), ('into', 'the'), ('the', 'room')]

    Solution: :ia2:solution:`70.7`


***********
 Solutions
***********

.. ia2:solution:: 70.1
    Grammaire hors-contexte (CFG) et arbre syntaxique

    Solution de :ia2:ex:`70.1`

    a. **Catégories grammaticales :**

       * *The* : Déterminant (D)
       * *drone* : Nom (N)
       * *detects* : Verbe (V)
       * *the* : Déterminant (D)
       * *target* : Nom (N)

    b. **Décomposition et structure de l'arbre syntaxique :**

       * Groupe nominal sujet : :math:`NP_1 \rightarrow D + N \Rightarrow \text{« The drone »}`
       * Groupe nominal objet : :math:`NP_2 \rightarrow D + N \Rightarrow \text{« the target »}`
       * Groupe verbal : :math:`VP \rightarrow V + NP_2 \Rightarrow \text{« detects the target »}`
       * Phrase complète : :math:`S \rightarrow NP_1 + VP \Rightarrow \text{« The drone detects the target »}`

.. ia2:solution:: 70.2
    Tokenisation et extraction de n-grammes

    Solution de :ia2:ex:`70.2`

    a. **Limites du simple découpage par espace :**
       Un simple ``.split()`` conserve les signes de ponctuation collés aux mots (ex. « *room.* » devient distinct de « *room* »). De plus, il ne sait pas traiter correctement les apostrophes (ex. « *o'clock* »), les mots composés avec tirets (ex. « *pearl-grey* ») ou distinguer un point abréviatif (ex. « *Mr.* ») d'une fin de phrase.

    b. **n-grammes pour « The robot moves fast » :**

       * **Unigrammes (n=1) :** ``["The", "robot", "moves", "fast"]``
       * **Bigrammes (n=2) :** ``[("The", "robot"), ("robot", "moves"), ("moves", "fast")]``
       * **Trigrammes (n=3) :** ``[("The", "robot", "moves"), ("robot", "moves", "fast")]``

.. ia2:solution:: 70.3
    Classificateur de Bayes naïf avec Lissage de Laplace

    Solution de :ia2:ex:`70.3`

    a. **Rôle du lissage de Laplace :**
       Le lissage de Laplace (:math:`\alpha = 1`) évite qu'un mot jamais observé dans une classe lors de l'entraînement n'ait une probabilité conditionnelle nulle (:math:`P=0`). Sans ce lissage, un seul mot inédit annulerait complètement le produit global de probabilité de la classe concernée.

    b. **Calcul des probabilités conditionnelles (


******
 Quiz
******

.. ia2:exercice:: Question 1

    Considérez la grammaire hors-contexte ci-dessous, où :math:`S` est le symbole de départ :

    .. code-block:: text

        S -> NP V
        NP -> N | A NP
        A -> "small" | "white"
        N -> "cats" | "trees"
        V -> "climb" | "run"

    Considérez également les quatre phrases suivantes :

    1.  *Cats run.*
    2.  *Cats climb trees.*
    3.  *Small cats run.*
    4.  *Small white cats climb.*

    Parmi ces quatre phrases, lesquelles peuvent être dérivées de cette grammaire hors-contexte ?


.. ia2:exercice:: Question 2

    Laquelle des affirmations suivantes est **fausse** ?

    *   Les mécanismes d'attention peuvent être utilisés pour déterminer quelles parties d'une séquence d'entrée sont les plus importantes à privilégier.
    *   Les représentations *one-hot* des mots représentent mieux le sens des mots que les représentations distribuées (*embeddings*).
    *   Les *Transformers* peuvent être plus rapides à entraîner que les réseaux de neurones récurrents (RNN) car ils sont plus facilement parallélisables.
    *   Un classificateur Naïve Bayes suppose que l'ordre des mots n'a pas d'importance lors de la classification.


.. ia2:exercice:: Question 3

    Pourquoi le « lissage » (*smoothing*) est-il utile lors de l'application de Naïve Bayes ?

    *   Le lissage permet à Naïve Bayes de mieux gérer les cas où une preuve (*evidence*) n'est jamais apparue pour une catégorie particulière.
    *   Le lissage permet à Naïve Bayes de mieux gérer les cas où il y a de nombreuses catégories à classifier, au lieu de seulement deux.
    *   Le lissage permet à Naïve Bayes d'être moins « naïf » en ne supposant pas que les preuves sont conditionnellement indépendantes.
    *   Le lissage permet à Naïve Bayes de transformer une probabilité conditionnelle d'une preuve sachant une catégorie en une probabilité d'une catégorie sachant une preuve.

.. ia2:exercice:: Question 4

    À partir de la phrase « *must be the truth* », combien de 2-grammes de mots (*n-grammes* de longueur 2) peuvent être extraits ?


Solutions du quiz
=================

.. ia2:solution:: Question 1

    Les phrases **1**, **3** et **4**.

    *Explication :*

    *   **Phrase 1** (*Cats run*) : :math:`S \rightarrow NP \; V \rightarrow N \; V \rightarrow \text{"cats" "run"}`.
    *   **Phrase 2** (*Cats climb trees*) : La règle :math:`S \rightarrow NP \; V` n'autorise pas de groupe nominal complément (*trees*) après le verbe.
    *   **Phrase 3** (*Small cats run*) : :math:`S \rightarrow NP \; V \rightarrow A \; NP \; V \rightarrow A \; N \; V \rightarrow \text{"small" "cats" "run"}`.
    *   **Phrase 4** (*Small white cats climb*) : :math:`S \rightarrow NP \; V \rightarrow A \; NP \; V \rightarrow A \; A \; NP \; V \rightarrow A \; A \; N \; V \rightarrow \text{"small" "white" "cats" "climb"}`.


.. ia2:solution:: Question 2

    L'affirmation **« Les représentations one-hot des mots représentent mieux le sens des mots que les représentations distribuées des mots »** est fausse.

    *Explication :* Les représentations *one-hot* traitent tous les mots de manière orthogonale (la distance entre n'importe quelle paire de mots est identique), sans capter aucune relation sémantique. Les représentations distribuées (*word embeddings*) placent les mots dans un espace vectoriel continu où le sens et la proximité sémantique sont préservés.


.. ia2:solution:: Question 3

    **Le lissage permet à Naïve Bayes de mieux gérer les cas où une preuve n'est jamais apparue pour une catégorie particulière.**

    *Explication :* Sans lissage (par exemple le lissage de Laplace), si un mot n'est jamais présent dans une catégorie lors de l'entraînement, sa probabilité conditionnelle :math:`P(\text{mot} \mid \text{catégorie})` est égale à zéro. Multiplier les probabilités de la phrase par zéro annulerait complètement la probabilité globale de cette catégorie, même si tous les autres mots de la phrase correspondent à cette catégorie.


.. ia2:solution:: Question 4

    **3**

    *Explication :* Les trois 2-grammes (bigrammes) de mots issus de cette phrase de 4 mots sont :

    1.  « *must be* »
    2.  « *be the* »
    3.  « *the truth* »
