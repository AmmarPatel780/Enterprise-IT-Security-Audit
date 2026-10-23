
import sqlite3
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "audit_history.db"

def save_audit():
    with open(BASE_DIR / "audit_results.json", encoding="utf-8-sig") as f:
        audit = json.load(f)

    with open(BASE_DIR / "security_report.json", encoding="utf-8") as f:
        findings = json.load(f)

    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                hostname TEXT,
                operating_system TEXT,
                passed INTEGER,
                warnings INTEGER,
                failed INTEGER,
                unknown INTEGER,
                findings_json TEXT NOT NULL
            )
        """)

        counts = {
            status: sum(
                1 for item in findings
                if item["Status"] == status
            )
            for status in ["PASS", "WARNING", "FAIL", "UNKNOWN"]
        }

        conn.execute("""
            INSERT INTO audits (
                timestamp, hostname, operating_system,
                passed, warnings, failed, unknown, findings_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            audit.get("ScanTime", datetime.now().isoformat()),
            audit.get("Hostname", "Unknown"),
            audit.get("OperatingSystem", "Unknown"),
            counts["PASS"],
            counts["WARNING"],
            counts["FAIL"],
            counts["UNKNOWN"],
            json.dumps(findings)
        ))

        conn.commit()

    print("Audit saved to SQLite database successfully!")

if __name__ == "__main__":
    save_audit()
