from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

# Load .env from project root: /Users/udaykumar/agents/.env
ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

# Ensure output folder exists (tasks.yaml writes output/*)
(Path(__file__).parent / "output").mkdir(exist_ok=True)

from crew.project_2.crew import StockPicker

def run():
    inputs = {
        "sector": "Technology",
        "current_date": str(datetime.now()),
    }

    result = StockPicker().crew().kickoff(inputs=inputs)

    print("\n\n=== FINAL DECISION ===\n")
    print(result)

if __name__ == "__main__":
    run()

