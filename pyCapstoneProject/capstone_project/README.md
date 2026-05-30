# Basic Web Vulnerability Scanner

## Description
This project is a simple Python-based web vulnerability scanner.
It checks websites for common security vulnerabilities such as:

- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)

The program scans HTML forms and tests them using malicious payloads.

---

## Features

- Accepts a website URL
- Detects HTML forms automatically
- Extracts form details
- Tests SQL Injection payloads
- Tests XSS payloads
- Displays scan report in terminal
- Saves report to a text file

---

## Technologies Used

- Python
- requests
- BeautifulSoup

---

## Installation

Install required libraries:

```bash
pip install requests beautifulsoup4
```

---

## Python venv setup steps:

1. Create virtual environment:
```bash
   python -m venv venv
```
2. Activate (Git Bash):
```bash
   source venv/Scripts/activate
```
3. Run program:
```bash
   python <file_name>.py
```
4. Deactivate (Git Bash):
```bash
   deactivate
```
---

## How to run the scanner:

```bash
python scanner.py
```
Then enter the website URL.

Example:
```bash
Enter website URL to scan: http://example.com
```
Example Output
```bash
============================================================
WARNING: This tool is for educational purposes only
============================================================

Enter website URL to scan: http://testphp.vulnweb.com

Website is accessible
Detected 2 forms on the website

Starting SQL Injection scan...
Starting XSS scan...

============================================================
SCAN REPORT
============================================================
Target URL: http://testphp.vulnweb.com
Forms Detected: 2

SQL Injection Results:
No SQL Injection vulnerabilities detected

XSS Results:
Possible XSS Vulnerability Detected

Report saved to scan_report.txt
```

---

## Ethical Warning

This tool is for educational purposes only. Only scan websites you own or have permission to test.

---
### Author
Gideon K. Gyebi

Capstone Project Submission

---
### Acknowledgements

AI was used as a learning and development aid during the development of this project. The final implementation, testing, and understanding of the project remain the responsibility of the author.