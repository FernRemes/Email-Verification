# Email Verification with String Patterns

from functools import lru_cache
# Requirements: 
    # 1. Email must be at least 6 characters long
    # 2. Email must have an @ symbol
    # 3. Email must have a.com,.org, or.net suffix
    # 4. Email must not have any spaces
    # 5. Email must not start or end with a period
    # 6. Email must not have two periods in a row
    # 7. Email must not start or end with an underscore
    # 8. Email must not have any periods in a row
    # 9. Email must not have any spaces in a row
    # 10. Email must not have two underscores in a row 
    # 11. Email must not have any dashes in a row
@lru_cache(maxsize = None)
def is_valid_email(email):
    if len(email) < 6:
        return "Invalid Email: {} is too short".format(email)
    
    elif not email[0].isalpha():
        return "Invalid Email: {} cannot start with a number".format(email)
    elif email.count("@") != 1:
        return "Invalid Email: {} does not have an @ symbol or has too many".format(email)
    
    elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
        return "Invalid Email: {} does not have a .com, .org, or .net suffix".format(email)
    
    elif " " in email:
        return "Invalid Email: {} contains spaces".format(email)
    
    elif email[0] == "." or email[-1] == ".":
        return "Invalid Email: {} starts or ends with a period".format(email)
    
    elif ".." in email:
        return "Invalid Email: {} has too many periods in a row".format(email)
    
    elif email[0] == "_" or email[-1] == "_":
        return "Invalid Email: {} starts or ends with an underscore".format(email)
    
    elif "_" in email:
        return "Invalid Email: {} has too many underscores in a row".format(email)
    
    elif "-" in email:
        return "Invalid Email: {} has too many dashes in a row".format(email)

    else:
        return "Valid Email: {}".format(email)


email = input("Enter your email: ")
print(is_valid_email(email))