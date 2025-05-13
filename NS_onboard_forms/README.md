# NS Onboard Form Processor

This utility reads Excel-based onboarding forms and transforms them into structured JSON outputs using DuckDB and pandas.

---

## 🧰 Requirements

Install the necessary Python packages:

```bash
pip install duckdb pandas openpyxl
```

---

## 📄 Files Included

- `duckdb_cli.py` — Python script that processes Excel data using SQL
- `NS_onboard_forms.xlsx` — Input Excel file
- `run_onboard_transform.bat` — Easy-run script for Windows

---

## ▶️ How to Run

### ✅ Option 1: Run using the `.bat` file

Double-click the file:
```
run_onboard_transform.bat
```

Or run it from PowerShell:

```powershell
\.run_onboard_transform.bat
```

> This will process the `Job` sheet in the Excel and output **all three** JSON formats to your Desktop.

---

### ✅ Option 2: Run directly from the terminal

If you want to run manually or customize it:

```powershell
python "C:/Users/britter009/Desktop/NS_onboard_forms/duckdb_cli.py" `
  --input "C:/Users/britter009/Desktop/NS_onboard_forms/NS_onboard_forms.xlsx" `
  --sheet "Job" `
  --output_simple "C:/Users/britter009/Desktop/output_simple.json" `
  --output_array "C:/Users/britter009/Desktop/output_array.json" `
  --output_custom "C:/Users/britter009/Desktop/output_custom.json"
```

---

## 🔄 Customizing Output

You **do not need to generate all three** JSON files every time.

- You can **edit the `.bat` file** and remove the output options you don’t want.
- Or, when running from the terminal, you can include **just one** of the output flags like this:

```powershell
python duckdb_cli.py `
  --input "your_excel_file.xlsx" `
  --sheet "Job" `
  --output_custom "your_custom_output.json"
```

Only the JSON formats you specify will be created.

---

## ✅ Output Files

- `output_simple.json` — Newline-delimited flat JSON
- `output_array.json` — JSON array of objects
- `output_custom.json` — Nested JSON with profile/metrics structure

---

## 💡 Notes

- You can change `--sheet` to another tab like `Workflow`, `Source_Details`, etc.
- Ensure the input Excel has columns like `Job_ID`, `Job_Name`, and `External_Job_Type`
- The script pauses after execution so you can review results.
