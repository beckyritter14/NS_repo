@echo off
REM Run onboarding form processing via DuckDB + Pandas

python "C:\Users\britter009\Desktop\NS_onboard_forms\duckdb_cli.py" ^
  --input "C:\Users\britter009\Desktop\NS_onboard_forms\NS_onboard_forms.xlsx" ^
  --sheet "Job" ^
  --output_simple "C:\Users\britter009\Desktop\NS_onboard_forms\output\output_simple.json" ^
  --output_array "C:\Users\britter009\Desktop\NS_onboard_forms\output\output_array.json" ^
  --output_custom "C:\Users\britter009\Desktop\NS_onboard_forms\output\output_custom.json"

pause
