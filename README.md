# Cryptoguard

Cryptoguard is a lightweight CLI password strength analyzer for security-conscious users and pentesters.

Features:
- Length and composition checks (lower/upper/digits/symbols)
- Entropy estimation (bits)
- Check against a common password list (wordlist)
- Strength classification and visual meter
- JSON report output option

Usage examples:
```
# Analyze a single password
python3 cryptoguard.py -p "P@ssw0rd123!" -v

# Read password from stdin (pipe)
echo "password123" | python3 cryptoguard.py

# Output JSON report
python3 cryptoguard.py -p "secretpass" --json-out report.json
```


### 📊 Example Output (with Power Meter)
```
╔═══════════════════════════════════════════╗
║           C R Y P T O G U A R D            ║
╚═══════════════════════════════════════════╝

[+] Password: ************
[+] Length: 15 ✅
[+] Contains: lower, upper, digits, symbols
[+] Entropy: 89.7 bits 🔐
[=] Strength: Very Strong
[=] Power: [████████████████████████████████████████████░░░░░░░░░░░░░░░] 78%
```
