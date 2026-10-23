# 🛡️ Enterprise IT Security Audit & Monitoring Dashboard

### Automated Windows Endpoint Security Assessment | Python • PowerShell • SQLite • Streamlit

A Windows security auditing and monitoring project that automates endpoint configuration checks, evaluates security controls, stores historical audit results, and visualizes security posture through an interactive dashboard.

This project demonstrates practical skills in IT administration, security monitoring, Python automation, PowerShell scripting, data analysis, and security reporting.

## 📌 Project Overview

IT administrators need visibility into endpoint security configurations to identify potential security weaknesses and monitor changes over time.

This project simulates an enterprise endpoint security assessment workflow by collecting Windows system information, evaluating selected security controls, recording audit results, and presenting findings through a web-based dashboard.

**Project objectives:**
- Automate Windows endpoint configuration assessments
- Identify disabled or potentially misconfigured security controls
- Reduce repetitive manual security checks
- Maintain historical audit records
- Detect changes between security assessments
- Present security findings in an easy-to-understand dashboard

## 🚀 Key Features

### 1. Automated Windows Security Auditing

Uses PowerShell to collect information about:

- Windows operating system
- Installed system memory
- Available disk space
- Windows Defender antivirus status
- Real-time antivirus protection
- Domain firewall configuration
- Private firewall configuration
- Public firewall configuration

### 2. Security Assessment Engine

A Python-based analysis engine evaluates collected system information and categorizes findings as:

- **PASS:** Configuration meets the implemented check
- **WARNING:** Configuration requires attention
- **FAIL:** Configuration does not meet the implemented check
- **UNKNOWN:** Configuration could not be evaluated

### 3. Interactive Security Dashboard

Developed using Streamlit and Plotly to display:

- System information
- Security assessment summary
- Passed and failed security checks
- Security status visualizations
- Historical audit records
- Security change notifications

### 4. Historical Audit Tracking

SQLite stores historical security assessment summaries, enabling comparison between previous and current audits.

### 5. Security Change Detection

Compares audit results to identify potential changes in endpoint security posture.

Includes simulated security failure scenarios for testing detection and visualization functionality.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Security analysis and reporting |
| PowerShell | Windows configuration collection |
| SQLite | Historical audit storage |
| Streamlit | Interactive web dashboard |
| Pandas | Data processing |
| Plotly | Security data visualization |
| JSON | Structured audit data |

## 🏗️ Project Architecture

The application follows this workflow:

**Windows Endpoint → PowerShell Audit → JSON Data → Python Security Analysis → SQLite Database → Streamlit Dashboard**

1. PowerShell collects system security configuration information.
2. The audit script exports results into a JSON file.
3. Python evaluates security configurations against predefined checks.
4. SQLite records historical audit results.
5. Streamlit displays the assessment and historical trends.
6. Security change detection highlights differences between assessments.

## 📂 Project Structure

```text
Enterprise-IT-Security-Audit/
│
├── audit.ps1
├── analyze_audit.py
├── database.py
├── dashboard.py
├── requirements.txt
├── .gitignore
└── README.md
```

**File descriptions:**

- `audit.ps1` — Collects Windows security configuration data.
- `analyze_audit.py` — Evaluates security checks and generates assessment results.
- `database.py` — Stores historical audit summaries in SQLite.
- `dashboard.py` — Displays security results and audit history.
- `requirements.txt` — Lists required Python packages.
- `.gitignore` — Excludes local data and generated files from version control.

## 💻 Installation and Usage

### Prerequisites

- Windows 10 or Windows 11
- Python 3
- Windows PowerShell
- Required Python packages

### Step 1: Clone the repository

```bash
git clone https://github.com/AmmarPatel780/Enterprise-IT-Security-Audit.git
cd Enterprise-IT-Security-Audit
```

### Step 2: Install dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 3: Run the Windows security audit

Open PowerShell with appropriate permissions and run:

```powershell
powershell.exe -NoProfile -File .\audit.ps1
```

### Step 4: Analyze the audit

```powershell
py analyze_audit.py
```

### Step 5: Save the audit results

```powershell
py database.py
```

### Step 6: Launch the dashboard

```powershell
py -m streamlit run dashboard.py
```

Open the local dashboard at:

`http://localhost:8501`

## 📊 Dashboard Screenshots

### Security Assessment Overview

*Add a screenshot showing Windows system information and the security assessment summary.*

### Historical Security Audits

*Add a screenshot showing historical audit records and security trends.*

### Security Change Alerts

*Add a screenshot showing a simulated security failure and the corresponding alert.*

## 🧪 Testing and Validation

The application was tested on a Windows 11 system.

**Observed assessment results:**
- Six security configuration checks passed during the initial audit.
- Audit summaries were successfully saved in SQLite.
- Historical audit records were displayed in the dashboard.
- Simulated security failures were recorded and visualized.
- Security change notifications distinguished simulated assessments from real audit results.

Simulation results are for demonstration purposes and do not represent actual security incidents.

## 🔒 Security Considerations

- The application performs configuration checks rather than a complete vulnerability assessment.
- Audit findings are limited to the security controls implemented in the scripts.
- Generated audit data may contain sensitive system information and should not be committed to public repositories.
- The application is intended for educational use and authorized endpoint assessments.

## 🎯 Skills Demonstrated

- Windows endpoint administration
- PowerShell automation
- Python scripting
- Security configuration assessment
- Endpoint security monitoring
- Security event and audit reporting
- SQLite database integration
- Data visualization
- Troubleshooting and testing
- Technical documentation

## 🔮 Future Improvements

- Add Windows Update compliance checks
- Implement BitLocker encryption status monitoring
- Support auditing multiple authorized endpoints
- Generate downloadable PDF security reports
- Add email notifications for security configuration changes
- Map selected security checks to recognized security frameworks
- Implement scheduled security assessments

## 👨‍💻 About the Developer

**Ammar Patel**

IT Management Student | Indiana Wesleyan University

Expected Graduation: June 2027

Interested in IT Support, Systems Administration, Cybersecurity, and IT Infrastructure.

[GitHub](https://github.com/AmmarPatel780) | [LinkedIn](https://www.linkedin.com/in/ammarpatel780)

---

*This project was developed as a hands-on learning exercise to strengthen practical IT administration, security monitoring, and automation skills.*
