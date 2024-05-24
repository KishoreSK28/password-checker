import re

def password_complexity_checker(password):
    # Define the complexity criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Compile the results
    criteria_met = {
        "Length (>= 8)": length_criteria,
        "Uppercase letter": uppercase_criteria,
        "Lowercase letter": lowercase_criteria,
        "Digit": digit_criteria,
        "Special character": special_char_criteria,
    }

    # Count the number of criteria met
    score = sum(criteria_met.values())
    strength = "Very Weak"
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    elif score == 1:
        strength = "Very Weak"

    # Print the results
    print(f"Password: {password}")
    for criterion, met in criteria_met.items():
        print(f"{criterion}: {'Met' if met else 'Not Met'}")
    print(f"Overall Strength: {strength}")

    return strength

# Example usage:
password = input("enter the password:")
strength = password_complexity_checker(password)
