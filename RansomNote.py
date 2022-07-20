ransomNote = "aab"
magazine = "bba"

d = {}
f = 0
ran = sorted(ransomNote)
mag = sorted(magazine)

# cout each letter in ransomNote
for r in ran:
    val = ran.count(r)
    d[r] = val
print(d)

for k, v in d.items():
    if k in mag and mag.count(k) >= v:
        pass
    else: 
        print(False)

    


