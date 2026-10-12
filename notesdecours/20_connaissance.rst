###############
 Connaissances
###############

Les humains raisonnent sur la base de connaissances existantes et en tirent des
conclusions. Le concept consistant à représenter les connaissances et à en tirer
des conclusions est également utilisé en IA, et dans cette leçon, nous
explorerons comment nous pouvons reproduire ce comportement.

Agents basés sur la connaissance
    Ce sont des agents qui raisonnent en manipulant des représentations internes
    de connaissances.

Que signifie « raisonner sur la base de connaissances pour tirer une conclusion
» ?

Commençons par y répondre avec un exemple tiré de Harry Potter. Considérez les
phrases suivantes :

1. S’il n’a pas plu, Harry a rendu visite à Hagrid aujourd’hui.
2. Harry a rendu visite à Hagrid ou à Dumbledore aujourd’hui, mais pas aux deux.
3. Harry a rendu visite à Dumbledore aujourd’hui.

En nous basant sur ces trois phrases, nous pouvons répondre à la question «
a-t-il plu aujourd’hui ? », même si aucune des phrases prises individuellement
ne nous dit explicitement s’il pleut aujourd’hui. Voici comment nous pouvons
procéder : en regardant la phrase 3, nous savons que Harry a rendu visite à
Dumbledore. En regardant la phrase 2, nous savons que Harry a rendu visite soit
à Dumbledore, soit à Hagrid, et nous pouvons donc en conclure :

1. Harry n’a pas rendu visite à Hagrid.

   Maintenant, en regardant la phrase 1, nous comprenons que s’il n’avait pas
   plu, Harry aurait rendu visite à Hagrid. Cependant, grâce à la phrase 4, nous
   savons que ce n’est pas le cas. Par conséquent, nous pouvons conclure :

1. Il a plu aujourd’hui.

   Pour arriver à cette conclusion, nous avons utilisé la logique, et la leçon
   d’aujourd’hui explore comment l’IA peut utiliser la logique pour parvenir à
   de nouvelles conclusions fondées sur des informations existantes.

Phrase
    Une phrase est une affirmation sur le monde dans un langage de
    représentation des connaissances. Une phrase est la manière dont l’IA stocke
    la connaissance et l’utilise pour déduire de nouvelles informations.

**************************
 Logique propositionnelle
**************************

La logique propositionnelle repose sur des propositions, qui sont des
déclarations sur le monde pouvant être soit vraies soit fausses, comme c’est le
cas pour les phrases 1 à 5 ci-dessus.

Symboles propositionnels
    Les symboles propositionnels sont le plus souvent des lettres (P, Q, R)
    utilisées pour représenter une proposition.

Connecteurs logiques
    Les connecteurs logiques sont des symboles logiques qui relient des symboles
    propositionnels afin de raisonner de manière plus complexe à propos du
    monde.

Non
    Inverse la valeur de vérité de la proposition. Ainsi, par exemple, si
    :math:`P` : « Il pleut », alors :math:`\lnot P` : « Il ne pleut pas ».

Les tables de vérité sont utilisées pour comparer toutes les assignations de
valeurs de vérité possibles aux propositions. Cet outil nous aidera à mieux
comprendre les valeurs de vérité des propositions lorsqu’elles sont reliées par
différents connecteurs logiques. Par exemple, voici notre première table de
vérité :

========= ===============
:math:`P` :math:`\lnot P`
========= ===============
faux      vrai
vrai      faux
========= ===============

Et
    Relie deux propositions différentes. Lorsque ces deux propositions,
    :math:`P` et :math:`Q`, sont reliées par :math:`\land`, la proposition
    résultante :math:`P \land Q` n’est vraie que dans le cas où :math:`P` et
    :math:`Q` sont toutes les deux vraies.

    ========= ========= ================
    :math:`P` :math:`Q` :math:`P \lor Q`
    ========= ========= ================
    faux      faux      faux
    faux      vrai      faux
    vrai      faux      faux
    vrai      vrai      vrai
    ========= ========= ================

Ou
    Est vrai tant que l’un ou l’autre de ses arguments est vrai. Cela signifie
    que pour que :math:`P \lor Q` soit vrai, au moins l’un de :math:`P` ou
    :math:`Q` doit être vrai.

    ========= ========= ================
    :math:`P` :math:`Q` :math:`P \lor Q`
    ========= ========= ================
    faux      faux      faux
    faux      vrai      vrai
    vrai      faux      vrai
    vrai      vrai      vrai
    ========= ========= ================

Il est utile de mentionner qu’il existe deux types de « Ou » : un Ou inclusif et
un Ou exclusif. Dans un Ou exclusif, :math:`P \lor Q` est faux si :math:`P \land
Q` est vrai. C’est-à-dire qu’un Ou exclusif exige qu’un seul de ses arguments
soit vrai, et non les deux. Un Ou inclusif est vrai si P, Q, ou :math:`P \land
Q` est vrai. Dans le cas du Ou (:math:`\lor`) présenté ici, l’intention est
celle d’un Ou inclusif.

.. sidebar:: Quelques notes non mentionnées dans le cours

    * Parfois, un exemple aide à comprendre la différence entre un Ou inclusif
      et un Ou exclusif. Ou inclusif : « pour avoir un dessert, tu dois nettoyer
      ta chambre ou tondre la pelouse. ». Dans ce cas, si vous faites les deux
      corvées, vous aurez quand même les biscuits. Ou exclusif : « Pour le
      dessert, tu peux avoir soit des biscuits soit de la glace. ». Dans ce cas,
      vous ne pouvez pas avoir les deux.
    * Si vous êtes curieux, le Ou exclusif est souvent abrégé en XOR et un
      symbole courant pour le représenter est :math:`\oplus`.

