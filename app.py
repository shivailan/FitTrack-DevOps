from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(host="localhost", database="fittrack", user="shiva", password="")

def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5: cat = "Insuffisance weight"
    elif imc < 25: cat = "Normal"
    elif imc < 30: cat = "Surpoids"
    else: cat = "Obésité"
    return round(imc, 2), cat

# Design HTML/CSS avec Bootstrap
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FitTrack - Suivi Minceur</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .card { border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .btn-primary { background-color: #007bff; border: none; }
        .header-title { color: #2c3e50; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card p-4">
                    <h2 class="text-center header-title mb-4">FitTrack Suivi Quotidien</h2>
                    
                    {% if message %}
                    <div class="alert alert-success" role="alert">
                        {{ message }}
                    </div>
                    {% endif %}

                    <form method="post">
                        <div class="mb-3">
                            <label class="form-label">Date du relevé</label>
                            <input type="date" name="date" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Poids (kg)</label>
                            <input type="number" step="0.1" name="poids" class="form-control" placeholder="ex: 75.5" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Taille (m)</label>
                            <input type="number" step="0.01" name="taille" class="form-control" value="1.75" required>
                        </div>
                        <div class="d-grid gap-2">
                            <button type="submit" class="btn btn-primary btn-lg">Calculer et Enregistrer</button>
                        </div>
                    </form>
                    <hr>
                    <p class="text-muted text-center small">Interface connectée à PostgreSQL - Pipeline Jenkins opérationnel</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    if request.method == 'POST':
        try:
            poids = float(request.form['poids'])
            taille = float(request.form['taille'])
            date = request.form['date']
            imc, cat = calculer_imc(poids, taille)
            
            conn = get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES (%s, %s, %s, %s)", (date, poids, imc, cat))
            conn.commit()
            cur.close()
            conn.close()
            message = f"Succès ! IMC : {imc} ({cat}) enregistré pour le {date}."
        except Exception as e:
            message = f"Erreur : {str(e)}"
    
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)