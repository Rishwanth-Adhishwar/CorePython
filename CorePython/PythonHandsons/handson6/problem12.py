s = input()
k = int(input())

count = 0

for ch in s:
    if s.count(ch) == 1:
        count += 1

        if count == k:
            print(ch)
            break
else:
    print("Less than k non-repeating characters in input.")