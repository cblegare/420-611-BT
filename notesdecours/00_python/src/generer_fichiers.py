# generer_fichiers.py
import argparse
import os
from pathlib import Path


def generer_fichiers(dossier: Path, nombre: int, taille_mb: int) -> None:
    dossier.mkdir(parents=True, exist_ok=True)
    taille_octets = taille_mb * 1024 * 1024
    taille_bloc = 1024 * 1024  # 1 MB par écriture

    for i in range(1, nombre + 1):
        chemin_fichier = dossier / f"fichier_{i:03d}.bin"
        restant = taille_octets
        with open(chemin_fichier, "wb") as f:
            while restant > 0:
                a_ecrire = min(taille_bloc, restant)
                f.write(os.urandom(a_ecrire))
                restant -= a_ecrire
        print(f"Généré : {chemin_fichier} ({taille_mb} MB)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Génère N fichiers aléatoires de M MB.")
    parser.add_argument("n", type=int, help="Nombre de fichiers à générer")
    parser.add_argument("m", type=int, help="Taille de chaque fichier en MB")
    parser.add_argument(
        "-d",
        "--dossier",
        type=Path,
        default=Path("./donnees_test"),
        help="Répertoire de destination (défaut: ./donnees_test)",
    )
    args = parser.parse_args()
    generer_fichiers(args.dossier, args.n, args.m)


if __name__ == "__main__":
    main()