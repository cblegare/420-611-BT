###########
 Recherche
###########

Les problèmes de recherche impliquent un agent auquel on donne un état initial
et un état cible, et qui retourne une solution expliquant comment passer du
premier au second. Une application de navigation utilise un processus de
recherche typique, où l’agent (la partie pensante du programme) reçoit en entrée
votre position actuelle et votre destination souhaitée, et, sur la base d’un
algorithme de recherche, retourne une suggestion de chemin. Cependant, il existe
de nombreuses autres formes de problèmes de recherche, comme les casse-têtes ou
les labyrinthes.

.. figure:: /assets/figures/15puzzle.png
    :alt: Un jeu de Taquin complété

    Un jeu de Taquin complété

Trouver une solution à un jeu de taquin (15 puzzle) nécessiterait l’utilisation
d’un algorithme de recherche.

.. index:: recherche; définitions

.. index:: agent, recherche; agent

Agent
    Une entité qui perçoit son environnement et agit sur celui-ci. Dans une
    application de navigation, par exemple, l’agent serait la représentation
    d’une voiture qui doit décider quelles actions entreprendre pour arriver à
    destination.

.. index:: état, recherche; état

État
    Une configuration d’un agent dans son environnement. Par exemple, dans un
    `taquin <https://en.wikipedia.org/wiki/15_puzzle?utm_source=gemini>`__, un
    état correspond à n’importe quelle disposition de tous les nombres sur le
    plateau.

.. index:: action, recherche; action

Actions
    Les choix qui peuvent être faits dans un état. Plus précisément, les actions
    peuvent être définies comme une fonction. En recevant l’état :math:`s` en
    entrée, :math:`Actions(s)` retourne en sortie l’ensemble des actions qui
    peuvent être exécutées dans l’état :math:`s`. Par exemple, dans un *jeu de
    taquin*, les actions d’un état donné sont les façons dont vous pouvez faire
    glisser les carrés dans la configuration actuelle (4 si le carré vide est au
    milieu, 3 s’il est contre un bord, 2 s’il est dans un coin).

.. index:: modèle de transition, recherche; modèle de transition

Modèle de transition
    Une description de l’état qui résulte de l’exécution de toute action
    applicable dans n’importe quel état. Plus précisément, le modèle de
    transition peut être défini comme une fonction. En recevant l’état :math:`s`
    et l’action :math:`a` en entrée, :math:`Results(s, a)` retourne l’état
    résultant de l’exécution de l’action :math:`a` dans l’état :math:`s`. Par
    exemple, étant donné une certaine configuration d’un *taquin* (état
    :math:`s`), déplacer un carré dans n’importe quelle direction (action
    :math:`a`) mènera à une nouvelle configuration du casse-tête (le nouvel
    état).

.. index:: espace d'états, recherche; espace d'états

Espace d’états
    L’ensemble de tous les états atteignables depuis l’état initial par
    n’importe quelle séquence d’actions. Par exemple, dans un taquin de 15,
    l’espace d’états est constitué de toutes les 16!/2 configurations sur le
    plateau qui peuvent être atteintes depuis n’importe quel état initial.
    L’espace d’états peut être visualisé comme un graphe orienté avec des états,
    représentés par des nœuds, et des actions, représentées par des flèches
    entre les nœuds.

.. figure:: /assets/figures/statespace.png
    :alt: Plusieurs états possibles d'un taquin

    Plusieurs états possibles d'un taquin

.. index:: test de but, recherche; test de but

Test de but
    La condition qui détermine si un état donné est un état cible. Par exemple,
    dans une application de navigation, le test de but consisterait à vérifier
    si la position actuelle de l’agent (la représentation de la voiture) se
    trouve à la destination. Si c’est le cas — le problème est résolu. Si ce
    n’est pas le cas — nous continuons la recherche.

.. index:: coût du chemin, recherche; coût du chemin

