# 5. Inversão de String

def inverteString(string):
    stringInvertida = ""

    for char in string:
        stringInvertida = char + stringInvertida
    return stringInvertida

string = input("Informe uma string: ")
print("String invertida:", inverteString(string))