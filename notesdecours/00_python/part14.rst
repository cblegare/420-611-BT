#####################
 Classes et méthodes
#####################

*********************************
 Fonctionnalités orientées objet
*********************************

Python est un langage de programmation orienté objet, ce qui signifie qu'il
fournit des fonctionnalités qui prennent en charge la programmation orientée
objet.

Il n'est pas facile de définir la programmation orientée objet, mais nous en
avons déjà vu certaines caractéristiques :

* Les programmes sont constitués de définitions d'objets et de fonctions, et la
  plus grande partie du calcul s'exprime en termes d'opérations sur les objets.
* Chaque définition d'objet correspond à un objet ou à un concept du monde réel,
  et les fonctions qui opèrent sur cet objet correspondent aux manières dont les
  objets du monde réel interagissent.

Jusqu'à présent, nous n'avons pas profité des fonctionnalités que Python fournit
pour prendre en charge la programmation orientée objet. Ces fonctionnalités ne
sont pas strictement nécessaires ; la plupart d'entre elles fournissent une
syntaxe alternative pour des choses que nous avons déjà faites. Mais dans de
nombreux cas, l'alternative est plus concise et exprime plus précisément la
structure du programme.

Une méthode est une fonction qui est associée à une classe particulière. Les
méthodes sont sémantiquement identiques aux fonctions, mais il y existe deux
différences syntaxiques :

* Les méthodes sont définies à l'intérieur d'une définition de classe afin de
  rendre explicite la relation entre la classe et la méthode.
* La syntaxe pour invoquer une méthode est différente de la syntaxe pour appeler
  une fonction.

*********************
 Impression d'objets
*********************

Pour transformer une fonction en méthode, tout ce que nous avons à faire est de
déplacer la définition de la fonction à l'intérieur de la définition de la
classe. Par convention, le premier paramètre d'une méthode est appelé ``self``.

Dans la programmation orientée objet, les objets sont les agents actifs. Une
invocation de méthode comme ``start.print_time()`` signifie « Hé start ! S'il te
plaît, affiche-toi ».

.. topic:: Exercice

    Réécrivez ``time_to_int`` (de la section 16.4) sous forme de méthode.

******************
 Un autre exemple
******************

Voici une version de ``increment`` (de la section 16.3) réécrite sous forme de
méthode :

.. code-block:: python

    # à l'intérieur de la classe Time :


    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

Le sujet, ``start``, est affecté au premier paramètre, ``self``. L'argument,
``1337``, est affecté au second paramètre, ``seconds``.

***************************
 Un exemple plus compliqué
***************************

``is_after`` est légèrement plus compliqué car il prend deux objets ``Time``
comme paramètres. Dans ce cas, il est conventionnel de nommer le premier
paramètre ``self`` et le second paramètre ``other`` :

.. code-block:: python

    # à l'intérieur de la classe Time :


    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

*********************
 La méthode ``init``
*********************