Coût du chemin
    Un coût numérique associé à un chemin donné. Par exemple, une application de
    navigation ne se contente pas de vous amener à votre but ; elle le fait en
    minimisant le coût du chemin, trouvant ainsi le moyen le plus rapide
    possible pour vous d’atteindre votre état cible.

*************************************
 Résoudre des problèmes de recherche
*************************************

.. index:: noeud, node, recherche; noeud, recherche: node

Dans un processus de recherche, les données sont souvent stockées dans un
**nœud**, une structure de données qui contient les données suivantes :

* Un *état*
* Son *nœud parent*, par lequel le nœud actuel a été généré
* L’\ *action* qui a été appliquée à l’état du parent pour arriver au nœud
  actuel
* Le *coût du chemin* de l’état initial jusqu’à ce nœud

Les *nœuds* contiennent des informations qui les rendent très utiles pour les
algorithmes de recherche. Ils contiennent un *état*, qui peut être vérifié à
l’aide du *test de but* pour voir s’il s’agit de l’état final. Si c’est le cas,
le *coût du chemin* du nœud peut être comparé aux *coûts des chemins* d’autres
nœuds, ce qui permet de choisir la *solution optimale*. Une fois le nœud choisi,
grâce à l’enregistrement du *nœud parent* et de l’\ *action* qui a mené du
*parent* au nœud actuel, il est possible de retracer chaque étape depuis
l’\ *état initial* jusqu’à ce nœud, et cette séquence d’actions constitue la
*solution*.

.. index:: frontière, recherche; frontière

Cependant, les *nœuds* ne sont qu’une simple structure de données — ils ne
cherchent pas, ils stockent des informations. Pour véritablement effectuer une
recherche, nous utilisons la **frontière**, le mécanisme qui « gère » les
*nœuds*. La *frontière* commence par contenir un état initial et un ensemble
vide d’éléments explorés, puis répète les actions suivantes jusqu’à ce qu’une
solution soit trouvée :

Répéter :

    1. Si la frontière est vide,

           * *Arrêt.* Il n’y a pas de solution au problème.

    1. Retirer un nœud de la frontière. C’est le nœud qui sera pris en
       considération.

    1. Si le nœud contient l’état cible,

           * Retourner la solution. *Arrêt*.

           Sinon,

           * Étendre le nœud (trouver tous les nouveaux nœuds qui pourraient
             être atteints à partir de ce nœud), et ajouter les nœuds résultants
             à la frontière.
           * Ajouter le nœud actuel à l’ensemble exploré.

.. index:: dfs, recherche en profondeur, recherche; dfs, recherche; recherche en profondeur

Recherche en profondeur
=======================

Dans la description précédente de la *frontière*, un détail n’a pas été
mentionné. À l’étape 2 dans le pseudo-code ci-dessus, quel nœud doit être retiré
? Ce choix a des implications sur la qualité de la solution et la rapidité avec
laquelle elle est obtenue. Il existe de multiples façons d’aborder la question
des nœuds à considérer en premier, dont deux peuvent être représentées par les
structures de données de type **pile** (stack, dans la recherche en
*profondeur*) et **file d’attente** (queue, dans la *recherche en largeur* ; et
`voici une jolie démonstration animée
<https://www.google.com/search?q=https://www.youtube.com/watch%253Fv%253D2wM6_PuBIxY&utm_source=gemini>`__
de la différence entre les deux).

Nous commençons par l’approche de la recherche en *profondeur* (*DFS*).

Un algorithme de recherche en *profondeur* épuise chaque direction avant d’en
essayer une autre. Dans ces cas, la frontière est gérée comme une structure de
données de type *pile*. L’expression qu’il faut retenir ici est « *dernier
entré, premier sorti* » (LIFO). Après que des nœuds ont été ajoutés à la
frontière, le premier nœud à retirer et à considérer est le dernier à y avoir
été ajouté. Cela produit un algorithme de recherche qui va aussi profondément
que possible dans la première direction qui se présente à lui, tout en laissant
les autres directions pour plus tard.

