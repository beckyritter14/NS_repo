📄 GitHub Actions Linting Setup (PEP8 + pylint)
Purpose:
Automatically check all Python files for code quality and style issues on every push or pull request to the main branch.

🔧 What It Does
Installs pylint and pycodestyle (PEP8 style checker).

Finds all Python files in the repo.

Runs both linters and uploads the results as downloadable reports.

📁 File Location
.github/workflows/lint.yml

✅ Setup Steps
Copy the provided lint.yml into your repo under .github/workflows/.

Push to the main branch.

Check the Actions tab on GitHub to see results.

🔍 View Reports
Go to Actions.

Click on a workflow run.

Scroll to Artifacts at the bottom to download reports:

pylint.report.txt

pycodestyle.report.txt

🔄 Customization
To lint only specific folders, update find . -name "*.py" to something like find src/ -name "*.py".

To make CI fail on lint errors, remove --exit-zero and || true.

