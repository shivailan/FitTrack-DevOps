from app import calculer_imc
def test_calcul_imc():
    score, cat = calculer_imc(70, 1.75)
    assert score == 22.86
    assert cat == "Normal"
