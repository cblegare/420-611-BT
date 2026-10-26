#############
 Incertitude
#############

Lors de la dernière leçon, nous avons discuté de la manière dont l’IA peut
représenter et déduire de nouvelles connaissances. Cependant, bien souvent, dans
la réalité, l’IA ne possède qu’une connaissance partielle du monde, laissant
place à l’incertitude. Néanmoins, nous aimerions que notre IA prenne la
meilleure décision possible dans ces situations. Par exemple, lors des
prévisions météorologiques, l’IA dispose d’informations sur la météo
d’aujourd’hui, mais il n’y a aucun moyen de prédire avec une précision de 100 %
la météo de demain. Malgré tout, nous pouvons faire mieux que le hasard, et la
leçon d’aujourd’hui porte sur la façon dont nous pouvons créer une IA qui prend
des décisions optimales compte tenu d’informations limitées et d’incertitude.

*************
 Probabilité
*************

L’incertitude peut être représentée par un certain nombre d’événements et par la
vraisemblance, ou probabilité, que chacun d’eux se produise.

Mondes possibles
    Chaque situation possible peut être considérée comme un monde, représenté
    par la lettre grecque minuscule oméga :math:`\omega`. Par exemple, lancer un
    dé peut donner lieu à six mondes possibles : un monde où le dé donne 1, un
    monde où le dé donne 2, et ainsi de suite. Pour représenter la probabilité
    d’un certain monde, nous écrivons :math:`P(\omega)`.

Axiomes des probabilités
========================

* :math:`0 < P(\omega) < 1` : chaque valeur représentant une probabilité doit
    être comprise entre 0 et 1.

    * Zéro est un événement impossible, comme lancer un dé standard et obtenir
        un 7.

    * Un est un événement certain de se produire, comme lancer un dé standard
        et obtenir une valeur inférieure à 10.

    * En général, plus la valeur est élevée, plus l’événement a de chances de
        se produire.

* Les probabilités de chaque événement possible, lorsqu’elles sont additionnées,
    sont égales à 1.

.. figure:: /assets/figures/lotp.png

    La somme des probabilité de chaque événement possible donne 1

La probabilité d’obtenir un nombre *R* avec un dé standard peut être représentée
par :math:`P(R)`. Dans notre cas, :math:`P(R) = 1/6`, car il y a six mondes
possibles (obtenir n’importe quel nombre de 1 à 6) et que chacun a la même
probabilité de se produire. Considérons maintenant l’événement consistant à
lancer deux dés. Il y a maintenant 36 événements possibles, qui ont, là encore,
la même probabilité de se produire.

.. figure:: /assets/figures/36events1.png

Cependant, que se passe-t-il si nous essayons de prédire la somme des deux dés ?
Dans ce cas, nous n’avons que 11 valeurs possibles (la somme doit être comprise
entre 2 et 12), et elles ne se produisent pas aussi souvent les unes que les
autres.

.. figure:: /assets/figures/sumdice.png

Pour obtenir la probabilité d’un événement, nous divisons le nombre de mondes
dans lesquels il se produit par le nombre total de mondes possibles. Par
exemple, il y a 36 mondes possibles lorsqu’on lance deux dés. Dans un seul de
ces mondes, lorsque les deux dés donnent un 6, nous obtenons la somme de 12.
Ainsi, :math:`P(12) = 1/36`, ou, en mots, la probabilité de lancer deux dés et
d’obtenir deux nombres dont la somme est 12 est de 1/36. Quelle est :math:`P(7)`
? Nous comptons et voyons que la somme 7 se produit dans 6 mondes. Ainsi,
:math:`P(7) = 6/36 = 1/6`.

Probabilité inconditionnelle
    La probabilité inconditionnelle est le degré de croyance en une proposition
    en l'absence de toute autre preuve. Toutes les questions que nous avons
    posées jusqu'à présent étaient des questions de probabilité
    inconditionnelle, car le résultat du lancer d'un dé ne dépend pas des
    événements précédents.

****************************
 Probabilité conditionnelle
****************************

La probabilité conditionnelle est le degré de croyance en une proposition
sachant qu’une certaine preuve a déjà été révélée. Comme discuté dans
l’introduction, l’IA peut utiliser des informations partielles pour faire des
suppositions éclairées sur l’avenir. Pour utiliser ces informations, qui
affectent la probabilité que l’événement se produise dans le futur, nous nous
appuyons sur la probabilité conditionnelle.

La probabilité conditionnelle s’exprime à l’aide de la notation suivante:
:math:`P(a | b)`, signifiant « la probabilité que l’événement *a* se produise
sachant que nous savons que l’événement *b* s’est produit », ou, plus
succinctement, « la probabilité de *a* sachant *b* ». Nous pouvons maintenant
poser des questions telles que : quelle est la probabilité de pluie aujourd’hui
sachant qu’il a plu hier :math:`P(\text{pluie aujourd’hui} | \text{pluie
hier})`, ou quelle est la probabilité que le patient ait la maladie compte tenu
de ses résultats de test :math:`P(\text{maladie} | \text{résultats du test})`.

Mathématiquement, pour calculer la probabilité conditionnelle de *a* sachant
*b*, nous utilisons la formule suivante :

.. figure:: /assets/figures/conditional.png

En mots, la probabilité que *a* sachant *b* soit vrai est égale à la probabilité
que *a* et *b* soient tous deux vrais, divisée par la probabilité de *b*. Une
façon intuitive de raisonner à ce sujet est la réflexion « nous nous intéressons
aux événements où à la fois *a* et *b* sont vrais (le numérateur), mais
uniquement parmi les mondes où nous savons que *b* est vrai (le dénominateur) ».
Diviser par *b* restreint les mondes possibles à ceux où *b* est vrai. Les
formules suivantes sont des formes algébriquement équivalentes à la formule
ci-dessus :

.. figure:: /assets/figures/conditionalequivalent.png

Par exemple, considérez :math:`P(\text{somme 12} | \text{un dé fait six})`, ou
la probabilité de lancer deux dés et d’obtenir une somme de douze, sachant que
nous avons déjà lancé un dé et obtenu un six. Pour calculer cela, nous
restreignons d’abord nos mondes à ceux où la valeur du premier dé est six :

.. figure:: /assets/figures/sumconditional1.png

Maintenant, nous demandons combien de fois l’événement *a* (la somme étant 12)
se produit dans les mondes auxquels nous avons restreint la question (en
divisant par :math:`P(b)`, soit la probabilité que le premier dé donne 6).

.. figure:: /assets/figures/sumconditional2.png

**********************
 Variables aléatoires
**********************

Une variable aléatoire est une variable en théorie des probabilités possédant un
domaine de valeurs possibles qu’elle peut prendre. Par exemple, pour représenter
les résultats possibles lors du lancer d’un dé, nous pouvons définir une
variable aléatoire *Lancer*, qui peut prendre les valeurs :math:`{1, 2, 3, 4, 5,
6}`. Pour représenter le statut d’un vol, nous pouvons définir une variable
*Vol* qui prend les valeurs :math:`{\text{à l’heure}, \text{retardé},
\text{annulé}}`.

Souvent, nous sommes intéressés par la probabilité avec laquelle chaque valeur
se produit. Nous représentons cela à l’aide d’une distribution de probabilité.
Par exemple,

* :math:`P(Vol = \text{à l’heure}) = 0.6`
* :math:`P(Vol = \text{retardé}) = 0.3`
* :math:`P(Vol = \text{annulé}) = 0.1`