Implication
    Représente une structure de type « si P alors Q ». Par exemple, si P : « Il
    pleut » et Q : « Je suis à l’intérieur », alors :math:`P \implies Q`
    signifie « S’il pleut, alors je suis à l’intérieur ». Dans le cas où P
    implique Q (:math:`P \implies Q`), P est appelé l’\ **antécédent** et Q est
    appelé le *conséquent*.

    Lorsque l’\ **antécédent** est vrai, l’implication complète est vraie dans
    le cas où le **conséquent** est vrai (ce qui est logique : s’il pleut et que
    je suis à l’intérieur, alors la phrase « s’il pleut, alors je suis à
    l’intérieur » est vraie). Lorsque l’\ **antécédent** est vrai, l’implication
    est fausse si le **conséquent** est faux (si je suis dehors alors qu’il
    pleut, alors la phrase « S’il pleut, alors je suis à l’intérieur » est
    fausse). Cependant, lorsque l’\ **antécédent** est faux, l’implication est
    toujours vraie, quel que soit le **conséquent**. Cela peut parfois être un
    concept déroutant. Logiquement, nous ne pouvons rien apprendre d’une
    implication (:math:`P \implies Q`) si l’\ **antécédent** (P) est faux. En
    reprenant notre exemple, s’il ne pleut pas, l’implication ne dit rien sur le
    fait que je sois à l’intérieur ou non. Je pourrais être du genre casanier et
    ne jamais sortir, même quand il ne pleut pas, ou je pourrais être du genre
    plein air et être toujours dehors quand il ne pleut pas. Lorsque
    l’antécédent est faux, on dit que l’implication est *trivialement* vraie.

    ========= ========= ====================
    :math:`P` :math:`Q` :math:`P \implies Q`
    ========= ========= ====================
    faux      faux      vrai
    faux      vrai      vrai
    vrai      faux      faux
    vrai      vrai      vrai
    ========= ========= ====================

Biconditionnel
    Est une implication qui va dans les deux sens. Vous pouvez la lire comme «
    si et seulement si ». :math:`P \iff Q` est la même chose que :math:`P
    \implies Q` et :math:`Q \implies P` pris ensemble. Par exemple, si P : « Il
    pleut. » et Q : « Je suis à l’intérieur, » alors :math:`P \iff Q` signifie
    que « S’il pleut, alors je suis à l’intérieur, » et « si je suis à
    l’intérieur, alors il pleut ». Cela signifie que nous pouvons déduire
    davantage de choses qu’avec une simple implication. Si P est faux, alors Q
    est également faux ; s’il ne pleut pas, nous savons que je ne suis pas non
    plus à l’intérieur.

    ========= ========= ================
    :math:`P` :math:`Q` :math:`P \iff Q`
    ========= ========= ================
    faux      faux      vrai
    faux      vrai      vrai
    vrai      faux      faux
    vrai      vrai      vrai
    ========= ========= ================

Modèle
    Le modèle est une assignation d’une valeur de vérité à chaque proposition.
    Pour rappel, les propositions sont des affirmations sur le monde qui peuvent
    être vraies ou fausses. Cependant, les connaissances sur le monde sont
    représentées dans les valeurs de vérité de ces propositions. Le modèle est
    l’assignation de valeurs de vérité qui fournit des informations sur le
    monde.

    Par exemple, si P : « Il pleut. » et Q : « C’est mardi. », un modèle
    pourrait être l’assignation de valeurs de vérité suivante : {P = Vrai, Q =
    Faux}. Ce modèle signifie qu’il pleut, mais que ce n’est pas mardi.
    Cependant, il existe d’autres modèles possibles dans cette situation (par
    exemple, {P = Vrai, Q = Vrai}, où il pleut et c’est mardi). En fait, le
    nombre de modèles possibles est de 2 à la puissance du nombre de
    propositions. Dans ce cas, nous avions 2 propositions, soit 2²=4 modèles
    possibles.

Base de connaissances
    La base de connaissances est un ensemble de phrases connues par un agent
    basé sur la connaissance. Il s’agit des connaissances qui sont fournies à
    l’IA sur le monde sous forme de phrases en logique propositionnelle qui
    peuvent être utilisées pour faire des déductions supplémentaires sur le
    monde.

Conséquence logique: opérateur logique binaire :math:`\models`
    Si :math:`\alpha \models \beta` (:math:`\alpha` \text{a pour conséquence
    logique} \beta ), alors dans tout monde où :math:`\alpha` est vrai, \beta
    est vrai aussi.

    Par exemple, si :math:`\alpha` : « C’est un mardi de janvier » et
    :math:`\beta` : « Nous sommes en janvier, » alors nous savons que
    :math:`\alpha \models \beta`. S’il est vrai que c’est un mardi de janvier,
    nous savons aussi que nous sommes en janvier. La conséquence logique est
    différente de l’implication. L’implication est un connecteur logique entre
    deux propositions. La conséquence logique, en revanche, est une relation qui
    signifie que si toutes les informations contenues dans :math:`\alpha` sont
    vraies, alors toutes les informations contenues dans \beta sont vraies.

***********
 Inférence
***********

L’inférence est le processus consistant à dériver de nouvelles phrases à partir
d’anciennes.

Par exemple, dans l’exemple de Harry Potter plus tôt, les phrases 4 et 5 ont été
déduites des phrases 1, 2 et 3.

Il existe de multiples façons de déduire de nouvelles connaissances à partir de
connaissances existantes. Premièrement, nous examinerons l’algorithme de
**vérification de modèles**.

* Pour déterminer si :math:`KB \models \alpha` (en d’autres termes, répondre à
  la question « pouvons-nous conclure que \alpha est vrai sur la base de notre
  base de connaissances ? »)

  * Énumérer tous les modèles possibles.
  * Si dans chaque modèle où KB est vraie, \alpha est également vrai, alors KB a
    pour conséquence logique \alpha (:math:`KB \models \alpha`).

