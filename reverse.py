def stringInvertida(text):
     result = ""
     for char in text:
         result = char + result
     return result

print(stringInvertida("Inverta essa string"))