Pour interpréter la distribution de probabilité avec des mots, cela signifie
qu’il y a 60 % de chances que le vol soit à l’heure, 30 % de chances qu’il soit
retardé, et 10 % de chances qu’il soit annulé. Notez que, comme montré
précédemment, la somme des probabilités de tous les résultats possibles vaut 1.

Une distribution de probabilité peut être représentée plus succinctement sous
forme de vecteur. Par exemple, :math:`P (Vol) = <0.6, 0.3, 0.1>`. Pour que cette
notation soit interprétable, les valeurs possèdent un ordre défini (dans notre
cas, *à l’heure, retardé, annulé*).

Indépendance
    L’indépendance est le fait de savoir que la survenue d’un événement
    n’affecte pas la probabilité de l’autre événement. Par exemple, lors du
    lancer de deux dés, le résultat de chaque dé est indépendant de l’autre.
    Lancer un 4 avec le premier dé n’influence pas la valeur du second dé que
    nous lançons. Cela s’oppose aux événements dépendants, comme la présence de
    nuages le matin et de pluie l’après-midi. S’il fait nuageux le matin, il est
    plus probable qu’il pleuve l’après-midi, ces événements sont donc
    dépendants.

    L’indépendance peut être définie mathématiquement : les événements *a* et
    *b* sont indépendants si et seulement si la probabilité de *a* et *b* est
    égale à la probabilité de *a* multipliée par la probabilité de *b* :
    :math:`P(a \land b) = P(a)P(b)`.

****************
 Règle de Bayes
****************

La règle de Bayes est couramment utilisée en théorie des probabilités pour
calculer la probabilité conditionnelle. En mots, la règle de Bayes stipule que
la probabilité de *b* sachant *a* est égale à la probabilité de *a* sachant *b*,
multipliée par la probabilité de *b*, divisée par la probabilité de *a*.

.. figure:: /assets/figures/bayesrule.png

Par exemple, nous aimerions calculer la probabilité qu’il pleuve l’après-midi
s’il y a des nuages le matin, ou :math:`P(pluie | nuages)`. Nous commençons avec
les informations suivantes :

* 80 % des après-midis pluvieux commencent par des matinées nuageuses, ou
    :math:`P(nuages | pluie)`.
* 40 % des jours ont des matinées nuageuses, ou :math:`P(nuages)`.
* 10 % des jours ont des après-midis pluvieux, ou :math:`P(pluie)`.

En appliquant la règle de Bayes, nous calculons :math:`(0.1)(0.8)/(0.4) = 0.2`.
C’est-à-dire que la probabilité qu’il pleuve l’après-midi sachant qu’il faisait
nuageux le matin est de 20 %.

Connaître :math:`P(a|b)`, en plus de :math:`P(a)` et :math:`P(b)`, nous permet
de calculer :math:`P(b | a)`. C’est utile, car connaître la probabilité
conditionnelle d’un effet visible sachant une cause inconnue,
:math:`P(\text{effet visible} | \text{cause inconnue})`, nous permet de calculer
la probabilité de la cause inconnue sachant l’effet visible,
:math:`P(\text{cause inconnue} | \text{effet visible})`. Par exemple, nous
pouvons apprendre :math:`P(\text{résultats de test médical} | \text{maladie})`
grâce à des essais cliniques, où nous testons des personnes atteintes de la
maladie et observons à quelle fréquence le test la détecte. En sachant cela,
nous pouvons calculer :math:`P(\text{maladie} | \text{résultats de test médical}
)`, ce qui représente une information de diagnostic précieuse.

***********************
 Probabilité conjointe
***********************

La probabilité conjointe est la vraisemblance que de multiples événements se
produisent tous ensemble.

Considérons l’exemple suivant, concernant les probabilités de nuages le matin et
de pluie l’après-midi.

================= =======================
:math:`C = nuage` :math:`C = \lnot nuage`
================= =======================
0.4               0.6
:math:`R = pluie` :math:`R = \lnot pluie`
—                 —
0.1               0.9
================= =======================

En examinant ces données, nous ne pouvons pas dire si les nuages matinaux sont
liés à la probabilité de pluie l’après-midi. Pour ce faire, nous devons examiner
les probabilités conjointes de tous les résultats possibles des deux variables.
Nous pouvons représenter cela dans un tableau de la manière suivante :

======================= =======================
:math:`R = *pluie*`     :math:`R = \lnot pluie`
======================= =======================
:math:`C = nuage`       0.08
:math:`C = \lnot nuage` 0.02
======================= =======================

Maintenant, nous sommes en mesure de connaître les informations sur la
co-occurrence des événements. Par exemple, nous savons que la probabilité qu’un
jour donné ait des nuages le matin et de la pluie l’après-midi est de 0.08. La
probabilité qu’il n’y ait pas de nuages le matin ni de pluie l’après-midi est de
0.58.

À l’aide des probabilités conjointes, nous pouvons déduire la probabilité
conditionnelle. Par exemple, si nous nous intéressons à la distribution de
probabilité des nuages le matin sachant qu’il pleut l’après-midi. :math:`P(C |
pluie) = \frac{P(C, pluie)}{P(pluie)}` (une remarque en passant : en
probabilité, les virgules et :math:`\land` s’utilisent de manière
interchangeable). Ainsi, :math:`P(C, pluie) = P(C \land pluie)`). En mots, nous
divisons la probabilité conjointe de pluie et de nuages par la probabilité de
pluie.

Dans la dernière équation, il est possible de considérer :math:`P(pluie)` comme
une constante par laquelle :math:`P(C, pluie)` est multipliée. Ainsi, nous
pouvons réécrire :math:`\frac{P(C, pluie)}{P(pluie)}= \alpha P(C, pluie)`, ou
:math:`\alpha <0.08, 0.02>`. Factoriser :math:`\alpha` nous laisse avec les
proportions des probabilités des valeurs possibles de C sachant qu’il pleut
l’après-midi. À savoir, s’il pleut l’après-midi, la proportion des probabilités
de présence de nuages le matin et d’absence de nuages le matin est de 0.08:0.02.
Notez que 0.08 et 0.02 ne s’additionnent pas pour donner 1 ; cependant,
puisqu’il s’agit de la distribution de probabilité pour la variable aléatoire C,
nous savons qu’ils devraient s’additionner pour donner 1. Par conséquent, nous
devons normaliser les valeurs en calculant α tel que :math:`\alpha 0.08 + \alpha
0.02 = 1`. Finalement, nous pouvons dire que :math:`P(C | pluie) = <0.8, 0.2>`.

*************************
 Règles des probabilités
*************************

Négation
    Cela découle du fait que la somme des probabilités de tous les mondes
    possibles est de 1, et que les littéraux complémentaires *a* et :math:`\lnot
    a` incluent tous les mondes possibles.

Inclusion-Exclusion
    Cela peut être interprété de la manière suivante : les mondes dans lesquels
    *a* ou *b* sont vrais sont égaux à tous les mondes où *a* est vrai, plus les
    mondes où *b* est vrai. Cependant, dans ce cas, certains mondes sont comptés
    deux fois (les mondes où à la fois *a* et *b* sont vrais). Pour nous
    débarrasser de ce chevauchement, nous soustrayons une fois les mondes où *a*
    et *b* sont vrais en même temps (puisqu’ils ont été comptés deux fois).

        Voici un exemple extérieur au cours qui peut clarifier cela. Supposons
        que je mange de la glace 80 % des jours et des biscuits 70 % des jours.
        Si nous calculons la probabilité qu’aujourd’hui je mange de la glace ou
        des biscuits :math:`P(\text{glace} \lor \text{biscuits})` sans
        soustraire :math:`P(\text{glace} \land \text{biscuits})`, nous nous
        retrouvons à tort avec :math:`0.7 + 0.8 = 1.5`. Cela contredit l’axiome
        selon lequel la probabilité est comprise entre 0 et 1. Pour corriger le
        double comptage des jours où j’ai mangé à la fois de la glace et des
        biscuits, nous devons soustraire :math:`P(\text{glace} \land
        \text{biscuits})` une seule fois.

