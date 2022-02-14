def hangrend(szo):
    melymagan =['a','á','o','ó','u','ú']
    magasmagan=['e','i','í','ü','ű','ö','ő','é']
    voltmely = False
    voltmagas = False
    for betu in szo:
        if betu in melymagan:
            voltmely = True
        elif betu in magasmagan:
            voltmagas = True
    if voltmely and not voltmagas:
        return('mely')
    elif not voltmely and voltmagas:
        return('magas')
    elif voltmely and voltmagas:
        return('vegyes')
    else:
        return('nincssemmulol')