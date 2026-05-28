# Refatorar o projeto da aula anterior evitando Bugs!
print("Primeiro desafio do curso de Python")

nome = input("Nome:")
if not nome.strip():
    print("Erro: Nome não pode ser vazio ou apenas espaços.")
elif not nome.strip().replace(" ", "").isalpha():
    print("Erro: Nome não pode conter números ou caracteres especiais.")
else:
    try:
        salario = float(input("Salário:"))
        if salario < 0:
            print("Erro: Salário não pode ser negativo.")
        else:
            try:
                porcentagem_bonus = float(input("Porcentagem de bônus:"))
                if porcentagem_bonus < 0:
                    print("Erro: Porcentagem de bônus não pode ser negativa.")
                else:
                    print("O cálculo do KPI do bônus de 2024 é '1000 + salario * bonus'")
                    print("O valor bonus do " + nome + " é: " + str(1000 + salario * porcentagem_bonus))
            except ValueError:
                print("Erro: Porcentagem de bônus inválida. Digite um número.")
    except ValueError:
        print("Erro: Salário inválido. Digite um número.")