Marginalisation
    L’idée ici est que *b* et :math:`\lnot b` sont des probabilités disjointes.
    C’est-à-dire que la probabilité que *b* et :math:`\lnot b` se produisent en
    même temps est 0. Nous savons également que *b* et :math:`\lnot b`
    s’additionnent pour donner 1. Ainsi, lorsque *a* se produit, *b* peut soit
    se produire, soit ne pas se produire. Lorsque nous prenons la probabilité
    que *a* et *b* se produisent en plus de la probabilité de *a* et
    :math:`\lnot b`, nous nous retrouvons simplement avec la probabilité de *a*.

    La marginalisation peut être exprimée pour les variables aléatoires de la
    manière suivante :

    .. figure:: /assets/figures/marginalization.png

    Le côté gauche de l’équation signifie « La probabilité que la variable
    aléatoire X prenne la valeur :math:`x_i` ». Par exemple, pour la variable C
    que nous avons mentionnée plus tôt, les deux valeurs possibles sont *nuages
    le matin* et *pas de nuages le matin*. La partie droite de l’équation
    correspond à l’idée de la marginalisation. :math:`P(X = x_i)` est égale à la
    somme de toutes les probabilités conjointes de :math:`x_i` et de chaque
    valeur de la variable aléatoire Y. Par exemple, :math:`P(C = \text{nuage}) =
    P(C = \text{nuage}, R = \text{pluie}) + P(C = \text{nuage}, R = \lnot
    \text{pluie}) = 0.08 + 0.32 = 0.4`.

Conditionnement
    Il s’agit d’une idée similaire à la marginalisation. La probabilité que
    l’événement *a* se produise est égale à la probabilité de *a* sachant *b*
    multipliée par la probabilité de *b*, plus la probabilité de *a* sachant
    :math:`\lnot b` multipliée par la probabilité de :math:`\lnot b`.

    .. figure:: /assets/figures/conditioning.png

Dans cette formule, la variable aléatoire X prend la valeur :math:`x_i` avec une
probabilité qui est égale à la somme des probabilités de :math:`x_i` sachant
chaque valeur de la variable aléatoire Y, multipliée par la probabilité que la
variable Y prenne cette valeur. Cela est logique si nous nous rappelons que
:math:`P(a|b) = P(a, b)/P(b)`. Si nous multiplions cette expression par
:math:`P(b)`, nous nous retrouvons avec :math:`P(a, b)`, et à partir de là, nous
faisons la même chose qu’avec la marginalisation.

***************************************
 Réseaux bayésiens (Bayesian Networks)
***************************************

Un réseau bayésien est une structure de données qui représente les dépendances
entre des variables aléatoires. Les réseaux bayésiens possèdent les propriétés
suivantes :

* Ce sont des graphes orientés.
* Chaque nœud sur le graphe représente une variable aléatoire.
* Une flèche de X à Y représente le fait que X est un parent de Y. C’est-à-dire
      que la distribution de probabilité de Y dépend de la valeur de X.
* Chaque nœud X a une distribution de probabilité :math:`P(X | Parents(X))`.

Prenons un exemple de réseau bayésien impliquant des variables qui affectent
notre capacité à arriver à l’heure à notre rendez-vous.

.. figure:: /assets/figures/bayesiannetwork.png

Décrivons ce réseau bayésien de haut en bas :

* La Pluie (*Rain*) est le nœud racine dans ce réseau. Cela signifie que sa
    distribution de probabilité ne dépend d’aucun événement antérieur. Dans
    notre exemple, *Rain* est une variable aléatoire qui peut prendre les
    valeurs {*aucune, légère, forte*} avec la distribution de probabilité
    suivante :

    ======== ======== =======
    *aucune* *légère* *forte*
    ======== ======== =======
    0.7      0.2      0.1
    ======== ======== =======

* La Maintenance (*Maintenance*), dans notre exemple, encode le fait qu’il y ait
    ou non un entretien des voies ferrées, prenant les valeurs {*oui, non*}.
    La Pluie (*Rain*) est un nœud parent de *Maintenance*, ce qui signifie que
    la distribution de probabilité de *Maintenance* est affectée par *Rain*.

    ======== ===== =====
    R        *oui* *non*
    ======== ===== =====
    *aucune* 0.4   0.6
    *légère* 0.2   0.8
    *forte*  0.1   0.9
    ======== ===== =====

* Le Train (*Train*) est la variable qui encode si le train est à l’heure ou
    retardé, prenant les valeurs {*à l’heure, retardé*}. Notez que *Train* a
    des flèches pointant vers lui provenant à la fois de *Maintenance* et de
    *Rain*. Cela signifie que tous deux sont des parents de *Train*, et que
    leurs valeurs affectent la distribution de probabilité de *Train*.

    ======== === =========== =========
    R        M   *à l’heure* *retardé*
    ======== === =========== =========
    *aucune* oui 0.8         0.2
    *aucune* non 0.9         0.1
    *légère* oui 0.6         0.4
    *légère* non 0.7         0.3
    *forte*  oui 0.4         0.6
    *forte*  non 0.5         0.5
    ======== === =========== =========

* Le Rendez-vous (*Appointment*) est une variable aléatoire qui représente le
    fait que nous assistions ou non à notre rendez-vous, prenant les valeurs
    {*présent, raté*}. Notez que son seul parent est *Train*. Ce point sur le
    réseau bayésien est à souligner : les parents n’incluent que les relations
    directes. Il est vrai que l’entretien affecte la ponctualité du train, et
    que la ponctualité du train affecte notre présence au rendez-vous.
    Cependant, au final, ce qui affecte directement nos chances d’assister au
    rendez-vous, c’est de savoir si le train est arrivé à l’heure, et c’est ce
    qui est représenté dans le réseau bayésien. Par exemple, si le train est
    arrivé à l’heure, il a pu y avoir de fortes pluies et un entretien des
    voies, mais cela n’a aucun effet sur le fait que nous soyons arrivés à
    notre rendez-vous.

    =========== ========= ======
    T           *présent* *raté*
    =========== ========= ======
    *à l’heure* 0.9       0.1
    *retardé*   0.6       0.4
    =========== ========= ======

Par exemple, si nous voulons trouver la probabilité de rater la réunion alors
que le train était en retard un jour sans entretien et avec une pluie légère, ou
:math:`P(\text{légère}, \text{non}, \text{retardé}, \text{raté})`, nous
calculerons ce qui suit :

.. math::

    P(\text{légère})P(\text{non} | \text{légère})P(\text{retardé} | \text{légère}, \text{non})P(\text{raté} | \text{retardé})

La valeur de chacune des probabilités individuelles peut être trouvée dans les
distributions de probabilités ci-dessus, puis ces valeurs sont multipliées pour
produire

.. math::

    P(\text{non}, \text{légère}, \text{retardé}, \text{raté})

Inférence
=========

Lors de la dernière leçon, nous avons examiné l’inférence par la conséquence
logique. Cela signifie que nous pouvions définitivement conclure de nouvelles
informations sur la base des informations que nous possédions déjà. Nous pouvons
également déduire de nouvelles informations en nous basant sur les probabilités.
Bien que cela ne nous permette pas de connaître de nouvelles informations avec
certitude, cela nous permet de calculer les distributions de probabilités pour
certaines valeurs. L’inférence a de multiples propriétés.

