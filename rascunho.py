import random

p = "MUNDO"

p2 = "$" * 9
print(p2)

print()

j = "                     camaleão"

print(j)

print(j.strip())

jooj = ["opa", "upa", "cola"]

word = random.choice(jooj)

print(word)


palavra = "jaca"
indicie = 3

palavra = palavra[:indicie] + "_" + palavra[indicie + 1:]
print(palavra)