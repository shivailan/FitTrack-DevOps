-- Création des tables [cite: 47, 48, 49]
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    sexe CHAR(1),
    date_naissance DATE,
    taille FLOAT
);

CREATE TABLE weight_logs (
    id SERIAL PRIMARY KEY,
    date_rec DATE,
    poids FLOAT,
    imc FLOAT,
    categorie_imc TEXT
);

CREATE TABLE meal_logs (
    id SERIAL PRIMARY KEY,
    date_rec DATE,
    repas TEXT,
    calories INT
);

-- Données de démo obligatoires (Mars à Mai) [cite: 51, 85]
INSERT INTO weight_logs (date_rec, poids, imc, categorie_imc) VALUES 
('2025-03-10', 85.0, 27.76, 'Surpoids'),
('2025-04-12', 82.5, 26.94, 'Surpoids'),
('2025-05-05', 79.0, 25.80, 'Surpoids');

INSERT INTO meal_logs (date_rec, repas, calories) VALUES 
('2025-03-10', 'Petit-déjeuner', 500),
('2025-04-12', 'Déjeuner', 700),
('2025-05-05', 'Dîner', 600);