* Requête **X**\
    distribution de probabilité.
* Variables de preuve **E**\
    pour l’événement **e**. Par exemple, nous pourrions avoir observé qu’il y
    a une pluie légère, et cette observation nous aide à calculer la
    probabilité que le train soit en retard.
* Variables cachées **Y**\
    pas non plus été observées. Par exemple, debout à la gare, nous pouvons
    observer s’il pleut, mais nous ne pouvons pas savoir s’il y a des travaux
    sur la voie plus loin. Ainsi, *Maintenance* serait une variable cachée
    dans cette situation.
* L’objectif
    de probabilité de la variable *Train* (la requête) en fonction de la
    preuve **e** selon laquelle nous savons qu’il y a une pluie légère.

Prenons un exemple. Nous voulons calculer la distribution de probabilité de la
variable *Appointment* (Rendez-vous) compte tenu de la preuve qu’il y a une
pluie légère et aucun entretien des voies. C’est-à-dire, nous savons qu’il y a
une pluie légère et aucun entretien des voies, et nous voulons déterminer
quelles sont les probabilités que nous assistions au rendez-vous et que nous
rations le rendez-vous, :math:`P(Appointment | \text{légère}, non)`. À partir de
la section sur la probabilité conjointe, nous savons que nous pouvons exprimer
les valeurs possibles de la variable aléatoire *Appointment* sous la forme d’une
proportion, en réécrivant :math:`P(Appointment | \text{légère}, non)` en tant
que :math:`\alpha P(Appointment, \text{légère}, non)`. Comment pouvons-nous
calculer la distribution de probabilité de *Appointment* si son parent est
uniquement la variable *Train*, et non *Rain* ou *Maintenance* ? Ici, nous
utiliserons la marginalisation. La valeur de :math:`P(Appointment,
\text{légère}, non)` est égale à

.. math::

    \alpha (P(Appointment, \text{légère}, \text{non}, \text{retardé}) + P(Appointment, \text{légère}, \text{non}, \text{à l’heure}))

Inférence par énumération
=========================

L’inférence par énumération est un processus permettant de trouver la
distribution de probabilité de la variable X sachant la preuve observée e et
certaines variables cachées Y.

.. figure:: /assets/figures/inferencebyenumeration.png

Dans cette équation, X représente la variable de la requête, e la preuve
observée, y toutes les valeurs des variables cachées, et α normalise le résultat
de telle sorte que nous nous retrouvons avec des probabilités qui s’additionnent
pour faire 1. Pour expliquer l’équation avec des mots, elle signifie que la
distribution de probabilité de X sachant e est égale à une distribution de
probabilité normalisée de X et e. Pour obtenir cette distribution, nous
additionnons la probabilité normalisée de X, e, et y, où y prend à chaque fois
une valeur différente des variables cachées Y.

De multiples bibliothèques existent en Python pour faciliter le processus
d’inférence probabiliste. Nous examinerons la bibliothèque *pomegranate* pour
voir comment les données ci-dessus peuvent être représentées en code.

Tout d’abord, nous créons les nœuds et fournissons une distribution de
probabilité pour chacun d’eux.

.. code-block:: python

    from pomegranate import *

    # Le nœud Pluie (rain) n'a pas de parents
    rain = Node(
        DiscreteDistribution({"none": 0.7, "light": 0.2, "heavy": 0.1}), name="rain"
    )

    # Le nœud Entretien des voies (maintenance) est conditionnel à la pluie
    maintenance = Node(
        ConditionalProbabilityTable(
            [
                ["none", "yes", 0.4],
                ["none", "no", 0.6],
                ["light", "yes", 0.2],
                ["light", "no", 0.8],
                ["heavy", "yes", 0.1],
                ["heavy", "no", 0.9],
            ],
            [rain.distribution],
        ),
        name="maintenance",
    )

    # Le nœud Train (train) est conditionnel à la pluie et à l'entretien
    train = Node(
        ConditionalProbabilityTable(
            [
                ["none", "yes", "on time", 0.8],
                ["none", "yes", "delayed", 0.2],
                ["none", "no", "on time", 0.9],
                ["none", "no", "delayed", 0.1],
                ["light", "yes", "on time", 0.6],
                ["light", "yes", "delayed", 0.4],
                ["light", "no", "on time", 0.7],
                ["light", "no", "delayed", 0.3],
                ["heavy", "yes", "on time", 0.4],
                ["heavy", "yes", "delayed", 0.6],
                ["heavy", "no", "on time", 0.5],
                ["heavy", "no", "delayed", 0.5],
            ],
            [rain.distribution, maintenance.distribution],
        ),
        name="train",
    )

    # Le nœud Rendez-vous (appointment) est conditionnel au train
    appointment = Node(
        ConditionalProbabilityTable(
            [
                ["on time", "attend", 0.9],
                ["on time", "miss", 0.1],
                ["delayed", "attend", 0.6],
                ["delayed", "miss", 0.4],
            ],
            [train.distribution],
        ),
        name="appointment",
    )

Ensuite, nous créons le modèle en ajoutant tous les nœuds puis en décrivant quel
nœud est le parent de quel autre nœud en ajoutant des arêtes entre eux
(rappelez-vous qu’un réseau bayésien est un graphe orienté, constitué de nœuds
avec des flèches entre eux).

.. code-block:: python

    # Créer un réseau bayésien et ajouter des états
    model = BayesianNetwork()
    model.add_states(rain, maintenance, train, appointment)

    # Ajouter des arêtes connectant les nœuds
    model.add_edge(rain, maintenance)
    model.add_edge(rain, train)
    model.add_edge(maintenance, train)
    model.add_edge(train, appointment)

    # Finaliser le modèle
    model.bake()

Maintenant, pour demander la probabilité d’un certain événement, nous exécutons
le modèle avec les valeurs qui nous intéressent. Dans cet exemple, nous voulons
demander quelle est la probabilité qu’il n’y ait pas de pluie, pas d’entretien
des voies, que le train soit à l’heure, et que nous assistions à la réunion.

.. code-block:: python

    # Calculer la probabilité pour une observation donnée
    probability = model.probability([["none", "no", "on time", "attend"]])

    print(probability)

Autrement, nous pourrions utiliser le programme pour fournir des distributions
de probabilités pour toutes les variables compte tenu de certaines preuves
observées. Dans le cas suivant, nous savons que le train a été retardé. Sachant
cette information, nous calculons et imprimons les distributions de probabilités
des variables *Rain*, *Maintenance*, et *Appointment*.

.. code-block:: python

    # Calculer les prédictions en se basant sur la preuve que le train était en retard
    predictions = model.predict_proba({"train": "delayed"})

    # Imprimer les prédictions pour chaque nœud
    for node, prediction in zip(model.states, predictions):
        if isinstance(prediction, str):
            print(f"{node.name}: {prediction}")
        else:
            print(f"{node.name}")
            for value, probability in prediction.parameters[0].items():
                print(f"    {value}: {probability:.4f}")

Le code ci-dessus utilisait l’inférence par énumération. Cependant, cette
méthode de calcul de probabilité est inefficace, surtout lorsqu’il y a de
nombreuses variables dans le modèle. Une façon différente de procéder serait
d’abandonner l’\ **inférence exacte** au profit de l’\ **inférence
approximative**. En faisant cela, nous perdons une certaine précision dans les
probabilités générées, mais souvent cette imprécision est négligeable. En
retour, nous gagnons une méthode de calcul des probabilités qui est évolutive.

*****************
 Échantillonnage
*****************

