from morning import Morning
from night import Night

morning = Morning()
night = Night()

periodo = input("Digite o período do dia:")
entradas = [0,0,0,0,0]
for i in range(5):
    resposta = input("Digite o tipo de prato:")
    entradas[i] = resposta
print(entradas)