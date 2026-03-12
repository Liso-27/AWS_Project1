# analyzer.py
# Password Strength Analyzer - Core Logic
# Uses regex (re module) to check password strength

import re

def check_length(password):
    """Check if password is long enough"""
    length = len(password)
    
    if length < 6:
        return {"score": 0, "max": 3, "passed": False,
                "feedback": f"Too short ({length} chars) — use at least 8"}
    elif length < 8:
        return {"score": 1, "max": 3, "passed": False,
                "feedback": f"Short ({length} chars) — aim for 12+"}
    elif length < 12:
        return {"score": 2, "max": 3, "passed": True,
                "feedback": f"OK length ({length} chars) — 12+ is better"}
    else:
        return {"score": 3, "max": 3, "passed": True,
                "feedback": f"Great length ({length} chars) ✓"}


def check_uppercase(password):
    """Check for at least one uppercase letter using regex"""
    has_upper = bool(re.search(r"[A-Z]", password))
    
    return {
        "score": 1 if has_upper else 0,
        "max": 1,
        "passed": has_upper,
        "feedback": "Has uppercase letters ✓" if has_upper else "No uppercase letters — add A-Z"
    }


def check_lowercase(password):
    """Check for at least one lowercase letter using regex"""
    has_lower = bool(re.search(r"[a-z]", password))
    
    return {
        "score": 1 if has_lower else 0,
        "max": 1,
        "passed": has_lower,
        "feedback": "Has lowercase letters ✓" if has_lower else "No lowercase letters — add a-z"
    }


def check_numbers(password):
    """Check for at least one digit using regex"""
    has_number = bool(re.search(r"[0-9]", password))
    
    return {
        "score": 1 if has_number else 0,
        "max": 1,
        "passed": has_number,
        "feedback": "Has numbers ✓" if has_number else "No numbers — add digits 0-9"
    }


def check_special_chars(password):
    """Check for special characters like !@#$ using regex"""
    has_special = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]", password))
    
    return {
        "score": 2 if has_special else 0,
        "max": 2,
        "passed": has_special,
        "feedback": "Has special characters ✓" if has_special else "No special chars — add !@#$%"
    }


def check_no_common_words(password):
    """Check that password doesn't contain common weak words"""
    # List of passwords people commonly use (bad!)
    common_words = ["password", "123456", "qwerty", "abc123", "admin",
                    "letmein", "welcome", "monkey", "dragon", "hello"]
    
    lower_password = password.lower()
    
    # Also check for repeated characters like "aaa" or "111"
    has_repeat = bool(re.search(r"(.)\1{2,}", password))
    
    found = [word for word in common_words if word in lower_password]
    
    if found or has_repeat:
        msg = f"Contains weak pattern: '{found[0]}'" if found else "Has repeated characters (e.g. 'aaa')"
        return {"score": 0, "max": 1, "passed": False, "feedback": msg}
    
    return {"score": 1, "max": 1, "passed": True,
            "feedback": "No common weak patterns ✓"}


def analyze_password(password):
    """
    Main function — runs all checks and returns a full analysis.
    This is the function you call to analyze any password.
    """
    
    # Run all 5 checks
    checks = {
        "Length":         check_length(password),
        "Uppercase":      check_uppercase(password),
        "Lowercase":      check_lowercase(password),
        "Numbers":        check_numbers(password),
        "Special Chars":  check_special_chars(password),
        "No Weak Patterns": check_no_common_words(password),
    }
    
    # Add up the scores
    total_score  = sum(c["score"] for c in checks.values())
    max_possible = sum(c["max"]   for c in checks.values())  # = 9
    
    # Convert to a score out of 10
    score = round((total_score / max_possible) * 10)
    score = min(score, 10)  # cap at 10
    
    # Decide strength label based on score
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    # Build suggestions — only for checks that failed
    suggestions = []
    if not checks["Length"]["passed"]:
        suggestions.append("Make your password longer (at least 12 characters)")
    if not checks["Uppercase"]["passed"]:
        suggestions.append("Add uppercase letters (A-Z)")
    if not checks["Lowercase"]["passed"]:
        suggestions.append("Add lowercase letters (a-z)")
    if not checks["Numbers"]["passed"]:
        suggestions.append("Add numbers (0-9)")
    if not checks["Special Chars"]["passed"]:
        suggestions.append("Add special characters like !@#$%")
    if not checks["No Weak Patterns"]["passed"]:
        suggestions.append("Avoid common words and repeated characters")
    
    if not suggestions:
        suggestions.append("Great password! Keep it safe and don't reuse it.")
    
    return {
        "score":       score,
        "strength":    strength,
        "checks":      checks,
        "suggestions": suggestions,
    }
