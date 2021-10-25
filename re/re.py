'''import re
txt="this is spain"
x=re.search("^is.*spain$",txt)'''
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "Esta nublando en Espana"
x = re.search("^Esta.*Espana$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")