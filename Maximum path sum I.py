import pyperclip

MaxTotal = 0

Text = pyperclip.paste().split('\r\n')

for x in range(len(Text)):
    Text[x] = Text[x].split()
    Text[x] = list(map(int, Text[x]))

while(

print(MaxTotal)