(Un exemple hors du cours : Prenez une situation où vous cherchez vos clés. Dans
une approche de recherche en *profondeur*, si vous choisissez de commencer par
chercher dans vos pantalons, vous passeriez d’abord en revue chaque poche, en
vidant chaque poche et en examinant son contenu attentivement. Vous ne cesserez
de chercher dans vos pantalons et ne commencerez à chercher ailleurs qu’une fois
que vous aurez complètement épuisé la recherche dans chaque poche de vos
pantalons.)

* Avantages :

      * Dans le meilleur des cas, cet algorithme est le plus rapide. S’il a « de
        la chance » et choisit toujours le bon chemin vers la solution (par
        hasard), alors la recherche en *profondeur* prend le moins de temps
        possible pour arriver à une solution.

* Inconvénients :

      * Il est possible que la solution trouvée ne soit pas optimale.
      * Dans le pire des cas, cet algorithme explorera tous les chemins
        possibles avant de trouver la solution, prenant ainsi le plus de temps
        possible avant d’y parvenir.

Exemple de code :

.. code-block:: python

    # Définit la fonction qui retire un nœud de la frontière et le retourne.
    def remove(self):
        # Termine la recherche si la frontière est vide, car cela signifie qu'il n'y a pas de solution.
        if self.empty():
            raise Exception("frontière vide")
        else:
            # Sauvegarde le dernier élément de la liste (qui est le nœud ajouté le plus récemment)
            node = self.frontier[-1]
            # Sauvegarde tous les éléments de la liste à l'exception du dernier nœud (c.-à-d. retire le dernier nœud)
            self.frontier = self.frontier[:-1]
            return node

.. index:: bfs, recherche en largeur, recherche; bfs, recherche; recherche en largeur

Recherche en largeur
====================

L’opposé de la recherche en *profondeur* serait la recherche en *largeur*
(*BFS*).

Un algorithme de recherche en *largeur* suivra de multiples directions en même
temps, faisant un pas dans chaque direction possible avant de faire un second
pas dans chaque direction. Dans ce cas, la frontière est gérée comme une
structure de données de type *file d’attente*. L’expression qu’il faut retenir
ici est « *premier entré, premier sorti* » (FIFO). Dans ce cas, tous les
nouveaux nœuds s’ajoutent à la file, et les nœuds sont examinés en fonction de
celui qui a été ajouté en premier (premier arrivé, premier servi !). Cela donne
un algorithme de recherche qui fait un pas dans chaque direction possible avant
de faire un deuxième pas dans une quelconque direction.

(Un exemple hors du cours : supposons que vous soyez dans une situation où vous
cherchez vos clés. Dans ce cas, si vous commencez par vos pantalons, vous
regarderez dans votre poche droite. Après cela, au lieu de regarder dans votre
poche gauche, vous jetterez un coup d’œil dans un tiroir. Puis sur la table. Et
ainsi de suite, dans chaque endroit auquel vous pouvez penser. Ce n’est qu’après
avoir épuisé tous les emplacements que vous reviendrez à vos pantalons pour
chercher dans la poche suivante.)

* Avantages :

      * Cet algorithme est garanti de trouver la solution optimale.

* Inconvénients :

      * Cet algorithme est presque garanti de prendre plus de temps que le temps
        d’exécution minimal.
      * Dans le pire des cas, cet algorithme prend le temps d’exécution le plus
        long possible.

Exemple de code :

.. code-block:: python

    # Définit la fonction qui retire un nœud de la frontière et le retourne.
    def remove(self):
        # Termine la recherche si la frontière est vide, car cela signifie qu'il n'y a pas de solution.
        if self.empty():
            raise Exception("frontière vide")
        else:
            # Sauvegarde l'élément le plus ancien de la liste (qui a été le premier à être ajouté)
            node = self.frontier[0]
            # Sauvegarde tous les éléments de la liste sauf le premier (c.-à-d. retire le premier nœud)
            self.frontier = self.frontier[1:]
            return node

