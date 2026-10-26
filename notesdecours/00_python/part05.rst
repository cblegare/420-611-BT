#######################
 Fonctions productives
#######################

*******************
 Valeurs de retour
*******************

Certaines des fonctions intégrées que nous avons utilisées, telles que les
fonctions mathématiques, produisent des résultats. L'appel de la fonction génère
une valeur, que nous affectons généralement à une variable ou que nous utilisons
dans une expression.

.. code-block:: python

    e = math.exp(1.0)
    hauteur = rayon * math.sin(radians)

Mais jusqu'à présent, aucune des fonctions que nous avons écrites n'a retourné
de valeur.

Dans ce chapitre, nous allons écrire des fonctions productives (*fruitful
functions*). Le premier exemple est ``aire``, qui retourne l'aire d'un cercle
avec le rayon donné :

.. code-block:: python

    import math


    def aire(rayon):
        a = math.pi * rayon**2
        return a

Nous avons vu l'instruction ``return`` auparavant, mais dans une fonction
productive, l'instruction ``return`` inclut une expression. Cette instruction
signifie : « Retourne immédiatement de cette fonction et utilise l'expression
suivante comme valeur de retour. » L'expression fournie peut être arbitrairement
compliquée, nous pourrions donc écrire cette fonction de manière plus concise :

.. code-block:: python

    def aire(rayon):
        return math.pi * rayon**2

D'un autre côté, les variables temporaires comme ``a`` peuvent rendre le
débogage plus facile.

Parfois, il est utile d'avoir plusieurs instructions de retour, une dans chaque
branche d'une condition :

.. code-block:: python

    def valeur_absolue(x):
        if x < 0:
            return -x
        else:
            return x

Puisque ces instructions ``return`` sont dans une condition alternative, une
seule d'entre elles sera exécutée.

Dès qu'une instruction de retour s'exécute, la fonction se termine sans exécuter
les instructions suivantes. Tout code qui apparaît après une instruction
``return``, ou à tout autre endroit que le flux d'exécution ne peut jamais
atteindre, est appelé du code mort (*dead code*).

Dans une fonction productive, c'est une bonne idée de s'assurer que chaque
chemin possible à travers le programme atteint une instruction ``return``. Par
exemple :

.. code-block:: python

    def valeur_absolue(x):
        if x < 0:
            return -x
        if x > 0:
            return x

Cette fonction est incorrecte car si ``x`` se trouve être 0, aucune des
conditions n'est vraie, et la fonction se termine sans toucher à une instruction
``return``. Si le flux d'exécution atteint la fin d'une fonction, la valeur de
retour est ``None``, ce qui n'est pas la valeur absolue de 0.

.. code-block:: python-console

    >>> print(valeur_absolue(0))
    None

***************************
 Développement incrémental
***************************

Au fur et à mesure que vous écrirez des fonctions plus grandes, vous constaterez
peut-être que vous passez plus de temps à déboguer. Pour faire face à des
programmes de plus en plus complexes, vous voudrez peut-être essayer un
processus appelé développement incrémental (*incremental development*).

L'objectif du développement incrémental est d'éviter les longues sessions de
débogage en ajoutant et en testant seulement une petite quantité de code à la
fois.

À titre d'exemple, supposons que vous souhaitiez trouver la distance entre deux
points, donnés par leurs coordonnées (x\ :sub:`1`, y\ :sub:`1`) et (x\ :sub:`2`,
y\ :sub:`2`). Par le théorème de Pythagore, la distance est :

.. math::

    distance = \sqrt{(x_2 - x_1)^2 + (y_2) - Y_1)^2}

La première étape consiste à considérer à quoi devrait ressembler la fonction
``distance`` en Python. Autrement dit, quelles sont les entrées (paramètres) et
quelle est la sortie (valeur de retour) ?

Dans ce cas, les entrées sont deux points, que vous pouvez représenter à l'aide
de quatre nombres. La valeur de retour est la distance, qui est une valeur à
virgule flottante.

Vous pouvez déjà écrire le squelette de la fonction :

.. code-block:: python

    def distance(x1, y1, x2, y2):
        return 0.0

Évidemment, cette version ne calcule pas les distances ; elle retourne toujours
zéro. Mais elle est syntaxiquement correcte, et elle s'exécutera, ce qui
signifie que vous pouvez la tester avant de la rendre plus compliquée.

Pour tester la nouvelle fonction, appelez-la avec des exemples d'arguments :

.. code-block:: python-console

    >>> distance(1, 2, 4, 6)
    0.0

