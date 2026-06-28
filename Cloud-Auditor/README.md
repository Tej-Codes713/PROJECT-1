# ☁️ Cloud Infrastructure Auditor & Cost Optimizer

> A professional-grade **Python-based Cloud Infrastructure Auditor** that scans AWS resources, identifies idle or misconfigured infrastructure, estimates potential monthly savings, and provides an interactive dashboard with security insights, AI recommendations, and cloud analytics.

---

## 🚀 Overview

Cloud Infrastructure Auditor is a DevOps and FinOps automation tool that helps organizations reduce cloud costs by identifying unused or underutilized AWS resources.

The application scans multiple AWS services, generates detailed reports, estimates monthly savings, highlights security issues, and presents the results in a modern Flask dashboard.

---

# ✨ Features

## ☁ AWS Resource Scanning

* ✅ EC2 Instance Scanner
* ✅ Unused EBS Volume Scanner
* ✅ Elastic IP Scanner
* ✅ S3 Bucket Scanner
* ✅ IAM User Scanner
* ✅ Security Group Scanner

---

## 💰 Cost Optimization

* Monthly Savings Estimation
* Region-wise Cost Breakdown
* Top Costly Resources
* Executive Cost Dashboard

---

## 🛡 Security Center

* IAM User Analysis
* Security Group Analysis
* Security Recommendations
* Resource Health Monitoring

---

## 🤖 AI Features

* AI Recommendations
* AI Risk Score
* AI Cost Prediction
* Natural Language Search

---

## 📊 Interactive Dashboard

* Executive Dashboard
* Animated Charts (Chart.js)
* Dark / Light Mode
* Responsive Layout
* Live Statistics
* Region Overview
* Scan History
* Loading Animation

---

## 📁 Report Generation

* JSON Export
* CSV Export
* CLI Reports

---

## 🧹 Cleanup

Supports safe cleanup suggestions for:

* Unused EBS Volumes
* Elastic IPs
* Idle EC2 Instances

---

# 🏗 Project Architecture

```text
                    AWS Account
                         │
                         ▼
                Boto3 Resource Scanners
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
    EC2               EBS Scanner       IAM Scanner

      ▼                  ▼                  ▼

Elastic IP          S3 Scanner      Security Groups

              ▼

      Cost Calculator

              ▼

     Recommendation Engine

              ▼

        Flask Dashboard

              ▼

      Charts + Reports
```

---

# 📂 Folder Structure

```text
Cloud-Auditor/

│

├── dashboard.py

├── main.py

├── requirements.txt

├── README.md

│

├── scanners/

│   ├── ec2_scanner.py

│   ├── ebs_scanner.py

│   ├── eip_scanner.py

│   ├── s3_scanner.py

│   ├── iam_scanner.py

│   └── security_group_scanner.py

│

├── recommendations/

│   ├── ai_engine.py

│   ├── security_center.py

│   ├── region_cost.py

│   ├── dashboard_summary.py

│   └── ...

│

├── reports/

│   ├── report_generator.py

│   ├── exporter.py

│   └── cost_calculator.py

│

├── cleanup/

│   └── cleanup_manager.py

│

├── history/

│   └── history_manager.py

│

├── templates/

│   └── index.html

│

├── static/

│   ├── style.css

│   ├── dashboard.js

│   └── loader.js

│

└── exports/
```

---

# 🛠 Tech Stack

### Programming Language

* Python 3.x

### Backend

* Flask

### Cloud SDK

* Boto3

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Reports

* JSON
* CSV

### Cloud Platform

* Amazon Web Services (AWS)

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Cloud-Auditor.git

cd Cloud-Auditor
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the CLI

```bash
python main.py scan
```

---

# ▶ Run Dashboard

```bash
python dashboard.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📸 Dashboard Preview

## Executive Dashboard

> Add Screenshot Here

```
screenshots/dashboard.png
```

---

## Security Center

> Add Screenshot Here

```
screenshots/security.png
```

---

## Cost Dashboard

> Add Screenshot Here

```
screenshots/cost.png
```

---

## Region Overview

> Add Screenshot Here

```
screenshots/region.png
```

---

# 📈 Dashboard Features

* Executive Dashboard
* Cost Analytics
* Cloud Health
* Security Center
* Region Overview
* AI Recommendations
* AI Cost Prediction
* AI Risk Score
* Scan History
* Charts
* Dark Mode

---

# 📊 Reports

Supported Formats

* JSON
* CSV

Example

```
exports/

audit_report.json

audit_report.csv
```

---

# 🔒 Security

The application only uses your configured AWS credentials.

No credentials are stored.

Supports IAM authentication through Boto3.

---

# 🚀 Future Enhancements

* Docker Support
* PDF Reports
* Email Notifications
* Multi-Cloud Support (AWS + GCP + Azure)
* Auto Scan Scheduler
* Kubernetes Scanner
* Terraform Analysis
* CI/CD Integration

---

# 🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* AWS SDK (Boto3)
* Flask Development
* DevOps Automation
* FinOps Principles
* Cloud Cost Optimization
* Security Auditing
* Dashboard Development
* Report Generation
* Data Visualization

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sai Nadh**

GitHub:
https://github.com/SAINADH-24

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
