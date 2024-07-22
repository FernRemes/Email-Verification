# Email Verification with Regular Expressions
# a-z
# 0-9
# . _ times 1
# @ times 1
#

import re


def is_valid_email(user_email, email_condition):
    return re.match(email_condition, user_email) is not None 
        
def main(email_condition):
    
    while True:
        user_email = input("Enter your email (or type 'quit' to leave): ").strip()

        if user_email == "quit":
            print("Goodbye")
            break
        elif is_valid_email(user_email, email_condition):
            print("Valid Email")
            break
        else:
            print("Invalid Email")

if __name__ == '__main__':
    
    email_condition = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    main(email_condition)

