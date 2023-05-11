# Name: Matthew Preston
# Date: Feb 15, 2023
# File: Lab04_Preston.py
# Purpose: Practice working with strings

# Open the file
file = open("spam_log.txt")

# Create variables to hold different information
unique_emails = []
unique_domains = []
email_frequency = {}
spam_results = {"Suspicious": 0, "Innocent": 0}
count_am = 0
count_pm = 0
confidence_spam = 0
confidence_innocent = 0
confidence_suspicious = 0

for line in file:
    # TASK 0: Remove newline characters '\n' from each line
    pass

    # SITUATION: Who are the potential spam senders?
    # --> Explanation: For email addresses, what comes before the `@` symbol is the user name and what follows the `@` symbol is the domain
    # TASK 1: Use the list called `unique_emails` to track unique email addresses and use `unique_domains` to track unique domains
    # TASK 1 (BONUS): Use the dictionary called `email_frequency ` to count how many emails each user sends
    if ("From:" in line):
        remain = line[5:]       # Why is it somewhat safe to start at 5?
        print(remain)  
        email = remain.strip()

        if email not in unique_emails:
            unique_emails.append(email)

        at_pos = email.find("@")
        domain = email[at_pos+1:]

        if domain not in unique_domains:
            unique_domains.append(domain)

    # SITUATION: How many spam emails are being sent?
    # TASK 2: Use the dictionary called `spam_results` to count suspicious and innocent emails
    if ("Result:" in line):
        pos = line.find(":")    # What does this code allow me to do?
        result = line[pos+1:].strip()
        spam_results[result] += 1

    # SITUATION: When are these potentially suspicious emails being sent?
    # TASK 3: The system is using military time (i.e. 1pm is 13:00) to log when emails are sent
    # Use `count_am` to track how many emails are sent between midnight and noon (that is 00:00 and 11:59)
    # Use `count_pm` to track how many emails are sent between noon and midnight (that is 12:00 and 23:59)
    if "Processed" in line:
        position = line.find(":")
        second = line.find(":",position+1)
        hour = line[second-2:second]
        hour = int(hour)
        if (hour<12 and hour>0):
            count_am+=1
        elif (hour>12 and hour<24):
            count_pm+=1

    # SITUATION: What is the average confidence for our spam filter?
    # TASK 4: Based on the category determined in task 2
    # HINT: Add the values in the for loop, then use `spam_results` to divide the total by the count
    if "Confidence" in line:
        position = line.find(":")
        confidence_number = line[position+1:]
        confidence_number = confidence_number.strip()
        confidence_number = float(confidence_number)
        if result == "Innocent":
            confidence_innocent += confidence_number
        elif result == "Suspicious":
            confidence_suspicious += confidence_number
        


# Calculate average confidence (Task 4) here
confidence_innocent = confidence_innocent/spam_results["Innocent"]
confidence_suspicious = confidence_suspicious/spam_results["Suspicious"]

### DO NOT MODIFY BELOW###
# assert statements check whether your code above is working correctly

assert len(unique_emails) == 14
print(f"There are {len(unique_emails)} email addresses in the spam log.")

assert len(unique_domains) == 8
print(f"Those emails originated from {len(unique_domains)} unique domains.")

# Uncomment asserts below if you did the bonus
# assert email_frequency["zqian@umich.edu"] == 4
# assert email_frequency["david.horwitz@uct.ac.za"] == 3
# assert email_frequency["mwfrank@anderson.edu"] == 1

assert spam_results["Suspicious"] == 4
assert spam_results["Innocent"] == 23
print(f'Of the emails captured, {spam_results["Suspicious"]} were marked as suspicious and {spam_results["Innocent"]} as innocent')

assert count_am == 16
assert count_pm == 11
print(f"{count_am} emails were sent between midnight and noon, and {count_pm} emails were sent between noon and midnight.")

#assert confidence_spam == 0.589175
assert confidence_innocent == 0.742517391304348
print(f"The spam filter classified spam emails with {int(confidence_suspicious*100)}% confidence")
print(f"The spam filter classified innocent emails with {int(confidence_innocent*100)}% confidence")
print(confidence_suspicious)