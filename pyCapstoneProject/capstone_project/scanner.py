# Import required libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


# Display ethical warning
print("=" * 60)
print("WARNING: This tool is for educational purposes only")
print("Only scan websites you own or have permission to test")
print("=" * 60)


# Retrieve all forms from a webpage
def get_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all("form")


# Extract form details
def get_form_details(form):
    details = {}

    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()

    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")

        inputs.append({
            "type": input_type,
            "name": input_name
        })

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs

    return details


# Submit form data
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])

    data = {}

    for input_field in form_details["inputs"]:
        input_name = input_field.get("name")

        if input_name:
            data[input_name] = value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)


# SQL Injection testing
def scan_sql_injection(url):

    sql_payloads = [
        "' OR '1'='1",
        "admin' --",
        "test123"
    ]

    sql_errors = {
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "sql syntax",
        "mysql_fetch",
        "sqlite error",
        "oracle error"
    }

    forms = get_forms(url)
    vulnerabilities = []

    for form in forms:
        form_details = get_form_details(form)

        for payload in sql_payloads:
            response = submit_form(form_details, url, payload)
            content = response.text.lower()

            for error in sql_errors:
                if error in content:
                    vulnerabilities.append({
                        "type": "SQL Injection",
                        "payload": payload,
                        "form_action": form_details["action"]
                    })
                    break

    return vulnerabilities


# Cross-Site Scripting (XSS) testing
def scan_xss(url):

    xss_payload = "<script>alert(1)</script>"

    forms = get_forms(url)
    vulnerabilities = []

    for form in forms:
        form_details = get_form_details(form)

        response = submit_form(form_details, url, xss_payload)

        if xss_payload in response.text:
            vulnerabilities.append({
                "type": "Cross-Site Scripting (XSS)",
                "payload": xss_payload,
                "form_action": form_details["action"]
            })

    return vulnerabilities


# Validate website access
url = input("Enter website URL to scan: ")

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("\nWebsite is accessible")
    else:
        print("\nWebsite returned status code:", response.status_code)

except requests.exceptions.RequestException:
    print("\nUnable to access website")
    exit()


# Detect forms
forms = get_forms(url)
print(f"\nDetected {len(forms)} forms on the website")


# Run vulnerability scans
print("\nStarting SQL Injection scan...")
sql_vulnerabilities = scan_sql_injection(url)

print("\nStarting XSS scan...")
xss_vulnerabilities = scan_xss(url)


# Generate scan report
print("\n" + "=" * 60)
print("SCAN REPORT")
print("=" * 60)

print(f"Target URL: {url}")
print(f"Forms Detected: {len(forms)}")

print("\nSQL Injection Results:")

if sql_vulnerabilities:
    for vulnerability in sql_vulnerabilities:
        print("- Possible SQL Injection Detected")
        print("  Form Action:", vulnerability["form_action"])
        print("  Payload:", vulnerability["payload"])
else:
    print("No SQL Injection vulnerabilities detected")

print("\nXSS Results:")

if xss_vulnerabilities:
    for vulnerability in xss_vulnerabilities:
        print("- Possible XSS Vulnerability Detected")
        print("  Form Action:", vulnerability["form_action"])
        print("  Payload:", vulnerability["payload"])
else:
    print("No XSS vulnerabilities detected")


# Save report to file
with open("scan_report.txt", "w") as file:

    file.write("WEB VULNERABILITY SCANNER REPORT\n")
    file.write(f"Target URL: {url}\n")
    file.write(f"Forms Detected: {len(forms)}\n\n")

    file.write("SQL Injection Results:\n")

    if sql_vulnerabilities:
        for vulnerability in sql_vulnerabilities:
            file.write("Possible SQL Injection Detected\n")
            file.write(f"Form Action: {vulnerability['form_action']}\n")
            file.write(f"Payload: {vulnerability['payload']}\n\n")
    else:
        file.write("No SQL Injection vulnerabilities detected\n\n")

    file.write("XSS Results:\n")

    if xss_vulnerabilities:
        for vulnerability in xss_vulnerabilities:
            file.write("Possible XSS Vulnerability Detected\n")
            file.write(f"Form Action: {vulnerability['form_action']}\n")
            file.write(f"Payload: {vulnerability['payload']}\n\n")
    else:
        file.write("No XSS vulnerabilities detected\n")

print("\nReport saved to scan_report.txt")