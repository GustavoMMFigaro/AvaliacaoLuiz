# Fez a criação da função calcular_juros_atraso(),
# criando as variáveis valor_principal, taxa_juros_anual, dias_atraso dentro da função.
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):

# A variável "taxa_juros_diaria" tem como valor a taxa de juros anual dividido por 36500.
    taxa_juros_diaria = taxa_juros_anual / 365 / 100

# Criação da variável "juros", com o valor da taxa de juros diária
# multiplicado pelo valor principal(1000) e pelos dias de atraso(30).
    juros = valor_principal * taxa_juros_diaria * dias_atraso

# Criação da variável "valor_total", para representar o todal que deve ser pago,
# o valor principal mais os juros calculados.
    valor_total = valor_principal + juros
    return valor_total, juros  # Retorna o valor total e o juros.

# Colocando valor para as três variáveis: valor_principal; taxa_juros_anual; dias_atraso.
valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30

# Chama a função, realiza o calculo dos juros e escreve eles,
# com a formatação correta.
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")