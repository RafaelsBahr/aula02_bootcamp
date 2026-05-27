# Exercício 21: Conversor de Temperatura
# print("Conversor de ºCelsius para ºFahrenheit")
# try: 
#     graus_celcius = float(input("Insira quantos graus Celsius quer saber: "))
#     graus_fahrenheit = graus_celcius * (9/5) + 32
#     print(f"O resultado é: {graus_fahrenheit:.1f}ºF")
# except ValueError:
#     print("Número não valido, tente usar . ao invés de ,")

# Exercício 22: Verificador de Palíndromo
try:
        entrada = input("Teste palíndromo: ")
    teste_palidromo = entrada.lower().replace(" ", "")[::-1]
    if teste_palidromo == entrada:
        print("Seu texto é um palíndromo!")
    else:
        print("Seu texto não é um palindromo!")
except ValueError:
    print("Texto não é valido!")
# Esse foi dificil, especialmente porque não conhecia os comandos .replace() nem [::-1]
# Enunciado pedia para usar isinstance(), mas pelo que pesquisei isinstance neste caso não funcionaria porque é tudo string e input sempre gera string
# Try except também não imagino como poderia dar erro

