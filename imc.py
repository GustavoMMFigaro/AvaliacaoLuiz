# Cria a função "calcular_imc()" com as variáveis: peso e altura nela.
def calcular_imc(peso, altura):

    # Calcula e retorna o IMC.
    imc = peso / (altura ** 2)
    return imc

# Cria a função "classificar_imc" com a variável "imc" nela.
def classificar_imc(imc):

    # Classifica o IMC baseado no valor dele e retorna o a classificação.
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:  # Qualquer valor além dos utilizados no if retornará Obesidade grau 3
        return "Obesidade grau 3"

# Cria a função "sugestao_atividade_fisica" com a variável "classificacao_imc" nela.
def sugestao_atividade_fisica(classificacao_imc):

    # Dependendo da classificação do IMC, retorna a sugestão de atividade física adequada.
    if classificacao_imc == "Abaixo do peso":
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
    else:
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

# Pede ao usuário o peso e altura.
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Chama as funções, calcula, classifica e informa a sugestão.
imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

# Escreve o resultado.
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")
