from morning import Morning
from night import Night
from metodos import Metodos

morning = Morning()
night = Night()
metodos = Metodos()

periodo = input("Digite o período do dia:")
entradas = [2, 1, 3, 4, 5]
quantidade_entradas = 0
metodos.order_list(entradas)
print(entradas)

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

