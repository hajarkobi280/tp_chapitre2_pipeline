import duckdb

db_path = "ventes.duckdb"
con = duckdb.connect(db_path)

# Créer la table nettoyée
con.execute(\"\"\"
    CREATE OR REPLACE TABLE ventes_clean AS
    SELECT 
        date,
        produit,
        categorie,
        quantite,
        prix_unitaire,
        ville,
        quantite * prix_unitaire AS chiffre_affaires
    FROM ventes_raw
    WHERE quantite > 0 AND prix_unitaire > 0
\"\"\")

# Créer le résumé par catégorie
con.execute(\"\"\"
    CREATE OR REPLACE TABLE ventes_resume AS
    SELECT 
        categorie,
        SUM(quantite) AS total_quantite,
        SUM(chiffre_affaires) AS total_ca
    FROM ventes_clean
    GROUP BY categorie
\"\"\")

con.close()
print("Transformation terminee : ventes_clean et ventes_resume creees")
