text = 'Я! Есть. Грут?! Я, Грут и Есть.'
symbol = '.,;:!?'
res_symbol = set(symbol)
res_text = set(text)
print(res_symbol)
print(res_text)
result = len(res_symbol.intersection(res_text))
print(result)