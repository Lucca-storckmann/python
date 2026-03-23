primeira_nota = float (input ("Insira aqui sua nota: "))
segunda_nota = float (input ("Insira aqui sua nota: "))
terceira_nota =  float (input ("Insira aqui sua nota: "))
media_final = (primeira_nota + segunda_nota + terceira_nota) / 3
print (media_final)

if media_final > 7:
    print ("Parabéns, você foi aprovado")
elif media_final < 7:
    print ("Infelizamente você foi reprovado")