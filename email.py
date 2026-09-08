import re

pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

text = """
Contact us at support@example.com
Sales: sales.team@business.co.in
Parth: parth23@gmail.com
Invalid: not-an-email
"""

# Find emails
emails = re.findall(pattern, text)

print("Emails found:")
for email in emails:
    print(email)

# Validate emails
print("\nEmail Validation:")

test = [
    "john@gmail.com",
    "invalid-email",
    "user@site",
    "hello@company.com"
]

for email in test:
    if re.fullmatch(pattern, email):
        print(email, "-> VALID")
    else:
        print(email, "-> INVALID")