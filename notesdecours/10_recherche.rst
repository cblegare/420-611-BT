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

.. ia2:exercice:: 10.1
    Formalisation d'un problème de recherche (Jeu de Taquin)

    Un jeu de taquin consiste à déplacer des tuiles numérotées sur une grille
    pour atteindre un ordre précis.

    a. Modélisez ce qu'est un **état** du système dans ce contexte précis.
    b. Définissez la fonction **Actions(s)** pour ce problème.
    c. Quel serait un **test de but** approprié ?

    Solution: :ia2:solution:`10.1`

.. ia2:exercice:: 10.2
    Recherche non informée (DFS vs BFS)

    Un agent de navigation doit trouver un chemin dans un graphe d'états.
    Le mécanisme de frontière détermine l'ordre d'exploration des nœuds.

    a. Si l'agent utilise la **recherche en profondeur (DFS)**, quelle
       structure de données régit la frontière et quel est le risque principal
       lié à la qualité de la solution ?

    b. Si l'agent utilise la **recherche en largeur (BFS)**, quelle structure
       de données régit la frontière et quelle garantie l'algorithme offre-t-il ?

    Solution: :ia2:solution:`10.2`

.. ia2:exercice:: 10.3
    Recherche A* et Heuristiques

    Dans le cadre d'un algorithme de recherche A*, l'agent utilise une fonction
    heuristique :math:`h(n)` pour estimer la distance vers l'objectif.

    a. Quelle condition absolue la fonction :math:`h(n)` doit-elle respecter
       pour être qualifiée d'**admissible** ?

    b. Expliquez la condition de **cohérence** (ou consistance) pour une
       heuristique à l'aide de l'équation mathématique appropriée impliquant
       le coût d'étape :math:`c`.

    Solution: :ia2:solution:`10.3`

.. ia2:exercice:: 10.4
    Recherche antagoniste (Minimax et Élagage Alpha-Bêta)

    Dans un jeu de Tic-Tac-Toe, une IA simule de manière récursive toutes
    les parties possibles jusqu'à atteindre un état terminal pour choisir
    son coup.

    a. Comment la fonction **Utility(a)** évalue-t-elle les conditions de
       victoire pour le camp maximisant et le camp minimisant ?

    b. Expliquez le rôle de l'**élagage Alpha-Bêta** dans l'optimisation
       de ce processus récursif.

    Solution: :ia2:solution:`10.4`

.. ia2:exercice:: 10.5
    Implémentation de la frontière en Python (DFS vs BFS)

    Le cours présente la façon dont on retire un nœud de la frontière en
    Python selon que l'on utilise une recherche en profondeur (DFS) ou en
    largeur (BFS).
    Supposons que nous avons une classe avec un attribut `self.frontier`
    (une liste Python).

    a. Complétez la méthode Python suivante pour qu'elle implémente la logique
       d'une **pile** (recherche en profondeur - DFS), en utilisant le
       découpage (*slicing*) de liste comme démontré dans le cours.

    .. code-block:: python

        def remove(self):
            if self.empty():
                raise Exception("frontière vide")
            else:
                # À compléter : extraire le nœud (LIFO) et mettre à jour la frontière
                pass

    b. Modifiez ensuite cette méthode pour implémenter la logique d'une
       **file d'attente** (recherche en largeur - BFS) en respectant le
       principe FIFO.

    Solution: :ia2:solution:`10.5`

.. ia2:exercice:: 10.6
    Calcul de l'heuristique : Distance de Manhattan en Python

    La recherche gloutonne et la recherche A* utilisent souvent la distance
    de Manhattan comme fonction heuristique pour estimer le coût restant
    dans un labyrinthe. Cette distance ignore les murs et compte le nombre
    de pas vers le haut, le bas ou les côtés nécessaires pour relier deux
    points.

    a. Écrivez une fonction Python `distance_manhattan(pos_actuelle, pos_cible)` qui accepte deux tuples représentant des coordonnées (x, y) et retourne la distance de Manhattan entre ces deux points.

    Solution: :ia2:solution:`10.6`

