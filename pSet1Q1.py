s = "ertyabcdefgghklmzfr"
char1 = ''
char2 = ''
currentLong = ""
newLong = ""
x = 0
y = 1
lastChar = ""
sLen = len(s)
#count = 0
while x < sLen:
    y = x + 1
    newLong = s[x]
    lastChar = ""
    for letter in s:
        if y == sLen:
            break
        char1 = s[x]
        #print(char1)
        char2 = s[y]
        #print(char2)
        if char1 <= char2 and lastChar <= char2:
            newLong += char2
            #print("char added")
            #print(newLong)
            lastChar = char2
            y += 1
        elif char1 > char2:
            #print("break")
            break
    if len(currentLong) < len(newLong):
        currentLong = newLong
    x += 1

print("Longest suvstring in alphabetical order is: " + currentLong)