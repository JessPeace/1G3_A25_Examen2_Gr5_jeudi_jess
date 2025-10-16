from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)

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
    resultat = pourcentage_mots_max(mots, 5) #avec count_sup et total_valide a 5 sa marche, mais je doutes que sa marches autrement.

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

def test_pourcentage_mots_max_liste_invalide(): #AHA. wow j'ai fallis pas le voir!
    mots = 7
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None