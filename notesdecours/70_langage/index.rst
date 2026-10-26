#########
 Langage
#########

Jusqu’à présent dans le cours, nous devions façonner les tâches et les données
de manière à ce qu’une IA puisse les traiter. Aujourd’hui, nous allons examiner
comment une IA peut être construite pour traiter le langage humain.

Le **Traitement du Langage Naturel** (*Natural Language Processing* ou NLP)
englobe toutes les tâches dans lesquelles l’IA reçoit du langage humain en
entrée. Voici quelques exemples de ces tâches :

* **Résumé automatique** (*automatic summarization*)
      entrée et produit un résumé de ce texte en sortie.
* **Extraction d’informations** (*information extraction*)
      corpus de texte et en extrait des données structurées.
* **Identification de la langue** (*language identification*)
      texte et retourne la langue dans laquelle il est écrit.
* **Traduction automatique** (*machine translation*)
      une langue source et produit sa traduction dans une langue cible.
* **Reconnaissance d’entités nommées** (*named entity recognition*)
      reçoit un texte et extrait les noms des entités présentes (par exemple,
      des noms d’entreprises, de personnes ou de lieux).
* **Reconnaissance de la parole** (*speech recognition*)
      vocal et produit les mots correspondants sous forme de texte.
* **Classification de texte** (*text classification*)
      doit le catégoriser selon une classe ou un type particulier.
* **Désambiguïsation du sens des mots** (*word sense disambiguation*)
      doit choisir la bonne signification d’un mot possédant plusieurs sens (par
      exemple, le mot « banque » qui désigne aussi bien une institution
      financière que le bord d’un cours d’eau).

***********************
 Syntaxe et sémantique
***********************

La **syntaxe** désigne la structure des phrases. En tant que locuteurs natifs
d’une langue humaine, nous n’avons aucun mal à produire des phrases
grammaticales et à identifier les phrases incorrectes. Par exemple, la phrase «
*Just before nine o’clock Sherlock Holmes stepped briskly into the room* » est
grammaticale, tandis que la phrase « *Just before Sherlock Holmes nine o’clock
stepped briskly the room* » ne l’est pas. La syntaxe peut être à la fois
grammaticale et ambiguë, comme dans « *I saw the man with the telescope* ».
Ai-je vu (l’homme avec le télescope), ou ai-je vu (l’homme) en observant à
travers le télescope ? Pour être capable d’analyser et de produire du langage
humain, l’IA doit maîtriser la syntaxe.

La **sémantique** désigne le sens des mots ou des phrases. Bien que la phrase «
*Just before nine o’clock Sherlock Holmes stepped briskly into the room* » soit
syntaxiquement différente de « *Sherlock Holmes stepped briskly into the room
just before nine o’clock* », leur contenu est pratiquement identique. De même,
bien que la phrase « *A few minutes before nine, Sherlock Holmes walked quickly
into the room* » utilise des mots différents des phrases précédentes, elle porte
un sens très similaire. De plus, une phrase peut être parfaitement grammaticale
tout en étant totalement dénuée de sens, comme dans l’exemple célèbre de Chomsky
: « *Colorless green ideas sleep furiously* » (Des idées vertes sans couleur
dorment furieusement). Pour être capable d’analyser et de produire du langage
humain, l’IA doit également maîtriser la sémantique.

*************************
 Grammaire hors-contexte
*************************

Une **grammaire formelle** est un système de règles permettant de générer des
phrases dans une langue. Dans une **grammaire hors-contexte** (*Context-Free
Grammar* ou CFG), le texte est abstrait de sa signification afin de représenter
la structure de la phrase à l’aide d'une grammaire formelle. Considérons la
phrase suivante :

« *She saw the city.* »

Il s’agit d’une phrase grammaticale simple, et nous aimerions générer un arbre
syntaxique représentant sa structure.

Nous commençons par attribuer à chaque mot sa catégorie grammaticale (partie du
discours). *She* et *city* sont des noms (*Noun*), que nous noterons N. *Saw*
est un verbe (*Verb*), que nous noterons V. *The* est un déterminant
(*Determiner*), qui indique si le nom suivant est défini ou indéfini, et que
nous noterons D. Désormais, la phrase ci-dessus peut être réécrite sous forme de
symboles.

Jusqu'à présent, nous avons abstrait chaque mot de sa signification sémantique
pour le réduire à sa catégorie grammaticale. Cependant, les mots d'une phrase
sont liés entre eux, et pour comprendre la phrase, nous devons comprendre
comment ils se connectent. Un **groupe nominal** (*Noun Phrase* ou NP) est un
groupe de mots qui se rattachent à un nom. Par exemple, le mot *She* constitue
un groupe nominal dans cette phrase. De plus, les mots *the city* forment
également un groupe nominal, composé d’un déterminant et d’un nom. Un **groupe
verbal** (*Verb Phrase* ou VP) est un groupe de mots qui se rattachent à un
verbe. Le mot *saw* est un groupe verbal en soi, mais les mots *saw the city*
forment aussi un groupe verbal composé d’un verbe et d'un groupe nominal. Enfin,
l’ensemble de la phrase (*Sentence* ou S) peut être représenté sous la forme
d’un arbre :

