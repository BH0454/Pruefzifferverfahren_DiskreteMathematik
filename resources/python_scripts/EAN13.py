def pruefziffer_ean13(basis: str) -> int:
    if len(basis) != 12 or not basis.isdigit():
        raise ValueError("EAN-13 Basisnummer muss aus genau 12 Ziffern bestehen.")
    
    summe = 0
    for i in range(12):
        ziffer = int(basis[i])
        if i % 2 == 0:       # i gerade
            summe += ziffer
        else:                # i ungerade
            summe += 3 * ziffer

    pruefziffer = (10 - (summe % 10)) % 10
    return pruefziffer

print("EAN-13:", "400580882980" + str(pruefziffer_ean13("400580882980")))