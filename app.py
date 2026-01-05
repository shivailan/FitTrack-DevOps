def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5: cat = "Insuffisance"
    elif imc < 25: cat = "Normal"
    elif imc < 30: cat = "Surpoids"
    else: cat = "Obésité"
    return round(imc, 2), cat
