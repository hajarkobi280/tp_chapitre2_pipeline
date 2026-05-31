import subprocess
import sys

def run_step(name, command):
    print(f"\n{'='*50}")
    print(f"ETAPE : {name}")
    print(f"{'='*50}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"ERREUR dans {name} !")
        sys.exit(1)
    print(f"✓ {name} terminee avec succes")

# Pipeline complet
run_step("Ingestion", "python pipeline/ingest.py")
run_step("Validation", "python pipeline/validate.py")
run_step("Transformation", "python pipeline/transform.py")
run_step("Tests", "python pipeline/test_data.py")

print(f"\n{'='*50}")
print("PIPELINE COMPLETE AVEC SUCCES !")
print(f"{'='*50}")