J'ai choisi ces valeurs pour que la distance horizontale soit 3 et la distance
verticale soit 4 ; de cette façon, le résultat est 5 (l'hypoténuse d'un triangle
3-4-5). Lors du test d'une fonction, il est utile de connaître la bonne réponse.

À ce stade, nous avons confirmé que la fonction est syntaxiquement correcte, et
nous pouvons commencer à ajouter du code. Après chaque changement, nous testons
à nouveau le programme. Si une erreur survient à n'importe quel point, nous
savons où elle se trouve : elle doit se trouver dans la dernière ligne que nous
avons ajoutée.

Une étape logique de calcul consiste à trouver les différences x\ :sub:`2` -
x\ :sub:`1` et y\ :sub:`2` - y\ :sub:`1`. Nous stockerons ces valeurs dans des
variables temporaires et les imprimerons :

.. code-block:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        print("dx est", dx)
        print("dy est", dy)
        return 0.0

Si la fonction fonctionne, elle devrait afficher ``dx est 3`` et ``dy est 4``.
Si c'est le cas, nous savons que la fonction obtient les bons arguments et
effectue le premier calcul correctement. Si ce n'est pas le cas, il n'y a que
quelques lignes à vérifier.

Ensuite, nous calculons la somme des carrés de ``dx`` et ``dy`` :

.. code-block:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        carre_dx = dx**2
        carre_dy = dy**2
        print("carre_dx est", carre_dx)
        print("carre_dy est", carre_dy)
        return 0.0

Encore une fois, vous devez exécuter le programme à ce stade et vérifier la
sortie (qui devrait être 25).

Enfin, vous pouvez utiliser la fonction ``math.sqrt`` pour calculer et retourner
le résultat :

.. code-block:: python

    import math


    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        carre_dx = dx**2
        carre_dy = dy**2
        resultat = math.sqrt(carre_dx + carre_dy)
        return resultat

Si cela fonctionne correctement, vous avez terminé. Sinon, vous voudrez
peut-être afficher la valeur de ``resultat`` avant l'instruction de retour.

La version finale de la fonction n'affiche rien lorsqu'elle est exécutée ; elle
retourne simplement une valeur. Les instructions ``print`` que nous avons
écrites sont utiles pour le débogage, mais une fois que vous avez vérifié que la
fonction fonctionne, vous devez les supprimer. Un code comme celui-ci est appelé
code d'échafaudage (*scaffolding*) car il est utile pour construire le programme
mais ne fait pas partie du produit final.

*************
 Composition
*************

Comme vous devriez vous y attendre à ce jour, vous pouvez appeler une fonction à
partir d'une autre. Cette capacité est appelée composition (*composition*).

À titre d'exemple, nous allons écrire une fonction qui prend deux points, le
centre du cercle et un point sur le périmètre, et qui calcule l'aire du cercle.

Supposons que le point central est stocké dans les variables ``xc`` et ``yc``,
et le point de périmètre est dans ``xp`` et ``yp``. La première étape consiste à
trouver le rayon du cercle, qui est la distance entre les deux points. Nous
venons d'écrire une fonction, ``distance``, qui fait cela :

.. code-block:: python

    rayon = distance(xc, yc, xp, yp)

La deuxième étape consiste à trouver l'aire d'un cercle avec ce rayon; nous
venons d'écrire cela aussi :

.. code-block:: python

    resultat = aire(rayon)

Encapsuler ces étapes dans une fonction produit ceci :

.. code-block:: python

    def aire_du_cercle(xc, yc, xp, yp):
        rayon = distance(xc, yc, xp, yp)
        resultat = aire(rayon)
        return resultat

Les variables temporaires ``rayon`` et ``resultat`` sont utiles pour le
développement et le débogage, mais une fois que le programme fonctionne, nous
pouvons le rendre plus concis en composant les appels de fonctions :

.. code-block:: python

    def aire_du_cercle(xc, yc, xp, yp):
        return aire(distance(xc, yc, xp, yp))

**********************
 Fonctions booléennes
**********************

Les fonctions peuvent retourner des booléens, ce qui est souvent pratique pour
cacher des tests complexes à l'intérieur de fonctions. Par exemple :

.. code-block:: python

    def est_divisible(x, y):
        if x % y == 0:
            return True
        else:
            return False

Il est courant de donner aux fonctions booléennes des noms qui ressemblent à des
questions par oui ou par non; ``est_divisible`` retourne ``True`` ou ``False``
pour indiquer si ``x`` est divisible par ``y``.

Voici un exemple :

.. code-block:: python-console

    >>> est_divisible(6, 4)
    False
    >>> est_divisible(6, 3)
    True