Recherche gloutonne de la meilleure option d’abord
==================================================

La recherche en largeur et en profondeur sont toutes deux des algorithmes de
recherche **non informés** (uninformed). C’est-à-dire que ces algorithmes
n’utilisent aucune connaissance sur le problème qu’ils n’auraient pas acquise
par leur propre exploration. Cependant, il arrive le plus souvent que certaines
connaissances sur le problème soient, en fait, disponibles. Par exemple,
lorsqu’un humain résolvant un labyrinthe entre dans une intersection, il peut
voir quel chemin se dirige dans la direction générale de la solution et quel
chemin ne le fait pas. L’IA peut faire de même. Un type d’algorithme qui prend
en compte des connaissances supplémentaires pour tenter d’améliorer ses
performances est appelé algorithme de recherche **informé** (informed).

La recherche **gloutonne de la meilleure option d’abord** développe le nœud qui
est le plus proche de l’objectif, tel que déterminé par une **fonction
heuristique** :math:`h(n)`. Comme son nom l’indique, la fonction estime à quelle
distance se trouve le prochain nœud par rapport à l’objectif, mais elle peut se
tromper. L’efficacité de l’algorithme glouton dépend de la qualité de la
fonction heuristique. Par exemple, dans un labyrinthe, un algorithme peut
utiliser une fonction heuristique qui s’appuie sur la **distance de Manhattan**
entre les nœuds possibles et la fin du labyrinthe. La *distance de Manhattan*
ignore les murs et compte combien de pas vers le haut, vers le bas ou sur les
côtés il faudrait faire pour aller d’un emplacement à l’emplacement cible. C’est
une estimation simple qui peut être déduite en fonction des coordonnées (x, y)
de la position actuelle et de la position cible.

.. figure:: /assets/figures/manhattandistance.png
    :alt: Distance de Manhattan

    Distance de Manhattan

Cependant, il est important de souligner que, comme pour toute heuristique, elle
peut se tromper et entraîner l’algorithme sur un chemin plus lent qu’il ne
l’aurait été autrement. Il est possible qu’un algorithme de recherche *non
informé* fournisse une meilleure solution plus rapidement, mais il est moins
susceptible de le faire qu’un algorithme *informé*.

Recherche A\*
=============

Évolution de l’algorithme glouton (greedy best-first), la *recherche A*\* prend
en compte non seulement :math:`h(n)`, le coût estimé entre l’emplacement actuel
et la cible, mais aussi :math:`g(n)`, le coût qui a été accumulé jusqu’à
l’emplacement actuel. En combinant ces deux valeurs, l’algorithme dispose d’un
moyen plus précis de déterminer le coût de la solution et d’optimiser ses choix
en cours de route. L’algorithme garde la trace du :math:`(\text{coût du chemin
jusqu’à présent} + \text{coût estimé vers l’objectif})`, et dès qu’il dépasse le
coût estimé d’une option précédente, l’algorithme abandonnera le chemin actuel
et reviendra à l’option précédente, s’évitant ainsi de s’engager sur un long
chemin inefficace que :math:`h(n)` aurait, à tort, marqué comme étant le
meilleur.

Là encore, comme cet algorithme s’appuie lui aussi sur une heuristique, il n’est
aussi bon que l’heuristique qu’il emploie. Il est possible que dans certaines
situations, il soit moins efficace que la recherche gloutonne ou même que les
algorithmes *non informés*. Pour que la *recherche A*\* soit optimale, la
fonction heuristique, :math:`h(n)`, devrait être :

1. *Admissible*, c’est-à-dire ne jamais *surestimer* le coût réel, et
2. *Cohérente* (Consistent), ce qui signifie que le coût estimé du chemin vers
   l’objectif d’un nouveau nœud, ajouté au coût de transition vers celui-ci
   depuis le nœud précédent, est supérieur ou égal au coût estimé du chemin vers
   l’objectif du nœud précédent. Pour l’exprimer sous forme d’équation,
   :math:`h(n)` est cohérente si, pour chaque nœud *n* et son nœud successeur
   *n’* avec un coût d’étape :math:`c`, :math:`h(n) ≤ h(n’) + c`.