L’échantillonnage est une technique d’inférence approximative. Dans
l’échantillonnage, chaque variable est échantillonnée pour une valeur selon sa
distribution de probabilité. Nous allons commencer par un exemple extérieur au
cours, puis couvrir l’exemple du cours.

    Pour générer une distribution en utilisant l’échantillonnage avec un dé,
    nous pouvons lancer le dé de multiples fois et noter quelle valeur nous
    avons obtenue à chaque fois. Supposons que nous avons lancé le dé 600 fois.
    Nous comptons combien de fois nous avons obtenu 1, ce qui est censé être
    approximativement 100, et ensuite nous répétons pour le reste des valeurs,
    de 2 à 6. Ensuite, nous divisons chaque compte par le nombre total de
    lancers. Cela va générer une distribution approximative des valeurs du
    lancer d’un dé : d’une part, il est peu probable que nous obtenions le
    résultat où chaque valeur a une probabilité de 1/6 de se produire (ce qui
    est la probabilité exacte), mais nous obtiendrons une valeur qui s’en
    rapproche.

Voici un exemple du cours : si nous commençons par échantillonner la variable
*Rain*, la valeur *aucune* sera générée avec une probabilité de 0.7, la valeur
*légère* sera générée avec une probabilité de 0.2, et la valeur *forte* sera
générée avec une probabilité de 0.1. Supposons que la valeur échantillonnée que
nous obtenons soit *aucune*. Lorsque nous arrivons à la variable *Maintenance*,
nous l’échantillonnons également, mais uniquement à partir de la distribution de
probabilité où *Rain* est égale à *aucune*, car c’est un résultat déjà
échantillonné. Nous continuerons à faire ainsi à travers tous les nœuds. Nous
avons maintenant un échantillon, et répéter ce processus de multiples fois
génère une distribution. Maintenant, si nous voulons répondre à une question,
telle que quelle est P(*Train = à l’heure*), nous pouvons compter le nombre
d’échantillons où la variable *Train* possède la valeur *à l’heure*, et diviser
le résultat par le nombre total d’échantillons. De cette manière, nous venons de
générer une probabilité approximative pour P(*Train = à l’heure*).

Nous pouvons également répondre à des questions qui impliquent une probabilité
conditionnelle, comme :math:`P(Rain = \text{légère} | Train = \text{à
l’heure})`. Dans ce cas, nous ignorons tous les échantillons où la valeur de
*Train* n’est pas *à l’heure*, et ensuite nous procédons comme avant. Nous
comptons combien d’échantillons ont la variable *Rain* = *légère* parmi les
échantillons qui ont *Train* = *à l’heure*, puis nous divisons par le nombre
total d’échantillons où *Train* = *à l’heure*.

Dans le code, une fonction d’échantillonnage peut ressembler à
``generate_sample`` :

.. code-block:: python

    import pomegranate

    from collections import Counter

    from model import model


    def generate_sample():

        # Correspondance (Mapping) du nom de la variable aléatoire à l'échantillon généré
        sample = {}

        # Correspondance de la distribution à l'échantillon généré
        parents = {}

        # Boucle sur tous les états, en supposant un ordre topologique
        for state in model.states:
            # Si nous avons un nœud non-racine, échantillonner conditionnellement aux parents
            if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
                sample[state.name] = state.distribution.sample(parent_values=parents)

            # Sinon, échantillonner simplement à partir de la distribution seule
            else:
                sample[state.name] = state.distribution.sample()

            # Garder la trace de la valeur échantillonnée dans la correspondance des parents
            parents[state.distribution] = sample[state.name]

        # Retourner l'échantillon généré
        return sample

Maintenant, pour calculer :math:`P(Appointment | Train = \text{retardé})`, qui
est la distribution de probabilité de la variable *Appointment* sachant que le
train est en retard, nous faisons ce qui suit :

.. code-block:: python

    # Échantillonnage par rejet (Rejection sampling)
    # Calculer la distribution d'Appointment sachant que le train est retardé
    N = 10000
    data = []

    # Répéter l'échantillonnage 10 000 fois
    for i in range(N):
        # Générer un échantillon basé sur la fonction que nous avons définie précédemment
        sample = generate_sample()

        # Si, dans cet échantillon, la variable Train a la valeur "retardé", sauvegarder l'échantillon. Puisque nous nous intéressons à la distribution de probabilité de Appointment sachant que le train est en retard, nous écartons l'échantillon où le train était à l'heure.
        if sample["train"] == "delayed":
            data.append(sample["appointment"])

    # Compter combien de fois chaque valeur de la variable est apparue. Nous pourrons plus tard normaliser en divisant les résultats par le nombre total d'échantillons sauvegardés pour obtenir les probabilités approximatives de la variable qui s'additionnent à 1.
    print(Counter(data))

**Pondération par vraisemblance**

Dans l’exemple d’échantillonnage ci-dessus, nous avons écarté les échantillons
qui ne correspondaient pas à la preuve que nous avions. Cela est inefficace. Une
façon de contourner cela est la pondération par vraisemblance, en utilisant les
étapes suivantes :

* Commencez par fixer les valeurs pour les variables de preuve.

* Échantillonnez les variables qui ne sont pas des preuves en utilisant des
    probabilités conditionnelles dans le réseau bayésien.

* Pondérez chaque échantillon par sa **vraisemblance**\
    toutes les preuves se produisent.

Par exemple, si nous avons l’observation que le train était à l’heure, nous
commencerons l’échantillonnage comme avant. Nous échantillonnons une valeur de
*Rain* sachant sa distribution de probabilité, puis de *Maintenance*, mais
lorsque nous arrivons à *Train* - nous lui donnons toujours la valeur observée,
dans notre cas, *à l’heure*. Ensuite, nous procédons et échantillonnons
*Appointment* en fonction de sa distribution de probabilité sachant *Train* = *à
l’heure*. Maintenant que cet échantillon existe, nous le pondérons par la
probabilité conditionnelle de la variable observée sachant ses parents
échantillonnés. C’est-à-dire, si nous avons échantillonné *Rain* et obtenu
*légère*, et que nous avons ensuite échantillonné *Maintenance* et obtenu *oui*,
alors nous pondérerons cet échantillon par :math:`P(Train = \text{à l’heure} |
\text{légère}, \text{oui})`.

*******************
 Modèles de Markov
*******************

Jusqu’à présent, nous avons examiné les questions de probabilité compte tenu de
certaines informations que nous avions observées. Dans ce type de paradigme, la
dimension du temps n’est représentée d’aucune façon. Cependant, de nombreuses
tâches s’appuient sur la dimension temporelle, comme la prédiction. Pour
représenter la variable de temps, nous allons créer une nouvelle variable, X, et
la changer en fonction de l’événement d’intérêt, de telle sorte que Xₜ soit
l’événement actuel, Xₜ₊₁ soit l’événement suivant, et ainsi de suite. Pour être
capable de prédire des événements dans le futur, nous utiliserons des Modèles de
Markov.

L’hypothèse de Markov
    L’hypothèse de Markov est l’hypothèse selon laquelle l’état actuel ne dépend
    que d’un nombre fini et fixe d’états précédents. C’est important pour nous.
    Pensez à la tâche consistant à prédire la météo. En théorie, nous pourrions
    utiliser toutes les données de l’année passée pour prédire la météo de
    demain. Cependant, c’est irréalisable, à la fois en raison de la puissance
    de calcul que cela nécessiterait et parce qu’il n’y a probablement aucune
    information sur la probabilité conditionnelle de la météo de demain basée
    sur la météo d’il y a 365 jours. En utilisant l’hypothèse de Markov, nous
    restreignons nos états précédents (par exemple, combien de jours précédents
    nous allons prendre en compte pour prédire la météo de demain), rendant
    ainsi la tâche gérable. Cela signifie que nous pourrions obtenir une
    approximation plus grossière des probabilités d’intérêt, mais cela est
    souvent suffisant pour nos besoins. De plus, nous pouvons utiliser un modèle
    de Markov basé sur les informations du tout dernier événement (par exemple,
    prédire la météo de demain en se basant sur la météo d’aujourd’hui).

