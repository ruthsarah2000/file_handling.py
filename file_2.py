'''
Problem Statement:
Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.
'''
import re

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
           
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
           
            return set(emails)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = "contacts.txt"
extracted_emails = extract_emails(filename)
if extracted_emails:
    print("Extracted email addresses:")
    for email in extracted_emails:
        print(email)
else:
    print("No email addresses found in the file.")
