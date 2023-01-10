notaA = float(input("Digite a primeira nota:"))
notaB = float(input("Digite a segunda nota:"))

mediafinal= (notaA + notaB) /2

if mediafinal >= 7:
    print("A Média: %.1f - Aprovado "% mediafinal)
else:
    print("A Média: %.1f - Reprovado "% mediafinal)