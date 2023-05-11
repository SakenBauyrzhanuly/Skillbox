import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

result = re.findall(r'\b[^aeiouAEIOU\s]\w*', text)
print(result)