Recherche antagoniste
=====================

Alors que, précédemment, nous avons discuté d’algorithmes qui doivent trouver
une réponse à une question, dans la **recherche antagoniste**, l’algorithme fait
face à un adversaire qui tente d’atteindre l’objectif opposé. Souvent, l’IA qui
utilise la recherche antagoniste se rencontre dans les jeux, tels que le
tic-tac-toe (morpion).

Minimax
-------

Type d’algorithme de recherche antagoniste, **Minimax** représente les
conditions de victoire par (-1) pour un camp et (+1) pour l’autre camp. Les
actions ultérieures seront dictées par ces conditions, le camp minimisant
essayant d’obtenir le score le plus bas, et le camp maximisant essayant
d’obtenir le score le plus élevé.

**Représenter une IA de Tic-Tac-Toe** :

* :math:`S_0` : État initial (dans notre cas, un plateau vide de 3x3).
* :math:`Players(s)` : une fonction qui, étant donné un état *s*, retourne le
  joueur dont c’est le tour (X ou O).
* :math:`Actions(s)` : une fonction qui, étant donné un état *s*, retourne tous
  les mouvements légaux dans cet état (quelles cases sont libres sur le
  plateau).
* :math:`Result(s, a)` : une fonction qui, étant donné un état *s* et une action
  *a*, retourne un nouvel état. C’est le plateau qui a résulté de l’exécution de
  l’action *a* sur l’état *s* (faire un mouvement dans le jeu).
* :math:`Terminal(a)` : une fonction qui, étant donné un état *s*, vérifie s’il
  s’agit de la dernière étape du jeu, c’est-à-dire si quelqu’un a gagné ou s’il
  y a égalité. Retourne *True* si le jeu est terminé, *False* sinon.
* :math:`Utility(a)` : une fonction qui, étant donné un état terminal *s*,
  retourne la valeur d’utilité de l’état : -1, 0, ou 1.

**Comment l’algorithme fonctionne** :

De manière récursive, l’algorithme simule toutes les parties possibles pouvant
avoir lieu à partir de l’état actuel et jusqu’à ce qu’un état terminal soit
atteint. Chaque état terminal est évalué comme (-1), 0, ou (+1).

.. figure:: /assets/figures/minimax_tictactoe.png
    :alt: Algorithme Minimax au Tic Tac Toe

    Algorithme Minimax au Tic Tac Toe

Sachant à qui est le tour en se basant sur l’état, l’algorithme peut savoir si
le joueur actuel, en jouant de manière optimale, choisira l’action qui mène à un
état de valeur inférieure ou supérieure. De cette façon, en alternant entre
minimisation et maximisation, l’algorithme crée des valeurs pour l’état qui
résulterait de chaque action possible. Pour donner un exemple plus concret, on
peut imaginer que le joueur maximisant demande à chaque tour : « si je prends
cette action, un nouvel état en résultera. Si le joueur minimisant joue de
manière optimale, quelle action ce joueur peut-il entreprendre pour amener à la
valeur la plus basse ? ». Cependant, pour répondre à cette question, le joueur
maximisant doit demander : « Pour savoir ce que fera le joueur minimisant, je
dois simuler le même processus dans l’esprit du minimiseur : le joueur
minimisant essaiera de demander : ‘si je prends cette action, quelle action le
joueur maximisant peut-il entreprendre pour amener à la valeur la plus élevée ?’
». C’est un processus récursif, et il peut être difficile de s’y retrouver ;
regarder le pseudo-code ci-dessous peut aider. Finalement, grâce à ce processus
de raisonnement récursif, le joueur maximisant génère des valeurs pour chaque
état qui pourrait résulter de toutes les actions possibles à l’état actuel.
Après avoir obtenu ces valeurs, le joueur maximisant choisit la plus élevée.

