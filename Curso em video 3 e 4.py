    ### declaração de variavel ###


n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1 + n2
print("a soma entre {} e {} é igual a {}!" .format(n1, n2, s))

    ### tipos primitivos de variaveis ###

a = input("digite algo: ") #aqui nesse caso o A é o obejto
print("É somente espaços? ", a.isspace())  #verica se é somente espaços
print("É um numero? ", a.isnumeric())  #vericia se é um numero
print("É alfabetico? ", a.isalpha())  #verifica se é alfabetico
print("É alfanumerico? " ,a.isalnum())  #verifica se é alfanumerico
print("Esta em letras maiúculas? ", a.isupper())  #verifica se esta totoalemnte em letras maiúculas
print("Esta em letras minúsculass? ", a.islower()) #verifica se esta totalemnte em letras minúsculas
print("Esta capitalizada? ", a.istitle()) #verifica se há letras tanto em maiúculas quanto minúsculas