# Email Verification
## Overview
Analyze the complexity of verifying an email address by using different techniques.

## First Strategy
Verify an email using string patterns. This includes caching the the string pattern, thus iterating takes les time complexity.

- ## Requirements: 
    ### 1. Email must be at least 6 characters long
    ### 2. Email must have an @ symbol
    ### 3. Email must have a.com,.org, or.net suffix
    ### 4. Email must not have any spaces
    ### 5. Email must not start or end with a period
    ### 6. Email must not have two periods in a row
    ### 7. Email must not start or end with an underscore
    ### 8. Email must not have any periods in a row
    ### 9. Email must not have any spaces in a row
    ### 10. Email must not have two underscores in a row 
    ### 11. Email must not have any dashes in a row

## Second Strategy

Verify an email address using standard business practice, regular expression (regex). This involves a match pattern search system that ensures the format of the email address conforms to the standards. The regex pattern checks various aspects, such as the presence of valid characters in the local part, the inclusion of the "@" symbol. By implementing such a system, businesses can filter out invalid email addresses during data entry or form submission, thereby reducing errors and ensuring more reliable communication. This method, while highly effective for format validation, should be complemented with other practices like sending confirmation emails to verify the existence and accessibility of the provided email address. 


- ## Requirements
    ### 1. Email Verification with Regular Expressions
    ### 2. a-z
    ### 3. 0-9
    ### 4. . _ times 1
    ### 5. @ times 1

***
Example:

```python

"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

```

***

# Conclusion

the different techniques used to validate email addresses must be complex inorde to ensure that all email addresses are accurate, valid, and unique to the users. Thus, a simple string validation pattern can lead to inefficiency and unwanted tiem complexity of O(n^2) due to iterating over string multiple times to validate all possible flags. However, a regular expression searching pattern can be effective as the function uses pattern matching techniques like Deterministic Finite Algorithms (DFA) and Nondeterministic Finite Algorithms (NFA) to search for valid email addresses in a optimized manner.
