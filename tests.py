# tests.py
# Simple tests for Password Strength Analyzer
# Run with: python tests.py

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from analyzer import analyze_password, check_length, check_uppercase, check_numbers, check_special_chars


def test(name, condition):
    """Helper to print pass/fail for each test"""
    status = "✓ PASS" if condition else "✗ FAIL"
    print(f"  {status}  {name}")
    return condition


print("\n  Running tests...\n  " + "-"*35)

passed = 0
total  = 0

# -- Length checks --
total += 1; passed += test("Very short password scores 0",    check_length("hi")["score"] == 0)
total += 1; passed += test("8-char password passes length",   check_length("hello123")["passed"] == True)
total += 1; passed += test("12+ char password scores 3",      check_length("hello12345678")["score"] == 3)

# -- Uppercase checks --
total += 1; passed += test("Uppercase detected",              check_uppercase("Hello")["passed"] == True)
total += 1; passed += test("No uppercase detected",           check_uppercase("hello")["passed"] == False)

# -- Numbers checks --
total += 1; passed += test("Number detected",                 check_numbers("hello1")["passed"] == True)
total += 1; passed += test("No number detected",              check_numbers("hello")["passed"] == False)

# -- Special char checks --
total += 1; passed += test("Special char detected",           check_special_chars("hi!")["passed"] == True)
total += 1; passed += test("Special char gives 2 points",     check_special_chars("hi!")["score"] == 2)

# -- Full analysis --
total += 1; passed += test("'hi' is Weak",                    analyze_password("hi")["strength"] == "Weak")
total += 1; passed += test("'hello123' is Medium",            analyze_password("hello123")["strength"] == "Medium")
total += 1; passed += test("Strong password is Strong/VeryStrong",
                           analyze_password("Hello@World99!")["strength"] in ("Strong","Very Strong"))
total += 1; passed += test("Score is between 0-10",           0 <= analyze_password("test")["score"] <= 10)
total += 1; passed += test("Suggestions exist for weak pw",   len(analyze_password("abc")["suggestions"]) > 0)
total += 1; passed += test("Empty password handled",          analyze_password("")["strength"] == "Weak")

print(f"\n  {'-'*35}")
print(f"  Result: {passed}/{total} tests passed\n")

sys.exit(0 if passed == total else 1)
