
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
AUDIT_FILE = BASE_DIR / "audit_results.json"

with open(AUDIT_FILE, "r", encoding="utf-8-sig") as file:
    audit = json.load(file)

findings = []

def add_finding(category, status, message):
    findings.append({
        "Category": category,
        "Status": status,
        "Message": message
    })

print("\n===== ENTERPRISE IT SECURITY AUDIT =====")
print("Computer:", audit.get("Hostname", "Unknown"))
print("Operating System:", audit.get("OperatingSystem", "Unknown"))
print()

# Check available disk space
disk = audit.get("DiskFreeGB")

if disk is None:
    add_finding("Disk", "UNKNOWN", "Disk information unavailable")
elif disk < 10:
    add_finding("Disk", "FAIL", "Critically low disk space")
elif disk < 20:
    add_finding("Disk", "WARNING", "Low disk space")
else:
    add_finding("Disk", "PASS", "Available disk space is acceptable")

# Check Windows Firewall profiles
firewalls = audit.get("Firewall", [])

for profile in ["Domain", "Private", "Public"]:
    item = next(
        (f for f in firewalls if f.get("Name") == profile),
        None
    )

    if item is None:
        add_finding(profile + " Firewall", "UNKNOWN",
                    "Firewall status unavailable")
    elif item.get("Enabled") in (True, 1):
        add_finding(profile + " Firewall", "PASS",
                    "Firewall enabled")
    elif item.get("Enabled") in (False, 0):
        add_finding(profile + " Firewall", "FAIL",
                    "Firewall disabled")
    else:
        add_finding(profile + " Firewall", "UNKNOWN",
                    "Unexpected firewall status")

# Check Microsoft Defender
defender = audit.get("Defender")

if defender is None:
    add_finding("Microsoft Defender", "UNKNOWN",
                "Defender information unavailable")
else:
    for key, label in [
        ("AntivirusEnabled", "Antivirus"),
        ("RealTimeProtectionEnabled", "Real-Time Protection")
    ]:
        value = defender.get(key)

        if value is True:
            add_finding(label, "PASS", label + " enabled")
        elif value is False:
            add_finding(label, "FAIL", label + " disabled")
        else:
            add_finding(label, "UNKNOWN",
                        label + " status unavailable")

# Display findings
for finding in findings:
    print(
        f"[{finding['Status']}] "
        f"{finding['Category']}: {finding['Message']}"
    )

# Summary
print("\n===== AUDIT SUMMARY =====")

for status in ["PASS", "WARNING", "FAIL", "UNKNOWN"]:
    count = sum(
        1 for finding in findings
        if finding["Status"] == status
    )
    print(f"{status}: {count}")

# Save report
report_file = BASE_DIR / "security_report.json"

with open(report_file, "w", encoding="utf-8") as file:
    json.dump(findings, file, indent=4)

print("\nReport saved to security_report.json")
