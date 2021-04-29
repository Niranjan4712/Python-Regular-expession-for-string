import re
s="Hello this is python, from regular expression"
i=re.search('^hello',s)
if(i):
    print("string match")
else:
    print("string not ,match")
