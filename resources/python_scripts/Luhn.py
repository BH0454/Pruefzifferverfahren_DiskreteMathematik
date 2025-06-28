def pruefziffer_luhn(basis: str) -> int:
    if not basis.isdigit():
        raise ValueError("Luhn-Basis muss Ziffern enthalten.")

    ziffern = list(map(int, basis[::-1]))  
    summe = 0

    for i, z in enumerate(ziffern):
        if i % 2 == 0:  
            doppelt = 2 * z
            summe += doppelt if doppelt < 10 else doppelt - 9  
        else:
            summe += z

    pruefziffer = (10 - (summe % 10)) % 10
    return pruefziffer

print("Luhn:", "49164940314172" + str(pruefziffer_luhn("49164940314172")))



