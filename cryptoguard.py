#!/usr/bin/env python3

import argparse
import hashlib
import requests
from zxcvbn import zxcvbn

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def breach_check(password):

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url, timeout=5)

        for line in res.text.splitlines():
            hash_suffix, count = line.split(":")

            if hash_suffix == suffix:
                return int(count)

    except Exception:
        return None

    return 0


def strength_meter(score):

    length = 50
    filled = int(length * score / 4)

    bar = "█" * filled + "░" * (length - filled)

    percent = int((score / 4) * 100)

    return f"[{bar}] {percent}%"


def color_strength(score):

    if score <= 1:
        return RED

    elif score == 2:
        return YELLOW

    else:
        return GREEN


def analyze(password):

    result = zxcvbn(password)

    score = result["score"]

    crack_time = result["crack_times_display"]["offline_fast_hashing_1e10_per_second"]

    feedback = result["feedback"]

    breach_count = breach_check(password)

    return score, crack_time, feedback, breach_count


def main():

    parser = argparse.ArgumentParser(description="CryptoGuard Advanced Password Analyzer")

    parser.add_argument("-p", "--password", help="Password to analyze")

    args = parser.parse_args()

    if not args.password:
        password = input("Enter password to analyze: ")
    else:
        password = args.password

    score, crack_time, feedback, breach_count = analyze(password)

    meter = strength_meter(score)

    color = color_strength(score)

    print()
    print(color + "[+] Password Strength Score:", score, "/4" + RESET)
    print("[+] Estimated Crack Time:", crack_time)
    print()
    print("[=] Power:", meter)
    print()

    if breach_count is None:
        print(BLUE + "[!] Breach check unavailable" + RESET)

    elif breach_count > 0:
        print(RED + f"[!] Password found in breaches {breach_count} times!" + RESET)

    else:
        print(GREEN + "[+] Password not found in known breaches" + RESET)

    if feedback["warning"]:
        print()
        print(RED + "Warning:" + RESET, feedback["warning"])

    if feedback["suggestions"]:
        print()
        print("Suggestions:")
        for s in feedback["suggestions"]:
            print("-", s)


if __name__ == "__main__":
    main()
