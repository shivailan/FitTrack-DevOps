import sys
import argparse
import psycopg2 # Ou import mysql.connector
from fpdf import FPDF

# 1. Récupération des paramètres envoyés par Jenkins
parser = argparse.ArgumentParser()
parser.add_argument('--taille', type=float, default=1.75)
parser.add_argument('--nom', type=str, default="Utilisateur")
args = parser.parse_args()

# 2. Connexion à la base de données
def fetch_data():
    conn = psycopg2.connect(host="localhost", database="fittrack", user="shiva", password="")
    cur = conn.cursor()
    
    # Récupération du suivi poids/IMC (Période Mars à Mai exigée)
    cur.execute("SELECT date_rec, poids, imc, categorie_imc FROM weight_logs WHERE date_rec BETWEEN '2025-03-01' AND '2025-05-31' ORDER BY date_rec")
    logs = cur.fetchall()
    
    cur.close()
    conn.close()
    return logs

# 3. Création du PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'FitTrack - Rapport de Suivi Minceur', 0, 1, 'C')
        self.ln(10)

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Informations Profil (Exigence 4.1)
pdf.cell(0, 10, f"Utilisateur : {args.nom}", ln=True)
pdf.cell(0, 10, f"Taille enregistree : {args.taille} m", ln=True)
pdf.ln(5)

# Tableau du Journal de Suivi (Exigence 4.3 & 4.4)
pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Date", 1)
pdf.cell(30, 10, "Poids (kg)", 1)
pdf.cell(30, 10, "IMC", 1)
pdf.cell(60, 10, "Categorie", 1)
pdf.ln()

pdf.set_font("Arial", size=12)
data = fetch_data()
for row in data:
    pdf.cell(40, 10, str(row[0]), 1)
    pdf.cell(30, 10, str(row[1]), 1)
    pdf.cell(30, 10, str(row[2]), 1)
    pdf.cell(60, 10, str(row[3]), 1)
    pdf.ln()

# Sauvegarde du fichier pour Jenkins
pdf.output("Rapport_Final_FitTrack.pdf")
print("PDF généré avec succès pour l'archive Jenkins.")