k = int(input())
s = input()

result = ""

for i in range(len(s)):
    if i < k - 1:
        result += s[i]
    else:
        result += chr(219 - ord(s[i]))

print(result)