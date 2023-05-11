import re

text = 'AV - Analytics community of India. India!'

result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)