.. figure:: /assets/figures/minimax_theoretical.png
    :alt: Le Maximiseur examine les valeurs possibles des états futurs.

    Le Maximiseur examine les valeurs possibles des états futurs.

Pour le mettre en pseudo-code, l’algorithme Minimax fonctionne de la manière
suivante :

Élagage Alpha-Bêta
------------------

Moyen d’optimiser le *Minimax*, **l’élagage Alpha-Bêta** ignore certains des
calculs récursifs qui sont décidément défavorables. Après avoir établi la valeur
d’une action, s’il y a des preuves initiales que l’action suivante peut amener
l’adversaire à obtenir un meilleur score que l’action déjà établie, il n’y a pas
besoin d’investiguer plus avant cette action, car elle sera décidément moins
favorable que celle établie précédemment.

Cela se démontre plus facilement avec un exemple : un joueur maximisant sait
qu’à l’étape suivante, le joueur minimisant essaiera d’atteindre le score le
plus bas. Supposons que le joueur maximisant ait trois actions possibles, et que
la première soit évaluée à 4. Ensuite, le joueur commence à générer la valeur
pour la prochaine action. Pour ce faire, le joueur génère les valeurs des
actions du minimiseur si le joueur actuel effectue cette action, sachant que le
minimiseur choisira la plus basse. Cependant, avant d’avoir terminé le calcul
pour toutes les actions possibles du minimiseur, le joueur constate que l’une
des options a une valeur de trois. Cela signifie qu’il n’y a aucune raison de
continuer à explorer les autres actions possibles pour le joueur minimisant. La
valeur de l’action non encore évaluée n’a pas d’importance, qu’elle soit de 10
ou de (-10). Si la valeur est 10, le minimiseur choisira l’option la plus basse,
3, ce qui est déjà pire que la valeur 4 préétablie. Si l’action non encore
évaluée s’avérait être (-10), le minimiseur prendrait cette option, (-10), ce
qui est encore plus défavorable pour le maximiseur. Par conséquent, le calcul
des actions possibles supplémentaires pour le minimiseur à ce stade est sans
pertinence pour le maximiseur, car le joueur maximisant a déjà un choix sans
équivoque meilleur dont la valeur est 4.

.. figure:: /assets/figures/alphabeta.png
    :alt: Élagage Alpha-Bêta

    Élagage Alpha-Bêta

Minimax à profondeur limitée
----------------------------

Il y a un total de 255 168 parties de Tic Tac Toe possibles, et 10²⁹⁰⁰⁰ parties
possibles aux échecs. L’algorithme minimax, tel que présenté jusqu’ici,
nécessite de générer toutes les parties hypothétiques à partir d’un certain
point jusqu’à la condition terminale. Bien que calculer toutes les parties de
Tic-Tac-Toe ne pose pas de défi pour un ordinateur moderne, le faire avec les
échecs est actuellement impossible.

Le **Minimax à profondeur limitée** considère seulement un nombre prédéfini de
coups avant de s’arrêter, sans jamais atteindre un état terminal. Cependant,
cela ne permet pas d’obtenir une valeur précise pour chaque action, puisque la
fin des parties hypothétiques n’a pas été atteinte. Pour faire face à ce
problème, le *Minimax à profondeur limitée* s’appuie sur une **fonction
d’évaluation** qui estime l’utilité attendue du jeu à partir d’un état donné,
ou, en d’autres termes, qui attribue des valeurs aux états. Par exemple, dans
une partie d’échecs, une fonction d’utilité prendrait en entrée une
configuration actuelle de l’échiquier, essaierait d’évaluer son utilité attendue
(en fonction des pièces que possède chaque joueur et de leur emplacement sur
l’échiquier), puis renverrait une valeur positive ou négative qui représente à
quel point l’échiquier est favorable pour un joueur par rapport à l’autre. Ces
valeurs peuvent être utilisées pour décider de la bonne action, et plus la
fonction d’évaluation est bonne, meilleur sera l’algorithme Minimax qui s’y fie.

