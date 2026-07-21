strings = ["aba", "abc", "121", "xyz", "madam", "aa", "1991", "python"]

count = 0

for word in strings:
    if len(word) > 2 and word == word[::-1]:
        count += 1

print("Palindrome count:", count)