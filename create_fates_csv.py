import pandas as pd

# Läs in Excel-filen
df = pd.read_excel("inputs/datasets/raw/uboat_fates.xlsx")

# Spara som CSV
df.to_csv("inputs/datasets/raw/uboat_fates.csv", index=False)

print("Konvertering klar: uboat_fates.csv skapad ✅")
