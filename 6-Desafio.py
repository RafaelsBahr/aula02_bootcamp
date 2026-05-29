# Refatorar o projeto da aula anterior evitando Bugs!
print("Segundo desafio do curso de Python")

# input() sempre retorna string, então nome já é string automaticamente
nome = input("Nome:")

# .strip() remove espaços do início e fim. String com qualquer coisa = True ; String vazia = False em Python,
# logo nome.strip() é False se for só espaços ou vazio, e True se tiver qualquer letra ou número.
# Colocamos not para inverter: Se nome.strip() não tiver nada, vai ser False e vai virar True, entrando no if. 
# Se nome.strip() tiver algo, vai ser True e virar False, caindo no else.
if not nome.strip():
    print("Erro: Nome não pode ser vazio ou apenas espaços.")

# .strip() remove os espaços do início e fim.
# .replace(" ", "") remove os espaços internos antes de validar.
# Isso prepara o objeto para .isalpha().
# .isalpha() retorna True se todos os caracteres forem LETRAS (não aceita números). e False se tiver qualquer número ou caractere especial.
# Então nome.strip().replace(" ", "").isalpha() é True se o nome tiver apenas letras.
# e False se tiver números ou caracteres especiais.
# O "not" inverte o resultado: se tiver apenas letras, o if vai para o Else. Se tiver números ou caracteres especiais, o if é executado.
elif not nome.strip().replace(" ", "").isalpha():
    print("Erro: Nome não pode conter números ou caracteres especiais.")

else:
    # try/except captura erros em tempo de execução sem travar o programa.
    # float() já provoca ValueError se o usuário digitar texto no lugar de número
    try:
        salario = float(input("Salário:"))
        # Validação de salário: if para validar que o salário não seja negativo, e else para seguir com o programa se for válido.
        if salario < 0:
            print("Erro: Salário não pode ser negativo.")
        else:
            # Validação em cascata: porcentagem_bonus só é pedida se salario for válido
            # Try/except e float() para validar a porcentagem de bonus igual fizemos com o salário, e if para validar que não seja negativa.
            try:
                porcentagem_bonus = float(input("Porcentagem de bônus:"))
                if porcentagem_bonus < 0:
                    print("Erro: Porcentagem de bônus não pode ser negativa.")
                else:
                    # Objetivo real do programa: chegar aqui com dados válidos e fazer o cálculo
                    print("O cálculo do KPI do bônus de 2024 é '1000 + salario * bonus'")
                    print("O valor bonus do " + nome + " é: " + str(1000 + salario * porcentagem_bonus))
            except ValueError:
                print("Erro: Porcentagem de bônus inválida. Digite um número.")
    except ValueError:
        print("Erro: Salário inválido. Digite um número.")