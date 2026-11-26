import re

passwords = ["Python@123", "python123"]

for p in passwords:
    if re.search(r'[A-Z]', p) and re.search(r'[0-9]', p) and re.search(r'[@#$!]', p):
        print(p, "- Valid password")
    else:
        print(p, "- Invalid password")