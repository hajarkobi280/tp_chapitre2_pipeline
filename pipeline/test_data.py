import duckdb

db_path = "ventes.duckdb"
con = duckdb.connect(db_path)

# Test 1 : Verifier que ventes_clean n'a pas de NULL dans produit
null_produits = con.execute("SELECT COUNT(*) FROM ventes_clean WHERE produit IS NULL").fetchone()[0]
assert null_produits == 0, f"ERREUR : {null_produits} produits NULL"

# Test 2 : Verifier que ventes_clean n'a pas de quantite <= 0
bad_quantite = con.execute("SELECT COUNT(*) FROM ventes_clean WHERE quantite <= 0").fetchone()[0]
assert bad_quantite == 0, f"ERREUR : {bad_quantite} lignes avec quantite <= 0"

# Test 3 : Verifier que ventes_resume a des categories non NULL
null_categorie = con.execute("SELECT COUNT(*) FROM ventes_resume WHERE categorie IS NULL").fetchone()[0]
assert null_categorie == 0, f"ERREUR : {null_categorie} categories NULL"

# Test 4 : Verifier que le total CA est coherent
total_ca_raw = con.execute("SELECT SUM(chiffre_affaires) FROM ventes_clean").fetchone()[0]
total_ca_resume = con.execute("SELECT SUM(total_ca) FROM ventes_resume").fetchone()[0]
assert total_ca_raw == total_ca_resume, f"ERREUR : CA incoherent {total_ca_raw} != {total_ca_resume}"

con.close()
print("Tous les tests sont passes avec succes !")
