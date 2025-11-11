import re
your_pattern= input()
try:
    re.compile(your_pattern)
    print("True")

except re.error:
    print("False")