Chaîne de Markov
    Une chaîne de Markov est une séquence de variables aléatoires où la
    distribution de chaque variable suit l’hypothèse de Markov. C’est-à-dire que
    chaque événement dans la chaîne se produit sur la base de la probabilité de
    l’événement qui le précède.

Pour commencer à construire une chaîne de Markov, nous avons besoin d’un
**modèle de transition** qui spécifiera les distributions de probabilités du
prochain événement sur la base des valeurs possibles de l’événement actuel.

.. figure:: /assets/figures/transitionmodel.png

Dans cet exemple, la probabilité que demain soit ensoleillé sachant
qu’aujourd’hui est ensoleillé est de 0.8. C’est raisonnable, car il est plus
probable qu’un jour ensoleillé suive un jour ensoleillé. Cependant, s’il pleut
aujourd’hui, la probabilité de pluie demain est de 0.7, puisque les jours de
pluie sont plus susceptibles de se suivre. En utilisant ce modèle de transition,
il est possible d’échantillonner une chaîne de Markov. Commencez par un jour
étant soit pluvieux, soit ensoleillé, puis échantillonnez le jour suivant sur la
base de la probabilité qu’il soit ensoleillé ou pluvieux compte tenu de la météo
d’aujourd’hui. Ensuite, conditionnez la probabilité d’après-demain en vous
basant sur demain, et ainsi de suite, ce qui donne une chaîne de Markov :

.. figure:: /assets/figures/markovchain.png

Étant donné cette chaîne de Markov, nous pouvons maintenant répondre à des
questions telles que « quelle est la probabilité d’avoir quatre jours de pluie
d’affilée ? ». Voici un exemple de la façon dont une chaîne de Markov peut être
implémentée en code :

.. code-block:: python

    from pomegranate import *

    # Définir les probabilités de départ
    start = DiscreteDistribution({"sun": 0.5, "rain": 0.5})

    # Définir le modèle de transition
    transitions = ConditionalProbabilityTable(
        [
            ["sun", "sun", 0.8],
            ["sun", "rain", 0.2],
            ["rain", "sun", 0.3],
            ["rain", "rain", 0.7],
        ],
        [start],
    )

    # Créer la chaîne de Markov
    model = MarkovChain([start, transitions])

    # Échantillonner 50 états depuis la chaîne
    print(model.sample(50))

**************************
 Modèles de Markov cachés
**************************

Un modèle de Markov caché est un type de modèle de Markov pour un système doté
d’états cachés qui génèrent certains événements observés. Cela signifie que
parfois, l’IA dispose d’une certaine mesure du monde mais n’a pas d’accès à
l’état précis du monde. Dans ces cas, l’état du monde est appelé l’\ **état
caché** et quelles que soient les données auxquelles l’IA a accès, ce sont les
**observations**. Voici quelques exemples de ceci :

* Pour un robot explorant un territoire inexploré, l’état caché est sa position,
    et l’observation correspond aux données enregistrées par les capteurs du
    robot.

* Dans la reconnaissance vocale, l’état caché correspond aux mots qui ont été
    prononcés, et l’observation correspond aux formes d’ondes audio.

* Lors de la mesure de l’engagement des utilisateurs sur les sites Web, l’état
    caché est le degré d’engagement de l’utilisateur, et l’observation
    correspond aux analyses (analytics) du site Web ou de l’application.

Pour notre discussion, nous utiliserons l’exemple suivant. Notre IA veut déduire
la météo (l’état caché), mais elle n’a accès qu’à une caméra intérieure qui
enregistre combien de personnes ont apporté un parapluie avec elles. Voici notre
**modèle de capteur** (également appelé **modèle d’émission**) qui représente
ces probabilités :

.. figure:: /assets/figures/sensormodel.png

Dans ce modèle, s’il fait soleil, il est plus probable que les gens n’apportent
pas de parapluie dans le bâtiment. S’il pleut, alors il est très probable que
les gens apportent des parapluies dans le bâtiment. En utilisant l’observation
permettant de savoir si les gens ont apporté un parapluie ou non, nous pouvons
prédire avec une vraisemblance raisonnable la météo qu’il fait à l’extérieur.

Hypothèse du capteur de Markov
    C’est l’hypothèse selon laquelle la variable de preuve ne dépend que de
    l’état correspondant. Par exemple, pour nos modèles, nous supposons que le
    fait que les gens apportent des parapluies au bureau dépend uniquement de la
    météo. Ce n’est pas nécessairement représentatif de la vérité absolue, car,
    par exemple, des personnes plus consciencieuses et réfractaires à la pluie
    pourraient emporter un parapluie partout avec elles même quand il fait
    soleil, et si nous connaissions la personnalité de tout le monde, cela
    ajouterait plus de données au modèle. Cependant, l’hypothèse du capteur de
    Markov ignore ces données, en supposant que seul l’état caché affecte
    l’observation.

Un modèle de Markov caché peut être représenté dans une chaîne de Markov avec
deux couches. La couche supérieure, la variable X, représente l’état caché. La
couche inférieure, la variable E, représente la preuve, les observations que
nous avons.

.. figure:: /assets/figures/hiddenmarkovchain.png

En s’appuyant sur des modèles de Markov cachés, de multiples tâches peuvent être
réalisées :

* Filtrage
    aujourd’hui, calculer la distribution de probabilité pour l’état actuel.
    Par exemple, compte tenu des informations sur les moments où les gens
    apportent des parapluies depuis le début des temps jusqu’à aujourd’hui,
    nous générons une distribution de probabilité quant à savoir s’il pleut
    aujourd’hui ou non.

* Prédiction
    calculer la distribution de probabilité pour un état futur.

* Lissage
    maintenant, calculer la distribution de probabilité pour un état passé.
    Par exemple, calculer la probabilité de pluie d’hier sachant que les gens
    ont apporté des parapluies aujourd’hui.

* L’explication la plus probable
    observations du début jusqu’à maintenant, calculer la séquence
    d’événements la plus probable.

La tâche de l’explication la plus probable peut être utilisée dans des processus
tels que la reconnaissance vocale, où, sur la base de multiples formes d’ondes,
l’IA déduit la séquence de mots ou de syllabes la plus probable qui a conduit à
ces formes d’ondes. Voici ensuite une implémentation Python d’un modèle de
Markov caché que nous allons utiliser pour une tâche d’explication la plus
probable :

.. code-block:: python

    from pomegranate import *

    # Modèle d'observation pour chaque état
    sun = DiscreteDistribution({"umbrella": 0.2, "no umbrella": 0.8})

    rain = DiscreteDistribution({"umbrella": 0.9, "no umbrella": 0.1})

    states = [sun, rain]

    # Modèle de transition
    transitions = numpy.array(
        [
            [0.8, 0.2],  # Prédictions de demain si aujourd'hui = soleil (sun)
            [0.3, 0.7],
        ]  # Prédictions de demain si aujourd'hui = pluie (rain)
    )

    # Probabilités de départ
    starts = numpy.array([0.5, 0.5])

    # Créer le modèle
    model = HiddenMarkovModel.from_matrix(
        transitions, states, starts, state_names=["sun", "rain"]
    )
    model.bake()

