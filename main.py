def verifier_fermat(
    a: int,
    b: int,
    c: int,
    n: int
):
    egal = a**n + b**n == c**n
    if egal and n >= 2:
        print("Bon sang, Fermat avait tord!")
    elif egal:
        print("L'égalité est juste!")
    else:
        print("Ça ne fonctionne pas")