.. ia2:exercice:: 10.7
    Propriétés des heuristiques : Admissibilité et Cohérence

    Rappelons que pour l'algorithme A*, une heuristique :math:`h(n)` est :

    * **Admissible** si elle ne surestime jamais le coût réel vers la cible
      (:math:`h(n) \le h^*(n)`).

    * **Cohérente** si elle respecte l'inégalité triangulaire pour chaque
      étape (:math:`h(n) \le c(n, n') + h(n')`), où :math:`c` est le coût
      de transition.

    Pour chacune des 8 mises en situation suivantes
    (composées d'un environnement et d'une heuristique),
    déterminez si l'heuristique est **admissible** et si elle est **cohérente**.

    a. **Système de navigation GPS :** L'agent est une voiture cherchant le trajet le plus court sur un réseau routier (le coût est la distance physique de la route). L'heuristique utilise la distance à vol d'oiseau (euclidienne) entre la position actuelle et la destination.

    b. **Robot d'entrepôt :** Un robot déplace des palettes mal rangées (coût = 1 par déplacement). L'heuristique correspond au nombre de palettes qui ne se trouvent pas encore dans leur baie de destination finale.

    c. **Drone à capteurs hétérogènes :** Un drone cartographe estime la batterie restante nécessaire pour rentrer. Dans la zone A (haute résolution), son capteur estime :math:`h(A) = 15\%`. Il se déplace vers la zone B adjacente (coût = :math:`1\%` de batterie). Or, dans la zone B, un capteur bas de gamme prend le relais et sous-estime grossièrement le retour : :math:`h(B) = 2\%`. (Le vrai coût est de :math:`20\%`).

    d. **Randonneur et table de référence :** Le coût est le temps de marche. Le randonneur utilise une table créée par un guide qui n'a jamais surestimé les temps. Au point X, la table indique :math:`h(X) = 60` minutes. Le randonneur marche 5 minutes pour atteindre le point Y, mais pour Y, le guide avait oublié d'entrer une valeur et a inscrit :math:`h(Y) = 0`.

    e. **Camion de livraison pessimiste :** Le coût est la distance en km. Le système calcule la distance exacte du chemin le plus court (:math:`h^*`), mais y ajoute systématiquement une pénalité fixe de 10 km (même à l'arrivée) pour compenser d'éventuelles routes barrées non prévues.

    f. **IA de gestion de projet :** Le coût est évalué en heures. Une IA possède un algorithme parfait capable de prédire le nombre d'heures exactes pour finir un projet. Toutefois, pour être certaine de ne pas décevoir le client, elle ajoute un "coussin de sécurité" de 24 heures à toutes les étapes de sa planification.

    g. **Jeu de rôle / D&D 5e :** Un personnage navigue sur une grille où les déplacements orthogonaux ET diagonaux coûtent exactement 1 point de mouvement. Le programmeur décide d'utiliser la **distance de Manhattan** (qui compte les pas orthogonaux uniquement) comme heuristique.

    h. **Covoiturage et tarification dynamique :** Le coût est le prix en dollars pour atteindre la destination. L'heuristique IA est instable : le point B est en zone de forte demande (surge pricing) et l'IA estime :math:`h(B) = 40\$`. Le point A, situé à :math:`2\$` de trajet de B, est hors de la zone et l'IA estime :math:`h(A) = 10\$`. Le vrai coût depuis ces deux points vers la destination finale est d'environ :math:`15\$`. L'agent évalue le trajet de B vers A.

    Solution: :ia2:solution:`10.7`

**********
 Solutions
**********

.. ia2:solution:: 10.1
    Formalisation d'un problème de recherche (Jeu de Taquin)

    Solution de :ia2:ex:`10.1`

    a. **État :** Une configuration spécifique de l'agent dans son environnement.
       Pour le taquin, un état correspond à la disposition spatiale exacte
       de tous les nombres sur le plateau de jeu à un moment donné.

    b. **Actions(s) :** Les choix exécutables depuis un état.
       Dans le taquin, il s'agit des directions possibles pour faire glisser
       les carrés adjacents vers l'espace vide (haut, bas, gauche, droite).

    c. **Test de but :** La condition vérifiant si l'état actuel est l'état
       cible. Le test consisterait à vérifier si toutes les tuiles sont
       ordonnées séquentiellement (de 1 à 15), avec l'espace vide positionné
       dans le coin inférieur droit.

.. ia2:solution:: 10.2
    Recherche non informée (DFS vs BFS)

    Solution de :ia2:ex:`10.2`

    a. **Recherche en profondeur (DFS) :** La frontière est gérée par une
       **pile** (stack), fonctionnant sur le principe « dernier entré,
       premier sorti » (LIFO). Le risque principal est que la solution
       trouvée peut ne pas être optimale.

    b. **Recherche en largeur (BFS) :** La frontière est gérée par une
       **file d'attente** (queue), fonctionnant sur le principe « premier
       entré, premier sorti » (FIFO). Cette structure garantit de toujours
       trouver la solution optimale.

.. ia2:solution:: 10.3
    Recherche A* et Heuristiques

    Solution de :ia2:ex:`10.3`

    a. **Admissibilité :** Une fonction heuristique est admissible si elle
       ne surestime jamais le coût réel du chemin pour atteindre l'objectif.

    b. **Cohérence :** Une heuristique est cohérente si le coût estimé depuis
       un nœud actuel vers l'objectif est inférieur ou égal au coût réel
       de transition vers le nœud suivant, additionné au coût estimé de
       ce nœud suivant vers l'objectif. L'équation mathématique est
       :math:`h(n) \le h(n') + c`.

.. ia2:solution:: 10.4
    Recherche antagoniste (Minimax et Élagage Alpha-Bêta)

    Solution de :ia2:ex:`10.4`

    a. **Évaluation (Utility) :** L'état terminal se voit attribuer une valeur 
       de (+1) pour une victoire du camp maximisant 
       (qui cherche le score le plus élevé), de (-1) pour une victoire du 
       camp minimisant (qui cherche le score le plus bas), et de 0 pour 
       une égalité.

    b. **Élagage Alpha-Bêta :** Cette technique optimise l'algorithme Minimax 
       en ignorant les branches de calcul récursif qui sont décidément 
       défavorables. Dès que l'algorithme prouve qu'une action permettra 
       à l'adversaire d'obtenir un meilleur score qu'une option déjà explorée, 
       il cesse d'évaluer cette branche.

.. ia2:solution:: 10.5
    Implémentation de la frontière en Python (DFS vs BFS)

    Solution de :ia2:ex:`10.5`

    a. **Recherche en profondeur (DFS - Pile / Stack) :**
       Pour appliquer le principe LIFO, on retire le dernier élément ajouté. 
       
       .. code-block:: python

           def remove(self):
               if self.empty():
                   raise Exception("frontière vide")
               else:
                   node = self.frontier[-1]
                   self.frontier = self.frontier[:-1]
                   return node

    b. **Recherche en largeur (BFS - File d'attente / Queue) :**
       Pour appliquer le principe FIFO, on retire le plus ancien élément
       de la liste, situé à l'indice 0.

       .. code-block:: python

           def remove(self):
               if self.empty():
                   raise Exception("frontière vide")
               else:
                   node = self.frontier[0]
                   self.frontier = self.frontier[1:]
                   return node

.. ia2:solution:: 10.6
    Calcul de l'heuristique : Distance de Manhattan en Python

    Solution de :ia2:ex:`10.6`

    a. **Fonction `distance_manhattan` :**
       La distance de Manhattan correspond à la somme des différences absolues
       des coordonnées cartésiennes de deux points.

       .. code-block:: python

           def distance_manhattan(pos_actuelle, pos_cible):
               # Déballage des tuples
               x1, y1 = pos_actuelle
               x2, y2 = pos_cible

               # Calcul de la distance
               return abs(x1 - x2) + abs(y1 - y2)


.. ia2:solution:: 10.7
    Propriétés des heuristiques : Admissibilité et Cohérence

    Solution de :ia2:ex:`10.7`

    a. **GPS - Distance Euclidienne :**

       * **Admissible (Oui) :** La ligne droite (vol d'oiseau) est le chemin mathématiquement le plus court entre deux points. Il est impossible que la route réelle soit plus courte, donc l'heuristique ne surestime jamais.

       * **Cohérente (Oui) :** En géométrie, la distance euclidienne respecte toujours l'inégalité triangulaire. La distance en ligne droite de A vers la cible sera toujours inférieure ou égale à la distance de A vers B plus la ligne droite de B vers la cible.

    b. **Robot d'entrepôt - Palettes mal rangées :**

       * **Admissible (Oui) :** Chaque palette mal rangée nécessitera obligatoirement au moins un déplacement pour être corrigée. L'estimation est donc toujours inférieure ou égale au coût réel.

       * **Cohérente (Oui) :** Une action (coût = 1) ne peut ranger qu'au maximum une seule palette à la fois. L'heuristique :math:`h` baissera donc d'au maximum 1. L'équation :math:`h(n) - h(n') \le 1 \implies h(n) \le 1 + h(n')` est respectée.

    c. **Drone - Capteurs hétérogènes :**

       * **Admissible (Oui) :** Les deux capteurs sous-estiment la batterie réelle de :math:`20\%` (:math:`15\% \le 20\%` et :math:`2\% \le 19\%`).

       * **Cohérente (Non) :** Lors du passage de la zone A à B, l'estimation chute brusquement à cause du changement de capteur. On a :math:`h(A) \le c(A,B) + h(B) \implies 15 \le 1 + 2`, ce qui est faux (:math:`15 \not\le 3`).

    d. **Randonneur - Valeur manquante :**

       * **Admissible (Oui) :** Le guide n'a jamais surestimé les temps (et :math:`0 \le` temps réel).

       * **Cohérente (Non) :** En faisant un pas qui coûte 5 minutes, l'heuristique chute de 60 minutes. L'inéquation de cohérence donne : :math:`60 \le 5 + 0`, ce qui est faux. L'heuristique est trop instable.

    e. **Camion - Pénalité de 10 km :**

       * **Admissible (Non) :** L'heuristique est :math:`h(n) = h^*(n) + 10`. Elle surestimera toujours la distance réelle exacte de 10 km.

       * **Cohérente (Oui) :** Le malus de 10 km s'applique à tous les nœuds uniformément. Dans l'inéquation :math:`h(n) \le c(n,n') + h(n')`, la constante de 10 km est présente des deux côtés et s'annule mathématiquement (:math:`h^*(n) + 10 \le c + h^*(n') + 10 \implies h^*(n) \le c + h^*(n')`). Puisque la distance réelle :math:`h^*` est cohérente, la version avec constante l'est aussi.

    f. **Gestion de projet - Coussin de 24h :**

       * **Admissible (Non) :** L'ajout de 24 heures aux estimations parfaites signifie que l'IA surestime volontairement le temps restant, ce qui casse l'admissibilité.

       * **Cohérente (Oui) :** Comme pour la situation précédente, le biais de 24h est constant sur tous les états. Une heure travaillée fait baisser l'estimation d'exactement une heure. L'inégalité :math:`h(n) \le 1 + h(n')` est toujours préservée.

    g. **D&D 5e - Diagonale vs Manhattan :**

       * **Admissible (Non) :** La distance de Manhattan surestime le coût. Si la cible est à 5 cases en diagonale, le coût réel est de 5 (puisqu'une diagonale coûte 1). La distance de Manhattan comptera 5 pas horizontaux et 5 pas verticaux, donnant une heuristique de 10 (:math:`10 > 5`).

       * **Cohérente (Non) :** Imaginons le départ à :math:`(0,0)` avec une cible à :math:`(5,5)`. :math:`h(0,0) = 10`. Le personnage fait un pas diagonal vers :math:`(1,1)` pour un coût de 1. La nouvelle heuristique est :math:`h(1,1) = 8`. Vérification de la cohérence : :math:`10 \le 1 + 8 \implies 10 \le 9`. C'est faux, l'heuristique chute trop vite par rapport au coût.

    h. **Covoiturage - Modèle tarifaire instable :**

       * **Admissible (Non) :** L'estimation au point B est de :math:`40\$`, alors que le vrai coût vers l'objectif n'est que de :math:`15\$`. L'algorithme surestime massivement.

       * **Cohérente (Non) :** Le déplacement du point B vers le point A coûte :math:`2\$`. L'estimation au point A est de :math:`10\$`. L'équation donne : :math:`h(B) \le c(B,A) + h(A) \implies 40 \le 2 + 10 \implies 40 \le 12`, ce qui est manifestement faux. Le modèle tarifaire chute de :math:`30\$` alors que l'agent n'a dépensé que :math:`2\$`.