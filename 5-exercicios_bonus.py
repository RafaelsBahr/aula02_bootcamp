# Exercício 21: Conversor de Temperatura
# print("Conversor de ºCelsius para ºFahrenheit")
# try: 
#     graus_celcius = float(input("Insira quantos graus Celsius quer saber: "))
#     graus_fahrenheit = graus_celcius * (9/5) + 32
#     print(f"O resultado é: {graus_fahrenheit:.1f}ºF")
# except ValueError:
#     print("Número não valido, tente usar . ao invés de ,")

# Exercício 22: Verificador de Palíndromo
# try:
#         entrada = input("Teste palíndromo: ")
#     teste_palidromo = entrada.lower().replace(" ", "")[::-1]
#     if teste_palidromo == entrada:
#         print("Seu texto é um palíndromo!")
#     else:
#         print("Seu texto não é um palindromo!")
# except ValueError:
#     print("Texto não é valido!")
# Esse foi dificil, especialmente porque não conhecia os comandos .replace() nem [::-1]
# Enunciado pedia para usar isinstance(), mas pelo que pesquisei isinstance neste caso não funcionaria porque é tudo string e input sempre gera string
# Try except também não imagino como poderia dar erro

# Exercício 23: Calculadora Simples
import operator

# Dicionário de funções para substituir os if-elif
operacoes = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

try:
    val1 = float(input("Primeiro número: "))
    val2 = float(input("Segundo número: "))
    op = input("Operador (+, -, *, /): ")

    # Verifica se o operador digitado existe no nosso dicionário
    if op in operacoes:
        # Chama a função correspondente ao operador
        resultado = operacoes[op](val1, val2)
        print(f"Resultado: {resultado}")
    else:
        print("Operador inválido!")

except ValueError:
    print("Erro: Entrada não numérica. Por favor, digite números válidos.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

# Foi dificil. Na aula foi passado bem rapido sobre import e if. Mas estudei e usei IA e entendi no final
# import operator permite que a gente tenha novos comandos como operator.add e operator.sub...
# A gente consegue criar uma espécie de condicional para os operadores string (linha 28)
# if op in operacoes encerra o raciocínio. Com IA fica facil, mas entendi tudo.

