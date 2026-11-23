"""
Découvrir le traitement d'entrées-sorties en calculant les sommes de contrôles.

Utilisez `generer_fichiers.py` pour produire des fichiers au contenu aléatoire,
puis lancer ce fichier-ci pour calculer les sommes de contrôle.

Une somme de contrôle[1] (checksum en anglais) est une courte séquence de
données numériques calculée à partir d'un bloc de données plus important
(par exemple un fichier ou un message) permettant de vérifier, avec une
très haute probabilité, que l'intégrité de ce bloc a été préservée lors
d'une opération de copie, stockage ou transmission.
On parle aussi parfois d'empreinte numérique. Pour l'utilisateur final,
les sommes de contrôle se présentent typiquement sous la forme de nombres
au format hexadécimal.
L'utilisation d'une somme de contrôle est une forme de contrôle par redondance.
"""

import asyncio
import hashlib
from pathlib import Path
import time


def calculer_md5_par_bloc(fichier_ouvert, taille_bloc: int = 8192) -> str:
    """Calcule le checksum MD5 d'un fichier déjà ouvert en lecture binaire."""
    hash_md5 = hashlib.md5()
    while bloc := fichier_ouvert.read(taille_bloc):
        hash_md5.update(bloc)
    return hash_md5.hexdigest()


class FichierChecksum:
    def __init__(self, chemin: Path):
        """
        Représente un fichier pour lequel on calculera la somme de contrôle.

        Args:
            chemin:
                Le chemin (*path*) de ce fichier.
        """
        self.chemin = chemin
        self.checksum: str | None = None

    def calculer_sync(self) -> str:
        with open(self.chemin, "rb") as f:
            self.checksum = calculer_md5_par_bloc(f)
        return self.checksum

    async def calculer_async(self) -> str:
        # Délègue la lecture disque bloquante à un fil d'exécution secondaire
        return await asyncio.to_thread(self.calculer_sync)


class GestionnaireChecksum:
    def __init__(self, repertoire: Path, max_concurrence: int = 4):
        """
        Gère la lecture des sommes de contrôle de fichier d'un répertoire.

        Args:
            repertoire:
                Dossier contenant les fichiers à vérifie le checksum
            max_concurrence:
                Nous limitons la concurence possible sans quoi la lecture
                en parallèle pourrait être moins performante qu'en séquence!
                Plusieurs raisons peuvent expliquer ceci:

                *   hashlib.md5() libère bien le GIL, mais si les fichiers
                    sont déjà en cache mémoire (RAM) après la passe synchrone,
                    le calcul devient purement lié au processeur (CPU-bound)
                    ou sature la bande passante mémoire/SSD.
                    Créer et synchroniser des threads ajoute alors uniquement
                    de la surcharge (overhead).

                *   Sur un SSD ou un disque dur classique, lancer 20 ou 50
                    lectures simultanées dans différents threads provoque
                    des accès concurrents aléatoires au lieu d'une lecture
                    séquentielle fluide.
        """
        self.repertoire = repertoire
        self.fichiers: list[FichierChecksum] = []
        self.semaphore = asyncio.Semaphore(max_concurrence)

    async def _calculer_avec_limite(self, fichier: FichierChecksum) -> str:
        async with self.semaphore:
            return await fichier.calculer_async()

    async def executer_async(self) -> None:
        taches = [self._calculer_avec_limite(f) for f in self.fichiers]
        await asyncio.gather(*taches)

    def executer_sync(self) -> None:
        for fichier in self.fichiers:
            fichier.calculer_sync()

    def scanner_repertoire(self) -> None:
        self.fichiers = [
            FichierChecksum(p)
            for p in sorted(self.repertoire.iterdir())
            if p.is_file()
        ]


async def main() -> None:
    dossier = Path("./donnees_test")
    gestionnaire = GestionnaireChecksum(dossier)
    gestionnaire.scanner_repertoire()

    if not gestionnaire.fichiers:
        print(f"Aucun fichier trouvé dans {dossier}.")
        return

    # Exécution synchrone
    debut_sync = time.perf_counter()
    gestionnaire.executer_sync()
    duree_sync = time.perf_counter() - debut_sync
    print(f"Mode synchrone  ({len(gestionnaire.fichiers)} fichiers) : {duree_sync:.4f} s")

    # Réinitialisation des empreintes avant le test asynchrone
    gestionnaire_synchrone = gestionnaire
    gestionnaire = GestionnaireChecksum(dossier)
    gestionnaire.scanner_repertoire()

    # Exécution asynchrone
    debut_async = time.perf_counter()
    await gestionnaire.executer_async()
    duree_async = time.perf_counter() - debut_async
    print(f"Mode asynchrone ({len(gestionnaire.fichiers)} fichiers) : {duree_async:.4f} s")

    gestionnaire_asynchrone = gestionnaire

    comparatif: dict[Path, tuple[str, str]] = {
        f_sync.chemin: (f_sync.checksum, f_async.checksum)
        for f_sync, f_async in zip(
            sorted(gestionnaire_synchrone.fichiers, key=lambda f: f.chemin),
            sorted(gestionnaire_asynchrone.fichiers, key=lambda f: f.chemin)
        )
    }

    # Affichage des résultats
    print("\nChecksums calculés :")
    for path, checksums in comparatif.items():
        checksum_sync, checksum_async = checksums
        identique = "identique" if checksum_sync == checksum_async else "différents"
        print(f"  {path} : {checksum_sync} {identique}")


if __name__ == "__main__":
    asyncio.run(main())