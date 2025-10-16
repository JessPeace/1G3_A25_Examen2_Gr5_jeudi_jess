from debogage_mot_long import mot_plus_long, pourcentage_mots_max

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)

def test_mots_plus_long_mots_liste_correcte():
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", "oiseau"]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 8)

    assert 100.0

def test_mots_plus_long_mots_liste_trop_courte():
    animaux = ["chat"]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 5)

    assert 0.0

def test_mots_plus_long_mots_liste_plusieurs_gros():
    animaux = ["chat","chien","kiwi",'vache']
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 6)

    assert 0.0

def test_mots_plus_long_mots_liste_plus_grande():
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", "oiseau","kiwi",'vache','serpent','chenille', 'ornithorinque','capibara' ]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 10)

    assert 100.0

def test_mots_plus_long_mots_liste_dans_liste():
    animaux = [
        ["chat", "chien", "éléphant", "souris"],
        ["hippopotame",'ornithorinque','capibara','serpent'],
        ["oiseau","kiwi",'vache','chenille']
    ]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 7)

    assert 100.0


# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    mots = ['serpent','chenille', 'ornithorinque','capibara']
    resultat = pourcentage_mots_max(mots, 5) #En mettant count_sup et total_valide à 5 sa fonctionne..

    assert resultat == 100.0

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    mots = ['kiwi','grue','koki','opo']
    resultat = pourcentage_mots_max(mots, 6)
    assert 0.0

def test_pourcentage_mots_max_liste_invalide(): #AHA! Wow, j'ai fallis pas le voir! j'ai changée le nom de la fonction car elle étais la même que celle du haut.
    mots = [7]
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None