Notez que notre modèle possède à la fois le modèle de capteur et le modèle de
transition. Nous avons besoin des deux pour le modèle de Markov caché. Dans
l’extrait de code suivant, nous voyons une séquence d’observations concernant le
fait que les gens aient apporté ou non des parapluies au bâtiment, et sur la
base de cette séquence, nous exécuterons le modèle, qui générera et affichera
l’explication la plus probable (c’est-à-dire la séquence météorologique qui a le
plus vraisemblablement conduit à ce schéma d’observations) :

.. code-block:: python

    from model import model

    # Données observées
    observations = [
        "umbrella",
        "umbrella",
        "no umbrella",
        "umbrella",
        "umbrella",
        "umbrella",
        "umbrella",
        "no umbrella",
        "no umbrella",
    ]

    # Prédire les états sous-jacents
    predictions = model.predict(observations)
    for prediction in predictions:
        print(model.states[prediction].name)

Dans ce cas, la sortie du programme sera pluie, pluie, soleil, pluie, pluie,
pluie, pluie, soleil, soleil. Cette sortie représente quel est le schéma
météorologique le plus probable compte tenu de nos observations de personnes
apportant ou n’apportant pas de parapluies dans le bâtiment.

====================================
Exercices : Chapitre 3 - Incertitude
====================================

***********
 Exercices
***********

.. :ia2:exercice:: 30.1
    Modélisation probabiliste en notation :math:`P(A)`

    Un système d'intelligence artificielle supervise une salle de classe intelligente afin d'optimiser l'apprentissage. On définit les événements suivants pour un étudiant donné à un moment précis :

    * :math:`P` : L'étudiant est présent en classe.
    * :math:`E` : L'étudiant est éveillé et attentif.
    * :math:`X` : C'est un jour d’examen.
    * :math:`D` : L'étudiant a remis son devoir.

    Modélisez les affirmations suivantes à l'aide de la notation formelle des probabilités (probabilités inconditionnelles ou conditionnelles) :

    a. La probabilité qu'un étudiant soit présent et éveillé.
    b. La probabilité qu'un étudiant soit présent sachant que c'est un jour d'examen.
    c. La probabilité qu'un étudiant ne soit pas éveillé sachant qu'il est présent et que ce n'est pas un jour d'examen.
    d. La probabilité qu'un étudiant ait remis son devoir sachant qu'il est présent et éveillé.
    e. Exprimez en langage naturel la signification de la notation :math:`P(X \mid \lnot P)`.

    Solution: :ia2:sol:`30.1`

.. :ia2:exercice:: 30.2
    Indépendance et dépendance d'événements

    Pour chacune des situations contextuelles suivantes, déterminez si les deux événements :math:`A` et :math:`B` sont **indépendants** ou **dépendants**. Justifiez brièvement votre réponse en vous appuyant sur la définition de l'indépendance probabiliste (:math:`P(A \land B) = P(A)P(B)` ou :math:`P(A \mid B) = P(A)`).

    a. **Situation 1 :** :math:`A` = Obtenir un 6 lors du lancer d'un dé équilibré ; :math:`B` = Obtenir « Pile » lors du lancer d'une pièce de monnaie.
    b. **Situation 2 :** :math:`A` = Il tombe 30 cm de neige à Québec ce matin ; :math:`B` = Le cours en présentiel au collège est annulé ou retardé.
    c. **Situation 3 :** :math:`A` = Tirer un As dans un jeu de 52 cartes sans remise ; :math:`B` = Tirer un second As au deuxième tirage.
    d. **Situation 4 :** :math:`A` = Un étudiant étudie 15 heures pour son examen d'IA ; :math:`B` = L'étudiant obtient une note supérieure à 90 %.

    Solution: :ia2:sol:`30.2`

.. :ia2:exercice:: 30.3
    Probabilité conditionnelle et Règle de Bayes

    Un serveur de plateforme Cloud est surveillé par une IA de diagnostic. On étudie la survenue de pannes de serveur (:math:`C`) et de pics d'utilisation du CPU (:math:`U`) :

    * La probabilité a priori qu'un serveur subisse une panne est :math:`P(C) = 0.02`.
    * La probabilité a priori d'observer un pic de CPU est :math:`P(U) = 0.15`.
    * Lorsqu'une panne se produit, un pic de CPU est observé dans 90 % des cas, soit :math:`P(U \mid C) = 0.90`.

    a. Calculez la probabilité conditionnelle qu'une panne soit en cours sachant qu'un pic de CPU est détecté, soit :math:`P(C \mid U)`, en utilisant la **règle de Bayes**.
    b. Si la probabilité globale d'un pic de CPU :math:`P(U)` augmente à :math:`0.30` sans changer :math:`P(C)` ni :math:`P(U \mid C)`, quel est le nouvel impact sur la certitude du diagnostic :math:`P(C \mid U)` ? Expliquez intuitivement ce résultat.

    Solution: :ia2:sol:`30.3`

.. :ia2:exercice:: 30.4
    Réseaux bayésiens et probabilité conjointe

    Soit un réseau bayésien simple modélisant les facteurs d'un trajet. Le réseau est composé des variables aléatoires booléennes suivantes :

    * :math:`P` : Pluie fine (Variables parents : Aucune)
    * :math:`T` : Travaux routiers (Dépend de :math:`P`)
    * :math:`R` : Retard à la réunion (Dépend de :math:`P` et :math:`T`)

    Les tables de probabilités conditionnelles (CPT) sont fournies comme suit :

    * :math:`P(P = \text{vrai}) = 0.30`
    * :math:`P(T = \text{vrai} \mid P = \text{vrai}) = 0.60` ; :math:`P(T = \text{vrai} \mid P = \text{faux}) = 0.20`
    * :math:`P(R = \text{vrai} \mid P = \text{vrai}, T = \text{vrai}) = 0.90`
    * :math:`P(R = \text{vrai} \mid P = \text{vrai}, T = \text{faux}) = 0.50`
    * :math:`P(R = \text{vrai} \mid P = \text{faux}, T = \text{vrai}) = 0.70`
    * :math:`P(R = \text{vrai} \mid P = \text{faux}, T = \text{faux}) = 0.10`

    a. Calculez la **probabilité conjointe** exacte de l'événement où il pleut, il y a des travaux et l'intervenant est en retard, soit :math:`P(P = \text{vrai}, T = \text{vrai}, R = \text{vrai})`.
    b. En utilisant la **marginalisation**, calculez la probabilité globale qu'il y ait des travaux :math:`P(T = \text{vrai})`.

    Solution: :ia2:sol:`30.4`

.. :ia2:exercice:: 30.5
    Modèles de Markov et Modèles de Markov Cachés (HMM)

    Un robot mobile évolue dans une pièce et tente de déterminer la météo extérieure à travers les indices d'un capteur de luminosité :

    * **États cachés (:math:`X_t`) :** Météo à l'instant :math:`t` (:math:`\text{Soleil}` ou :math:`\text{Pluie}`).
    * **Modèle de transition :** :math:`P(X_{t+1} = \text{Soleil} \mid X_t = \text{Soleil}) = 0.80`, :math:`P(X_{t+1} = \text{Pluie} \mid X_t = \text{Pluie}) = 0.70`.
    * **Modèle de capteur (Émission) :** :math:`P(E_t = \text{Lumière forte} \mid X_t = \text{Soleil}) = 0.90`, :math:`P(E_t = \text{Lumière forte} \mid X_t = \text{Pluie}) = 0.10`.

    a. Si l'état initial à :math:`t=0` est certain d'être :math:`X_0 = \text{Soleil}`, calculez la distribution de probabilité pour l'état à :math:`t=1`, soit :math:`P(X_1)`.
    b. Sachant que l'observation à :math:`t=1` est :math:`E_1 = \text{Lumière forte}`, calculez la probabilité filtrée :math:`P(X_1 = \text{Soleil} \mid E_1 = \text{Lumière forte})` en appliquant la formule du conditionnement et en normalisant le résultat.
    c. Expliquez brièvement la différence entre les tâches de **filtrage**, de **prédiction** et de **lissage** dans un Modèle de Markov Caché.

    Solution: :ia2:sol:`30.5`