La méthode ``init`` (abréviation d'« initialisation ») est une méthode spéciale
qui est invoquée lorsqu'un objet est instancié. Son nom complet est
``__init__``.

Une méthode ``init`` pour la classe ``Time`` pourrait ressembler à ceci :

.. code-block:: python

    # à l'intérieur de la classe Time :


    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

Les paramètres sont optionnels, donc si vous appelez ``Time`` sans arguments,
vous obtenez les valeurs par défaut.

.. topic:: Exercice

    Écrivez une méthode ``init`` pour la classe ``Point`` qui prend ``x`` et
    ``y`` comme paramètres optionnels et les affecte aux attributs
    correspondants.

************************
 La méthode ``__str__``
************************

``__str__`` est une méthode spéciale, comme ``__init__``, qui est censée
renvoyer une représentation sous forme de chaîne de caractères d'un objet.

.. code-block:: python

    # à l'intérieur de la classe Time :


    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

Lorsque vous affichez un objet, Python invoque la méthode ``str``.

.. topic:: Exercice

    Écrivez une méthode ``str`` pour la classe ``Point``. Créez un objet
    ``Point`` et affichez-le.

**************************
 Surcharge des opérateurs
**************************

En définissant d'autres méthodes spéciales, vous pouvez spécifier le
comportement des opérateurs sur les types définis par l'utilisateur. Par
exemple, si vous définissez une méthode nommée ``__add__`` pour la classe
``Time``, vous pouvez utiliser l'opérateur ``+`` sur les objets ``Time``.

.. code-block:: python

    # à l'intérieur de la classe Time :


    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

Modifier le comportement d'un opérateur pour qu'il fonctionne avec des types
définis par l'utilisateur s'appelle la **surcharge des opérateurs**.

.. topic:: Exercice

    Écrivez une méthode ``add`` pour la classe ``Point``.

*******************************
 Répartition basée sur le type
*******************************

La fonction intégrée ``isinstance`` prend une valeur et un objet classe, et
renvoie ``True`` si la valeur est une instance de la classe.

Cette opération est appelée une **répartition basée sur le type** (*type-based
dispatch*) parce qu'elle répartit le calcul vers différentes méthodes en
fonction du type des arguments.

La méthode spéciale ``__radd__`` signifie « addition côté droit » (*right-side
add*). Cette méthode est invoquée lorsqu'un objet ``Time`` apparaît du côté
droit de l'opérateur ``+``.

.. topic:: Exercice

    Écrivez une méthode ``add`` pour les points qui fonctionne soit avec un
    objet ``Point``, soit avec un tuple.

***************
 Polymorphisme
***************

Les fonctions qui peuvent fonctionner avec plusieurs types sont dites
**polymorphes**. Le polymorphisme peut faciliter la réutilisation du code.

En général, si toutes les opérations à l'intérieur d'une fonction fonctionnent
avec un type donné, alors la fonction fonctionne avec ce type.

**********
 Débogage
**********

Une autre façon d'accéder aux attributs d'un objet est d'utiliser l'attribut
spécial ``__dict__``, qui est un dictionnaire qui associe des noms d'attributs
(sous forme de chaînes) et des valeurs.

La fonction intégrée ``getattr`` prend un objet et un nom d'attribut (sous forme
de chaîne) et renvoie la valeur de l'attribut.

*****************************
 Interface et implémentation
*****************************

Un principe de conception qui aide à atteindre l'objectif de maintenabilité est
de **garder les interfaces séparées des implémentations**. Pour les objets, cela
signifie que les méthodes fournies par une classe ne doivent pas dépendre de la
façon dont les attributs sont représentés.

Garder l'interface séparée de l'implémentation signifie que vous devez cacher
les attributs. Le code dans les autres parties du programme doit utiliser des
méthodes pour lire et modifier l'état de l'objet, sans accéder directement aux
attributs. Ce principe est appelé **masquage de l'information** (*information
hiding*).

.. topic:: Exercice

    Téléchargez le code de ce chapitre (http://thinkpython.com/code/Time2.py).
    Modifiez les attributs de ``Time`` pour qu'ils soient un seul entier
    représentant les secondes depuis minuit. Modifiez ensuite les méthodes (et
    la fonction ``int_to_time``) pour qu'elles fonctionnent avec la nouvelle
    implémentation.

***********
 Glossaire
***********

.. glossary::

    langage orienté objet
    object-oriented language
        Un langage qui fournit des fonctionnalités, telles que des classes définies par l'utilisateur et une syntaxe de méthode, qui facilitent la programmation orientée objet.

    programmation orientée objet
    object-oriented programming
        Un style de programmation dans lequel les données et les opérations qui les manipulent sont organisées en classes et en méthodes.

    méthode
    method
        Une fonction qui est définie à l'intérieur d'une définition de classe et est invoquée sur des instances de cette classe.

    sujet
    subject
        L'objet sur lequel une méthode est invoquée.

    surcharge des opérateurs
    operator overloading
        Modifier le comportement d'un opérateur comme ``+`` pour qu'il fonctionne avec un type défini par l'utilisateur.

    répartition basée sur le type
    type-based dispatch
        Un modèle de programmation qui vérifie le type d'un opérande et invoque différentes fonctions pour différents types.

    polymorphe
    polymorphic
        Relatif à une fonction qui peut fonctionner avec plus d'un type.

    masquage de l'information
    information hiding
        Le principe selon lequel l'interface fournie par un objet ne doit pas dépendre de son implémentation, en particulier de la représentation de ses attributs.

***********
 Exercices
***********

.. topic:: Exercice

    Écrivez une définition pour une classe nommée ``Kangaroo`` avec les méthodes
    suivantes : une méthode ``__init__`` qui initialise un attribut nommé
    ``pouch_contents`` à une liste vide ; une méthode nommée ``put_in_pouch``
    qui ajoute un objet à la poche ; et une méthode ``__str__`` pour afficher le
    kangourou et le contenu de sa poche.

.. topic:: Exercice

    Le module ``Visual`` fournit des graphiques 3D. Modifiez le programme pour
    que chaque sphère dans un cube ait la couleur qui correspond à sa position
    dans l'espace RGB.