Considérez l’exemple suivant :

P : C’est mardi. Q : Il pleut. R : Harry ira courir. KB : :math:`(P \land \lnot
Q) \implies R` (en mots, P et non Q impliquent R). :math:`P` (P est vrai).
:math:`¬Q` (Q est faux). Requête : R (Nous voulons savoir si R est vrai ou faux
; Est-ce que :math:`KB \models R` ?)

Pour répondre à la requête en utilisant l’algorithme de vérification de modèles,
nous énumérons tous les modèles possibles.

========= ========= ========= ==========
:math:`P` :math:`Q` :math:`R` :math:`KB`
========= ========= ========= ==========
faux      faux      faux
faux      faux      vrai
faux      vrai      faux
faux      vrai      vrai
vrai      faux      faux
vrai      faux      vrai
vrai      vrai      faux
vrai      vrai      vrai
========= ========= ========= ==========

Ensuite, nous parcourons chaque modèle et vérifions s’il est vrai compte tenu de
notre base de connaissances.

Tout d’abord, dans notre KB, nous savons que P est vrai. Ainsi, nous pouvons
dire que la KB est fausse dans tous les modèles où P n’est pas vrai.

========= ========= ========= ==========
:math:`P` :math:`Q` :math:`R` :math:`KB`
========= ========= ========= ==========
faux      faux      faux      faux
faux      faux      vrai      faux
faux      vrai      faux      faux
faux      vrai      vrai      faux
vrai      faux      faux
vrai      faux      vrai
vrai      vrai      faux
vrai      vrai      vrai
========= ========= ========= ==========

Ensuite, de manière similaire, dans notre KB, nous savons que Q est faux. Ainsi,
nous pouvons dire que la KB est fausse dans tous les modèles où Q est vrai.

========= ========= ========= ==========
:math:`P` :math:`Q` :math:`R` :math:`KB`
========= ========= ========= ==========
faux      faux      faux      faux
faux      faux      vrai      faux
faux      vrai      faux      faux
faux      vrai      vrai      faux
vrai      faux      faux
vrai      faux      vrai
vrai      vrai      faux      faux
vrai      vrai      vrai      faux
========= ========= ========= ==========

Enfin, il nous reste deux modèles. Dans les deux, P est vrai et Q est faux. Dans
un modèle, R est vrai et dans l’autre, R est faux. Étant donné que :math:`(P
\land \lnot Q) \implies R` se trouve dans notre KB, nous savons que dans le cas
où P est vrai et Q est faux, R doit être vrai. Ainsi, nous disons que notre KB
est fausse pour le modèle où R est faux, et vraie pour le modèle où R est vrai.

========= ========= ========= ==========
:math:`P` :math:`Q` :math:`R` :math:`KB`
========= ========= ========= ==========
faux      faux      faux      faux
faux      faux      vrai      faux
faux      vrai      faux      faux
faux      vrai      vrai      faux
vrai      faux      faux      faux
vrai      faux      vrai      vrai
vrai      vrai      faux      faux
vrai      vrai      vrai      faux
========= ========= ========= ==========

En regardant ce tableau, il n’y a qu’un seul modèle où notre base de
connaissances est vraie. Dans ce modèle, nous voyons que R est également vrai.
Selon notre définition de la conséquence logique, si R est vrai dans tous les
modèles où la KB est vraie, alors KB \models R.

Ensuite, examinons comment les connaissances et la logique peuvent être
représentées sous forme de code.

.. code-block:: python

    from logic import *

    # Créer de nouvelles classes, chacune ayant un nom, ou un symbole,
    # représentant chaque proposition.

    rain = Symbol("rain")  # Il pleut.
    hagrid = Symbol("hagrid")  # Harry a rendu visite à Hagrid
    dumbledore = Symbol("dumbledore")  # Harry a rendu visite à Dumbledore

    # Sauvegarder les phrases dans la KB

    knowledge = And(
        # En commençant par le connecteur logique "And" (Et),
        # car chaque proposition représente une connaissance que nous
        # savons être vraie.
        Implication(
            Not(rain), hagrid
        ),  # ¬(Il pleut) \implies (Harry a rendu visite à Hagrid)
        Or(hagrid, dumbledore),  # (Harry a rendu visite à Hagrid) \lor
        # (Harry a rendu visite à Dumbledore).
        Not(
            And(hagrid, dumbledore)
        ),  # ¬(Harry a rendu visite à Hagrid \land Harry a rendu visite
        # à Dumbledore) c'est-à-dire que Harry n'a pas visité à la
        # fois Hagrid et Dumbledore.
        dumbledore,  # Harry a rendu visite à Dumbledore.
        # Notez que si les propositions précédentes contenaient
        # plusieurs symboles avec des connecteurs,
        # il s'agit ici d'une proposition composée d'un seul
        # symbole.
        # Cela signifie que nous prenons comme fait que,
        # dans cette KB, Harry a rendu visite à Dumbledore.
    )

Pour exécuter l’algorithme de vérification de modèles, les informations
suivantes sont nécessaires :

* Une Base de Connaissances, qui sera utilisée pour faire des déductions
* Une requête, c’est-à-dire la proposition pour laquelle nous voulons savoir si
  elle est la conséquence logique de la KB
* Des symboles, une liste de tous les symboles (ou propositions atomiques)
  utilisés (dans notre cas, il s’agit de ``rain``, ``hagrid`` et ``dumbledore``)
* Un Modèle, soit une assignation de valeurs vraies ou fausses aux symboles

L’algorithme de vérification de modèles se présente comme suit :

