#######################################
 Programmation asynchrone : async/await
#######################################

**************************************
 Le problème de l'exécution synchrone
**************************************

Jusqu'à présent, nos programmes Python s'exécutaient de manière **synchrone**
(ou séquentielle) : chaque instruction attend que la précédente soit terminée
avant de commencer.

Prenons l'exemple d'une fonction qui simule le téléchargement d'une page web
à l'aide du module ``time`` :

.. code-block:: python

    import time

    def telecharger_page(url):
        print(f"Début du téléchargement de {url}")
        time.sleep(2)  # Simule une attente réseau de 2 secondes
        print(f"Fin du téléchargement de {url}")
        return f"Contenu de {url}"

Si nous appelons cette fonction deux fois de suite, le programme reste bloqué
pendant 4 secondes au total :

.. code-block:: python

    debut = time.time()
    telecharger_page("site1.com")
    telecharger_page("site2.com")
    print(f"Temps total : {time.time() - debut:.2f} s")

À l'affichage, nous obtenons :

.. code-block:: text

    Début du téléchargement de site1.com
    Fin du téléchargement de site1.com
    Début du téléchargement de site2.com
    Fin du téléchargement de site2.com
    Temps total : 4.00 s

Pendant que ``time.sleep(2)`` s'exécute, le processeur ne fait rien : il attend.
Dans le cas d'opérations d'entrée/sortie (**E/S** ou *I/O* en anglais), comme
les requêtes réseau ou la lecture de fichiers, ce temps d'attente est gaspillé.

La **programmation asynchrone** permet de résoudre ce problème en autorisant
un programme à mettre une tâche en pause lorsqu'elle attend une ressource externe,
afin d'exécuter une autre tâche pendant ce temps.

*********************
 Coroutines et async
*********************

Pour écrire du code asynchrone en Python, nous utilisons le module intégré
``asyncio`` ainsi que deux nouveaux mots-clés : ``async`` et ``await``.

Lorsque vous définissez une fonction avec ``async def`` au lieu de ``def``,
vous créez une **fonction coroutine** :

.. code-block:: python

    import asyncio

    async def saluer():
        print("Bonjour !")

Contrairement à une fonction classique, appeler ``saluer()`` n'exécute pas
immédiatement le code à l'intérieur. Cela renvoie un objet **coroutine** :

.. code-block:: python-console

    >>> cor = saluer()
    >>> print(cor)
    <coroutine object saluer at 0x7f8b1c2d3e40>

Pour exécuter réellement une coroutine, il faut la confier à une **boucle
d'événements** (*event loop*). La fonction ``asyncio.run()`` crée cette boucle,
exécute la coroutine jusqu'à sa fin, puis ferme la boucle :

.. code-block:: python-console

    >>> asyncio.run(saluer())
    Bonjour !

.. note::

    Si vous créez une coroutine sans l'exécuter avec ``asyncio.run()`` ou
    ``await``, Python affichera un avertissement ``RuntimeWarning: coroutine
    'saluer' was never awaited``.

.. ia2:exercice::
    :id: async-ex-1

    Définissez une coroutine nommée ``dire_bonjour`` qui prend un ``nom`` en
    paramètre et affiche ``"Bonjour <nom> !"``. Exécutez ensuite cette
    coroutine pour le nom ``"Alice"`` à l'aide de ``asyncio.run()``.

.. ia2:solution::
    :id: async-ex-1

    .. code-block:: python

        import asyncio

        async def dire_bonjour(nom):
            print(f"Bonjour {nom} !")

        asyncio.run(dire_bonjour("Alice"))

****************************
 Mettre en pause avec await
****************************

Le mot-clé ``await`` permet de suspendre l'exécution de la coroutine courante
jusqu'à ce qu'une opération asynchrone (appelée un objet **awaitable**) soit
terminée. Pendant cette pause, la boucle d'événements est libre d'exécuter
d'autres tâches.

