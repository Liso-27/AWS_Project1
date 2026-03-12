# main.py
# Password Strength Analyzer - Command Line Interface
# Run this file: python main.py

from analyzer import analyze_password


def print_report(result):
    """Print the analysis report in a clean, readable format"""
    
    score    = result["score"]
    strength = result["strength"]
    checks   = result["checks"]
    suggestions = result["suggestions"]
    
    # Draw a simple progress bar using text characters
    filled = "█" * score
    empty  = "░" * (10 - score)
    bar    = f"[{filled}{empty}]"
    
    print()
    print("=" * 50)
    print("       PASSWORD STRENGTH REPORT")
    print("=" * 50)
    print(f"  Strength  : {strength}")
    print(f"  Score     : {score}/10")
    print(f"  Meter     : {bar}")
    print("-" * 50)
    
    # Show each check with pass/fail
    print("  CHECKS:")
    for name, check in checks.items():
        icon = "✓" if check["passed"] else "✗"
        print(f"    {icon} {name:<22} → {check['feedback']}")
    
    print("-" * 50)
    print("  SUGGESTIONS:")
    for i, tip in enumerate(suggestions, 1):
        print(f"    {i}. {tip}")
    
    print("=" * 50)
    print()


def main():
    """Main loop - keeps asking for passwords until user quits"""
    
    print()
    print("  🔐 Password Strength Analyzer")
    print("  Type a password to check it. Type 'quit' to exit.")
    print()
    
    while True:
        # Get input from user
        password = input("  Enter password: ").strip()
        
        # Exit condition
        if password.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye! Stay secure. 👋\n")
            break
        
        # Skip empty input
        if not password:
            print("  (Please enter a password)\n")
            continue
        
        # Analyze and show the report
        result = analyze_password(password)
        print_report(result)


if __name__ == "__main__":
    main()
