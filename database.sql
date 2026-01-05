-- Contenu de database.sql
CREATE TABLE users (id SERIAL PRIMARY KEY, nom TEXT, prenom TEXT, taille FLOAT);
CREATE TABLE weight_logs (id SERIAL PRIMARY KEY, date_rec DATE, poids FLOAT, imc FLOAT, categorie_imc TEXT);
CREATE TABLE meal_logs (id SERIAL PRIMARY KEY, date_rec DATE, repas TEXT, calories INT);

-- Données de démo obligatoires (Mars à Mai) [cite: 51]
INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES 
('2025-03-10', 85.0, 27.76, 'Surpoids'),
('2025-04-12', 82.5, 26.94, 'Surpoids'),
('2025-05-05', 79.0, 25.80, 'Surpoids');