Dans un contexte asynchrone, on remplace ``time.sleep()`` (qui bloque tout le
programme) par ``asyncio.sleep()`` (qui met uniquement la coroutine en pause) :

.. code-block:: python

    import asyncio

    async def telecharger_page_async(url):
        print(f"Début du téléchargement de {url}")
        await asyncio.sleep(2)  # Pause non bloquante de 2 secondes
        print(f"Fin du téléchargement de {url}")
        return f"Contenu de {url}"

Il est important de retenir deux règles fondamentales :

* Le mot-clé ``await`` ne peut être utilisé **qu'à l'intérieur** d'une fonction
  définie avec ``async def``.
* On ne peut utiliser ``await`` que devant un objet **awaitable** (comme une
  coroutine ou une tâche).

Si nous écrivons une coroutine principale qui enchaîne deux appels avec ``await`` :

.. code-block:: python

    import time

    async def main():
        debut = time.time()
        await telecharger_page_async("site1.com")
        await telecharger_page_async("site2.com")
        print(f"Temps total : {time.time() - debut:.2f} s")

    asyncio.run(main())

L'exécution prend encore 4 secondes ! En effet, ``await`` attend que la première
coroutine soit complètement finie avant de passer à la ligne suivante. Pour
gagner du temps, nous devons exécuter ces coroutines de manière **concurrente**.

.. ia2:exercice::
    :id: async-ex-2

    Écrivez une coroutine appelée ``compte_a_rebours`` qui prend un entier
    ``n`` en paramètre, affiche les nombres de ``n`` jusqu'à ``1`` en attendant
    1 seconde entre chaque affichage avec ``asyncio.sleep(1)``, puis affiche
    ``"Décollage !"``. Testez-la avec ``n = 3``.

.. ia2:solution::
    :id: async-ex-2

    .. code-block:: python

        import asyncio

        async def compte_a_rebours(n):
            for i in range(n, 0, -1):
                print(i)
                await asyncio.sleep(1)
            print("Décollage !")

        asyncio.run(compte_a_rebours(3))

**********************************
 Exécution concurrente avec gather
**********************************

