#!/usr/bin/env python3
"""
Cryptoguard — CLI Password Strength Analyzer (with Power Meter)

Features:
- Check length and character classes (lower, upper, digits, symbols)
- Estimate entropy (bits)
- Strength classification and 50-block power meter
- Optional JSON output of the analysis
"""

from __future__ import annotations
import argparse
import math
import json
import sys
from pathlib import Path
from typing import Dict

from banner import print_banner

SYMBOLS = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"


def estimate_entropy(password: str) -> float:
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in SYMBOLS for c in password):
        pool += len(SYMBOLS)

    if pool == 0:
        return 0.0

    return len(password) * math.log2(pool)


def classify_strength(entropy_bits: float, length: int) -> str:

    if entropy_bits < 28 or length < 6:
        return "Very Weak"

    if entropy_bits < 36:
        return "Weak"

    if entropy_bits < 60:
        return "Moderate"

    if entropy_bits < 90:
        return "Strong"

    return "Very Strong"


def analyze_password(password: str) -> Dict:

    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    entropy = estimate_entropy(password)

    strength = classify_strength(entropy, length)

    return {
        "password": password,
        "length": length,
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "entropy_bits": round(entropy, 2),
        "strength": strength
    }


def compute_score(res: Dict) -> int:

    length = res["length"]
    entropy = res["entropy_bits"]

    length_score = min(length, 20) / 20 * 35

    diversity = sum([
        res["has_lower"],
        res["has_upper"],
        res["has_digit"],
        res["has_symbol"]
    ])

    diversity_score = (diversity / 4) * 30

    entropy_score = min(entropy, 120) / 120 * 35

    score = length_score + diversity_score + entropy_score

    return int(round(score))


def strength_meter(score: int, length: int = 50) -> str:

    filled = int(length * score // 100)

    bar = "█" * filled + "░" * (length - filled)

    return f"[{bar}] {score}%"


def parse_args():

    p = argparse.ArgumentParser(
        prog="cryptoguard",
        description="Cryptoguard — password strength analyzer (CLI)"
    )

    p.add_argument(
        "-p",
        "--password",
        help="Password to analyze. If omitted, reads from stdin.",
        default=None
    )

    p.add_argument(
        "--json-out",
        type=Path,
        help="Write JSON output to file"
    )

    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    return p.parse_args()


def mask_password(password: str) -> str:

    if len(password) <= 2:
        return "*" * len(password)

    return password[0] + "*" * (len(password) - 2) + password[-1]


def main():

    print_banner()

    args = parse_args()

    if args.password is None:

        if sys.stdin.isatty():

            try:
                args.password = input("Enter password to analyze: ")
            except KeyboardInterrupt:
                print()
                sys.exit(1)

        else:
            args.password = sys.stdin.read().strip()

    res = analyze_password(args.password)

    score = compute_score(res)

    meter = strength_meter(score, length=50)

    masked = mask_password(res["password"])

    print()

    print(f"[+] Password: {masked}")
    print(f"[+] Length: {res['length']}")

    contains = []

    if res["has_lower"]:
        contains.append("lower")

    if res["has_upper"]:
        contains.append("upper")

    if res["has_digit"]:
        contains.append("digits")

    if res["has_symbol"]:
        contains.append("symbols")

    print(f"[+] Contains: {', '.join(contains) if contains else 'none'}")

    print(f"[+] Entropy: {res['entropy_bits']} bits")

    if args.verbose:
        print()
        print("Details:")
        print(json.dumps(res, indent=2))

    print()

    print(f"[=] Strength: {res['strength']}")
    print(f"[=] Power: {meter}")

    if args.json_out:

        try:

            args.json_out.write_text(
                json.dumps(
                    {"summary": res, "score": score},
                    indent=2
                ),
                encoding="utf-8"
            )

            print(f"[+] JSON report written to {args.json_out}")

        except Exception as e:

            print(f"[!] Failed to write JSON: {e}")


if __name__ == "__main__":
    main()
