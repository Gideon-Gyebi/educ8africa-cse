# Project Documentation

## Step-by-Step Workflow

This document explains how the Basic Web Vulnerability Scanner operates from start to finish.

---

## Step 1: User Enters a URL

The program prompts the user to enter the target website URL.

```python
url = input("Enter website URL to scan: ")
```

### Purpose

This URL becomes the target that the scanner will analyze for vulnerabilities.

---

## Step 2: Website Validation

The scanner checks whether the website is accessible before continuing.

```python
response = requests.get(url)
```

### Purpose

This ensures the website is reachable and prevents the scanner from running against an invalid target.

---

## Step 3: Form Detection

The scanner searches the webpage for HTML forms.

```python
forms = get_forms(url)
```

Inside the function:

```python
soup.find_all("form")
```

### Purpose

Most web vulnerabilities are tested through input fields inside forms. The scanner must first identify these forms before testing them.

---

## Step 4: Extract Form Information

The scanner extracts important information from each form.

```python
form_details = get_form_details(form)
```

Information collected includes:

- Form action
- Form method (GET or POST)
- Input fields
- Input names
- Input types

### Purpose

This information is required to properly submit test payloads to the form.

---

## Step 5: Submit Test Payloads

The scanner automatically submits test values to the detected forms.

Example:

```python
response = submit_form(form_details, url, payload)
```

### Purpose

This simulates user input and allows the scanner to observe how the website handles potentially malicious data.

---

## Step 6: SQL Injection Testing

The scanner tests forms using SQL Injection payloads.

Example payloads:

```text
' OR '1'='1
admin' --
test123
```

### Purpose

The goal is to identify situations where user input is improperly handled by the database.

The scanner checks the server response for common SQL error messages such as:

```text
you have an error in your sql syntax
warning: mysql
sqlite error
oracle error
```

---

## Step 7: Cross-Site Scripting (XSS) Testing

The scanner tests forms using an XSS payload.

Example:

```html
<script>alert(1)</script>
```

### Purpose

The scanner checks whether the payload is reflected back into the webpage without proper sanitization.

If the payload appears in the response, a potential XSS vulnerability may exist.

---

## Step 8: Analyze Responses

The scanner reviews all responses received from the website.

### SQL Injection Analysis

The scanner searches for:

- SQL syntax errors
- Database error messages
- Warning messages

### XSS Analysis

The scanner searches for:

- Reflected JavaScript code
- Unsanitized user input

### Purpose

This step determines whether any potential vulnerabilities were detected.

---

## Step 9: Generate Scan Report

After testing is complete, the scanner generates a report.

Example:

```python
print("SCAN REPORT")
```

The report contains:

- Target URL
- Number of forms detected
- SQL Injection results
- XSS results
- Payloads used

### Purpose

This provides a summary of the scan findings.

---

## Step 10: Save Report to File

The scanner saves the results to a text file.

```python
with open("scan_report.txt", "w") as file:
```

### Purpose

Saving the report allows the user to review the results later and maintain records of previous scans.

---

## Summary

The scanner follows the workflow below:

1. User enters URL
2. Validate website accessibility
3. Detect HTML forms
4. Extract form details
5. Submit test payloads
6. Test for SQL Injection
7. Test for XSS
8. Analyze responses
9. Generate report
10. Save report to file

---

## Ethical Notice

This tool is intended for educational purposes only.

Only scan websites that you own or have explicit permission to test.

Unauthorized security testing may violate laws, regulations, or terms of service.