Le résultat de l'opérateur ``==`` est un booléen, nous pouvons donc écrire la
fonction de manière plus concise en le retournant directement :

.. code-block:: python

    def est_divisible(x, y):
        return x % y == 0

Les fonctions booléennes sont souvent utilisées dans des instructions
conditionnelles :

.. code-block:: python

    if est_divisible(x, y):
        print("x est divisible par y")

Il peut être tentant d'écrire quelque chose comme :

.. code-block:: python

    if est_divisible(x, y) == True:
        print("x est divisible par y")

Mais la comparaison supplémentaire est inutile.

***********
 Glossaire
***********

.. glossary::

    variable temporaire
    temporary variable
        Une variable utilisée pour stocker une valeur intermédiaire
        dans un calcul complexe.

    code mort
    dead code
        Une partie d'un programme qui ne peut jamais être exécutée,
        souvent parce qu'elle apparaît après une instruction de retour.

    développement incrémental
    incremental development
        Un plan de développement de programme destiné à éviter
        le débogage en ajoutant et en testant seulement une petite
        quantité de code à la fois.

    code d'échafaudage
    scaffolding
        Code qui est utilisé pendant le développement du programme
        mais qui ne fait pas partie du produit final.

    fonction booléenne
    boolean function
        Une fonction qui retourne un booléen.

***********
 Exercices
***********

.. topic:: Exercice 1

    Écrivez une fonction ``compare`` qui prend deux valeurs, ``x`` et ``y``, et
    qui retourne ``1`` si ``x > y``, ``0`` si ``x == y``, et ``-1`` si ``x <
    y``.

.. topic:: Exercice 2

    Utilisez un développement incrémental pour écrire une fonction nommée
    ``hypotenuse`` qui retourne la longueur de l'hypoténuse d'un triangle
    rectangle, étant donné la longueur des deux autres côtés. Enregistrez chaque
    étape du processus de développement au fur et à mesure que vous avancez.

.. topic:: Exercice 3

    Écrivez une fonction booléenne ``est_entre(x, y, z)`` qui retourne ``True``
    si ``x ≤ y ≤ z`` et ``False`` sinon.

.. ia2:exercice:: 05.1
    Valeurs de retour et développement incrémental

    Le développement incrémental consiste à construire et tester du code par de
    petites étapes vérifiables afin d'éviter les erreurs complexes.

    a. Écrivez la formule mathématique permettant de calculer la distance
       euclidienne entre deux points :math:`(x_1, y_1)` et :math:`(x_2, y_2)`.
    b. Proposez l'implémentation d'une fonction ``distance(x1, y1, x2, y2)`` en
       appliquant la démarche du développement incrémental (calcul des écarts
       :math:`dx` et :math:`dy`, somme des carrés, puis racine carrée avec
       ``math.sqrt``).

    Solution: :ia2:solution:`05.1`

.. ia2:exercice:: 05.2
    Composition de fonctions

    Une fois qu'une fonction a été écrite et vérifiée, elle peut être utilisée à
    l'intérieur d'une autre fonction.

    a. Écrivez une fonction ``aire_disque(rayon)`` qui calcule l'aire d'un
       disque de rayon donné (:math:`A = \pi r^2`) en utilisant ``math.pi``.
    b. Écrivez une fonction ``aire_disque_depuis_points(xc, yc, xp, yp)`` qui
       prend le centre d'un cercle :math:`(x_c, y_c)` et un point situé sur sa
       circonférence :math:`(x_p, y_p)`, et retourne l'aire du disque en
       composant les fonctions ``distance`` et ``aire_disque``.

    Solution: :ia2:solution:`05.2`

.. ia2:exercice:: 05.3
    Fonctions booléennes et simplification

    Les fonctions peuvent retourner des valeurs booléennes (``True`` ou
    ``False``), ce qui est particulièrement utile pour masquer des tests
    complexes.

    a. Écrivez une fonction ``est_entre(x, y, z)`` qui retourne ``True`` si
       :math:`x \le y \le z` et ``False`` sinon.
    b. Expliquez pourquoi il est inutile d'utiliser une structure ``if ...
       else`` pour retourner directement un résultat booléen et montrez la
       version simplifiée en une seule ligne.

    Solution: :ia2:solution:`05.3`

.. ia2:exercice:: 05.4
    Récursivité et validation des arguments (Gardes)

    Si l'on passe une valeur inattendue (comme un nombre négatif ou un nombre à
    virgule flottante) à une fonction récursive comme la factorielle, le cas de
    base risque de ne jamais être atteint.

    a. Écrivez la définition récursive standard de la fonction
       ``factorielle(n)``.
    b. Ajoutez des vérifications de garde à l'aide de la fonction intégrée
       ``isinstance`` pour vous assurer que ``n`` est bien un entier positif ou
       nul. Si ce n'est pas le cas, affichez un message d'erreur approprié et
       retournez ``None``.

    Solution: :ia2:solution:`05.4`

