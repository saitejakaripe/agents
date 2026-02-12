import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root: .../agents/.env
ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

# IMPORTANT: run from project_3 folder so output/ goes inside project_3
PROJECT_DIR = Path(__file__).parent
os.chdir(PROJECT_DIR)

# Ensure output folder exists
(PROJECT_DIR / "output").mkdir(exist_ok=True)

from crew.project_3.crew import ResearchCrew


def run(company: str = "Apple"):
    result = ResearchCrew().crew().kickoff(inputs={"company": company})
    print("\n\n=== FINAL REPORT ===\n")
    print(result)
    print("\nSaved to: crew/project_3/output/report.md")


if __name__ == "__main__":
    run()
