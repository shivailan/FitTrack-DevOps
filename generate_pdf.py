import sys
from fpdf import FPDF

# Récupération de la taille passée par Jenkins [cite: 66]
taille = sys.argv[2] if len(sys.argv) > 2 else "1.75"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Rapport de Suivi Minceur - FitTrack", ln=1, align='C')
pdf.cell(200, 10, txt=f"Taille enregistrée : {taille} m", ln=2)
pdf.cell(200, 10, txt="Suivi Mars - Mai", ln=3) # Période obligatoire [cite: 4, 31]

# Sauvegarde du fichier que Jenkins va archiver [cite: 63]
pdf.output("Rapport_Final.pdf")
print("Rapport généré avec succès.")