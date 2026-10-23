
import json
import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Enterprise IT Security Audit",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Enterprise IT Security Audit")
st.caption("Windows Endpoint Monitoring & Security Assessment")

# Load audit data
try:
    with open(BASE_DIR / "audit_results.json", encoding="utf-8-sig") as f:
        audit = json.load(f)

    with open(BASE_DIR / "security_report.json", encoding="utf-8") as f:
        findings = json.load(f)

except (FileNotFoundError, json.JSONDecodeError) as error:
    st.error(f"Unable to load audit files: {error}")
    st.stop()

# SYSTEM OVERVIEW
st.subheader("System Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Operating System",
    audit.get("OperatingSystem", "Unknown")
)
col2.metric(
    "Installed RAM",
    f"{audit.get('TotalRAMGB', 0)} GB"
)
col3.metric(
    "Free Disk Space",
    f"{audit.get('DiskFreeGB', 0)} GB"
)

st.divider()

# SECURITY ASSESSMENT
st.subheader("Security Assessment")

df = pd.DataFrame(findings)
counts = df["Status"].value_counts()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Passed", int(counts.get("PASS", 0)))
col2.metric("Warnings", int(counts.get("WARNING", 0)))
col3.metric("Failed", int(counts.get("FAIL", 0)))
col4.metric("Unknown", int(counts.get("UNKNOWN", 0)))

fig = px.bar(
    df,
    x="Category",
    color="Status",
    title="Security Audit Results",
    color_discrete_map={
        "PASS": "#22c55e",
        "WARNING": "#f59e0b",
        "FAIL": "#ef4444",
        "UNKNOWN": "#64748b"
    }
)

st.plotly_chart(fig, width="stretch")

st.subheader("Detailed Findings")
st.dataframe(df, width="stretch", hide_index=True)

st.subheader("Export Security Report")

st.download_button(
    "Download CSV Report",
    data=df.to_csv(index=False),
    file_name="security_audit_report.csv",
    mime="text/csv"
)

st.caption(
    "Security assessment is based on selected Windows configuration "
    "checks and does not represent a complete vulnerability assessment."
)

# HISTORICAL AUDITS
st.divider()
st.subheader("Historical Security Audits")

db_path = BASE_DIR / "audit_history.db"

if db_path.exists():
    with sqlite3.connect(db_path) as conn:
        history = pd.read_sql_query(
            """
            SELECT id, timestamp, hostname,
                   passed, warnings, failed, unknown
            FROM audits
            ORDER BY id
            """,
            conn
        )

    if not history.empty:
        st.dataframe(
            history,
            width="stretch",
            hide_index=True
        )

        fig_history = px.line(
            history,
            x="timestamp",
            y=["passed", "warnings", "failed"],
            markers=True,
            title="Security Audit History"
        )

        st.plotly_chart(fig_history, width="stretch")
else:
    st.info("No saved audit history yet.")

# SECURITY CHANGE ALERTS
st.divider()
st.subheader("Security Change Alerts")

if db_path.exists():
    with sqlite3.connect(db_path) as conn:
        records = conn.execute("""
            SELECT id, hostname, findings_json
            FROM audits
            ORDER BY id DESC
            LIMIT 2
        """).fetchall()

    if len(records) >= 2:
        latest = {
            item["Category"]: item
            for item in json.loads(records[0][2])
        }

        previous = {
            item["Category"]: item
            for item in json.loads(records[1][2])
        }

        changes = []

        for category in sorted(set(latest) | set(previous)):
            old_status = previous.get(
                category, {}
            ).get("Status", "MISSING")

            new_status = latest.get(
                category, {}
            ).get("Status", "MISSING")

            if old_status != new_status:
                changes.append(
                    (category, old_status, new_status)
                )

        if "[SIMULATION]" in records[0][1]:
            st.warning(
                "Latest audit is simulated, not a real security scan."
            )

        if changes:
            for category, old_status, new_status in changes:
                message = (
                    f"{category}: {old_status} → {new_status}"
                )

                if new_status == "FAIL":
                    st.error("Security alert: " + message)
                elif new_status == "PASS":
                    st.success(
                        "Security improvement: " + message
                    )
                else:
                    st.warning("Status changed: " + message)
        else:
            st.info(
                "No status changes between the two latest audits."
            )
    else:
        st.info("At least two audits are required.")
else:
    st.info("No audit database found.")
