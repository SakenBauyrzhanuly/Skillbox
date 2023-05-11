numbers = 'qWe456rtY'
result = ''.join(filter(lambda x: not x.isdigit() and not x.isupper(), numbers))
print(result)