.. code-block:: python

    def check_all(knowledge, query, symbols, model):

        # Si le modèle possède une assignation pour chaque symbole
        #
        # (La logique ci-dessous peut être un peu confuse :
        # nous commençons avec une liste de symboles.
        # La fonction est récursive,
        # et chaque fois qu'elle s'appelle elle-même,
        # elle retire un symbole de la liste des symboles et
        # génère des modèles à partir de lui.
        # Ainsi, lorsque la liste des symboles est vide,
        # nous savons que nous avons fini de générer des modèles avec
        # toutes les assignations de vérité possibles des symboles.)
        if not symbols:
            # Si la base de connaissances est vraie dans le modèle, alors la requête doit également être vraie
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:
            # Choisir l'un des symboles non utilisés restants
            remaining = symbols.copy()
            p = remaining.pop()

            # Créer un modèle où le symbole est vrai
            model_true = model.copy()
            model_true[p] = True

            # Créer un modèle où le symbole est faux
            model_false = model.copy()
            model_false[p] = False

            # S'assurer que la conséquence logique (entailment) tient dans les deux modèles
            return check_all(knowledge, query, remaining, model_true) and check_all(
                knowledge, query, remaining, model_false
            )

Notez que nous ne nous intéressons qu’aux modèles où la KB est vraie. Si la KB
est fausse, alors les conditions que nous savons être vraies ne se produisent
pas dans ces modèles, ce qui les rend hors de propos pour notre cas.

