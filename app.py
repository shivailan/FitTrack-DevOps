from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(host="localhost", database="fittrack", user="shiva", password="")

# --- NOUVELLE FONCTION : LOGIQUE DE NOTIFICATION ENCOURAGEANTE ---
def generer_notification_motivante(imc_actuel, imc_precedent):
    if imc_precedent is None:
        return "C'est votre premier relevé ! Bienvenue dans votre parcours de santé. 💪"
    
    if imc_actuel < imc_precedent:
        return f"Incroyable ! Votre IMC a baissé (passant de {imc_precedent} à {imc_actuel}). Vos efforts paient vraiment ! 🌟"
    elif imc_actuel == imc_precedent:
        return "Votre IMC est stable. La régularité est la clé du succès, continuez ainsi ! 👍"
    else:
        # RÉSULTAT NON FAVORABLE MAIS MESSAGE POSITIF (Consigne 7 Janv)
        return f"Votre IMC est de {imc_actuel}. Rappelez-vous : le progrès n'est pas une ligne droite. Demain est une nouvelle opportunité, restez motivé ! 😊"

def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5: cat = "Insuffisance"
    elif imc < 25: cat = "Normal"
    elif imc < 30: cat = "Surpoids"
    else: cat = "Obésité"
    return round(imc, 2), cat

# --- MISE À JOUR DU DESIGN POUR LES NOTIFICATIONS ---
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>FitTrack - Version Optimisée</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f1f3f5; }
        .card { border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); border: none; }
        .alert-info { background-color: #e7f3ff; border-left: 5px solid #007bff; color: #0056b3; }
        .header-title { color: #2c3e50; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-7">
                <div class="card p-4">
                    <h2 class="text-center header-title mb-4">WeightWise : Coaching Agile</h2>
                    
                    {% if notification %}
                    <div class="alert alert-info shadow-sm mb-4" role="alert">
                        <h5 class="alert-heading">📢 Message de l'équipe :</h5>
                        <p class="mb-0">{{ notification }}</p>
                    </div>
                    {% endif %}

                    {% if error %}
                    <div class="alert alert-danger">{{ error }}</div>
                    {% endif %}

                    <form method="post">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Date du relevé</label>
                                <input type="date" name="date" class="form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Poids actuel (kg)</label>
                                <input type="number" step="0.1" name="poids" class="form-control" required>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Taille habituelle (m)</label>
                            <input type="number" step="0.01" name="taille" class="form-control" value="1.75" required>
                        </div>
                        <div class="d-grid">
                            <button type="submit" class="btn btn-primary btn-lg">Actualiser mon IMC</button>
                        </div>
                    </form>
                    <hr>
                    <div class="text-center">
                        <span class="badge bg-success">Culture DevOps Active</span>
                        <span class="badge bg-info">Jira Synced</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    notification = None
    error = None
    if request.method == 'POST':
        try:
            poids = float(request.form['poids'])
            taille = float(request.form['taille'])
            date = request.form['date']
            imc, cat = calculer_imc(poids, taille)
            
            conn = get_db()
            cur = conn.cursor()
            
            # 1. RÉCUPÉRER LE DERNIER IMC POUR COMPARER (Actualisation auto)
            cur.execute("SELECT imc FROM weight_logs ORDER BY date_rec DESC LIMIT 1")
            row = cur.fetchone()
            ancien_imc = row[0] if row else None
            
            # 2. GÉNÉRER LA NOTIFICATION ENCOURAGEANTE
            notification = generer_notification_motivante(imc, ancien_imc)
            
            # 3. ENREGISTRER DANS LA BASE
            cur.execute("INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES (%s, %s, %s, %s)", (date, poids, imc, cat))
            conn.commit()
            cur.close()
            conn.close()
            
        except Exception as e:
            error = f"Erreur de connexion : {str(e)}"
    
    return render_template_string(HTML_TEMPLATE, notification=notification, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)