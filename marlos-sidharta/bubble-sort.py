lista=[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
print("Lista original:", lista)
#total de algarismos
N=20 
#algarismos da variavel lista
lista=[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
#de quanto em quanto sera organizada a lista
for i in range(0, N - 1, 1):
# comando para gerar a lista
    for j in range(i + 1, N , 1):
# comando para trocar os elementos da lista toda vez que i for maior que j 
        if lista[i]>lista[j]:
# cria uma variavel que guarda os elementos da lista i, temporariamente, enquanto estao ocorrendo as trocas 
            temp=lista[i]
# agora igualamos a variavel i com o elemento da variavel j
            lista[i]=lista[j]
# por fiim, podemos associar o elementoda lista j a variavel temp, pois trocamos de lugar a variavel i e a variavel j
            lista[j]=temp
print ("Lista em ordem crescente:", lista)
print ("Cinco maiores valores:", lista[N-5:N])
print ("Cinco menores valores:", lista[0:N-15])