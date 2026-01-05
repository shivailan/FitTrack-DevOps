from app import calculer_imc

def test_calculer_imc():
    # Test d'un cas normal : 80kg pour 1.80m
    score, categorie = calculer_imc(80, 1.80)
    assert score == 24.69
    assert categorie == "Normal"