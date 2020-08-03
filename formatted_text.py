import pyperclip

text = pyperclip.paste()

lines = text.split("\n")
print(lines)

for i in range(len(lines)):
    lines[i] = "*"+lines[i]
    
print(lines)
    
text = "\n".join(lines) 
pyperclip.copy(text)



