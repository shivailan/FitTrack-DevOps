from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Connexion BDD [cite: 19]
def get_db():
    return psycopg2.connect(host="localhost", database="fittrack", user="shiva", password="")

# Calcul IMC obligatoire [cite: 35, 37, 38]
def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5: cat = "Insuffisance"
    elif imc < 25: cat = "Normal"
    elif imc < 30: cat = "Surpoids"
    else: cat = "Obésité"
    return round(imc, 2), cat

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        poids = float(request.form['poids'])
        taille = float(request.form['taille'])
        date = request.form['date']
        imc, cat = calculer_imc(poids, taille)
        
        # Stockage IMC + Catégorie obligatoire [cite: 39]
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES (%s, %s, %s, %s)", (date, poids, imc, cat))
        conn.commit()
        return f"Enregistré : IMC {imc} ({cat})"
    
    return '''<form method="post">
        Date: <input type="date" name="date"><br>
        Poids: <input type="number" step="0.1" name="poids"><br>
        Taille: <input type="number" step="0.01" name="taille" value="1.75"><br>
        <input type="submit">
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)