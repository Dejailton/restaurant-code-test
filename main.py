from morning import Morning
from night import Night

morning = Morning()
night = Night()

periodo = input("Digite o período do dia:")
entradas = [0, 0, 0, 0, 0]
quantidade_entradas = 0

#entradas
for i in range(5):
    resposta = input("Digite o tipo de prato:")
    if resposta != '':
        entradas[i] = resposta
        quantidade_entradas += 1


#tentativa de limpar a lista e deixar apenas valores relevantes 
for i in range(4):
    print(i)
    if int(entradas[i]) == 0: 
        entradas.remove(0)

print(entradas)

