print('Digite uma frase a ser descriptografada: ')
frase = input()
if (len(frase)==0):
   print('invalido')
else:
   pdcrip = ""
   for ind in range(0, len(frase)):
       cod = ord(frase[ind])
       cod -= 2
       newchar = chr(cod)
       pdcrip += newchar
   print('a mensagem descriptografada é: ')
   print(pdcrip)