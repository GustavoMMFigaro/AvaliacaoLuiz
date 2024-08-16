# Criação de uma função "calcular_area_comodos()".
def calcular_area_comodos():
    total_area = 0  # Criou a variável "total_area" e deu valor 0 para ela.

# Criação de um while loop que enquanto for verdade irá se repetir.
    while True:

# Pede, com o comando input,
# para o usuário dar o valor das variáveis: "largura" e "comprimento"
        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Cria a variável "area_comodo", que representa a área do cômodo,
# com os valores dados pelo usuário, além de escrever o valor da área.
        area_comodo = largura * comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

# O valor da variável "area_comodo" será somado ao da variável "total_area" com ela mesma.
        total_area += area_comodo

# Utilizando o while loop, o código permite o usuário adicionar mais cômodos caso queira,
# digitar "s" continua no loop e caso digite "n" para o loop.
        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
        if mais_comodos != 's':
            break

        return total_area # Retorna o valor total de todos os cômodos.

# Chama a função, calcula a área dos cômodos,
# e com a formatação correta, escreve a area total.
area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")
