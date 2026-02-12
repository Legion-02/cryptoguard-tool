# 🔐 Cryptoguard

### CLI Password Strength Analyzer with Entropy & Power Meter

> A professional-grade command-line password strength analyzer that
> evaluates entropy, character diversity, and overall security posture
> using measurable scoring logic.

------------------------------------------------------------------------

## 🚀 Overview

**Cryptoguard** is a Python-based CLI tool designed to evaluate password
strength using:

-   🔢 Entropy estimation (bits)
-   🔡 Character diversity analysis
-   📏 Length-based scoring
-   📊 100-point scoring model
-   📈 50-block visual strength meter
-   📄 Optional structured JSON reporting

This tool demonstrates applied knowledge of: - Information theory
(entropy calculation) - Secure password evaluation logic - CLI
development - Structured reporting - Clean Python architecture

------------------------------------------------------------------------

## ✨ Features

### 🔎 Password Analysis

-   Detects:
    -   Lowercase characters
    -   Uppercase characters
    -   Digits
    -   Symbols
-   Calculates estimated entropy in bits

### 📊 Strength Classification

Passwords are classified as: - Very Weak - Weak - Moderate - Strong -
Very Strong

Based on entropy thresholds and length.

### 📈 Power Meter (Visual Output)

Generates a 50-block strength bar:

    [████████████████████████████░░░░░░░░░░░░░░░░░░░░] 72%

### 🧮 Scoring Model (Out of 100)

Score is calculated using:

-   Length component (35%)
-   Character diversity (30%)
-   Entropy scaling (35%)

### 📄 JSON Export Support

Structured output for automation workflows and reporting.

------------------------------------------------------------------------

## 🛠️ Installation

``` bash
git clone https://github.com/yourusername/cryptoguard.git
cd cryptoguard
python cryptoguard.py -h
```

No external dependencies required (pure Python).

------------------------------------------------------------------------

## ▶️ Usage

### Basic Analysis

``` bash
python cryptoguard.py -p "MySecurePass123!"
```

### Verbose Mode

``` bash
python cryptoguard.py -p "MySecurePass123!" -v
```

### Read from Input

``` bash
echo "MySecurePass123!" | python cryptoguard.py
```

### Save JSON Report

``` bash
python cryptoguard.py -p "MySecurePass123!" --json-out report.json
```

------------------------------------------------------------------------

## 🖥️ Sample Output

    [+] Password: ***************
    [+] Length: 16
    [+] Contains: lower, upper, digits, symbols
    [+] Entropy: 94.21 bits

    [=] Strength: Very Strong
    [=] Power: [██████████████████████████████████████████████░░░░] 91%

------------------------------------------------------------------------

## 🧠 Technical Highlights

-   Entropy calculation using log2
-   Information-theoretic password strength estimation
-   Secure password masking in terminal output
-   Structured CLI with argparse
-   Clean scoring algorithm design
-   JSON report generation
-   Modular and maintainable code

------------------------------------------------------------------------

## 🔐 Why This Project Matters

Cryptoguard demonstrates practical cybersecurity skills: - Understanding
of password complexity metrics - Application of entropy in security -
Defensive security mindset - Automation-ready output handling

------------------------------------------------------------------------

## ⚠️ Disclaimer

This tool is intended for educational and security awareness purposes
only.

------------------------------------------------------------------------

## 👨‍💻 Author

**Anush**\
Cyber Security Enthusiast