Pour exécuter plusieurs coroutines en même temps (de façon concurrente sur un
seul fil d'exécution), le module ``asyncio`` fournit la fonction
``asyncio.gather()``.

``asyncio.gather()`` prend plusieurs coroutines en arguments, les planifie
simultanément dans la boucle d'événements, et renvoie une liste contenant
leurs valeurs de retour dans l'ordre où elles ont été passées :

.. code-block:: python

    async def main():
        debut = time.time()
        resultats = await asyncio.gather(
            telecharger_page_async("site1.com"),
            telecharger_page_async("site2.com")
        )
        print(f"Résultats : {resultats}")
        print(f"Temps total : {time.time() - debut:.2f} s")

    asyncio.run(main())

Voici ce qui s'affiche maintenant :

.. code-block:: text

    Début du téléchargement de site1.com
    Début du téléchargement de site2.com
    Fin du téléchargement de site1.com
    Fin du téléchargement de site2.com
    Résultats : ['Contenu de site1.com', 'Contenu de site2.com']
    Temps total : 2.00 s

Le temps total est passé de 4 secondes à 2 secondes : les deux attentes se sont
superposées.

.. ia2:exercice::
    :id: async-ex-3

    Écrivez une coroutine ``obtenir_valeur(x, delai)`` qui attend ``delai``
    secondes puis renvoie ``x * 10``. Dans une coroutine ``main()``, utilisez
    ``asyncio.gather()`` pour appeler ``obtenir_valeur(2, 1)`` et
    ``obtenir_valeur(5, 2)`` en même temps, puis affichez la somme des deux
    résultats.

.. ia2:solution::
    :id: async-ex-3

    .. code-block:: python

        import asyncio

        async def obtenir_valeur(x, delai):
            await asyncio.sleep(delai)
            return x * 10

        async def main():
            res = await asyncio.gather(
                obtenir_valeur(2, 1),
                obtenir_valeur(5, 2)
            )
            print(f"Somme : {sum(res)}")

        asyncio.run(main())

************************
 Gestion avec les Tasks
************************

Parfois, vous souhaitez lancer une coroutine en arrière-plan, faire autre
chose pendant qu'elle avance, puis récupérer son résultat plus tard. Pour cela,
on enveloppe la coroutine dans une **tâche** (*Task*) à l'aide de
``asyncio.create_task()``.

Dès que ``asyncio.create_task()`` est appelée, la coroutine est programmée pour
s'exécuter dès que possible :

.. code-block:: python

    async def main():
        # Planifie immédiatement les deux tâches
        tache1 = asyncio.create_task(telecharger_page_async("site1.com"))
        tache2 = asyncio.create_task(telecharger_page_async("site2.com"))

        print("Les téléchargements sont lancés en arrière-plan...")

        # Attend la fin des tâches et récupère leurs résultats
        res1 = await tache1
        res2 = await tache2
        print(f"Terminé : {res1}, {res2}")

    asyncio.run(main())

Vous pouvez également annuler une tâche en cours grâce à sa méthode
``cancel()`` :

.. code-block:: python

    tache = asyncio.create_task(telecharger_page_async("site_lent.com"))
    await asyncio.sleep(0.5)
    tache.cancel()

.. ia2:exercice::
    :id: async-ex-4

    Créez une coroutine ``preparer_cafe()`` qui attend 2 secondes et renvoie
    ``"Café prêt"``, ainsi qu'une coroutine ``griller_pain()`` qui attend 1
    seconde et renvoie ``"Pain grillé"``. Utilisez ``asyncio.create_task()``
    dans ``main()`` pour lancer les deux préparations en même temps et affichez
    les deux résultats.

.. ia2:solution::
    :id: async-ex-4

    .. code-block:: python

        import asyncio

        async def preparer_cafe():
            await asyncio.sleep(2)
            return "Café prêt"

        async def griller_pain():
            await asyncio.sleep(1)
            return "Pain grillé"

        async def main():
            tache_cafe = asyncio.create_task(preparer_cafe())
            tache_pain = asyncio.create_task(griller_pain())

            cafe = await tache_cafe
            pain = await tache_pain
            print(f"{cafe} et {pain} !")

        asyncio.run(main())


*****************************************
 Synchronisation : Verrous et Sémaphores
*****************************************

Lorsque plusieurs coroutines s'exécutent de manière concurrente, il est parfois
nécessaire de coordonner leur accès à une ressource partagée ou de limiter le
nombre d'opérations simultanées. Le module ``asyncio`` fournit deux mécanismes
principaux pour contrôler cette concurrence : les **verrous** (*locks* ou
*mutex*) et les **sémaphores**.


Verrous (``asyncio.Lock``)
==========================

Même si le code asynchrone s'exécute sur un seul fil d'exécution, une coroutine
peut être interrompue à chaque instruction ``await``. Si deux coroutines lisent
et modifient une même ressource partagée de part et d'autre d'un ``await``,
leurs opérations peuvent s'entrelacer et produire un résultat incohérent. Ce
problème s'appelle une **situation de compétition** (*race condition*).

Un **verrou** (*mutex*, pour *mutual exclusion*) garantit qu'une seule
coroutine à la fois peut exécuter une portion critique de code. On l'utilise
généralement avec le gestionnaire de contexte asynchrone ``async with`` :

.. code-block:: python

    import asyncio

    solde = 100
    verrou = asyncio.Lock()

    async def retirer(montant):
        global solde
        async with verrou:  # Acquiert le verrou (attend s'il est déjà pris)
            if solde >= montant:
                nouveau_solde = solde - montant
                await asyncio.sleep(0.1)  # Simule une opération réseau/BD
                solde = nouveau_solde
                print(f"Retrait de {montant} $ réussi. Solde : {solde} $")
            else:
                print(f"Fonds insuffisants pour {montant} $.")

    async def main():
        await asyncio.gather(retirer(80), retirer(80))

    asyncio.run(main())

Sans ``async with verrou:``, les deux coroutines liraient un solde de ``100``
avant la mise à jour et autoriseraient deux retraits de ``80 $``, laissant un
solde de ``20 $`` au lieu de refuser la seconde opération.

.. note::

    N'utilisez jamais ``threading.Lock`` dans une coroutine : s'il est déjà
    verrouillé, il bloquera toute la boucle d'événements. Utilisez toujours
    ``asyncio.Lock``.


Sémaphores (``asyncio.Semaphore``)
==================================

Alors qu'un verrou limite l'accès à **une seule** coroutine, un **sémaphore**
permet à au plus $N$ coroutines d'accéder simultanément à une ressource.

Un sémaphore maintient un compteur interne initialisé à $N$ :

* À l'entrée d'un bloc ``async with semaphore:``, le compteur est décrémenté.
  Si le compteur est supérieur à zéro, la coroutine poursuit immédiatement.
  S'il vaut zéro, la coroutine est mise en pause jusqu'à ce qu'une place se
  libère.
* À la sortie du bloc ``async with semaphore:``, le compteur est incrémenté,
  réveillant la prochaine coroutine en attente.

Les sémaphores sont très utiles pour éviter de saturer un serveur distant ou
un disque lors du lancement d'un grand nombre de tâches avec
``asyncio.gather()`` :

.. code-block:: python

    import asyncio

    # Autorise au maximum 3 requêtes simultanées
    limite = asyncio.Semaphore(3)

    async def interroger_api(numero):
        async with limite:
            print(f"Requête {numero} : début")
            await asyncio.sleep(1)
            print(f"Requête {numero} : fin")

    async def main():
        taches = [interroger_api(i) for i in range(1, 8)]
        await asyncio.gather(*taches)

    asyncio.run(main())

Dans cet exemple, bien que 7 tâches soient lancées en même temps, elles
s'exécutent par vagues de 3 maximum.

.. ia2:exercice::
    :id: async-sync-1

    Vous devez télécharger 10 fichiers identifiés par les entiers ``1`` à
    ``10``. Écrivez une coroutine ``telecharger_fichier(id_fichier, semaphore)``
    qui affiche ``"Téléchargement #<id>..."``, attend 1 seconde avec
    ``asyncio.sleep(1)``, puis affiche ``"Fichier #<id> terminé."``.
    Utilisez un ``asyncio.Semaphore(2)`` dans ``main()`` pour garantir qu'au
    plus 2 téléchargements s'exécutent en parallèle.

.. ia2:solution::
    :id: async-sync-1

    .. code-block:: python

        import asyncio

        async def telecharger_fichier(id_fichier, semaphore):
            async with semaphore:
                print(f"Téléchargement #{id_fichier}...")
                await asyncio.sleep(1)
                print(f"Fichier #{id_fichier} terminé.")

        async def main():
            sem = asyncio.Semaphore(2)
            taches = [telecharger_fichier(i, sem) for i in range(1, 11)]
            await asyncio.gather(*taches)

        asyncio.run(main())


**********
 Débogage
**********

L'erreur la plus fréquente en programmation asynchrone consiste à oublier le
mot-clé ``await`` devant l'appel d'une coroutine :

.. code-block:: python

    async def calculer():
        return 42

    async def main():
        valeur = calculer()  # Oubli de await !
        print(valeur + 1)

Ce code provoque une ``TypeError`` car ``valeur`` est un objet coroutine et non
un entier :

.. code-block:: text

    TypeError: unsupported operand type(s) for +: 'coroutine' and 'int'

Une autre erreur courante est d'appeler une fonction bloquante (comme
``time.sleep()`` ou ``requests.get()``) à l'intérieur d'une coroutine. Cela
fige toute la boucle d'événements et annule les bénéfices de l'asynchrone.

