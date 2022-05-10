#!/usr/bin/env python
#
# english.py
# Extract strings from uncompressed versions of english.mgl,
# french.mgl, and german.mgl. Corrects character encoding

languages = ["english", "french", "german"]
output_language = "german"

conv = "nÇÜÄÖΔ∑¹𝐍∴⎛⎝⎞⎠Φσ×∎çüäö"

strs = {"english":[], "french":[], "german":[]}
for lang in languages:
  
  with open(lang,"rb") as f:
    txt = f.read()

  valid = True
  n = 0
  addr = 0

  while valid and n < 100000:
    v = txt[n:n+2]
    prev_addr = addr
    addr = int.from_bytes(v, byteorder="big")
    if addr > prev_addr:

      i = addr
      a = []
      while txt[i] != 0:
        a.append(txt[i])
        i += 1

      s = "".join([chr(c) for c in a])
      s = s.replace("\xFF","\\n") # newlines
      for c in range(0,22): # special characters in French/German
        s = s.replace(chr(c),conv[c])
      strs[lang].append(s)
      n += 2
    else:
      valid = False

for n in range(len(strs["english"])):
  print(f"{n+1}\t{hex(n+1)}\t{strs[output_language][n]}") 
