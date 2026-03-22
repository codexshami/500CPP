#1-Reverse a string
str1='shami'
rev_str=str1[::-1]
print(rev_str)   

# 2 - CHECK  if two srings are anagrams
def are_anagrams(s1, s2): 
    return sorted(s1)==sorted(s2)
print(are_anagrams("listen","silent"))  

# 3- Find the non repeating character in a string
def non_repating_str(s):
    for char in s:
        if s.count(char)==1:
            return char
print(non_repating_str("aabbssdhsmi"))

# 4- Count the frequency of each character in a string
s = "hello world"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# 5- Remove all vowels from string 
def remove_vowels(str4):
    vowels = "aeiouAEIOU"
    result = ""
    for char in str4:
        if char not in vowels:
            result += char
    return result
print(remove_vowels("Mohd Shami"))

# 6- Replace a substring in a string
str5 = "Shami is a great player"
str6 = "Sammy"

result = str5.replace("Shami", str6)
print(result)

# 7- Check if a sting is a valid palindrom
str7="shami"
str8="imahs"
str9=str8[::-1]
if str8==str9:
    print("The strings are plindrome.")
else:
    print("The strings are not plindrome.")
 
# 8- find the longest substring without repeating characters
s = "abcabcbb"
longest = ""
current = ""

for char in s:
    if char in current:
        current = current[current.index(char)+1:]
    current += char
    if len(current) > len(longest):
        longest = current

print("Longest substring without repeating characters:", longest)
print("Length:", len(longest))

# 9- implement the strstr() function 
def strstr(haystack, needle):
    if needle == "":
        return 0  # As per C/C++ behavior

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# 10-  Check if a String Has All Unique Characters
def is_unique(s):
    for char in s:
        if s.count(char) > 1:
            return False
    return True

# Test cases
print(is_unique("abcdef"))  # True
print(is_unique("hello"))   # False

