# Cria a função "calcular_custo_viagem()"
# e as variáveis: distancia; custo_combustivel; consumo_veiculo; numero_pedagios e custo_pedagio nela.
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):

# Realiza o calculo do custo do combustível e armazena na variável "custo_combustivel_total".
    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

# Realiza o calculo do custo do pedagio e armazena na variável "custo_pedagio_total".
    custo_pedagio_total = numero_pedagios * custo_pedagio

# Realiza o calculo do custo total e armazena na variável "custo_total".
    custo_total = custo_combustivel_total + custo_pedagio_total

    return custo_total, custo_combustivel_total, custo_pedagio_total  # Retorna os resultados.

# Pede ao usuário a distância; custo do combustível, o consumo do veículo; o número de pedágios;
# e o custo do pedágio.
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

# Chama a função e calcula o valor da viagem.
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel,
consumo_veiculo, numero_pedagios,
custo_pedagio)

# Escreve os custos da viagem.
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")