***********
 Exercices
***********

=================================================
Exercices : Chapitre 2 - Connaissances et Logique
=================================================

.. :ia2:exercice:: 20.1
    Logique propositionnelle et équivalence

    La règle d'élimination de l'implication stipule que l'expression
    :math:`P \implies Q` est logiquement équivalente à :math:`\lnot P \lor Q`.

    a. Dressez la table de vérité complète incluant les colonnes pour
        :math:`P`, :math:`Q`, :math:`\lnot P`, :math:`P \implies Q`, et
        :math:`\lnot P \lor Q`.

    b. À l'aide de la table de vérité, prouvez que la proposition
        biconditionnelle
        :math:`(P \implies Q) \iff (\lnot P \lor Q)` est une tautologie
        (toujours vraie).

    Solution: :ia2:sol:`20.1`

.. :ia2:exercice:: 20.2
    Inférence par vérification de modèles

    Considérez les propositions suivantes :

    * P : Il fait froid.
    * Q : Il neige.
    * R : Je mets un manteau.

    Votre base de connaissances (KB) contient les règles et faits suivants :

    1. S'il neige, alors il fait froid : :math:`Q \implies P`

    2. S'il fait froid ou s'il neige, alors je mets un manteau :
        :math:`(P \lor Q) \implies R`

    3. Il neige : :math:`Q`

    a. Combien de modèles possibles (assignations de vérité) existent pour
        cet univers à 3 propositions (P, Q, R) ?

    b. En utilisant l'algorithme de vérification de modèles, éliminez les
        modèles où la KB est fausse.

    c. Le système peut-il conclure que je mets un manteau
        (est-ce que :math:`KB \models R`) ? Justifiez.

    Solution: :ia2:sol:`20.2`