Si vous utilisez ``await`` en dehors d'une fonction ``async def``, Python
lèvera une erreur de syntaxe :

.. code-block:: text

    SyntaxError: 'await' outside function

***********
 Glossaire
***********

.. glossary::

    programmation synchrone
    synchronous programming
        Mode d'exécution où les instructions sont exécutées l'une après l'autre, chaque opération bloquant la suite jusqu'à sa fin.

    programmation asynchrone
    asynchronous programming
        Mode d'exécution permettant à une tâche de céder le contrôle pendant une phase d'attente afin que d'autres tâches puissent progresser.

    coroutine
        Fonction définie avec ``async def`` dont l'exécution peut être suspendue et reprise. L'appel d'une fonction coroutine renvoie un objet coroutine.

    boucle d'événements
    event loop
        Mécanisme central du module ``asyncio`` qui orchestre, planifie et exécute les coroutines et les tâches.

    awaitable
        Tout objet pouvant être utilisé avec l'expression ``await`` (principalement les coroutines et les objets ``Task``).

    tâche
    task
        Enveloppe autour d'une coroutine créée avec ``asyncio.create_task()``, permettant de planifier son exécution concurrente dans la boucle d'événements.

    concurrence
    concurrency
        Capacité d'un programme à gérer plusieurs tâches qui progressent durant la même période, en alternant leur exécution lors des temps d'attente.



