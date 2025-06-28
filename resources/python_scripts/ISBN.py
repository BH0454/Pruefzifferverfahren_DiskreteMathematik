def ist_gueltige_isbn10(isbn: str) -> bool:
    if len(isbn) != 10:
        return False

    summe = 0
    for i in range(10):
        zeichen = isbn[i]
        if i == 9 and zeichen == 'X':
            wert = 10
        elif zeichen.isdigit():
            wert = int(zeichen)
        else:
            return False  
        summe += (10 - i) * wert

    return summe % 11 == 0

print(ist_gueltige_isbn10("382742559X"))  
print(ist_gueltige_isbn10("3827425591"))  