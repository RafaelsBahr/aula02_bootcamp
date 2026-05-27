# Exercício 21: Conversor de Temperatura
print("Conversor de ºCelsius para ºFahrenheit")
try: 
    graus_celcius = float(input("Insira quantos graus Celsius quer saber: "))
    graus_fahrenheit = graus_celcius * (9/5) + 32
    print(f"O resultado é: {graus_fahrenheit:.1f}ºF")
except ValueError:
    print("Número não valido, tente usar . ao invés de ,")

    