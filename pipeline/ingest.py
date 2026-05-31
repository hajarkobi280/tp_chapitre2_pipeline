import pandas as pd
import duckdb
from pathlib import Path

csv_path = Path("data/ventes.csv")
db_path = "ventes.duckdb"

df = pd.read_csv(csv_path)
con = duckdb.connect(db_path)
con.execute("CREATE OR REPLACE TABLE ventes_raw AS SELECT * FROM df")
con.close()

print("Ingestion terminee : ventes_raw creee dans DuckDB")
