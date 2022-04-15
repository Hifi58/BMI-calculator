print("======================")
print("= Calculez votre IMC =")
print("======================")

height = float(input("Entrez votre taille en cm : "))
weight = float(input("Entrez votre poid en kg : "))

bmi = weight/(height/100)**2

print("Votre IMC est de " ,bmi)

if bmi <= 18.5:
    print("Vous êtes en sous-poid")
elif bmi <= 24.9:
    print("Votre poid est parfait")
elif bmi <= 29.9:
    print("Vous êtes en surpoid")
else:
    print("Vous êtes atteint d'obésité")
