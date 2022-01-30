"""
Given an array of string as input, create a string consisting of the first character of each string in the array.
Input-> ["Hello","how","are","you"]
Output-> Hhay
"""

ls = ["Hello","how","are","you"]
ln = len(ls)
st = ""
for i in range(0,ln):
  e = ls[i]
  ln2 = len(e)
  for j in range(0,ln2):
    ch = e[j]
    if(j==0):
      st += ch
print(st)
