ransomNote = "aab"
magazine = "bba"

d = {}
f = 0
ran = sorted(ransomNote)
mag = sorted(magazine)

# count each letter in ransomNote
for r in ran:
    val = ran.count(r)
    d[r] = val
print(d)

# compare number of each letter in magazine to letters
# and number of items in dictionary created according to
# ransomNote
for k, v in d.items():
    if k in mag and mag.count(k) >= v:
        pass
    else: 
        print(False)

    


