#Aula de python Operadores lógicos e laços condicionais
# Aula 22/08/23

#Operadores:
#> Maior
#< Menor
#== Igual
#>= Maior igual
#<= Menor igual
#!= Diferente

#xor = se somente uma é true, resultado = true
#xor = se as duas forem true ou false = false

#& = se uma for false, resultado será = false
#& = se duas forem false, resultado será = false
#& = se duas forem true, resulta = true

#or = se uma for true, resultado = true
#or = se duas forem true, resultado = true
#or = se duas forem false, resultado = false

#not = 



#Laços:

#if 2>1 : 
#[    print]
#Quando a condição for falsa, o programa irá ler automaticamente o proximo laço/bloco de código.

#Primeiro Exercício:
#Pegar a idade 

nome= input("Digite seu nome: ")
anoNas= input("Digite seu ano de nascimento: ")

if int(anoNas) <= 2005 :
    print("Seu nome é: " +nome+ " e você tem mais de 18 anos")

if int(anoNas) > 2005 :
    print("Seu nome é: " +nome+ " e você tem menos de 18 anos")