.. :ia2:exercice:: 20.3
    Conversion en Forme Normale Conjonctive (CNF)

    Pour utiliser l'algorithme de résolution, une base de connaissances
    doit être convertie sous Forme Normale Conjonctive (CNF), c'est-à-dire
    une conjonction de clauses (les clauses étant des disjonctions de littéraux).

    a. Convertissez la proposition suivante en CNF étape par étape :
        :math:`\lnot (A \implies B) \lor C`

    b. Nommez explicitement la règle logique utilisée à chaque étape
        (ex: Élimination de l'implication, Loi de De Morgan, etc.).

    Solution: :ia2:sol:`20.3`

.. :ia2:exercice:: 20.4
    Preuve par résolution et contradiction

    Soit une base de connaissances (KB) contenant les trois clauses
    (en CNF) suivantes :

    1. :math:`(A \lor B)`

    2. :math:`(\lnot A \lor C)`

    3. :math:`(\lnot B \lor C)`

    Vous souhaitez prouver que la proposition :math:`C` est une conséquence
    logique de cette KB (:math:`KB \models C`).

    a. Quelle clause devez-vous ajouter à la KB pour entamer une preuve
        par contradiction ?

    b. Appliquez l'algorithme de résolution étape par étape sur les clauses
        pour arriver à la clause vide :math:`()`, prouvant ainsi la
        contradiction.

    Solution: :ia2:sol:`20.4`

.. :ia2:exercice:: 20.5
    Logique du premier ordre (Quantificateurs)

    Traduisez les phrases suivantes en langage naturel vers la logique du
    premier ordre. Utilisez les prédicats :math:`Etudiant(x)`,
    :math:`Cours(x)`, :math:`Difficile(x)`, et :math:`Inscrit(x, y)`
    (qui signifie "x est inscrit à y").

    a. Tous les étudiants sont inscrits à au moins un cours.

    b. Il existe un cours difficile auquel aucun étudiant n'est inscrit.

    Solution: :ia2:sol:`20.5`


***********
 Solutions
***********




.. ia2:solution:: 20.1
    Logique propositionnelle et équivalence

    Solution de :ia2:ex:`20.1`

    a. **Table de vérité :**

        ========= ========= ============= ==================== ======================
        :math:`P` :math:`Q` :math:`\lnot P` :math:`P \implies Q` :math:`\lnot P \lor Q`
        ========= ========= ============= ==================== ======================
        faux      faux      vrai          vrai                 vrai
        faux      vrai      vrai          vrai                 vrai
        vrai      faux      faux          faux                 faux
        vrai      vrai      faux          vrai                 vrai
        ========= ========= ============= ==================== ======================

    b. **Preuve de la tautologie :**
        Les valeurs de la colonne :math:`P \implies Q` et de la colonne
        :math:`\lnot P \lor Q` sont strictement identiques pour chaque ligne
        (modèle). Un biconditionnel (:math:`\iff`) est vrai si et seulement
        si les deux côtés ont la même valeur de vérité. Puisque c'est le
        cas pour les 4 modèles possibles, le résultat final est entièrement
        composé de "vrai". C'est donc une tautologie logique.

.. ia2:solution:: 20.2
    Inférence par vérification de modèles

    Solution de :ia2:ex:`20.2`

    a. **Nombre de modèles :**
        Il y a 3 symboles propositionnels (P, Q, R). Le nombre de modèles
        possibles est :math:`2^3 = 8` modèles.

    b. **Élimination des modèles falsifiant la KB :**
        * Fait 3 (:math:`Q` est vrai) : On élimine tous les modèles où
            :math:`Q` est faux (reste 4 modèles).

        * Règle 1 (:math:`Q \implies P`) : Sachant que :math:`Q` est vrai,
            pour que l'implication soit vraie, :math:`P` doit obligatoirement
            être vrai. On élimine les modèles où :math:`P` est faux
            (reste 2 modèles : {P=V, Q=V, R=F} et {P=V, Q=V, R=V}).

        * Règle 2 (:math:`(P \lor Q) \implies R`) : Sachant que P et Q sont
            vrais, l'antécédent :math:`(P \lor Q)` est vrai.
            Pour que la KB soit vraie, le conséquent :math:`R` doit donc
            être vrai. Le modèle où R est faux est éliminé.

        * Il ne reste qu'un seul modèle valide : {P=Vrai, Q=Vrai, R=Vrai}.

    c. **Conclusion :**
        Oui, :math:`KB \models R`. Dans l'unique modèle où l'entièreté de
        la KB est vraie, la proposition :math:`R` est également vraie.
        La conséquence logique est prouvée.

.. ia2:solution:: 20.3
    Conversion en Forme Normale Conjonctive (CNF)

    Solution de :ia2:ex:`20.3`

    a et b. **Étapes de conversion :**

    1. :math:`\lnot (A \implies B) \lor C`
        *(Proposition initiale)*

    2. :math:`\lnot (\lnot A \lor B) \lor C`
        *(Application de l'élimination de l'implication sur ce qui est entre
        parenthèses)*

    3. :math:`(\lnot(\lnot A) \land \lnot B) \lor C`
        *(Application de la Loi de De Morgan pour distribuer la négation
        à l'intérieur)*

    4. :math:`(A \land \lnot B) \lor C`
        *(Application de l'élimination de la double négation sur A)*

    5. :math:`(A \lor C) \land (\lnot B \lor C)`
        *(Application de la propriété de distributivité du OU sur le ET)*

    La forme finale en CNF est : :math:`(A \lor C) \land (\lnot B \lor C)`.

.. ia2:solution:: 20.4
    Preuve par résolution et contradiction

    Solution de :ia2:ex:`20.4`

    a. **Clause à ajouter :**
       Pour une preuve par contradiction, nous devons supposer que le but
        est faux. Il faut donc ajouter la