**********
 Solutons
**********

.. ia2:solution:: 30.1
    Modélisation probabiliste en notation :math:`P(A)`

    Solution de :ia2:ex:`30.1`

    a. **Présent et éveillé :**
       :math:`P(P \land E)` (ou :math:`P(P, E)`).

    b. **Présent sachant que c'est un jour d'examen :**
       :math:`P(P \mid X)`.

    c. **Pas éveillé sachant qu'il est présent et que ce n'est pas un jour d'examen :**
       :math:`P(\lnot E \mid P \land \lnot X)`.

    d. **Remis son devoir sachant qu'il est présent et éveillé :**
       :math:`P(D \mid P \land E)`.

    e. **Signification de :math:`P(X \mid \lnot P)` :**
       C'est la probabilité que ce soit un jour d'examen sachant que l'étudiant est absent (non présent).

.. ia2:solution:: 30.2
    Indépendance et dépendance d'événements

    Solution de :ia2:ex:`30.2`

    a. **Situation 1 : Événements INDÉPENDANTS.**
       Le résultat du dé n'a aucun impact physique ni logique sur le lancer de la pièce (:math:`P(A \land B) = P(A) \cdot P(B) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}`).

    b. **Situation 2 : Événements DÉPENDANTS.**
       Une forte chute de neige augmente considérablement la probabilité que les cours soient annulés (:math:`P(B \mid A) > P(B)`).

    c. **Situation 3 : Événements DÉPENDANTS.**
       Puisqu'il n'y a pas de remise, le premier tirage modifie la composition du paquet pour le second tirage. La probabilité d'obtenir un As au second tirage dépend directement du fait d'en avoir tiré un au premier (:math:`P(B \mid A) = \frac{3}{51} \neq P(B \mid \lnot A) = \frac{4}{51}`).

    d. **Situation 4 : Événements DÉPENDANTS.**
       Le temps d'étude influence la maîtrise du sujet et augmente la probabilité de réussir l'examen (:math:`P(B \mid A) > P(B)`).

.. ia2:solution:: 30.3
    Probabilité conditionnelle et Règle de Bayes

    Solution de :ia2:ex:`30.3`

    a. **Calcul de :math:`P(C \mid U)` par la règle de Bayes :**

       Selon la règle de Bayes :

       .. math::

          P(C \mid U) = \frac{P(U \mid C) \cdot P(C)}{P(U)}

       En substituant les valeurs :

       .. math::

          P(C \mid U) = \frac{0.90 \cdot 0.02}{0.15} = \frac{0.018}{0.15} = 0.12

       La probabilité qu'il y ait une panne sachant qu'un pic de CPU est détecté est de **12 %**.

    b. **Impact d'une augmentation de :math:`P(U)` à 0.30 :**

       .. math::

          P(C \mid U) = \frac{0.90 \cdot 0.02}{0.30} = \frac{0.018}{0.30} = 0.06 \quad (6 \%)

       *Explication intuitive :* Si les pics de CPU deviennent très fréquents de manière générale (ex. charges de travail ordinaires élevées), l'observation d'un pic de CPU devient un indicateur moins spécifique d'une panne réelle (augmentation des faux positifs).

.. ia2:solution:: 30.4
    Réseaux bayésiens et probabilité conjointe

    Solution de :ia2:ex:`30.4`

    a. **Calcul de la probabilité conjointe :**

       D'après la propriété de décomposition d'un réseau bayésien :

       .. math::

          P(P, T, R) = P(P) \cdot P(T \mid P) \cdot P(R \mid P, T)

       Pour :math:`P = \text{vrai}, T = \text{vrai}, R = \text{vrai}` :

       .. math::

          P(P=\text{vrai}, T=\text{vrai}, R=\text{vrai}) = 0.30 \cdot 0.60 \cdot 0.90 = 0.162 \quad (16.2 \%)

    b. **Calcul de :math:`P(T = \text{vrai})` par marginalisation :**

       Par marginalisation sur la variable parent :math:`P` :

       .. math::

          P(T=\text{vrai}) = P(T=\text{vrai} \mid P=\text{vrai}) \cdot P(P=\text{vrai}) + P(T=\text{vrai} \mid P=\text{faux}) \cdot P(P=\text{faux})

       Sachant que :math:`P(P=\text{faux}) = 1 - 0.30 = 0.70` :

       .. math::

          P(T=\text{vrai}) = (0.60 \cdot 0.30) + (0.20 \cdot 0.70) = 0.18 + 0.14 = 0.32 \quad (32 \%)

.. ia2:solution:: 30.5
    Modèles de Markov et Modèles de Markov Cachés (HMM)

    Solution de :ia2:ex:`30.5`

    a. **Distribution de probabilité à :math:`t=1` (:math:`P(X_1)`) :**

       Sachant :math:`X_0 = \text{Soleil}` :

       * :math:`P(X_1 = \text{Soleil}) = P(X_1 = \text{Soleil} \mid X_0 = \text{Soleil}) = 0.80`
       * :math:`P(X_1 = \text{Pluie}) = P(X_1 = \text{Pluie} \mid X_0 = \text{Soleil}) = 1 - 0.80 = 0.20`

       Donc, :math:`P(X_1) = \langle 0.80, 0.20 \rangle`.

    b. **Probabilité filtrée :math:`P(X_1 \mid E_1 = \text{Lumière forte})` :**

       On applique le théorème de Bayes / la formule du conditionnement avec le facteur de normalisation :math:`\alpha` :

       .. math::

          P(X_1 \mid E_1) = \alpha \cdot P(E_1 \mid X_1) \cdot P(X_1)

       * Pour :math:`X_1 = \text{Soleil}` : :math:`0.90 \cdot 0.80 = 0.72`
       * Pour :math:`X_1 = \text{Pluie}` : :math:`0.10 \cdot 0.20 = 0.02`

       Normalisation (:math:`\alpha = \frac{1}{0.72 + 0.02} = \frac{1}{0.74}`) :

       * :math:`P(X_1 = \text{Soleil} \mid E_1) = \frac{0.72}{0.74} \approx 0.973 \quad (97.3 \%)`
       * :math:`P(X_1 = \text{Pluie} \mid E_1) = \frac{0.02}{0.74} \approx 0.027 \quad (2.7 \%)`

    c. **Différences entre Filtrage, Prédiction et Lissage :**

       * **Filtrage :** Calculer la distribution de probabilité de l'état *actuel* :math:`X_t` en fonction de toutes les observations reçues jusqu'à présent :math:`E_1, \dots, E_t`.
       * **Prédiction :** Calculer la distribution de probabilité d'un état *futur* :math:`X_{t+k}` (:math:`k > 0`) en fonction des observations jusqu'à aujourd'hui.
       * **Lissage :** Recalculer la distribution de probabilité d'un état *passé* :math:`X_k` (:math:`k < t`) en utilisant l'ensemble des observations passées et ultérieures :math:`E_1, \dots, E_t`.
