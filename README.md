# 🔐 Attacker Recon Framework — V2 (ARF-V2)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Pentest](https://img.shields.io/badge/Pentest-Ethical-red?style=for-the-badge)

</div>

> **A modular, professional offensive reconnaissance framework for ethical security testing and research.**

ARF-V2 is a Python-based reconnaissance framework built with a real-world pentest mindset:
clean architecture, modular design, structured reporting, and extensibility.

⚠️ **For authorized security testing only. Unauthorized use is illegal.**

---

## 🎯 Objectives

ARF-V2 was designed with these principles:

- ✅ Professional, modular architecture  
- ✅ Clear separation of core, recon, and reporting logic  
- ✅ Machine-readable (JSON) + human-readable (PDF) reports  
- ✅ Ready for automation and future CI/CD  
- ✅ Easily extensible with new modules (Auth, API, JWT, etc.)

---

## 🏗️ Project Architecture (V2)

attacker-framework-v2/
│
├── main.py
├── requirements.txt
├── README.md
│
├── core/
│ ├── init.py
│ ├── reporter.py
│ ├── pdf_reporter.py
│ └── logger.py
│
├── recon/
│ ├── init.py
│ ├── dns.py
│ ├── http.py
│ └── port_scan.py
│
└── data/
└── wordlists/


---

## 🔍 Current Capabilities (V2)

### 🔎 DNS Recon (`recon/dns.py`)
- Collects:
  - A, MX, NS, TXT records  
- Returns structured JSON data  

### 🌐 HTTP Fingerprinting (`recon/http.py`)
- Retrieves:
  - HTTP status code  
  - Server header  
  - Timestamp  

### 🔌 Port Scanning (`recon/port_scan.py`)
- Scans common ports:
  - 21, 22, 23, 25, 53, 80, 443, 8080  
- Reports open ports in structured format  

### 📄 Professional Reporting
Generates:
- `report_<target>_<timestamp>.json` → structured findings  
- `report_<target>_<timestamp>.pdf` → executive-ready PDF report  

---

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/attacker-framework-v2.git
cd attacker-framework-v2
pip install -r requirements.txt

▶️ Usage
Basic scan
python3 main.py --target example.com

Output files

You will get:

report_example_com_YYYYMMDD_HHMMSS.json
report_example_com_YYYYMMDD_HHMMSS.pdf

📄 Example PDF Content

The generated PDF includes:

Tool name and target

Timestamp

Findings by module:

DNS records

HTTP status & server

Open ports

🗺️ Roadmap (V3 — Planned)

✅ More professional multi-page PDF report

✅ REST API mode

✅ JWT / Auth testing module

✅ Docker support

✅ Unit tests (pytest)

✅ GitHub Actions CI/CD

✅ Web dashboard for reports

🤝 Contributing

Fork the repository

Create a feature branch

Implement your changes

Submit a Pull Request

⚖️ Legal Disclaimer

This framework is strictly for:

Authorized penetration testing

Cybersecurity research

Security education

Do not use this tool without permission.

👨‍💻 Author

Created by AshDevvv