import pyperclip
import re

text = str(pyperclip.paste())

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))? #phone code
    (\s|-|\.)? #space or - .
    (\d{3}) #first 3 numbers
    (\s|-|\.) #space or - .
    (\d{4}) #last 4 numbers
)""", re.VERBOSE)#(555)-333-4444

email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+ #username
    @ #at
    [a-zA-Z0-9._%+-]+ #domain name
    \.[a-zA-Z]{2,4} # com co ru)
)""", re.VERBOSE)

res = []
for i in phone_regex.findall(text):
    res.append(i[0])
for i in email_regex.findall(text):
    res.append(i)

if len(res)>0:
    pyperclip.copy("\n".join(res))
    print("Copied to the clipboard")
else:
    print("Emails and phone numbers not found")