.. ia2:exercice:: 05.5
    Suite de Fibonacci et l'acte de foi

    L'« acte de foi » (*leap of faith*) consiste à assumer que les appels
    récursifs sur des sous-problèmes plus petits fonctionnent correctement sans
    chercher à suivre mentalement toute l'arborescence des appels.

    a. Écrivez la fonction récursive ``fibonacci(n)`` pour calculer le
       :math:`n`-ième terme de la suite de Fibonacci, définie par :math:`F_0 =
       0`, :math:`F_1 = 1` et :math:`F_n = F_{n-1} + F_{n-2}` pour :math:`n \ge
       2`.
    b. Tracez l'arbre d'exécution des appels récursifs générés lors de
       l'évaluation de ``fibonacci(4)`` et donnez la valeur finale retournée.

    Solution: :ia2:solution:`05.5`

**********
 Solutons
**********

.. ia2:solution:: 05.1
    Valeurs de retour et développement incrémental

    Solution de :ia2:ex:`05.1`

    a. **Formule de la distance euclidienne :**

       .. math::

          d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    b. **Implémentation par développement incrémental :**

       .. code-block:: python

           import math

           def distance(x1, y1, x2, y2):
               dx = x2 - x1
               dy = y2 - y1
               carres = dx**2 + dy**2
               resultat = math.sqrt(carres)
               return resultat

.. ia2:solution:: 05.2
    Composition de fonctions

    Solution de :ia2:ex:`05.2`

    a. **Fonction ``aire_disque`` :**

       .. code-block:: python

           import math

           def aire_disque(rayon):
               return math.pi * (rayon**2)

    b. **Composition dans ``aire_disque_depuis_points`` :**

       .. code-block:: python

           def aire_disque_depuis_points(xc, yc, xp, yp):
               rayon = distance(xc, yc, xp, yp)
               return aire_disque(rayon)

.. ia2:solution:: 05.3
    Fonctions booléennes et simplification

    Solution de :ia2:ex:`05.3`

    a. **Version initiale (avec ``if/else``) :**

       .. code-block:: python

           def est_entre(x, y, z):
               if x <= y <= z:
                   return True
               else:
                   return False

    b. **Explication et version simplifiée :**

       L'expression de comparaison ``x <= y <= z`` évalue déjà directement un booléen (``True`` ou ``False``). Il est donc redondant d'utiliser un bloc ``if ... else`` pour retourner ce même booléen.

       .. code-block:: python

           def est_entre(x, y, z):
               return x <= y <= z

.. ia2:solution:: 05.4
    Récursivité et validation des arguments (Gardes)

    Solution de :ia2:ex:`05.4`

    a et b. **Implémentation récursive avec gardes :**

       .. code-block:: python

           def factorielle(n):
               # Vérification du type (garde)
               if not isinstance(n, int):
                   print("La factorielle est définie uniquement pour les entiers.")
                   return None
               # Vérification du domaine (garde)
               if n < 0:
                   print("La factorielle n'est pas définie pour les entiers négatifs.")
                   return None
               # Cas de base
               if n == 0:
                   return 1
               # Cas récursif
               return n * factorielle(n - 1)

.. ia2:solution:: 05.5
    Suite de Fibonacci et l'acte de foi

    Solution de :ia2:ex:`05.5`

    a. **Fonction récursive ``fibonacci`` :**

       .. code-block:: python

           def fibonacci(n):
               if n == 0:
                   return 0
               if n == 1:
                   return 1
               return fibonacci(n - 1) + fibonacci(n - 2)

    b. **Arbre d'exécution pour ``fibonacci(4)`` :**

       ::

           fibonacci(4)
           ├── fibonacci(3)
           │   ├── fibonacci(2)
           │   │   ├── fibonacci(1) -> 1
           │   │   └── fibonacci(0) -> 0
           │   └── fibonacci(1) -> 1
           └── fibonacci(2)
               ├── fibonacci(1) -> 1
               └── fibonacci(0) -> 0

       * ``fibonacci(2)`` vaut :math:`1 + 0 = 1`
       * ``fibonacci(3)`` vaut :math:`1 + 1 = 2`
       * ``fibonacci(4)`` vaut :math:`2 + 1 = 3`

       **Valeur finale retournée :** ``3``.
