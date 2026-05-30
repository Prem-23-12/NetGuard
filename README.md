# NetGuard

## Port Scan Detection and Open Port Monitoring System

NetGuard is a Python-based cybersecurity monitoring tool designed to detect suspicious port scanning activity and monitor open ports on a local machine. The project helps identify potential reconnaissance attempts by tracking connection patterns and generating alerts, reports, and monitoring data.

---

## Features

### Port Scan Detection

* Detects suspicious scanning behavior based on configurable thresholds.
* Tracks unique ports accessed by a source IP.
* Supports time-window-based analysis.

### Alert Management

* Generates real-time alerts for suspicious activity.
* Stores alerts in log files for future analysis.

### Report Generation

* Creates structured JSON reports.
* Maintains historical records of detected events.

### Open Port Monitoring

* Scans common local ports.
* Identifies currently open services.
* Generates machine-readable port reports.

### Dashboard (In Progress)

* Displays open ports.
* Displays detected alerts.
* Provides security statistics and monitoring insights.

---

## Project Architecture

```text
Network Events
      │
      ▼
Scan Detector
      │
      ▼
Alert Manager
      │
      ▼
Report Generator
      │
      ▼
JSON Reports
      │
      ▼
Dashboard
```

---

## Project Structure

```text
NetGuard/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── detector/
│   ├── scan_detector.py
│   ├── alert_manager.py
│   ├── report_generator.py
│   └── port_monitor.py
│
├── logs/
│   └── alerts.log
│
├── reports/
│   ├── report.json
│   └── open_ports.json
│
├── dashboard/
│   ├── app.py
│   ├── templates/
│   └── static/
│
└── tests/
```

---

## Technologies Used

* Python
* Flask
* JSON
* Object-Oriented Programming
* File Handling
* Logging

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/NetGuard.git
cd NetGuard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Example Output

### Alert Log

```text
2026-05-30 16:51:31 | Possible Port Scan Detected from 192.168.1.50
```

### Open Ports Report

```json
[
    {
        "port": 80,
        "service": "HTTP",
        "status": "Open"
    }
]
```

---

## Future Enhancements

* Real-time dashboard updates
* Email notifications
* Multi-host monitoring
* Threat severity scoring
* Data visualization and analytics
* Machine learning based anomaly detection
* Automatic firewall integration

---

## Limitations

* Uses threshold-based detection.
* Focused on local machine monitoring.
* Limited to predefined monitoring rules.
* Does not currently implement advanced behavioral analysis.

---

## Learning Outcomes

This project demonstrates:

* Cybersecurity fundamentals
* Network monitoring concepts
* Python application development
* JSON data management
* Logging and reporting
* Software architecture design
* Git and GitHub workflow


