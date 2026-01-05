import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuration de la connexion (à adapter avec tes accès)
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="fittrack",
        user="postgres",
        password=""
    )

def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5: cat = "Insuffisance"
    elif imc < 25: cat = "Normal"
    elif imc < 30: cat = "Surpoids"
    else: cat = "Obésité"
    return round(imc, 2), cat

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        poids = float(request.form['poids'])
        taille = float(request.form['taille'])
        date_saisie = request.form['date'] # Pour pouvoir remplir Mars à Mai
        
        imc, categorie = calculer_imc(poids, taille)
        
        # Enregistrement obligatoire en base (Exigence 4.3 & 5)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES (%s, %s, %s, %s)",
            (date_saisie, poids, imc, categorie)
        )
        conn.commit()
        cur.close()
        conn.close()
        
    return '''
        <h1>FitTrack - Saisie Quotidienne</h1>
        <form method="post">
            Date: <input type="date" name="date" required><br>
            Poids (kg): <input type="number" step="0.1" name="poids" required><br>
            Taille (m): <input type="number" step="0.01" name="taille" value="1.75" required><br>
            <button type="submit">Enregistrer</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)