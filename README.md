# threatscope-cti
Automated Cyber Threat Intelligence (CTI) engine for IOC extraction, OSINT aggregation, and dynamic risk scoring.
# ThreatScope - Cyber Threat Intelligence (CTI) Engine

ThreatScope is a modular, high-performance Python framework designed for automated **Indicator of Compromise (IOC)** extraction, threat aggregation, and multi-factor risk scoring from unstructured logs and threat feeds.

---

## Key Features

- **Automated IOC Extraction:** Fast Regex parsing for IPv4, IPv6, MD5, SHA256 hashes, and malicious domains.
- **Threat Aggregation Engine:** Correlates real-time reputation and abuse reports.
- **Dynamic Risk Scorer:** Heuristic calculation engine mapping threats into severity tiers (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
- **SOC-Ready Architecture:** Clean, modular structure built for SIEM and SOC automation pipelines.

---

## Architecture Overview

```text
threatscope-cti/
├── core/
│   ├── extractor.py       # IOC parsing & regex validation
│   ├── aggregator.py      # Threat reputation querying
│   └── scorer.py          # Dynamic risk severity calculation
├── requirements.txt       # Dependencies
├── main.py                # Pipeline entry point
└── README.md              # Project documentation



Getting Started
1. Clone the Repository
Bash
git clone [https://github.com/pairates077-ship/threatscope-cti.git](https://github.com/pairates077-ship/threatscope-cti.git)
cd threatscope-cti
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run Threat Analysis
Bash
python main.py
License
Distributed under the MIT License. See LICENSE for more information.
