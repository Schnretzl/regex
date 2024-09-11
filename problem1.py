# 1. Python Regular Expressions Deep Dive

# Task 1: Email Extraction Enhancement
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, me@-.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)