.. figure:: /assets/figures/syntactictree.png

Grâce à la grammaire formelle, l’IA est capable de représenter la structure des
phrases. La grammaire que nous venons de décrire contient suffisamment de règles
pour représenter cette phrase simple. Pour représenter des phrases plus
complexes, nous devrions ajouter des règles supplémentaires à notre grammaire
formelle.

******
 nltk
******

Comme c’est souvent le cas en Python, plusieurs bibliothèques existent pour
mettre en œuvre cette idée. **nltk** (*Natural Language Toolkit*) en fait
partie. Pour analyser la phrase précédente, nous fournissons à l’algorithme des
règles de grammaire :

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
fonction affiche l’arbre syntaxique résultant dans la console (``pretty_print``)
et génère également une représentation graphique (``draw``).

.. figure:: /assets/figures/trees.png

*******************
 :math:`n`-grammes
*******************

Un **:math:`n`-gramme** est une séquence de :math:`n` éléments tirés d’un
échantillon de texte. Dans un **:math:`n`-gramme de caractères**, les éléments
sont des caractères, et dans un **:math:`n`-gramme de mots**, les éléments sont
des mots. Un *unigramme*, un *bigramme* et un *trigramme* sont respectivement
des séquences de un, deux et trois éléments. Dans la phrase suivante, les trois
premiers :math:`n`-grammes (trigrammes) sont « *how often have* », « *often have
I* » et « *have I said* » :

« *How often have I said to you that when you have eliminated the impossible
whatever remains, however improbable, must be the truth?* »

Les :math:`n`-grammes sont très utiles pour le traitement de texte. Même si l’IA
n’a pas nécessairement déjà vu la phrase entière, elle a très certainement vu
des portions de celle-ci, comme « *have I said* ». Puisque certains mots
apparaissent ensemble plus fréquemment que d’autres, il est possible de prédire
le mot suivant avec une certaine probabilité. Par exemple, votre téléphone
intelligent vous suggère des mots basés sur une distribution de probabilité
dérivée des derniers mots que vous avez tapés. Ainsi, une étape essentielle du
traitement du langage naturel consiste à découper la phrase en
:math:`n`-grammes.

**************
 Tokenisation
**************

La **tokenisation** (ou segmentation) est la tâche consistant à découper une
séquence de caractères en morceaux appelés **jetons** (*tokens*). Les jetons
peuvent être aussi bien des mots que des phrases, auquel cas la tâche est
appelée **tokenisation de mots** (*word tokenization*) ou **tokenisation de
phrases** (*sentence tokenization*).

La tokenisation est nécessaire pour pouvoir analyser les :math:`n`-grammes, car
ceux-ci reposent sur des séquences de jetons. On peut commencer par séparer le
texte selon les espaces. Bien que ce soit un bon début, cette méthode est
imparfaite car elle conserve la ponctuation collée aux mots (par exemple
``remains,``). On pourrait supprimer toute la ponctuation, mais d’autres défis
apparaissent alors : les mots avec apostrophes (ex. ``o'clock``) ou avec tirets
(ex. ``pearl-grey``). De plus, certains signes de ponctuation sont essentiels à
la structure de la phrase, comme le point final. Il faut toutefois pouvoir faire
la différence entre le point abréviatif de « *Mr.* » et le point marquant la fin
d’une phrase. Gérer toutes ces subtilités constitue le cœur du processus de
tokenisation.

*******************
 Modèles de Markov
*******************

Comme vu dans les chapitres précédents, les modèles de Markov sont composés de
nœuds dont chaque valeur suit une distribution de probabilité basée sur un
nombre fini de nœuds précédents.

Les modèles de Markov peuvent être utilisés pour générer du texte. Pour ce
faire, nous entraînons le modèle sur un corpus de texte, puis nous établissons
les probabilités pour chaque :math:`n`-ième jeton d'un :math:`n`-gramme en
fonction des :math:`n - 1` mots qui le précèdent. Par exemple, avec des
trigrammes, après avoir reçu deux mots, le modèle de Markov peut choisir un
troisième mot selon la distribution de probabilité conditionnée par les deux
premiers. Il peut ensuite choisir un quatrième mot basé sur les deuxième et
troisième mots, et ainsi de suite.

À l’aide des modèles de Markov, nous sommes capables de générer du texte souvent
grammatical et superficiellement similaire au langage humain. Cependant, ces
phrases manquent de véritable sens et d’intention.

***********************
 Modèle du sac de mots
***********************

Le **sac de mots** (*Bag-of-Words*) est un modèle qui représente un texte comme
une collection non ordonnée de mots. Ce modèle ignore la syntaxe et ne prend en
compte que la présence et la fréquence des mots.

Cette approche est particulièrement utile dans les tâches de classification,
telles que l’\ **analyse de sentiments** (une autre tâche de classification
étant par exemple la distinction entre courriels légitimes et pourriels).
L’analyse de sentiments peut être utilisée sur des avis de produits
