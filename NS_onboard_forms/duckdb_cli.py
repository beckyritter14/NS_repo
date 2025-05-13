# --------------------------------------------- CLI FORMAT ---------------------------------------------
'''
# INSTALL DUCKDB AND PANDAS (if you haven't yet): 
pip install duckdb[excel] openpyxl pandas 
'''

import duckdb
import pandas as pd
import json
import argparse
import sys

# ---------- ARGUMENTS ----------
parser = argparse.ArgumentParser(description="Read Excel → SQL → JSON via DuckDB")
parser.add_argument("--input", required=True, help="Path to Excel file (.xlsx)")
parser.add_argument("--sheet", required=True, help="Sheet name to read from")
parser.add_argument("--output_simple", required=False, help="Path for newline-delimited JSON")
parser.add_argument("--output_array", required=False, help="Path for flat JSON array")
parser.add_argument("--output_custom", required=False, help="Path for nested custom JSON")
args = parser.parse_args()

# ---------- STEP 1: LOAD EXCEL ----------
print("[STEP 1] Reading Excel using pandas...")
try:
    df_raw = pd.read_excel(args.input, sheet_name=args.sheet, engine="openpyxl")
    print(f"[✅] Loaded sheet '{args.sheet}' from '{args.input}'")
    print("[DEBUG] Columns:", df_raw.columns.tolist())
except Exception as e:
    print("[❌] Failed to read Excel:", e)
    sys.exit(1)

# ---------- STEP 2: RUN SQL TRANSFORMATION ----------
print("[STEP 2] Running SQL transformation using DuckDB...")
try:
    con = duckdb.connect()
    con.register("raw_data", df_raw)
    con.execute("""
    CREATE OR REPLACE TABLE transformed AS
    SELECT
        Job_ID             AS id,
        UPPER(Job_Name)    AS job_name,
        External_Job_Type  AS job_type
    FROM raw_data
    WHERE Job_Name IS NOT NULL;
    """)
    print("[✅] SQL transformation complete.")
except Exception as e:
    print("[❌] SQL failed:", e)
    sys.exit(1)

# ---------- STEP 3: PREVIEW ----------
print("[STEP 3] Preview of transformed data:")
try:
    print(con.execute("SELECT * FROM transformed LIMIT 5").fetchdf())
except Exception as e:
    print("[⚠️] Could not show preview:", e)

# ---------- STEP 4: EXPORTS ----------

# A. Newline-delimited JSON
if args.output_simple:
    try:
        df = con.execute("SELECT * FROM transformed").fetchdf()
        df.to_json(args.output_simple, orient="records", lines=True)
        print(f"[✅] Flat JSON written to {args.output_simple}")
    except Exception as e:
        print("[❌] Failed to export flat JSON:", e)

# B. JSON array
if args.output_array:
    try:
        if 'df' not in locals():
            df = con.execute("SELECT * FROM transformed").fetchdf()
        df.to_json(args.output_array, orient="records", indent=2)
        print(f"[✅] Array JSON written to {args.output_array}")
    except Exception as e:
        print("[❌] Failed to export array JSON:", e)

# C. Custom nested JSON
if args.output_custom:
    try:
        if 'df' not in locals():
            df = con.execute("SELECT * FROM transformed").fetchdf()

        records = []
        for _, row in df.iterrows():
            records.append({
                "jobId": row["id"],
                "profile": {"fullName": row["job_name"]},
                "metrics": {"type": row["job_type"]}
            })

        with open(args.output_custom, "w", encoding="utf-8") as f:
            json.dump({"data": records, "count": len(records)}, f, indent=2)
        print(f"[✅] Custom JSON written to {args.output_custom}")
    except Exception as e:
        print("[❌] Failed to export custom JSON:", e)







''' 
# --------------------------------------- TERMINAL INSTRUCTIONS --------------------------------------------
# OPTION 1 - CLI CONTENTS: What to put into the terminal to generate all 3 outputs (simple, array, and custom JSON files)

python duckdb_cli.py `
  --input "C:/Users/you/Documents/intake_form.xlsx" `
  --sheet "Job" `
  --output_simple "C:/Users/you/Documents/output_simple.json" `
  --output_array "C:/Users/you/Documents/output_array.json" `
  --output_custom "C:/Users/you/Documents/output_custom.json"


  

# OPTION 2 - .BAT FILE: what to put into the terminal to run the .bat file (that contains the input, sheet, outputs) --> EASIEST

./run_onboard_transform.bat

  




# ------------------------------------------- TERMINAL EXAMPLES --------------------------------------------------
  
# OPTION 1 (CLI) Example: 
python "C:/Users/britter009/Desktop/NS_onboard_forms/duckdb_cli.py" `
  --input "C:/Users/britter009/Desktop/NS_onboard_forms/NS_onboard_forms.xlsx" `
  --sheet "Job" `
  --output_simple "C:/Users/britter009/Desktop/output_simple.json" `
  --output_array "C:/Users/britter009/Desktop/output_array.json" `
  --output_custom "C:/Users/britter009/Desktop/output_custom.json"



# OPTION 2 (.BAT) Example: 
./run_onboard_transform.bat


'''