***********
 Exercices
***********

.. ia2:exercice::
    :id: async-ex-5

    Le code ci-dessous contient deux erreurs qui l'empêchent de fonctionner
    correctement de manière asynchrone. Corrigez-le pour qu'il affiche ``15``
    au bout d'une seule seconde :

    .. code-block:: python

        import asyncio
        import time

        async def doubler(n):
            time.sleep(1)
            return n * 2

        async def main():
            a = doubler(5)
            b = doubler(2.5)
            print(a + b)

        asyncio.run(main())

.. ia2:solution::
    :id: async-ex-5

    Il fallait remplacer ``time.sleep(1)`` par ``await asyncio.sleep(1)`` et
    exécuter les deux coroutines de façon concurrente avec ``asyncio.gather()``
    (ou utiliser ``await``) :

    .. code-block:: python

        import asyncio

        async def doubler(n):
            await asyncio.sleep(1)
            return n * 2

        async def main():
            a, b = await asyncio.gather(doubler(5), doubler(2.5))
            print(int(a + b))

        asyncio.run(main())

.. ia2:exercice::
    :id: async-ex-6

    Écrivez une coroutine appelée ``verifier_serveur`` qui prend en paramètres
    un nom de serveur (chaîne) et un délai de réponse (flottant). Elle doit
    afficher ``"Vérification de <serveur>..."``, attendre ``delai`` secondes
    avec ``asyncio.sleep()``, puis renvoyer le tuple ``(serveur, "EN LIGNE")``.
    Créez ensuite une coroutine ``surveiller_parc`` qui prend une liste de
    tuples ``[(nom, delai), ...]``, lance toutes les vérifications en parallèle
    avec ``asyncio.gather()`` et affiche la liste des résultats retournés.

.. ia2:solution::
    :id: async-ex-6

    .. code-block:: python

        import asyncio

        async def verifier_serveur(serveur, delai):
            print(f"Vérification de {serveur}...")
            await asyncio.sleep(delai)
            return (serveur, "EN LIGNE")

        async def surveiller_parc(serveurs):
            taches = [verifier_serveur(nom, delai) for nom, delai in serveurs]
            resultats = await asyncio.gather(*taches)
            print(resultats)

        parc = [("web-01", 1.5), ("db-01", 2.0), ("cache-01", 0.5)]
        asyncio.run(surveiller_parc(parc))