.. sidebar:: Un exemple extérieur au cours

    Soit P : Harry joue attrapeur, Q: Olivier joue gardien, R : Gryffondor
    gagne. Notre KB spécifie que :math:`P Q (P \land Q`) \implies R`. En
    d’autres termes, nous savons que P est vrai, c’est-à-dire que Harry joue
    attrapeur, et que Q est vrai, c’est-à-dire qu’Olivier joue gardien, et que
    si à la fois P et Q sont vrais, alors R est vrai aussi, signifiant que
    Gryffondor gagne le match. Imaginez maintenant un modèle où Harry jouerait
    batteur au lieu d’attrapeur (donc, Harry n’a pas joué attrapeur,
    :math:`\lnot P`). Eh bien, dans ce cas, on se moque de savoir si Gryffondor
    a gagné (si R est vrai ou non), car nous avons l’information dans notre KB
    que Harry a joué attrapeur et non batteur. Nous ne sommes intéressés que par
    les modèles où, comme dans notre cas, P et Q sont vrais.

De plus, la manière dont la fonction ``check_all`` fonctionne est récursive.
C’est-à-dire qu’elle choisit un symbole, crée deux modèles, dans l’un desquels
le symbole est vrai et dans l’autre le symbole est faux, puis elle s’appelle à
nouveau, maintenant avec deux modèles qui diffèrent par l’assignation de vérité
de ce symbole. La fonction continuera de le faire jusqu’à ce que tous les
symboles se soient vus attribuer des valeurs de vérité dans les modèles,
laissant la liste ``symbols`` vide. Une fois qu’elle est vide (comme identifié
par la ligne ``if not symbols``), dans chaque instance de la fonction (où chaque
instance détient un modèle différent), la fonction vérifie si la KB est vraie
compte tenu du modèle. Si la KB est vraie dans ce modèle, la fonction vérifie si
la requête est vraie, comme décrit précédemment.

******************************
 Ingénierie des connaissances
******************************

L’ingénierie des connaissances est le processus consistant à trouver comment
représenter les propositions et la logique dans l’IA.

Pratiquons l’ingénierie des connaissances en utilisant le jeu Clue.

Dans le jeu, un meurtre a été commis par une *personne*, en utilisant une arme
(*outil*) dans un *lieu*. Les personnes, les armes et les lieux sont représentés
par des cartes. Une carte de chaque catégorie est tirée au hasard et placée dans
une enveloppe, et c’est aux participants de découvrir l’auteur du crime. Les
participants font cela en découvrant des cartes et en déduisant à partir de ces
indices ce qui doit se trouver dans l’enveloppe. Nous allons utiliser
l’algorithme de vérification de modèles vu précédemment pour élucider le
mystère. Dans notre modèle, nous marquons comme ``True`` (Vrai) les éléments que
nous savons être liés au meurtre et ``False`` (Faux) dans le cas contraire.

Pour nos besoins, supposons que nous avons trois personnes : Moutarde, Violet et
Rose ; trois armes : poignard, revolver et clé anglaise ; et trois lieux : salle
de bal, cuisine et bibliothèque.

Nous pouvons commencer à créer notre base de connaissances en ajoutant les
règles du jeu. Nous savons avec certitude qu’une personne est le meurtrier,
qu’une arme a été utilisée, et que le meurtre a eu lieu dans un endroit. Cela
peut être représenté en logique propositionnelle de la manière suivante :

* :math:`(Moutarde \lor Violet \lor Rose)`
* :math:`(poignard \lor revolver \lor \text{clé anglaise})`
* :math:`(salle de bal \lor cuisine \lor \text{bibliothèque})`

Le jeu commence avec chaque joueur voyant une personne, une arme et un lieu,
sachant ainsi qu’ils ne sont pas liés au meurtre. Les joueurs ne partagent pas
les informations qu’ils ont vues sur ces cartes. Supposons que notre joueur
reçoive les cartes Moutarde, cuisine et revolver. Ainsi, nous savons que ceux-ci
ne sont pas liés au meurtre et nous pouvons ajouter à notre KB :

* :math:`\lnot (Moutarde)`
* :math:`\lnot (cuisine)`
* :math:`\lnot (revolver)`

Dans d’autres situations du jeu, on peut faire une hypothèse, en suggérant une
combinaison de personne, d’arme et de lieu. Supposons que l’hypothèse soit que
Rose a utilisé une clé anglaise pour commettre le crime dans la bibliothèque. Si
cette hypothèse est fausse, alors ce qui suit peut être déduit et ajouté à la KB
:

* :math:`(\lnot Rose \lor \lnot \text{bibliothèque} \lor \lnot \text{clé
  anglaise})`

Maintenant, supposons que quelqu’un nous montre la carte Violet. Ainsi, nous
pouvons ajouter :

* :math:`\lnot (Violet)`

à notre KB.

À ce stade, nous pouvons conclure que la meurtrière est Rose, car il doit s’agir
de l’un des trois entre Moutarde, Violet et Rose, et nous avons la preuve que ce
ne sont pas les deux premiers.

L’ajout d’un seul élément de connaissance supplémentaire, par exemple, que ce
n’est pas la salle de bal, peut nous donner plus d’informations. Tout d’abord,
nous mettons à jour notre KB :

* :math:`\lnot (salle de bal)`

Et maintenant, en utilisant plusieurs données précédentes, nous pouvons déduire
que Rose a commis le meurtre avec un poignard dans la bibliothèque. Nous pouvons
déduire qu’il s’agit de la bibliothèque car il doit s’agir soit de la salle de
bal, soit de la cuisine, soit de la bibliothèque, et les deux premiers ont été
prouvés comme n’étant pas les lieux du crime. Cependant, lorsque quelqu’un a
émis l’hypothèse Rose, bibliothèque, clé anglaise, cette hypothèse était fausse.
Ainsi, au moins l’un des éléments de cette affirmation doit être faux. Puisque
nous savons que Rose et la bibliothèque sont tous deux vrais, nous savons que la
clé anglaise est la partie fausse ici. Puisque l’une des trois armes doit être
vraie, et que ce n’est ni la clé anglaise ni le revolver, nous pouvons conclure
que c’est le poignard.

Voici comment les informations seraient ajoutées à la base de connaissances en
Python :

.. code-block:: python

    # Ajouter les indices à la KB

    knowledge = And(
        # Commencer par les conditions du jeu :
        # un élément de chacune des trois catégories doit être vrai.
        Or(mustard, plum, scarlet),
        Or(ballroom, kitchen, library),
        Or(knife, revolver, wrench),
        # Ajouter les informations issues des trois cartes
        # initiales que nous avons vues
        Not(mustard),
        Not(kitchen),
        Not(revolver),
        # Ajouter l'hypothèse que quelqu'un a faite selon laquelle
        # c'est Rose (scarlet) qui a utilisé une clé anglaise dans
        # la bibliothèque
        Or(Not(scarlet), Not(library), Not(wrench)),
        # Ajouter les cartes auxquelles nous avons été exposés
        Not(plum),
        Not(ballroom),
    )

Nous pouvons également examiner d’autres énigmes logiques. Considérez l’exemple
suivant : quatre personnes différentes, Gilderoy, Pomona, Minerva et Horace,
sont assignées à quatre maisons différentes, Gryffondor, Poufsouffle, Serdaigle
et Serpentard. Il y a exactement une personne dans chaque maison. Représenter
les conditions de l’énigme en logique propositionnelle est assez lourd.
Premièrement, chacune des assignations possibles devra constituer une
proposition en elle-même : MinervaGryffondor, MinervaPoufsouffle,
MinervaSerdaigle, MinervaSerpentard, PomonaGryffondor…. Deuxièmement, pour
représenter le fait que chaque personne appartient à une maison, une instruction
« Ou » est requise avec toutes les assignations de maison possibles par personne
:

* :math:`(MinervaGryffondor \lor MinervaPoufsouffle \lor MinervaSerdaigle \lor MinervaSerpentard)`,
      à répéter pour chaque personne.

Ensuite, pour coder le fait que si une personne est affectée à une maison, elle
n’est pas affectée aux autres maisons, nous écrirons :

* :math:`(MinervaGryffondor \implies \lnot MinervaPoufsouffle) \land
  (MinervaGryffondor \implies \lnot MinervaSerdaigle) \land (MinervaGryffondor
  \implies \lnot MinervaSerpentard) \land (MinervaPoufsouffle \implies \lnot
  MinervaGryffondor)…`

et ainsi de suite pour toutes les maisons et toutes les personnes. Une solution
à cette inefficacité est proposée dans la section sur la logique du premier
ordre. Cependant, ce type d’énigme peut toujours être résolu avec l’un ou
l’autre type de logique, si l’on dispose de suffisamment d’indices.

Un autre type d’énigme pouvant être résolu grâce à la logique propositionnelle
est le jeu Mastermind. Dans ce jeu, le joueur 1 dispose des couleurs dans un
certain ordre, puis le joueur 2 doit deviner cet ordre. À chaque tour, le joueur
2 fait une supposition, et le joueur 1 renvoie un nombre, indiquant combien de
couleurs le joueur 2 a trouvé correctement. Simulons une partie avec quatre
couleurs. Supposons que le joueur deux suggère l’ordre suivant :

.. figure:: /assets/figures/mastermind1.png

Le joueur un répond « deux ». Ainsi, nous savons que deux des couleurs sont à la
bonne position, et que les deux autres sont au mauvais endroit. En se basant sur
cette information, le joueur deux essaie d’échanger l’emplacement de deux
couleurs.

.. figure:: /assets/figures/mastermind2.png

Maintenant, le joueur un répond « zéro ». Ainsi, le joueur deux sait que les
couleurs échangées étaient au bon emplacement initialement, ce qui signifie que
les deux couleurs non touchées étaient au mauvais emplacement. Le joueur deux
les échange.

.. figure:: /assets/figures/mastermind3.png

Le joueur un dit « quatre » et la partie est terminée.

Représenter cela en logique propositionnelle nécessiterait que nous ayons
(nombre de couleurs)² propositions atomiques. Ainsi, dans le cas de quatre
couleurs, nous aurions les propositions rouge0, rouge1, rouge2, rouge3, bleu0…
représentant la couleur et la position. L’étape suivante consisterait à
représenter les règles du jeu en logique propositionnelle (qu’il n’y a qu’une
seule couleur par position et qu’aucune couleur ne se répète) et à les ajouter à
la KB. La dernière étape consisterait à ajouter tous les indices dont nous
disposons à la KB. Dans notre cas, nous ajouterions que, lors de la première
proposition, deux positions étaient fausses et deux étaient correctes, et que
lors de la deuxième proposition, aucune n’était correcte. À l’aide de ces
connaissances, un algorithme de vérification de modèles peut nous donner la
solution à l’énigme.

********************
 Règles d’inférence
********************

La vérification de modèles (Model Checking) n’est pas un algorithme efficace car
elle doit examiner chaque modèle possible avant de donner la réponse (pour
rappel : une requête R est vraie si sous tous les modèles (assignations de
vérité) où la KB est vraie, R est également vrai). Les règles d’inférence nous
permettent de générer de nouvelles informations basées sur des connaissances
existantes sans avoir à examiner tous les modèles possibles.

Les règles d’inférence sont généralement représentées à l’aide d’une barre
horizontale qui sépare la partie supérieure, la prémisse, de la partie
inférieure, la conclusion. La prémisse correspond aux connaissances que nous
possédons, et la conclusion correspond aux connaissances qui peuvent être
générées sur la base de la prémisse.

.. figure:: /assets/figures/modusponensexample.png

Dans cet exemple, notre prémisse est constituée des propositions suivantes :

* S’il pleut, alors Harry est à l’intérieur.
* Il pleut.

À partir de cela, la plupart des humains raisonnables peuvent conclure que :

Modus Ponens
    Le type de règle d’inférence que nous utilisons dans cet exemple est le
    Modus Ponens, qui est une façon élégante de dire que si nous savons qu’une
    implication et son antécédent sont vrais, alors le conséquent est vrai
    également.

    .. figure:: /assets/figures/modusponens.png

Élimination de la conjonction (Et)
    Si une proposition Et (And) est vraie, alors n’importe quelle proposition
    atomique à l’intérieur de celle-ci est vraie également. Par exemple, si nous
    savons que Harry est ami avec Ron et Hermione, nous pouvons en conclure que
    Harry est ami avec Hermione.

    .. figure:: /assets/figures/andelimination.png

Élimination de la double négation
    Une proposition qui est niée deux fois est vraie. Par exemple, considérez la
    proposition « Il n’est pas vrai que Harry n’a pas réussi le test ». Nous
    pouvons l’analyser de la manière suivante : « Il n’est pas vrai que (Harry
    n’a pas réussi le test) », ou « \lnot (Harry n’a pas réussi le test) », et
    enfin « :math:`\lnot (\lnot (\text{Harry a réussi le test}))` ». Les deux
    mnégations s’annulent, ce qui marque la proposition « Harry a réussi le test
    » comme étant vraie.

    .. figure:: /assets/figures/doublenegationelimination.png

Élimination de l’implication
    Une implication équivaut à une relation Ou (Or) entre l’antécédent nié et le
    conséquent. À titre d’exemple, la proposition « S’il pleut, Harry est à
    l’intérieur » est équivalente à la proposition « (il ne pleut pas) ou (Harry
    est à l’intérieur) ».

    .. figure:: /assets/figures/implicationelimination.png

    Cela peut être un peu déroutant. Cependant, considérez la table de vérité
    suivante :

    ========= ========= ==================== ======================
    :math:`P` :math:`Q` :math:`P \implies Q` :math:`\lnot P \lor Q`
    ========= ========= ==================== ======================
    faux      faux      vrai                 vrai
    faux      vrai      vrai                 vrai
    vrai      faux      faux                 faux
    vrai      vrai      vrai                 vrai
    ========= ========= ==================== ======================

    Étant donné que :math:`P \implies Q` et :math:`\lnot P \lor Q` ont la même
    assignation de valeurs de vérité, nous savons qu’elles sont logiquement
    équivalentes. Une autre façon de voir les choses est qu’une implication est
    vraie si l’une des deux conditions possibles est remplie : premièrement, si
    l’antécédent est faux, l’implication est trivialement vraie (comme discuté
    plus tôt, dans la section sur l’implication). Cela est représenté par
    l’antécédent nié P dans :math:`\lnot P \lor Q`, ce qui signifie que la
    proposition est toujours vraie si P est faux. Deuxièmement, l’implication
    est vraie lorsque l’antécédent est vrai uniquement lorsque le conséquent est
    également vrai. C’est-à-dire que si P et Q sont tous deux vrais, alors
    :math:`\lnot P \lor Q` est vrai. Cependant, si P est vrai et que Q ne l’est
    pas, alors :math:`\lnot P \lor Q` est faux.

Élimination du biconditionnel
    Une proposition biconditionnelle est équivalente à une implication et à son
    inverse reliées par un connecteur Et (And). Par exemple, « Il pleut si et
    seulement si Harry est à l’intérieur » est équivalent à (« S’il pleut, Harry
    est à l’intérieur » Et « Si Harry est à l’intérieur, il pleut »).

    .. figure:: /assets/figures/biconditionalelimination.png

Lois de De Morgan
    Il est possible de transformer un connecteur Et en un connecteur Ou.
    Considérez la proposition suivante : « Il n’est pas vrai qu’à la fois Harry
    et Ron ont réussi le test. ». De cela, il est possible de conclure que « Il
    n’est pas vrai que Harry a réussi le test » Ou « Il n’est pas vrai que Ron a
    réussi le test. ». C’est-à-dire, pour que la proposition Et précédente soit
    vraie, au moins l’une des propositions de la proposition Ou doit être vraie.

    .. figure:: /assets/figures/demorgans1.png

    De manière similaire, il est possible de conclure l’inverse. Considérez la
    proposition « Il n’est pas vrai que Harry ou Ron a réussi le test. ». Cela
    peut être reformulé par « Harry n’a pas réussi le test » Et « Ron n’a pas
    réussi le test ».

    .. figure:: /assets/figures/demorgans2.png

Propriété de distributivité
    Une proposition avec deux éléments qui sont groupés avec des connecteurs Et
    ou Ou peut être distribuée, ou décomposée en, de plus petites unités
    composées de Et et de Ou.

    .. figure:: /assets/figures/distributive1.png

    .. figure:: /assets/figures/distributive2.png

Connaissance et problèmes de recherche
    L’inférence peut être considérée comme un problème de recherche possédant
    les propriétés suivantes :

    * État initial : la base de connaissances de départ
    * Actions : les règles d’inférence
    * Modèle de transition : la nouvelle base de connaissances après l’inférence
    * Test de but : vérifier si l’affirmation que nous essayons de prouver se
      trouve dans la KB
    * Fonction de coût du chemin : le nombre d’étapes dans la preuve

    Cela démontre à quel point les algorithmes de recherche sont polyvalents,
    nous permettant de dériver de nouvelles informations basées sur des
    connaissances existantes à l’aide de règles d’inférence.

************
 Résolution
************

La résolution est une règle d’inférence puissante qui stipule que si l’une des
deux propositions atomiques d’une proposition Ou (Or) est fausse, l’autre doit
être vraie. Par exemple, étant donné la proposition « Ron est dans la Grande
Salle » Ou « Hermione est dans la bibliothèque », en plus de la proposition «
Ron n’est pas dans la Grande Salle, » nous pouvons en conclure que « Hermione
est dans la bibliothèque ». Plus formellement, nous pouvons définir la
résolution de la manière suivante:

    .. figure:: /assets/figures/resolution1.png

La résolution s’appuie sur des **littéraux complémentaires**, c’est-à-dire deux
propositions atomiques identiques dont l’une est niée et l’autre non, telles que
P et :math:`\lnot P`.

La résolution peut être généralisée davantage. Supposons qu’en plus de la
proposition « Ron est dans la Grande Salle » Ou « Hermione est dans la
bibliothèque », nous sachions également que « Ron n’est pas dans la Grande Salle
» Ou « Harry dort ». Nous pouvons en déduire, en utilisant la résolution, que «
Hermione est dans la bibliothèque » Ou « Harry dort ». Pour le formuler en
termes formels :

    .. figure:: /assets/figures/resolution2.png

Les littéraux complémentaires nous permettent de générer de nouvelles phrases
par le biais d’inférences par résolution. Ainsi, les algorithmes d’inférence
localisent les littéraux complémentaires pour générer de nouvelles
connaissances.

Clause
    Une **Clause** est une disjonction de littéraux (un symbole propositionnel
    ou une négation d’un symbole propositionnel, tel que P, :math:`\lnot P`).

Disjonction
    Une **disjonction** consiste en des propositions qui sont reliées par un
    connecteur logique Ou (:math:`P \lor Q \lor R`).

Conjoncton
    Une **conjonction**, en revanche, consiste en des propositions qui sont
    reliées par un connecteur logique Et (:math:`P \land Q \land R`).

Les clauses nous permettent de convertir n’importe quelle déclaration logique
sous une **Forme normale conjonctive** (Conjunctive Normal Form - CNF), qui est
une conjonction de clauses, par exemple : math:`(A \lor B \lor C) \land (D \lor
\lnot E) \land (F \lor G)`.

Étapes de conversion des propositions sous la forme normale conjonctive (CNF)
=============================================================================

* Éliminer les biconditionnels

      * Transformer :math:`(\alpha \iff \beta)` en
            :math:`(\alpha \implies \beta ) \land (\beta \implies \alpha )`.

* Éliminer les implications

      * Transformer :math:`(\alpha \implies \beta)` en
            :math:`\lnot \alpha \lor \beta`.

* Déplacer la négation vers l’intérieur jusqu’à ce que seuls les littéraux
      soient niés (et non les clauses), en utilisant les lois de De Morgan.

      * Transformer :math:`\lnot (\alpha \land \beta )` en
            :math:`\lnot \alpha \lor \lnot \beta`.

Voici un exemple de conversion de (:math:`P \lor Q`) \implies R en Forme Normale
Conjonctive :

* :math:`(P \lor Q) \implies R`
* :math:`\lnot (P \lor Q) \lor R` /Éliminer l’implication
* :math:`(\lnot P \land \lnot Q) \lor R` /Loi de De Morgan
* :math:`(\lnot P \lor R) \land (\lnot Q \lor R)` /Loi de distributivité

À ce stade, nous pouvons exécuter un algorithme d’inférence sur la forme normale
conjonctive. Il peut arriver que, par le processus d’inférence par résolution,
nous nous retrouvions dans des cas où une clause contient deux fois le même
littéral. Dans ces cas, un processus appelé **factorisation** est utilisé, où le
littéral en double est supprimé. Par exemple, :math:`(P \lor Q \lor S) \land
(\lnot P \lor R \lor S)` nous permet de déduire par résolution que :math:`(Q
\lor S \lor R \lor S)`. Le S en double peut être retiré pour nous donner
:math:`(Q \lor R \lor S)`.

Résoudre un littéral et sa négation, c’est-à-dire :math:`\lnot P` et P, donne la
**clause vide ()**. La clause vide est toujours fausse, ce qui est logique car
il est impossible que P et :math:`\lnot P` soient tous deux vrais. Ce fait est
utilisé par l’algorithme de résolution.

* Pour déterminer si :math:`KB \models \alpha` :

      * Vérifier
            constitue une contradiction ?

            * Si oui, alors :math:`KB \models \alpha`.
            * Sinon, pas de conséquence logique.

La preuve par contradiction est un outil souvent utilisé en informatique. Si
notre base de connaissances est vraie et qu’elle contredit :math:`\lnot \alpha`,
cela signifie que :math:`\lnot \alpha` est faux, et par conséquent,
:math:`\alpha` doit être vrai. Plus techniquement, l’algorithme effectuerait les
actions suivantes :

* Pour déterminer si :math:`KB \models \alpha` :

      * Convertir :math:`(KB \land \lnot \alpha )` en forme normale conjonctive.
      * Continuer à vérifier pour voir si nous pouvons utiliser la résolution
        pour produire une nouvelle clause.
      * Si nous parvenons un jour à produire la clause vide (équivalente à
        Faux), félicitations !. Nous sommes parvenus à une contradiction,
        prouvant ainsi que :math:`KB \models \alpha`.
      * Cependant, si aucune contradiction n’est obtenue et qu’aucune autre
        clause ne peut être déduite, il n’y a pas de conséquence logique.

Voici un exemple illustrant comment cet algorithme pourrait fonctionner:

* Est-ce que :math:`(A \lor B) \land (\lnot B \lor C) \land (\lnot C)`
      implique logiquement (a pour conséquence) A ?
* Tout d’abord, pour prouver par contradiction, nous supposons que A
      est faux. Ainsi, nous arrivons à :math:`(A \lor B) \land (\lnot B \lor C)
      \land (\lnot C) \land (\lnot A)`.
* Maintenant, nous pouvons commencer à générer de nouvelles
      informations. Puisque nous savons que C est faux :math:`(\lnot C)`, la
      seule façon pour que :math:`(\lnot B \lor C)` soit vrai est que B soit
      également faux. Ainsi, nous pouvons ajouter :math:`(\lnot B)` à notre KB.
* Ensuite, puisque nous savons :math:`(\lnot B)`, la seule façon pour que
      :math:`(A \lor B)` soit vrai est que A soit vrai. Ainsi, nous pouvons
      ajouter :math:`(A)` à notre KB.
* Maintenant, notre KB possède deux littéraux complémentaires,
      :math:`(A)` et :math:`(\lnot A)`. Nous les résolvons, en arrivant à
      l’ensemble vide, :math:`()`. L’ensemble vide est faux par définition, nous
      sommes donc parvenus à une contradiction.

**************************
 Logique du premier ordre
**************************

La logique du premier ordre est un autre type de logique qui nous permet
d’exprimer des idées plus complexes de manière plus succincte que la logique
propositionnelle. La logique du premier ordre utilise deux types de symboles :
les *symboles de constantes* et les *symboles de prédicats*. Les symboles de
constantes représentent des objets, tandis que les symboles de prédicats
s’apparentent à des relations ou à des fonctions qui prennent un argument et
renvoient une valeur vraie ou fausse.

Par exemple, revenons à l’énigme logique avec les différentes personnes et les
assignations de maisons à Poudlard. Les symboles de constantes sont des
personnes ou des maisons, comme Minerva, Pomona, Gryffondor, Poufsouffle, etc.
Les symboles de prédicats sont des propriétés qui s’avèrent vraies ou fausses
pour certains symboles de constantes. Par exemple, nous pouvons exprimer l’idée
que Minerva est une personne en utilisant la phrase :math:`Personne(Minerva)`.
De même, nous pouvons exprimer l’idée que Gryffondor est une maison en utilisant
la phrase :math:`Maison(Gryffondor)`. Tous les connecteurs logiques fonctionnent
dans la logique du premier ordre de la même manière qu’auparavant. Par exemple,
:math:`\lnot Maison(Minerva)` exprime l’idée que Minerva n’est pas une maison.
Un symbole de prédicat peut également prendre deux arguments ou plus et exprimer
une relation entre eux. Par exemple, :math:`AppartientA` exprime une relation
entre deux arguments, la personne et la maison à laquelle la personne
appartient. Ainsi, l’idée que Minerva appartient à Gryffondor peut être exprimée
par :math:`AppartientA(Minerva, Gryffondor)`. La logique du premier ordre permet
d’avoir un symbole pour chaque personne et un symbole pour chaque maison. C’est
plus succinct que la logique propositionnelle, où chaque assignation
personne-maison exigerait un symbole différent.

Quantification universelle
    La quantification est un outil qui peut être utilisé en logique du premier
    ordre pour représenter des phrases sans utiliser un symbole de constante
    spécifique. La quantification universelle utilise le symbole :math:`\forall`
    pour exprimer « pour tout ». Ainsi, par exemple, la phrase :math:`\forall x,
    AppartientA(x, Gryffondor) \implies \lnot AppartientA(x, Poufsouffle)`
    exprime l’idée qu’il est vrai pour chaque symbole que si ce symbole
    appartient à Gryffondor, il n’appartient pas à Poufsouffle.

Quantification existentielle
    La quantification existentielle est une idée parallèle à la quantification
    universelle. Cependant, alors que la quantification universelle était
    utilisée pour créer des phrases qui sont vraies pour tous les x, la
    quantification existentielle est utilisée pour créer des phrases qui sont
    vraies pour au moins un x. Elle s’exprime à l’aide du symbole
    :math:`\exists`. Par exemple, la phrase :math:`\exists x. Maison(x) \land
    AppartientA(Minerva, x)` signifie qu’il y a au moins un symbole qui est à la
    fois une maison et à laquelle Minerva appartient. En d’autres termes, cela
    exprime l’idée que Minerva appartient à une maison.

    La quantification existentielle et la quantification universelle peuvent
    être utilisées dans la même phrase. Par exemple, la phrase :math:`\forall x.
    Personne(x) \implies (\exists y. Maison(y) \land AppartientA(x, y))` exprime
    l’idée que si x est une personne, alors il existe au moins une maison, y, à
    laquelle cette personne appartient. En d’autres termes, cette phrase
    signifie que chaque personne appartient à une maison.

Il existe également d’autres types de logique, et leur point commun est qu’elles
existent toutes dans le but de représenter de l’information. Ce sont les
systèmes que nous utilisons pour représenter les connaissances dans notre IA.
