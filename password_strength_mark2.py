import re

def passkey_strength(password):
    # Criteria for a strong password
    conditions = {
        #NIST standard for min length
        "Password must be 8 digits long": len(password) >= 8,
        "Uppercase letter": re.search(r'[A-Z]', password) is not None,
        "Lowercase letter": re.search(r'[a-z]', password) is not None,
        "Digit": re.search(r'\d', password) is not None,
        "Special character": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    # Check each condition and gather feedback
    Message = []
    for condition, passed in conditions.items():
        if not passed:
            Message.append(f"Password should include at least one {condition.lower()}.")
    
    if not Message:
        return "Password is strong."
    else:
        return "Password is weak. " + " ".join(Message)

if __name__ == '__main__':
    password = input("Enter your password: ")
    strength = passkey_strength(password)
    print(strength)
